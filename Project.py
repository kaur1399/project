from tkinter import *
from PIL import ImageTk,Image
import cv2
import numpy as np
import datetime

main_window=Tk()
main_window.title("DJ_wale_Babu")
main_window.iconbitmap(r'C:\Users\Lenovo\AppData\Local\Programs\Python\Python37\final_project\app_icon.ico')
main_window.geometry("500x450+390+135")
main_window.resizable(width=False,height=False)
bg=ImageTk.PhotoImage(Image.open(r'C:\Users\Lenovo\AppData\Local\Programs\Python\Python37\final_project\bg.jpg'))
bg_label=Label(main_window,image=bg)
bg_label.place(x=0,y=0,relwidth=1,relheight=1)


def splash_screen():
    splash_window=Toplevel()
    splash_window.wm_overrideredirect(True)#to hide the title bar
    splash_window.geometry("400x40+440+370")
    bg_frame=Frame(splash_window,bg="pink")
    label1=Label(bg_frame,text="Bss Bajna Chaiyeh ganna",font=("Comic Sans MS" , 20 , "bold"),bg="pink")
    label1.pack()
    bg_frame.place(x=0,y=0,relwidth=1,relheight=1)
    
    def main_app():#camera window
        splash_window.destroy()
        
        def snaps():
            image=Image.fromarray(img1)
            time=str(datetime.datetime.now().today()).replace(":","")+".jpg"
            image.save(time)

        cam_window=Toplevel()
        cam_window.iconbitmap(r'C:\Users\Lenovo\AppData\Local\Programs\Python\Python37\final_project\app_icon.ico')
        cam_window.geometry("500x600+390+60")
        cam_window.configure(bg="#9400D3")
        Label(cam_window,text="Help me to guess your Maholl",font=("Comic Sans MS" , 15 , "bold"),fg="black",bg="#9400D3").pack()
        f1=Frame(cam_window,bg="#ADFF2F")
        f1.pack()
        l1=Label(f1,bg="pink")
        l1.pack()
        Button(cam_window,text='Take Snapshot',font=("Comic Sans MS" , 15 , "bold"),fg="black",bg="#9400D3",command=snaps).pack(fill=X,expand=True)


        cam = cv2.VideoCapture(0)



        while True:
            ret , img = cam.read()
            img1=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
            img=ImageTk.PhotoImage(Image.fromarray(img1))
            l1['image']=img
    
    #cv2.imshow("AI EYE",img)

    
            cam_window.update()

        cam.release()



    splash_window.after(2000,main_app)# for closing the splash window
    

launch_button=Button(main_window,text="Launch_App",font=("Comic Sans MS" , 15 , "bold"),bg="yellow",activebackground="orange",command=splash_screen,)
launch_button.place(x=350,y=370)
#hover effect
def onButton(e):
    launch_button['bg']='#00FF00'

def offButton(e):
    launch_button['bg']="yellow"
   
#bind hover effect with button
launch_button.bind('<Enter>',onButton)
launch_button.bind('<Leave>',offButton)

main_window.mainloop()
