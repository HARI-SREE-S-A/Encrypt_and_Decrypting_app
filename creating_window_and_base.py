root = Tk()
root.geometry('500x300')
root.title("Encryptor")
root.resizable(0,0)


heading = Label(root,text = "Encryptor",fg = "white",bg = "blue",font = ("Calibri(Body)",22,'bold'))
heading.pack()
                
footer = Label(root,text = "harvis labs",bg = "white",fg = "black",font = ("Calibri(Body)",10,'bold'))
footer.pack(side = 'BOTTOM')



root.mainloop()
