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
