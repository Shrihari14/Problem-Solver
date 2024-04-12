from tkinter import *
from tkinter import messagebox
import datetime as date
import customtkinter
from PIL import Image
import math
customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("blue")
root = customtkinter.CTk()
date = date.datetime.now()
label1 = customtkinter.CTkLabel(root, text=f"{date:%A, %B %d, %Y}")
label1.pack(side=TOP, pady=1, fill=BOTH)
root.geometry("650x750")
root.maxsize(650, 750)
root.minsize(650, 750)
root.title("MECHANICS PROJECT-2")
theta=math.tau
frame1 = customtkinter.CTkFrame(root,width=600,height=175)
label2 = customtkinter.CTkLabel(frame1, text="Question:", font=("Futura", 25, UNDERLINE))
label2.pack(side=TOP, padx=30, fill=BOTH, pady=5)
label3 = customtkinter.CTkLabel(frame1, text="Determine the resultant R of the three tension forces acting on the eye bolt.\n Find the magnitude of R and the angle which R makes with the positive x-axis.",font=("Futura",15))
label3.pack(side=TOP, padx=30, fill=BOTH, pady=15)
frame1.pack(fill=BOTH, pady=5)
frame1.pack(fill=BOTH, pady=0)
image=customtkinter.CTkImage(dark_image=Image.open("/Users/shriharidesai/Desktop/Mech project/Diagram_2-removebg-preview.png"),size=(330,230))
label2=customtkinter.CTkLabel(root,text="",image=image)
label2.pack()
label3=customtkinter.CTkLabel(root,text="Enter the force F\N{SUBSCRIPT ONE} in kN:")
label3.pack(pady=2)
e1=customtkinter.CTkEntry(root)
e1.pack(pady=2)
label4=customtkinter.CTkLabel(root,text="Enter the force F\N{SUBSCRIPT TWO} in kN:")
label4.pack(pady=2)
e2=customtkinter.CTkEntry(root)
e2.pack(pady=2)
label7=customtkinter.CTkLabel(root,text="Enter the force F\N{SUBSCRIPT THREE} in kN:")
label7.pack(pady=2)
e5=customtkinter.CTkEntry(root)
e5.pack(pady=2)
label5=customtkinter.CTkLabel(root,text="Enter the angle alpha  in degrees:")
label5.pack(pady=2)
e3=customtkinter.CTkEntry(root)
e3.pack(pady=2)
label6=customtkinter.CTkLabel(root,text="Enter the angle theta  in degrees:")
label6.pack(pady=2)
e4=customtkinter.CTkEntry(root)
e4.pack(pady=2)
def submit1():
    f1 = int((e1.get()))
    f2 = int((e2.get()))
    f3 = int((e5.get()))
    x = int((e3.get()))
    alpha = math.radians(x)
    y = int((e4.get()))
    theta = math.radians(y)
    f1x = f1*math.sin(alpha)
    f1y = f1*math.cos(alpha)
    f2x = f2*math.sin(theta)
    f2y = f2*math.cos(theta)
    f3y = f3
    Rx = f1x+f2x
    Ry = f1y-f2y-f3y
    R = math.sqrt((Rx*Rx)+(Ry*Ry))
    angle1 = Ry / Rx
    angle2 = math.atan(angle1)
    angle3 = math.degrees(angle2)
    root1 = customtkinter.CTk()
    root1.geometry("600x250")
    root1.maxsize(600, 250)
    root1.minsize(600, 250)
    root1.title("MECHANICS PROJECT-2")
    final_label = customtkinter.CTkLabel(root1, text="The magnitude of the resultant:\n R= "+str(round(R,2))+" kN", font=("Times", 20))
    final_label.pack(pady=15)
    degree_sign = u'\N{DEGREE SIGN}'
    final_label2 = customtkinter.CTkLabel(root1, text="The angle that the resultant makes with the positive x-axis:\n" + str(round(angle3,2)) + degree_sign, font=("Times", 20))
    final_label2.pack(pady=15)

    def close():
        root1.destroy()

    b2 = customtkinter.CTkButton(root1, text="Close", command=close)
    b2.pack(pady=15)
    root1.mainloop()

b1 = customtkinter.CTkButton(root, text="Submit", command=submit1)
b1.pack(pady=14)
root.mainloop()