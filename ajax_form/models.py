from django.db import models

class contact_us(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email_address = models.CharField( max_length=50)
    website_name = models.CharField( max_length=50)
    customer_message = models.TextField()

    class Meta:
        verbose_name = 'Contact_us'
        verbose_name_plural = 'Contact_us'
