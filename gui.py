from tkinter import *
from PIL import Image
from PIL import ImageTk
from image_processing import *
from statistics import *

# PARAMETRY:
WIDTH_WINDOW = 1500
HEIGHT_WINDOW = 700
WIDTH_IMAGE = 300
HEIGHT_IMAGE = 300

file_name = "im0082"

input_image = cv2.imread("images/input/" + file_name + ".ppm")
input_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2RGB)

binary_input_image = cv2.imread("images/binary/" + file_name + ".ah.ppm")

binary_output_image, output_image = image_processing(input_image)
tpr, tnr, ppv, npv, f_measure = statistics(binary_input_image, binary_output_image)

print("TPR: " + str(tpr))
print("TNR: " + str(tnr))
print("PPV: " + str(ppv))
print("NPV: " + str(npv))
print("F-measure: " + str(f_measure))


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

label_binary_input_image = Label(root, text="Maska binarna wejściowa:")
label_binary_input_image.pack()
label_binary_input_image.place(x=510, y=50)
display_binary_input_image = Image.fromarray(binary_input_image)
resized_binary_input_image = display_binary_input_image.resize((WIDTH_IMAGE, HEIGHT_IMAGE), Image.NEAREST)
display_binary_input_image = ImageTk.PhotoImage(resized_binary_input_image)
f.create_image(574, 300, image=display_binary_input_image)

label_binary_output_image = Label(root, text="Maska binarna wyjściowa:")
label_binary_output_image.pack()
label_binary_output_image.place(x=870, y=50)
display_binary_output_image = Image.fromarray(binary_output_image)
resized_binary_output_image = display_binary_output_image.resize((WIDTH_IMAGE, HEIGHT_IMAGE), Image.NEAREST)
display_binary_output_image = ImageTk.PhotoImage(resized_binary_output_image)
f.create_image(936, 300, image=display_binary_output_image)

label_output_image = Label(root, text="Obraz wyjściowy:")
label_output_image.pack()
label_output_image.place(x=1255, y=50)
display_output_image = Image.fromarray(output_image)
resized_output_image = display_output_image.resize((WIDTH_IMAGE, HEIGHT_IMAGE), Image.NEAREST)
display_output_image = ImageTk.PhotoImage(resized_output_image)
f.create_image(1298, 300, image=display_output_image)

cv2.imwrite("output_binary_image_" + file_name + ".png", binary_output_image)
cv2.imwrite("output_image_" + file_name + ".png", cv2.cvtColor(output_image, cv2.COLOR_RGB2BGR))

root.mainloop()
