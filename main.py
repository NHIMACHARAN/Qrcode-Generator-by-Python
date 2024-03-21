import qrcode                                                                    # This imports the qrcode module, which allows us to create QR codes.
def generate_qr_code(data, filename):                                            #This defines a function named generate_qr_code which takes two parameters:
                                                                                 #data: The data that you want to encode into the QR code.
                                                                                 #filename: The filename (including extension) where you want to save the generated QR code image.
    qr = qrcode.QRCode(                                                          #qr = qrcode.QRCode(...): This creates a QRCode object with the specified parameters:

        version=1,                                                               #version: The size of the QR code. The default is 1, which is suitable for small amounts of data.
        error_correction=qrcode.constants.ERROR_CORRECT_L,                       #error_correction: The error correction level. Here it's set to ERROR_CORRECT_L, which stands for low error correction. Other options are ERROR_CORRECT_M, ERROR_CORRECT_Q, and ERROR_CORRECT_H.
        box_size=10,                                                             #box_size: The number of pixels each "box" of the QR code will take.
        border=4,                                                                #border: The number of boxes to include as a border around the QR code.
    )
    qr.add_data(data)                                                            #This adds the data to the QR code.
    qr.make(fit=True)                                                            #This generates the QR code. The fit=True parameter ensures that the QR code size will be adjusted to fit the data properly.

    img = qr.make_image(fill_color="black", back_color="white")                  #This creates an image representation of the QR code. It specifies the fill color for the QR code elements (here, black) and the background color (here, white).
    img.save(filename)                                                           #This saves the generated QR code image to the specified filename. Here, it's saving it in PNG format.

if __name__ == "__main__":                                                        #This block ensures that the code inside it runs only if the script is executed directly, not if it's imported as a module.
    data = input("Enter the data for QR code: ")                                  #This prompts the user to input the data they want to encode into the QR code.
    filename = input("Enter the filename to save QR code (e.g., example.png): ")  #This prompts the user to input the filename (including extension) where they want to save the generated QR code image.
    generate_qr_code(data, filename)                                              #This calls the generate_qr_code function with the user-provided data and filename.
    print(f"QR code saved as {filename}")                                         #This prints a message indicating that the QR code has been successfully saved with the provided filename.




