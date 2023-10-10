import qrcode

from django.conf import settings


def generate_qr_code(instance, book_url):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    absolute_url = 'http://' + settings.ALLOWED_HOSTS[0] + ':8000' + book_url

    qr.add_data(absolute_url)
    qr.make(fit=True)

    image = qr.make_image(fill_color="black", back_color="white")
    # file_path = f"books/{instance.slug}.png"
    file_path = f"{instance.slug}.png"
    image.save(file_path, "PNG")

    return file_path
