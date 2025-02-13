from tkinter import *
from tkinter import messagebox as mb
from PIL import Image

# Function to convert text to binary and encode into an image
def generate_data(pixels, data):
    data_in_binary = [format(ord(i), '08b') for i in data]  # Convert text to binary
    data_length = len(data_in_binary)
    image_data = iter(pixels)

    for a in range(data_length):
        pixels = [val for val in next(image_data)[:3] + next(image_data)[:3] + next(image_data)[:3]]

        for b in range(8):
            if (data_in_binary[a][b] == '1' and pixels[b] % 2 == 0):
                pixels[b] += 1
            elif (data_in_binary[a][b] == '0' and pixels[b] % 2 != 0):
                pixels[b] -= 1

        # Mark the end of the message
        if a == data_length - 1:
            if pixels[-1] % 2 == 0:
                pixels[-1] += 1  # Make sure it's odd to indicate the end

        yield tuple(pixels[:3])
        yield tuple(pixels[3:6])
        yield tuple(pixels[6:9])

# Function to encode text into an image
def encryption(img, data):
    size = img.size[0]
    (x, y) = (0, 0)

    for pixel in generate_data(img.getdata(), data):
        img.putpixel((x, y), pixel)
        if x == size - 1:
            x = 0
            y += 1
        else:
            x += 1

# Function to handle encoding process
def main_encryption(img, text, new_image_name):
    try:
        image = Image.open(img, 'r')

        if not text or not img or not new_image_name:
            mb.showerror("Error", "All fields are required!")
            return

        new_image = image.copy()
        encryption(new_image, text)

        new_image_name += '.png'
        new_image.save(new_image_name, 'png')
        mb.showinfo("Success", f"Image saved as {new_image_name}")

    except Exception as e:
        mb.showerror("Error", f"Something went wrong: {str(e)}")

# Function to decode text from an image
def main_decryption(img, strvar):
    try:
        image = Image.open(img, 'r')
        image_data = iter(image.getdata())

        data = ""
        while True:
            pixels = [val for val in next(image_data)[:3] + next(image_data)[:3] + next(image_data)[:3]]
            binary_string = ''.join(['0' if p % 2 == 0 else '1' for p in pixels[:8]])
            data += chr(int(binary_string, 2))

            if pixels[-1] % 2 != 0:
                break  # Stop when end marker is found

        strvar.set(data)
    except Exception as e:
        mb.showerror("Error", f"Decryption Failed: {str(e)}")

# Function to create encoding window
def encode_image():
    encode_wn = Toplevel(root)
    encode_wn.title("Encode Image")
    encode_wn.geometry('650x280')
    encode_wn.config(bg='#E3F6F5')

    Label(encode_wn, text='🖼 Encode an Image 🛡', font=("Segoe UI", 16, 'bold'), bg='#E3F6F5', fg='#008080').pack(pady=10)

    Label(encode_wn, text='📂 Image Path:', font=("Segoe UI", 12), bg='#E3F6F5').place(x=20, y=60)
    Label(encode_wn, text='✍️ Text to Encode:', font=("Segoe UI", 12), bg='#E3F6F5').place(x=20, y=100)
    Label(encode_wn, text='💾 Output File Name:', font=("Segoe UI", 12), bg='#E3F6F5').place(x=20, y=140)

    img_path = Entry(encode_wn, width=40, font=("Segoe UI", 11))
    img_path.place(x=320, y=60)

    text_to_be_encoded = Entry(encode_wn, width=40, font=("Segoe UI", 11))
    text_to_be_encoded.place(x=320, y=100)

    after_save_path = Entry(encode_wn, width=40, font=("Segoe UI", 11))
    after_save_path.place(x=320, y=140)

    Button(encode_wn, text='🔒 Encode Now', font=('Segoe UI', 12, 'bold'), bg='#A7E9AF', fg='#004D40', width=20,
           command=lambda: main_encryption(img_path.get(), text_to_be_encoded.get(), after_save_path.get())).place(x=230, y=200)

# Function to create decoding window
def decode_image():
    decode_wn = Toplevel(root)
    decode_wn.title("Decode Image")
    decode_wn.geometry('650x320')
    decode_wn.config(bg='#D5F3FE')

    Label(decode_wn, text='🖼 Decode an Image 🔍', font=("Segoe UI", 16, 'bold'), bg='#D5F3FE', fg='#0077B6').pack(pady=10)

    Label(decode_wn, text='📂 Image Path:', font=("Segoe UI", 12), bg='#D5F3FE').place(x=20, y=60)

    img_entry = Entry(decode_wn, width=40, font=("Segoe UI", 11))
    img_entry.place(x=320, y=60)

    text_strvar = StringVar()

    Button(decode_wn, text='🔓 Decode Now', font=('Segoe UI', 12, 'bold'), bg='#A0E7E5', fg='#004D40', width=20,
           command=lambda: main_decryption(img_entry.get(), text_strvar)).place(x=230, y=100)

    Label(decode_wn, text='📜 Decoded Text:', font=("Segoe UI", 12, 'bold'), bg='#D5F3FE', fg='#0077B6').place(x=20, y=150)

    text_entry = Entry(decode_wn, width=75, text=text_strvar, font=("Segoe UI", 11), state='disabled')
    text_entry.place(x=20, y=180, height=100)

# Main GUI window
root = Tk()
root.title('Image Steganography')
root.geometry('600x300')
root.config(bg='#001F3F')

Label(root, text='🔹 Image Steganography 🔹', font=('Trebuchet MS', 16, 'bold'), bg='#001F3F', fg='#00FFFF').pack(pady=20)

Button(root, text='🔒 Encode Message', width=30, font=('Century Gothic', 12, 'bold'), bg='#003366', fg='White',
       command=encode_image).pack(pady=10)

Button(root, text='🔓 Decode Message', width=30, font=('Century Gothic', 12, 'bold'), bg='#003366', fg='White',
       command=decode_image).pack(pady=10)

root.mainloop()
