#  import send_mail from django.core.mail (we will need this function later).
from django.core.mail import send_mail
from coffeeshops.models import CafeOwner
from django.db.models.signals import post_save, post_delete, pre_save
from django.dispatch import receiver
"""
if created is true, Send an email with the subject as New Cafe Owner and the body of the email as A new cafe owner has joined named <FULL_NAME_OF_CAFE_OWNER>. For the from_email you can use "sender@test.com" and recipient_list can be ["receiver@test.com"].
"""


@receiver(post_save, sender=CafeOwner)
def send_new_owner_email(sender, instance, created, **kwargs):
    if created == True:
        send_mail(
            'New Cafe Owner',
            'A new cafe owner has joined named ' + instance.full_name,
            'sender@test.com',
            ["receiver@test.com"],
            fail_silently=False,
        )
