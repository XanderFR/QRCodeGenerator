from tkinter import *
import pyqrcode
from PIL import ImageTk, Image
import png


def generate():
    linkName = nameEntry.get()
    link = linkEntry.get()
    fileName = linkName + ".png"  # File name of QR Code image
    url = pyqrcode.create(link)  # Generate QR Code
    url.png(fileName, scale=8)
    image = ImageTk.PhotoImage(Image.open(fileName))  # Prepare QR Code image
    imageLabel = Label(image=image)  # Create image label
    imageLabel.image = image
    canvas.create_window(200, 250, window=imageLabel)

root = Tk()
root.title("QR Code Generator")

canvas = Canvas(root, width=400, height=450)
canvas.pack()

appLabel = Label(root, text="QR Code Generator", fg='blue', font=("Arial", 30))
canvas.create_window(200, 50, window=appLabel)

nameLabel = Label(root, text="Link name")
linkLabel = Label(root, text="Link")
canvas.create_window(200, 100, window=nameLabel)
canvas.create_window(200, 160, window=linkLabel)

nameEntry = Entry(root, width=50)
linkEntry = Entry(root, width=50)
canvas.create_window(200, 130, window=nameEntry)
canvas.create_window(200, 190, window=linkEntry)

button = Button(text="Generate QR Code", command=generate)
canvas.create_window(200, 230, window=button)

root.mainloop()

