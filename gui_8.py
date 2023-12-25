from tkinter import *
root=Tk()
root.geometry("500x500")
def getvals():
    print(f"The value of username is {uservalue.get()}")
    print(f"The value of the password is {passvalue.get()}")


    with open("data.txt","a") as my_file:
        my_file.write(f"{uservalue.get()}\t\t<----->\t\t{passvalue.get()}\n")


Label(text="Welcome to the dance class!",bg="pink",font="comicscansms 19 bold"
      ,fg="grey").grid()
Label(root,text="Username").grid(row=1,padx=20)
Label(root,text="Password").grid(row=2)

uservalue=StringVar()
passvalue=StringVar()



Entry(root,textvariable=uservalue).grid(row=1,column=1,padx=50)
Entry(root,textvariable=passvalue).grid(row=2,column=1)

Button(text="Submit",command=getvals).grid()

root.mainloop()