from django.db import models

# Create your models here.
class Contact(models.Model):
    contact_name = models.CharField(max_length=100, verbose_name="Contact Name")
    address = models.CharField(max_length=200, null=True, blank=True, verbose_name="Address")

    def __str__(self):
        return self.contact_name



class PhoneNumber(models.Model):
    contact_id = models.ForeignKey(Contact, related_name="contact_phone", on_delete=models.CASCADE, verbose_name="Contact")
    phone_number = models.CharField(max_length=15, verbose_name="Phone Number")

    def __str__(self):
        return self.contact_id.contact_name