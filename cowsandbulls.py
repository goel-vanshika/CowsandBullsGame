class RNG():#Random number generator
    import random as rand#importing rand
    flag=1
    while(True):#getting a number that doesn't repeat digits
        flag=1
        n=str(rand.randrange(1000,10000))#random number
        for k in range(4):
            for l in range(4):
                if(n[k]==n[l] and k!=l):
                    flag=0
        if(flag==1):
            break            
    #print("The number to be guessed",n)
    #n="1234"
    n=list(n)
    score=10000
    count=1
s=RNG()#Creating an object of the class
from tkinter import *#importing tkinter
from PIL import Image #importing pillow
#creating buttons
root = Tk() #creates a window
root.title("COWS AND BULLS")
e = Entry(root , width = 60, borderwidth = 5,bg="SkyBlue1")
e.grid(row = 0 , column = 0 , columnspan = 3 , padx = 10, pady = 10)

#The function to print the number of cows and bulls

def cowsbulls(g):
    print("Your guess was",g)
    cows=0
    bulls=0
    if(s.count==26):#Out of attempts 
        e.insert(0,str(s.count)+" Attempts Your score is"+str(s.score))
        img = Image.open('Desktop\lose.jpeg')#Storing the image
        img.show()
           
    else:
        for i in range(4):
            if(s.n[i]==g[i]):
                cows+=1#Cows calculation
        
        if(cows==4):
            e.insert(0,str(s.count)+" Attempt(s) Your score is "+str(s.score))#Correct answer check
            if(s.count==1):#First try check
                img = Image.open('Desktop\perfect.jpg')#Storing the image
                img.show()
            else:
                img = Image.open('Desktop\close.jpeg')#Storing the image
                img.show()
        else:
            for i in range(4):
                for j in range(4):
                    if(s.n[i]==g[j] and i!=j):
                        bulls+=1#Bulls Calculation
            if(cows>0 or bulls>0):#Score check and calculation
                s.score=s.score-(50*bulls)
                s.score=s.score-(25*cows)
            else:
                s.score=s.score-400
            e.insert(0,"Cows: "+str(cows)+"Bulls: "+str(bulls)+" Attempts left: "+str(25-s.count)+" Current Score:"+str(s.score))

#Storing the users input
def click(number):
     current = e.get()
     e.delete(0,END)
     e.insert(0, str(current) + str(number))

#Emptying the entry
def clear():
     e.delete(0,END)

#Guess is now being checked
def equal():
    s_num = e.get()
    e.delete(0, END)
    cowsbulls(s_num)     #calling function
    s.count+=1
     
#define buttons

bt1 = Button(root, text = "1", padx = 60 , pady = 20, command = lambda : click(1),bg="light coral")#callback
bt2 = Button(root, text = "2", padx = 60 , pady = 20, command = lambda : click(2),bg="light coral")#callback
bt3 = Button(root, text = "3", padx = 60 , pady = 20, command = lambda : click(3),bg="light coral")#callback
bt4 = Button(root, text = "4", padx = 60 , pady = 20, command = lambda : click(4),bg="lime green")#callback
bt5 = Button(root, text = "5", padx = 60 , pady = 20, command = lambda : click(5),bg="lime green")#callback
bt6 = Button(root, text = "6", padx = 60 , pady = 20, command = lambda : click(6),bg="lime green")#callback
bt7 = Button(root, text = "7", padx = 60 , pady = 20, command = lambda : click(7),bg="salmon4")#callback
bt8 = Button(root, text = "8", padx = 60 , pady = 20, command = lambda : click(8),bg="salmon4")#callback
bt9 = Button(root, text = "9", padx = 60 , pady = 20, command = lambda : click(9),bg="salmon4")#callback
bt0 = Button(root, text = "0", padx = 60 , pady = 20, command = lambda : click(0),bg="gold")#callback
btEquals = Button(root, text = "=", padx = 200 , pady = 20, command = equal,bg="SpringGreen2")#callback
btClear = Button(root, text = "Clear", padx = 120 , pady = 20, command = clear,bg="gold")#callback

#grid

bt1.grid(row = 3, column = 0,columnspan = 1)
bt2.grid(row = 3, column = 1,columnspan = 1)
bt3.grid(row = 3, column = 2,columnspan = 1)
bt4.grid(row = 2, column = 0,columnspan = 1)
bt5.grid(row = 2, column = 1,columnspan = 1)
bt6.grid(row = 2, column = 2,columnspan = 1)
bt7.grid(row = 1, column = 0,columnspan = 1)
bt8.grid(row = 1, column = 1,columnspan = 1)
bt9.grid(row = 1, column = 2,columnspan = 1)
bt0.grid(row = 4, column = 0 ,columnspan = 1)
btEquals.grid(row = 5,columnspan = 3)
btClear.grid(row = 4, column = 1, columnspan = 2)

root.mainloop()

