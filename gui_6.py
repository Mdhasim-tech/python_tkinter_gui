from tkinter import *
root=Tk()
root.geometry("500x500")
f1=Frame(root,borderwidth=8,bg="red",relief=SUNKEN)
f1.pack(side="left",fill=Y,pady=230)

f2=Frame(root,borderwidth=8,bg="red",relief=SUNKEN)
f2.pack(side="top",fill=X)

label=Label(f1,text="This is the first frame")
label.pack()

label=Label(f2,text="This is the second frame")
label.pack()

root.mainloop()