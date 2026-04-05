from tkinter import *
import os
def restart():
    os.system("shutdown /r /t 1")
def shutdown():
    os.system("shutdown /s /t 1")
def logout():
    os.system("shutdown -1")

st = Tk()
st.title("ShutDown App")
st.geometry("400x500")
st.config(bg="blue",)
r_button = Button(st,text="Restart",font=("Time New Roman",23,"bold"),relief=RAISED,cursor="plus",command=restart)
r_button.place(x=125,y=50,height=40,width=150)

s_button = Button(st,text="ShutDown",font=("Time New Roman",20,"bold"),relief=RAISED,cursor="plus",command=shutdown)
s_button.place(x=125,y=140,height=40,width=150)

lg_button = Button(st,text="Logout",font=("Time New Roman",23,"bold"),relief=RAISED,cursor="plus",command=logout)
lg_button.place(x=125,y=230,height=40,width=150)



st.mainloop()
