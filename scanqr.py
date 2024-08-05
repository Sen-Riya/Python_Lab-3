import qrcode

def generate_qr_code(user):
    user_data = (
        f"User ID: {user['user_id']}\n"
        f"Name: {user['name']}\n"
        f"Email: {user['email']}\n"
        f"Age: {user['age']}"
    )
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(user_data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    filename = f"user_{user['user_id']}_qr.png"
    img.save(filename)
    return filename
