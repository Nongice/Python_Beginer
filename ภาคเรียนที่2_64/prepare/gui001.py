from tkinter import *
from tkinter import messagebox
count = 0
# สร้างฟังก์ชั่นเพื่อนับปุ่มกด Create new function for count press button.
def press():    
    global count
    count+=1
    print("Times Press:",count)
    app.title("Python Beginner - You press me with %s times!"%count)
    messagebox.showwarning("Nofications","Hey! You press me {} times.".format(count))

######################################################
app = Tk()
app.geometry("800x600")
app.title("Python Beginner - You press me with %s times!"%count)
button = Button(text='Click Me!',bg="lightgreen",command=press,height=100,width=100)
button.pack(side = TOP, pady = 150)
app.mainloop()
######################################################
