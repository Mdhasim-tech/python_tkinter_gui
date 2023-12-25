from tkinter import *
root=Tk()
root.geometry("500x400")
def getvals():
    print(f"The name of the person is {namevalue.get()}\n")

def cbutton1():
    if Checkbutton:
        print("The person is ready to take class in sunday")
        

def cbutton2():
    if Checkbutton:
        print("The person is not ready to take classes in sunday")
        
    


Label(root,text="welcome to Hasim's special classes",bg="magenta",fg="black"
      ,font="comicscansms 19 bold",relief=SUNKEN).grid(row=0,column=2)
Label(root,text="namevalue").grid(row=1,column=1)
Label(root,text="agevalue").grid(row=2,column=1)
Label(root,text="gendervalue").grid(row=3,column=1)

namevalue=StringVar()
agevalue=StringVar()
gender=StringVar()
checkbox=IntVar()

Entry(root,textvariable=namevalue).grid(row=1,column=2)
Entry(root,textvariable=agevalue).grid(row=2,column=2)
Entry(root,textvariable=gender).grid(row=3,column=2)

checkbutton1=Checkbutton(root,text="I want to take classes at Sunday?",command=cbutton1).grid(row=4,column=2)
checkbutton1=Checkbutton(root,text="No I don't want to take classes at Sunday?",command=cbutton2).grid(row=5,column=2)
Button(root,text="Submit to Hasim's classes",command=getvals).grid(row=6,column=2)

root.mainloop()