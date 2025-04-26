from tkinter import *
window=Tk()
bgc="#B1DDC6"
window.title("Flash Card")

window.config(padx=50,pady=50,bg=bgc)
canvas=Canvas(width=800,height=526)

cardimg=PhotoImage(file="card_front.png")
canvas.create_image(400,263,image=cardimg)
canvas.config(bg=bgc,highlightthickness=0)
canvas.create_text(400,150,text="Hello",font=("Ariel",40))
canvas.grid(row=0,column=0)















window.mainloop()

