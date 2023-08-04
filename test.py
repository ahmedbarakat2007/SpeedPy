import pyspeedtest
from tkinter import *
import threading
import webbrowser


def Speed_test():
	test = pyspeedtest.SpeedTest('www.google.com')
	myping.set(test.ping())
	down.set(test.download())

def about():
    def github():
       webbrowser.open('https://github.com/ahmedbarakat2007')
    def web():
       webbrowser.open('https://ahmed-barakat.netlify.com')
    m5 = Tk()
    m5.geometry("200x200")
    m5.resizable(0, 0)
    m5.title("About")
    
    Label(m5, text = "").pack()
    Label(m5, text="Speedpy", font='san-serif 14 bold' ).pack()
    Label(m5, text="Version : 1.0", font='san-serif 10 bold').pack()
    Label(m5, text="Made By Ahmed Barakat", font='san-serif 10 bold').pack()
    m3 = Button(m5, text='Github', font='san-serif 16 bold', bg='purple',fg='white', padx=2,command= github).pack()
    Label(m5).pack()
    m3 = Button(m5, text='My Website', font='san-serif 16 bold', bg='Black',fg='lightgreen', padx=2,command= web).pack()
    
master = Tk()

menubar = Menu(master, background="#16191f", foreground="white")
master.config(menu=menubar)

# create a menu
file_menu = Menu(menubar)

file_menu.add_command(
    label='About',
    command=about
)

file_menu.add_command(
    label='Exit',
    command=master.destroy
)

# add the File menu to the menubar
menubar.add_cascade(
    label="Menu",
    menu=file_menu
)

master.title('Speedpy (Made by Ahmed Barakat)')
master.resizable(0,0)
master.geometry('400x260')
myping = StringVar()
down = IntVar()
Label(master).pack()
Label(master,text='Speedpy', font='san-serif 14 bold').pack()
Label(master,text='Internet Speed Test App').pack()
Label(master).pack()
Label(master, text="Ping Result:").pack()


result = Label(master, text="", textvariable=myping,
			).pack()

Label(master).pack()

Label(master, text="Download Result:").pack()
result2 = Label(master, text="", textvariable=down,
				).pack()
Label(master).pack()

Speed_test()
b = Button(master, text="Retry", command=Speed_test)
b.pack()

mainloop()
