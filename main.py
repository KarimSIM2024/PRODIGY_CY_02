import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import numpy as np

# Function to encrypt the image by modifying pixel values
def encrypt_image(img, key):
    encrypted_img = img.copy()
    pixels = np.array(encrypted_img)
    # Convert to uint16 to avoid overflow, then back to uint8
    pixels = (pixels.astype(np.uint16) + key) % 256
    return Image.fromarray(pixels.astype('uint8'))

# Function to decrypt the image by reversing the encryption process
def decrypt_image(img, key):
    decrypted_img = img.copy()
    pixels = np.array(decrypted_img)
    pixels = (pixels.astype(np.uint16) - key) % 256
    return Image.fromarray(pixels.astype('uint8'))

# Function to load an image
def load_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        img = Image.open(file_path)
        img = img.resize((250, 250))  # Resize for display purposes
        return img
    return None

# Function to display the image on the GUI
def display_image(img, canvas, x, y):
    img_tk = ImageTk.PhotoImage(img)
    canvas.create_image(x, y, anchor='nw', image=img_tk)
    canvas.image = img_tk

# Main function to create the GUI
def create_gui():
    root = tk.Tk()
    root.title("Image Encryption Tool")

    canvas = tk.Canvas(root, width=800, height=400)
    canvas.pack()

    # Load Image Button
    btn_load = tk.Button(root, text="Load Image", command=lambda: load_and_display())
    btn_load.pack()

    # Encrypt Button
    btn_encrypt = tk.Button(root, text="Encrypt", command=lambda: encrypt_and_display())
    btn_encrypt.pack()

    # Decrypt Button
    btn_decrypt = tk.Button(root, text="Decrypt", command=lambda: decrypt_and_display())
    btn_decrypt.pack()

    original_img = [None]  # To store the loaded image
    key = 50  # Simple key for encryption/decryption

    def load_and_display():
        original_img[0] = load_image()
        if original_img[0]:
            display_image(original_img[0], canvas, 50, 50)

    def encrypt_and_display():
        if original_img[0]:
            encrypted_img = encrypt_image(original_img[0], key)
            display_image(encrypted_img, canvas, 300, 50)

    def decrypt_and_display():
        if original_img[0]:
            encrypted_img = encrypt_image(original_img[0], key)
            decrypted_img = decrypt_image(encrypted_img, key)
            display_image(decrypted_img, canvas, 550, 50)

    root.mainloop()

# Run the GUI
if __name__ == "__main__":
    create_gui()
