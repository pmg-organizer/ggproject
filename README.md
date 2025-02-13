Image Steganography using Python

📌 Overview

This is a Python-based GUI tool for image steganography, allowing users to hide (encode) secret text messages inside images and retrieve (decode) them later. It uses the Least Significant Bit (LSB) technique to manipulate pixel values subtly, making it difficult to detect hidden messages.

🛠 Features

Encode text messages into images.

Decode hidden text from images.

Simple and intuitive GUI built using Tkinter.

Supports PNG image format.

Error handling with user-friendly messages.

🔧 Requirements

Make sure you have the following dependencies installed:

pip install pillow

🚀 How to Run

Clone the repository:

https://github.com/pmg-organizer/ggproject

Run the script:

gg.py

🖥️ Usage

Encoding a Message:

Click on "Encode Message".

Enter the image path.

Type the secret message.

Specify the output file name.

Click "Encode Now" to embed the message in the image.

Decoding a Message:

Click on "Decode Message".

Enter the image path.

Click "Decode Now" to retrieve the hidden message.

🛠 Technologies Used

Python for scripting.

Tkinter for GUI.

Pillow (PIL) for image processing.

⚠️ Limitations

Works best with PNG images to avoid compression loss.

The embedded text should not exceed the image's storage capacity.
