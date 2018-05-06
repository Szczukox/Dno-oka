from tkinter import *
import cv2
from PIL import Image
from PIL import ImageTk

# PARAMETRY:
WIDTH_WINDOW = 1500
HEIGHT_WINDOW = 700
WIDTH_IMAGE = 300
HEIGHT_IMAGE = 300

input_image = cv2.imread("images/input/im0001.ppm")

binary_image = cv2.imread("images/binary/im0001.ah.ppm")

root = Tk()
root.title("Dno oka")
root.resizable(0, 0)

width_screen = root.winfo_screenwidth()
height_screen = root.winfo_screenheight()

x_position = (width_screen / 2) - (WIDTH_WINDOW / 2)
y_position = (height_screen / 2) - (HEIGHT_WINDOW / 2)

root.geometry('%dx%d+%d+%d' % (WIDTH_WINDOW, HEIGHT_WINDOW, x_position, y_position))

f = Canvas(root, width=WIDTH_WINDOW, height=HEIGHT_WINDOW)
f.pack()

label_input_image = Label(root, text="Obraz wejściowy:")
label_input_image.pack()
label_input_image.place(x=165, y=50)
display_input_image = Image.fromarray(input_image)
resized_input_image = display_input_image.resize((WIDTH_IMAGE, HEIGHT_IMAGE), Image.NEAREST)
display_input_image = ImageTk.PhotoImage(resized_input_image)
f.create_image(212, 300, image=display_input_image)

label_binary_image = Label(root, text="Maska binarna wejściowa:")
label_binary_image.pack()
label_binary_image.place(x=510, y=50)
display_binary_image = Image.fromarray(binary_image)
resized_binary_image = display_binary_image.resize((WIDTH_IMAGE, HEIGHT_IMAGE), Image.NEAREST)
display_binary_image = ImageTk.PhotoImage(resized_binary_image)
f.create_image(574, 300, image=display_binary_image)

label_output_image = Label(root, text="Maska binarna wyjściowa:")
label_output_image.pack()
label_output_image.place(x=870, y=50)
display_output_image = Image.fromarray(input_image)
resized_output_image = display_output_image.resize((WIDTH_IMAGE, HEIGHT_IMAGE), Image.NEAREST)
display_output_image = ImageTk.PhotoImage(resized_output_image)
f.create_image(936, 300, image=display_output_image)

label_output2_image = Label(root, text="Obraz wyjściowy:")
label_output2_image.pack()
label_output2_image.place(x=1255, y=50)
display_output2_image = Image.fromarray(input_image)
resized_output2_image = display_output2_image.resize((WIDTH_IMAGE, HEIGHT_IMAGE), Image.NEAREST)
display_output2_image = ImageTk.PhotoImage(resized_output2_image)
f.create_image(1298, 300, image=display_output2_image)

root.mainloop()
