import qrcode

from django.conf import settings


def generate_qr_code(instance):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

# def print_book(path=settings.BASE_DIR):
#     print(path) # D:\projects\miran\miran

