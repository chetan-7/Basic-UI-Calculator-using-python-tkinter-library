from tkinter import *
def btnClick(num):
    global operator     #This variable is accesible everywhere throghout the code.
    #operator=""
    operator=operator+str(num)
    text_input.set(operator)  #putting the value of as user clicking button to display.
def btnClearDisplay():
    global operator
    operator=""
    text_input.set(operator)
    #text_input.set("")  #Clearing the display screen.
def btnEqualOperator():
    global operator
    sumup=str(eval(operator))
    print(sumup)
    text_input.set(sumup)
    operator=""

cal=Tk()
cal.title('Calculator')#assignung title to window
operator=""      #type of operator is string
text_input=StringVar()   #for input the value to screen
txtDisplay=Entry(cal,font=('arial',20,'bold'),textvariable=text_input,bd=30,insertwidth=4,bg="Orange",justify='right').grid(columnspan=4)#bd=border,bg=background_colour,grid=placing
but7=Button(cal,padx=20,bd=8,fg="black",command=lambda :btnClick(7),font=('arial',20,'bold'),text="7").grid(row=1,column=0)#padx is for area to cover in x-axis.
but8=Button(cal,padx=20,bd=8,fg="black",command=lambda :btnClick(8),font=('arial',20,'bold'),text="8").grid(row=1,column=1)
but9=Button(cal,padx=20,bd=8,fg="black",command=lambda :btnClick(9),font=('arial',20,'bold'),text="9").grid(row=1,column=2)
but4=Button(cal,padx=20,bd=8,fg="black",command=lambda :btnClick(4),font=('arial',20,'bold'),text="4").grid(row=2,column=0)
but5=Button(cal,padx=20,bd=8,fg="black",command=lambda :btnClick(5),font=('arial',20,'bold'),text="5").grid(row=2,column=1)
but6=Button(cal,padx=20,bd=8,fg="black",command=lambda :btnClick(6),font=('arial',20,'bold'),text="6").grid(row=2,column=2)
but1=Button(cal,padx=20,bd=8,fg="black",command=lambda :btnClick(1),font=('arial',20,'bold'),text="1").grid(row=3,column=0)
but2=Button(cal,padx=20,bd=8,fg="black",command=lambda :btnClick(2),font=('arial',20,'bold'),text="2").grid(row=3,column=1)
but3=Button(cal,padx=20,bd=8,fg="black",command=lambda :btnClick(3),font=('arial',20,'bold'),text="3").grid(row=3,column=2)
ADD=Button(cal,padx=20,bd=8,fg="black",command=lambda :btnClick("+"),font=('arial',20,'bold'),text="+").grid(row=1,column=3)
SUB=Button(cal,padx=20,bd=8,fg="black",command=lambda :btnClick("-"),font=('arial',20,'bold'),text="-").grid(row=2,column=3)
MUL=Button(cal,padx=20,bd=8,fg="black",command=lambda :btnClick("*"),font=('arial',20,'bold'),text="*").grid(row=3,column=3)
but0=Button(cal,padx=20,bd=8,fg="black",command=lambda :btnClick(0),font=('arial',20,'bold'),text="0").grid(row=4,column=0)
butC=Button(cal,padx=20,bd=8,fg="black",command=btnClearDisplay,font=('arial',20,'bold'),text="C").grid(row=4,column=1)
butEQUAL=Button(cal,padx=20,bd=8,fg="black",command=btnEqualOperator,font=('arial',20,'bold'),text="=").grid(row=4,column=2)
DIV=Button(cal,padx=20,bd=8,fg="black",command=lambda :btnClick("/"),font=('arial',20,'bold'),text="/").grid(row=4,column=3)
cal.mainloop()