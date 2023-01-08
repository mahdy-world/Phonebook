import datetime
from django.db.models.aggregates import Sum, Count
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import *
from .models import Contact, PhoneNumber
from .forms import *
from django.contrib import messages



class ContactList(ListView):
    model = Contact
    paginate_by = 12

    def get_queryset(self):
        queryset = self.model.objects.all().order_by('-id')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ContactCreate(CreateView):
    model = Contact
    form_class = ContactForm
    template_name = 'Contact/contact_add.html'
    success_url = reverse_lazy('Contact:ContactList')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add New Contact'
        context['action_url'] = reverse_lazy('Contact:ContactCreate')
        if self.request.POST:
            context["formset"] = PhoneNumberFormSet(self.request.POST, instance=self.object)
        else:
            context['formset'] = PhoneNumberFormSet()
        return context

    def form_valid(self, form):
        myform = form.save(commit=False)
        # myform.contact_id = Contact.objects.get(id=self.kwargs['pk'])
        context = self.get_context_data()
        formset = context['formset']
        if formset.is_valid():
            myform.save()
            self.object = myform
            formset.instance = self.object
            formset.save()
        return redirect(self.get_success_url())

    def get_success_url(self):
        messages.success(self.request, "Add Success", extra_tags="success")
        if self.request.POST.get('url'):
            return self.request.POST.get('url')
        else:
            return self.success_url



class ContactUpdate(UpdateView):
    model = Contact
    form_class = ContactForm
    template_name = 'Contact/contact_add.html'
    success_url = reverse_lazy('Contact:ContactList')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update Contact' + str(self.object)
        context['action_url'] = reverse_lazy('Contact:ContactUpdate', kwargs={'pk': self.object.id})

        if self.request.POST:
            context["formset"] = PhoneNumberFormSet(self.request.POST, instance=self.object)
        else:
            context['formset'] = PhoneNumberFormSet(instance=self.object)
        return context

    def get_success_url(self):
        messages.success(self.request, "Contact Updated Sucess" + str(self.object), extra_tags="success")
        if self.request.POST.get('url'):
            return self.request.POST.get('url')
        else:
            return self.success_url