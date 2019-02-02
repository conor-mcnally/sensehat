from tkinter import *
#key down function

#Main
window = Tk()
window.title("Pixel Art Maker")
window.configure(background="white")



#Photo
photo = PhotoImage(file="ghost2.gif")
Label (window, image=photo, bg="white") .grid(row=0, column=0, sticky=W+E+N+S)
icon = PhotoImage(file="icon.png")
icon2 = PhotoImage(file="icon2.png")
icon3 = PhotoImage(file="icon3.png")

#Text
Label(window, text="Make your own pixel art!", bg="white", fg="black", font="arial 12 bold") .grid(row=1, column=0, sticky=W)

#Exit Function
def close_window():
	window.destroy()
	exit()

#Buttons
def callbackS():
	print("Submit!")
def callbackR():
	print("Reset!")

b1 = Button(window, bg="black", fg="white", compound=TOP, image=icon, text="Submit", command=callbackS, padx=5, pady=5)
b2 = Button(window, bg="black", fg="white", compound=TOP, image=icon2, text="Reset", command=callbackR, padx=5, pady=5)
b3 = Button(window, bg="black", fg="white", compound=TOP, image=icon3, text="Exit", command=close_window, padx=5, pady=5)
b1.config(relief=GROOVE, font="Arial 10")
b2.config(relief=GROOVE, font="Arial 10")
b3.config(relief=GROOVE, font="Arial 10")

b1.grid(row=2, column=2)
b2.grid(row=2, column=3)
b3.grid(row=2, column=4)

#Canvas Drawing
# master = Tk()
# w = Canvas(master, width=200, height=100)
# w.pack()

# w.create_line(0, 0, 200, 100)
# w.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))

# w.create_rectangle(50, 25, 150, 75, fill="red")

#8x8 Grid
#Useful for working out where each row and column is (visualise grid)
# for r in range(8):
# 	for c in range(8):
# 		Label(window, text="R%s/C%s"%(r,c), borderwidth=2).grid(row=r,column=c)
window.geometry('350x350')
#Run the main loop
window.mainloop()
# master.mainloop()
