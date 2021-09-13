from os import error, terminal_size
from tkinter import ttk
from tkinter import *               #All Tkinter Functions
import tkinter as tk                # Tkinter As tk
from tkinter import font,messagebox # font and Message box
from tkinter.font import BOLD
import PIL                          # for image processing
from PIL import Image,ImageTk
import subprocess
from tkinter.filedialog import asksaveasfilename,askopenfilename
import time

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Basic Shortkeys for IDE


#Label_info=Label(info_window,bg="Black",text="Basic Information For Using Coder IDE\nSome Shortkeys You can use in IDE\nUse ctrl + s for Saving File\nUse ctrl + o for opening Files\nUse Ctrl + r for Run Program ",fg="White",font=("Arial Bold",15))
#Label_info.place(height=300,width=400,)

#window.after(10000,info_window.destroy())

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------

window=Tk()
window.title("Coder")#window title
window.config(bg="black")#window Background
#window.attributes('-fullscreen', True)

width= window.winfo_screenwidth()#get window width
height= window.winfo_screenheight()               #get window height
window.geometry("%dx%d" % (width, height))  #set GUI window size according to device window size 
window.maxsize(width,height)#Can't change window size
window.minsize(width,height)#Can't change window size

main_path=''    #for storing file path of current working file
global recent_open_files
recent_open_files=[]


#Function

def set_file_path(path):#Create function for storing path to use in all function
    global recent_open_files
    global main_path
    main_path=path
    recent_open_files.append(main_path)

def Help_shortkeys():
    messagebox.showinfo("Shortcut Keys","Basic Information For Using Coder IDE\nSome Shortkeys You can use in IDE\nUse ctrl + s for Saving File\nUse ctrl + o for opening Files\nUse Ctrl + r for Run Program ",)

def open_file(event=""):#Create function for opeaning file 

    path=askopenfilename(title = "Select file",filetypes = [("Python Files","*.py")])#ask user to open file
    try:
        with open(path,'r') as file_open:#open and read file 
            code=file_open.read()#get file data
            coding_text_box.delete('1.0',END)#Clear text box
            coding_text_box.insert('1.0',code)#insert data in text box
            output_terminal.delete('1.0',END)#clear output box
            set_file_path(path)#send file path into main file path
            window.title(f"Coder {main_path}")#change window title and update 
            for i in range(1):
                sub_menu.add_command(label=path)#add recent file path into menu's submenu
    except:
        print("An Error!!")# show error in an error is there
        pass


def save_as(event=""):
    if main_path=='':
        path=asksaveasfilename(title = "Select file",filetypes = (("All Files","*.*"),("Text Files","*.txt"),("Python Files","*.py")))
    else:
        path=main_path
    for i in range(1):

        try:

            with open(path,'w') as file:
                code=coding_text_box.get('1.0',END)
                file.write(code)
                set_file_path(path)
        except:
            continue



def run_code(event=""):
    try:            
        if main_path=='':
            messagebox.showerror("Error","Save File!")
            save_as()
            set_file_path(main_path)
            window.title(f"Coder {main_path}")
        

        cmd= f'python {main_path}'
        process=subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
        output,error=process.communicate()
        output_terminal.insert('1.0',output)
        output_terminal.insert('1.0',error)
    except:
        pass

def debug():            
        cmd= f'python {main_path}'
        process=subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
        output,error=process.communicate()
        messagebox.showinfo("Debugging Error",error)


def Help_user(event=""):
    messagebox.showinfo("Help","Hey User, This is Basic IDE, and It is Made by Dhruv.if any error is here so Please Contact us on Telegram. Thanks for using our IDE...")

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------

#change Icon of Window
photo = PhotoImage(file ="D:\\Ashu_Documents\\Python_Ashu_Files\\GUI_Code_Editor\\logo.png")
window.iconphoto(False, photo)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------

#creat menu in project

menu=Menu(window,background='#ff8000', foreground='black',
activebackground='#374140', activeforeground='black',font=("Arial"),relief=RAISED)

file = Menu(menu, tearoff=0,font=("Arial"),borderwidth=2)
file.add_command(label="New",command=save_as)  
file.add_command(label="Open",command=open_file)
menu.add_cascade(label="File", menu=file,background="red")

#recent Open files Manager
sub_menu = Menu(file, tearoff=0)
file.add_cascade(label="Recent Open Files",menu=sub_menu)


save = Menu(menu,tearoff=0,activeforeground='black',font=("Arial"))
save.add_command(label="Save",command=save_as)
save.add_command(label="Save as...",command=save_as)  
save.add_command(label="Close")
menu.add_cascade(label="Save", menu=save,background="red",font=("Arial"))

#save.add_separator() 
#save.add_command(label="Exit", command=window.quit)

run=Menu(menu,tearoff=0,activebackground='black',font=("Arial"),borderwidth=2)
run.add_command(label="Run",command=run_code)#ommand=Run_Code)
run.add_command(label="Run F5",command=run_code)
run.add_command(label="Start Debugging F5",command=debug)

menu.add_cascade(label="Run",menu=run,background="black")

Help=Menu(menu,tearoff=0,activebackground='black',font=("Arial"),borderwidth=2)
Help.add_command(label="Help",command=Help_user)
Help.add_command(label="Short Key",command=Help_shortkeys)
menu.add_cascade(menu=Help,label="Help",)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Text Widget

coding_text_box=Text(window,bg="white",font=("Arial Bold",15))
coding_text_box.place(x=20,height=540,width=1510)

#Out Box
#terminal=Text(window,bg="white",fg="black",font=("Arial Bold",15),bd=2,relief=SUNKEN)
#terminal.place(x=50,y=550,height=250,width=1200)

output_terminal=Text(height=3,font=("Arial" "Bold",15),bd=2,relief=SUNKEN)
output_terminal.place(x=0,y=550,height=250,width=1520)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Bind ShortKeys
window.bind('<Control-r>',run_code)
window.bind('<F5>',run_code)
window.bind('<Control-o>',open_file)
window.bind('<Control-s>',save_as)
window.bind('<Control-h>',Help_user)

# attach both textbox to scrollbar

scrollbar = Scrollbar(coding_text_box)
scrollbar.pack(side=RIGHT, fill=Y)
coding_text_box.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=coding_text_box.yview)

scrollbar=Scrollbar(output_terminal)
scrollbar.pack(side=RIGHT,fill=Y)
output_terminal.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=output_terminal.yview)




#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
window.config(menu=menu)
mainloop()


