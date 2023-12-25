from tkinter import *
from PIL import Image,ImageTk
root=Tk()
root.geometry("500x500")

label1=Label(text="Muhammad[a] (Arabic: مُحَمَّد, romanized: Muḥammad; English: /\nmoʊˈhɑːməd/; Arabic: [mʊˈħæm.mæd]; c. 570 – 8 June 632 CE)[b] was an Arab \nreligious, social, and political leader and the founder of Islam.[c] According \nto Islamic doctrine, he was a prophet divinely inspired to preach and confirm \nthe monotheistic teachings of Adam, Abraham, Moses, Jesus, and other prophets.\n[2][3][4] He is believed to be the Seal of the Prophets within Islam, with the \nQuran as well as his teachings and practices forming the basis for Islamic \nreligious belief.",bg="yellow",fg="red",pady=200,font="comicscansms 19 bold",borderwidth=10,relief=SUNKEN)

label1.pack(side="left",padx=50)

root.mainloop()