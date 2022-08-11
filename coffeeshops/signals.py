#  import send_mail from django.core.mail (we will need this function later).
from django.core.mail import send_mail
from coffeeshops.models import CafeOwner, CoffeeShop, CoffeeShopAddress, Drink
from django.db.models.signals import post_save, post_delete, pre_save
from django.dispatch import receiver
from utils import create_slug
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
# Check if instance does not have a slug
# If our instance does not have a slug then just set instance.slug equal to create_slug(instance) where create_slug is imported from utils (i.e., from utils import create_slug).
# We want to make sure that an address object always exists for a CoffeeShop even if one was never created or if it is deleted.


@receiver(pre_save, sender=CoffeeShop)
def slugify_coffee_shop(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)


# Check if the instance has been created, and if instance.location is empty
# Set instance.location equal to the new CoffeeShopAddress object you've created.
# Save your instance.
@receiver(post_save, sender=CoffeeShop)
def add_default_address(sender, instance, created, **kwargs):
    if created and not instance.location:
        createdLocation = CoffeeShopAddress.objects.create(
            coffee_shop=instance)
        instance.location = createdLocation
        instance.save()
