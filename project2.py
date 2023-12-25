from tkinter import *
root=Tk()
def getvals():
    print("It works!")
root.geometry("777x666")
#Heading
Label(root,text="Welcome to Hasim Travel",font="comicscansms 19 bold",pady=15).grid(
    row=0,column=3)

#Text for our form and packing it in the geometry manager grid()
name=Label(root,text="Name").grid(row=1,column=2)
phone=Label(root,text="Phone").grid(row=2,column=2)
gender=Label(root,text="Gender").grid(row=3,column=2)
emergency=Label(root,text="Emergency").grid(row=4,column=2)
paymentmode=Label(root,text="Paymentmode").grid(row=5,column=2)


#tkinter variables for storing entries
namevalue=StringVar()
phonevalue=StringVar()
gendervalue=StringVar()
emergencyvalue=StringVar()
paymentmodevalue=StringVar()
foodservicevalue=IntVar()

#Entries for our form and packing it to the geometry manager grid()
nameentry=Entry(root,textvariable=namevalue).grid(row=1,column=3)
phoneentry=Entry(root,textvariable=phonevalue).grid(row=2,column=3)
genderentry=Entry(root,textvariable=gendervalue).grid(row=3,column=3)
emergencyentry=Entry(root,textvariable=emergencyvalue).grid(row=4,column=3)
paymentmodeentry=Entry(root,textvariable=paymentmodevalue).grid(row=5,column=3)

#checkbox and packing it
foodservice=Checkbutton(text="Want to prebook your meals?",variable=foodservicevalue)
foodservice.grid(row=6,column=3)

#Button and packing it and assigning it a command
Button(text="Submit to Hasim Travels",command=getvals).grid(row=7,column=3)


root.mainloop()

