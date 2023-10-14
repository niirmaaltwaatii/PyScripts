import qrcode

def generate_qr_code(data, file_name):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(file_name)

if __name__ == "__main__":
    data = input("Enter the Text : ")
    file_name = input("Enter the file name (e.g. myQR.png): ")

    try:
        generate_qr_code(data, file_name)
        print(f"QR code saved as {file_name}")
    except Exception as e:
        print(f"An error occurred: {e}")
