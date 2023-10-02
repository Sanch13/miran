# from django.db.models.signals import pre_save
# from django.dispatch import receiver
# from .models import Book
#
#
# @receiver(pre_save, sender=Book)
# def create_qr_code(sender, instance, **kwargs):
#     if not instance.qr_code:
#         qr_code.