import qrcode


def generate_qr_code(instance, book_url):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(book_url)
    qr.make(fit=True)

    image = qr.make_image(fill_color="black", back_color="white")
    file_path = f"books/media/{instance.slug}.png"
    image.save(file_path, "PNG")

    return file_path
