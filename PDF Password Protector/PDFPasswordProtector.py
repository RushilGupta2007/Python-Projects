from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PyPDF2 import PdfFileWriter, PdfFileReader
import os 

root = Tk()
root.title("PDF Protector")
root.geometry("600x400+300+100")
root.resizable(False,False)

def browse():
    global filename
    filename=filedialog.askopenfilename(initialdir=os.getcwd(), title="Select your PDF file...", filetype=(('PDF File','*.pdf'),('all files','*.*')))
    entry1.insert(END,filename)

def protect():
    mainfile=source.get()
    protectfile=target.get()
    code=password.get()

    if mainfile=="" and protectfile=="" and password.get()=="":
        messagebox.showerror("Invalid","All enteries are empty!!")
    elif mainfile=="":
        messagebox.showerror("Invalid","Please type source PDF filename!")

    elif protectfile=="":
        messagebox.showerror("Invalid","Please type the new name for the file!")

    elif password=="":
        messagebox.showerror("Invalid","Please type the password for the file!")

    else:
        try:
            out=PdfFileWriter()
            file=PdfFileReader(filename)
            num = file.numPages

            for idx in range(num):
                page=file.getPage(idx)
                out.addPage(page)

            out.encrypt(code)
            with open(protectfile, "wb") as f:
                out.write(f)

        except:
            messagebox.showerror("Invalid","Invalid Entry!!")




#Icon
image_icon = PhotoImage(file='C:\\Users\\india\\Desktop\\Python\\Projects\\PDF Password Protector\\icon.png')
root.iconphoto(False,image_icon)

#Main
Top_image = PhotoImage(file="C:\\Users\\india\\Desktop\\Python\\Projects\\PDF Password Protector\\bannerz.png")
Label(root, image=Top_image).pack()

frame = Frame(root, width=580, height=290, bd=5, relief=GROOVE)
frame.place(x=10,y=110)

########
source = StringVar()
Label(frame,text="Source PDF File: ",font="king 12 normal",fg="#4c4542").place(x=30,y = 30)
entry1 = Entry(frame,width=20,textvariable=source,font="king 17",bd=1)
entry1.place(x=200,y=28)

Button_icon = PhotoImage(file="C:\\Users\\india\\Desktop\\Python\\Projects\\PDF Password Protector\\folder.png")
Button(frame,image=Button_icon,width=35,height=24,bg="#d3cdcd",command=browse).place(x=500, y=27)


target = StringVar()
Label(frame,text="Target PDF File: ",font="king 12 normal",fg="#4c4542").place(x=30,y = 80)
entry2 = Entry(frame,width=20,textvariable=target,font="king 17",bd=1)
entry2.place(x=200,y=80)


password = StringVar()
Label(frame,text="Set User Password: ",font="king 12 normal",fg="#4c4542").place(x=15,y = 130)
entry3 = Entry(frame,width=20,textvariable=password,font="king 17",bd=1)
entry3.place(x=200,y=130)


button_icon = PhotoImage(file="C:\\Users\\india\\Desktop\\Python\\Projects\\PDF Password Protector\\icon.png")
protect=Button(root,text="Protect PDF File",compound=LEFT,image=button_icon,width=230,height=50,bg="#bfb9b9",font="king 14",command=protect)
protect.pack(side=BOTTOM,pady=40)


root.mainloop()
