from tkinter import *
import base64
options = ['Encode','Decode']

root = Tk()
root.title("ENCRYPTOR")
root.geometry('500x300')
root.resizable(0,0)



vari = StringVar()
Text = StringVar()
p_key =StringVar()
modee = StringVar()
result = StringVar()




def encode(keyy,message):
    enc  =[]
    print(message)
    for i in range(len(message)):
        key_c = keyy[i % len(keyy)]
        enc.append(chr((ord(message[i]) + ord(key_c)) % 256))
        
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()
        
def Decode(keyy,message):
    dec=[]
    message = base64.urlsafe_b64decode(message).decode()

    for i in range(len(message)):
        key_c = keyy[i % len(keyy)]
        dec.append(chr((256 + ord(message[i])- ord(key_c)) % 256))
    return "".join(dec)
def moode():
    m = vari.get()
    if m == 'Encode':
        result.set(encode(p_key.get(), Text.get()))
    else:
        result.set(Decode(p_key.get(), Text.get()))
        






heading = Label(root,text='Encryptor',fg = '#57a1f8',bg = 'black',font=('Microsoft YaHei VI Light',23,'bold'))
heading.pack()

footer = Label(root,text = 'harvis lab',fg = 'black',bg = 'white',font = ('Calibri(Body)',12))
footer.pack(side = BOTTOM)
#############################################################################################################
input_text =Label(root,text = "MESSAGE INPUT *",fg = 'white',bg = 'blue',font = ("Calibri(Body)",13,'bold'))
input_text.place(x = 50,y = 75)
Text = Entry(root,width = 25,fg = 'white',bg = 'blue',font = ('Calibri(Body)',13))
Text.place(x = 280,y = 75)

############################################################################################################

keyy = Label(root,text = 'ENCRYPTION KEY',fg ='white',bg = 'blue',font = ('Calibri(Body)',13,'bold'))
keyy.place(x = 50,y = 125)
p_key = Entry(root,width = 25,fg = 'white',bg  ='blue',font = ('Calibri(Body)',13,'bold'))
p_key.place(x = 280,y = 125)

############################################################################################################

mode = Label(root,text = "Encode or Decode",fg = 'white',bg = 'blue',font = ('Calibri(Body)',13,'bold'))
mode.place(x = 50,y = 175)

vari = StringVar()
vari.set(options[0])

mode_m = OptionMenu(root,vari,*options)
mode_m.place(x = 280,y = 175)
##########################################################################################################
Entry(root, font = 'arial 10 bold', textvariable = result, bg ='ghost white').place(x=290, y = 230)

Btn = Button(root,text = "Process",width = 7,cursor = "hand2",fg = "white",bg = 'blue',font = ('Calibri(Body)',12,'bold'),command = moode)
Btn.place(x = 50,y = 270)










root.mainloop()

