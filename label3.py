from tkinter import*

root = Tk()
photo = PhotoImage(file=r"D:\20251223\dog2.gif")
label = Label(root, image=photo)
label.pack()
root.mainloop()