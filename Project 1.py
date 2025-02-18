from tkinter import *
from tkinter import filedialog

root=Tk()
root.geometry("200x160")

def encrypt_image():
    file1=filedialog.askopenfile(mode='r', filetype=[('png files','*.png')])
    if file1 is not None:
        #print(file1)
        file_name=file1.name
        #print(file_name)
        key=entry1.get("1.0",'end-1c')
        print(file_name,key)
        f1=open(file_name,'rb')
        image=f1.read()
        f1.close()
        image=bytearray(image)
        for index,value in enumerate(image):
            image[index]=value^ord(key[index%len(key)])
        f2=open(file_name,'wb')
        f2.write(image)
        f2.close()




b1=Button(root,text="encrypt",command=encrypt_image)
b1.place(x=70,y=10)

entry1=Text(root,height=1,width=10)
entry1.place(x=50,y=50)

root.mainloop()