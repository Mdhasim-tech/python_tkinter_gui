from tkinter import *
from PIL import  ImageTk, Image

root = Tk()
root.title("CodeWithHasim News - Aapka Apna Akhbaar")
root.geometry("1000x1000")


photos = []
texts=[]

for i in range(0,2):
    with open(f"{i+1}.txt") as f:
        content = f.read()
    new_content=""
    for i in range(len(content)):
        new_content+=content[i]
        if i%100==0 and i!=0:
            new_content+="\n"
    texts.append(new_content)


for i in range (0,2):
    image = Image.open(f"{i+1}.jpg")
    #TODO: Resize these images
    image = image.resize((225, 240), Image.Resampling.LANCZOS)
    photos.append(ImageTk.PhotoImage(image))

f0 = Frame(root, width=800, height=70,borderwidth=10,relief=SUNKEN)
Label(f0, text="Code With Hasim News", font="lucida 33 bold").pack()
Label(f0, text="January 19, 2050", font="lucida 13 bold").pack()
f0.pack()


f1 = Frame(root, width=900, height=200, pady=14)
Label(f1, text=texts[0], padx=22, pady=22).pack(side="left")
Label(f1, image=photos[0], anchor="e").pack()
f1.pack(anchor="w")


f2 = Frame(root, width=900, height=200, pady=14, padx=22)
Label(f2, text=texts[1], padx=22, pady=22).pack(side="right")
Label(f2, image=photos[1], anchor="e", padx=22).pack()
f2.pack(anchor="w")



root.mainloop()



