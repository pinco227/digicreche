from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import ActivityImage


@receiver(post_delete, sender=ActivityImage)
def delete_file_from_storage(sender, instance, *args, **kwargs):
    print('signal received')
    if instance and instance.image:
        print('instance in')
        instance.image.delete(save=False)
