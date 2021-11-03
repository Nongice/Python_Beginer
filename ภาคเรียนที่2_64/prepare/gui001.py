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
def reset():
    global count
    if count > 1:
        count = 0
        print("Reset to:",count)
        app.title("Python Beginner - You press me with %s times!"%count)
        messagebox.showinfo("Nofications","Hey! You are reset.")
    else:
        messagebox.showerror("Nofications","Hey! You can't reset with 0 press time.")
######################################################
app = Tk()
app.geometry("800x600")
app.title("Python Beginner - You press me with %s times!"%count)
btn_plus_count = Button(text='Click Me!',bg="lightgreen",command=press,height=100,width=100)
btn_reset_count = Button(text='Reset',bg="red",command=reset).pack(side=BOTTOM, pady=7)
btn_plus_count.pack(side = TOP, pady = 150)
app.mainloop()
######################################################
