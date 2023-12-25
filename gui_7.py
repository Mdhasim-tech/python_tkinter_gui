from tkinter import *
def c1():
    print("Hello this is button 2")
root=Tk()
root.geometry("500x500")
frame=Frame(root,borderwidth=5,bg="pink",relief=SUNKEN)
frame.pack(side="left",anchor=NW)
b1=Button(frame,fg="red",text="print now")
b1.pack(side=LEFT)

b2=Button(frame,fg="red",text="print now",command=c1) 
b2.pack(side=LEFT,padx=50)

frame=Frame(root,borderwidth=5,bg="pink",relief=SUNKEN)
frame.pack(side="left",anchor=NW,padx=10)
b3=Button(frame,fg="red",text="print now")
b3.pack(side=LEFT)

frame=Frame(root,borderwidth=5,bg="pink",relief=SUNKEN)
frame.pack(side="top")
b4=Button(frame,fg="red",text="print now")
b4.pack()




root.mainloop()