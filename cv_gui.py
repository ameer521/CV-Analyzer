from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from ttkthemes import themed_tk as tk
import tkinter.messagebox

#----------title----------#
root = tk.ThemedTk()
root.get_themes()
root.set_theme("radiance")
root.title("CV_Analyzer")

#---------menubar---------#
menubar = Menu(root,activeborderwidth=0)
root.config(menu=menubar,highlightthickness=0)


#--------submenu----------#

subMenu1 = Menu(menubar,tearoff=0)
subMenu2 = Menu(menubar,tearoff=0)
subMenu3 = Menu(menubar,tearoff=0)

def _browse_file():
    filename = filedialog.askopenfilename()
    print(filename)

def _Light_Theme():
    root.configure(bg='#eee')
    subMenu1.configure(bg="#eee",fg='#161b21')
    subMenu2.configure(bg="#eee",fg='#161b21')
    subMenu3.configure(bg="#eee",fg='#161b21')
    list.configure(bg='#eee',borderwidth=0)
    label.configure(bg='#eee', fg='#161b21')
def _Dark_Theme():
    root.configure(bg='#161b21')
    subMenu1.configure(bg="#161b21",fg='#eee')
    subMenu2.configure(bg="#161b21",fg='#eee')
    subMenu3.configure(bg="#161b21",fg='#eee')
    list.configure(bg='#161b21',borderwidth=0)
    label.configure(bg='#161b21',fg='#eee')

def _quit():
    root.quit()

def _about():
    tkinter.messagebox.showinfo('CV_analyzer','Cv_Analyser 1.0   "An ML and NLP implementation"\n\n@ cv.analyzer@gmail.com\n\nVerifies CVs and arrange them according to users requirements.')

menubar.add_cascade(label="File",menu=subMenu1)
subMenu1.add_command(label="Open",command_=_browse_file)
#subMenu1.add_separator()
subMenu1.add_command(label="Exit",command=_quit)

menubar.add_cascade(label="Settings",menu=subMenu2)
subMenu2.add_command(label="Light Theme",command_=_Light_Theme)
subMenu2.add_command(label="Dark Theme",command_=_Dark_Theme)

menubar.add_cascade(label="About",menu=subMenu3)
subMenu3.add_command(label="About CV_Analyzer",command=_about)

#-------windowConfig--------#

root.geometry('700x500')
root.configure(bg='#eee')
root.iconbitmap(r'cv_analyzer.ico')
root.resizable(0, 0)

#listbox
list = Listbox(root, height=15,width=25, borderwidth=0,highlightthickness=0)
list.pack(pady=0,side="left")
list.place(x=13,y=100)
#list.configure(bg="#eee")

#label
var = StringVar()
label = Label( root, textvariable=var)
labelname="CV_Analyzer"
labelname.casefold()
label.configure(font=("Helvetica", "13"))
var.set(labelname+"\n\nA Machine Learning and NLP innovative\n for analysing 'RESUMES' ")
label.pack()
label.place(x=220,y=120)

#Button
b = ttk.Button(root, text="Upload CV",command=_browse_file)
b.pack_propagate(0)
b.place(x=306,y=220)


root.mainloop()


