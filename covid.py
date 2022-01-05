from tkinter import *
import tkinter as tk
import tkinter.font as font
import tkinter.ttk as ttk
from tkinter import *
import os
import sys
from PIL import Image, ImageTk
import time
import tkinter
##import webbrowser
import csv
from tkinter import messagebox

window = tk.Tk()
window.title("WELCOME")
window.geometry('1920x923')

##

##window.configure(background ="light green")
ima = PhotoImage(file = 'C:\\Users\\sredd\\OneDrive\\Desktop\\covid\\main.png')
label = tk.Label(window, image = ima)


lb1=tk.Label(window, text="Covid Detection using CNN ",font=("Avro",34,"bold","italic"),foreground="black",bg="white")
lb1.place(x=480,y=50)
lb2=tk.Label(window, text=" One of the crucial step in fighting COVID-19 is the ability to detect the infected patients ",font=("Century Gothic",14,"bold","italic"),foreground="black",bg="white")
lb2.place(x=50,y=300)
lb2=tk.Label(window, text=" early enough & put them under special care. The COVID-19 pandemic is causing a major outbreak  ",font=("Century Gothic",14,"bold","italic"),foreground="black",bg="white")
lb2.place(x=50,y=350)
lb2=tk.Label(window, text=" in more than 150 countries around the world. Having a severe impact on the health and life of many people globally. ",font=("Century Gothic",14,"bold","italic"),foreground="black",bg="white")
lb2.place(x=50,y=400)
# lb2=tk.Label(window, text=" One of the crucial step in fighting COVID-19 is the ability to detect the infected patients early enough & put them under special care.  ",font=("Century Gothic",14,"bold","italic"),foreground="black",bg="white")
# lb2.place(x=50,y=250)

# lb1=tk.Label(window, text="The COVID-19 pandemic is causing a major outbreak in more than 150 countries around the world...",font=("Century Gothic",14,"bold","italic"),foreground="black",bg="white")
# lb1.place(x=50,y=435)

# lb3=tk.Label(window, text="Having a severe impact on the health and life of many people globally... ",font=("Century Gothic",14,"bold","italic"),foreground="black",bg="white")
# lb3.place(x=50,y=470)
def login1():
    messagebox.showinfo("welcome","Login Successfully")
      
    print("Login Successfully")
    os.system("python covid1.py")

def fun1():
    os.system("python regi.py")




##    window = tk.Toplevel()
##    window.title("WELCOME")
##    window.geometry('1280x800')
##    ##window.configure(background ="light green")
##    ima = PhotoImage(file = 'C:\\Users\\sredd\\OneDrive\\Desktop\\covid\\dd.png')
##    label = tk.Label(window, image = ima)
##
##
##    lb1=tk.Label(window, text="User Name ",font=("Century Gothic",22,"bold","italic"),foreground="white",bg="black")
##    lb1.place(x=50,y=100)
##    
##    entry_1=Entry(window,text="",font=("Century Gothic",12,"bold","italic"),foreground="black",bg="white")
##    entry_1.place(x=250,y=100)
##
##    lb1=tk.Label(window, text="Password ",font=("Century Gothic",22,"bold","italic"),foreground="white",bg="black")
##    lb1.place(x=50,y=200)
##    
##    
##    entry_2=Entry(window,text="",show='*',font=("Century Gothic",12,"bold","italic"),foreground="black",bg="white")
##    entry_2.place(x=250,y=200)
##
##    def fun():
##        os.system("python frnt.py")
##
##    def submit():
##        print("Login Successfully")
##        
##        User=(entry_1.get())
##        Password=(entry_2.get())
##        
##        row=[User,Password]
##        with open("File.csv",'a+')as csvFile:
##            writer=csv.writer(csvFile)
##            writer.writerow(row)
##            csvFile.close()
##   
##
##    
##    # button1=Button(window,text="Submit",command=submit,width=8,font=("Century Gothic",24,"bold","italic"),foreground="white",bg="black")
##    # button1.place(x=50,y=300)
##
##    button1=Button(window,text="Login",command=login1,width=8,font=("Century Gothic",24,"bold","italic"),foreground="white",bg="black")
##    button1.place(x=250,y=300)
######
###### 
##    label.pack()
##    window.mainloop()  
##
##
##    

button1=Button(window,text="Login",command =fun1,font=("Century Gothic",14,"bold","italic"),foreground="white",background="green")
button1.place(x=300,y=150)







def fun():
        
        os.system("python frnt.py")   

# button1=Button(window,text="Detection",command=fun,font=("Century Gothic",14,"bold","italic"),foreground="white",background="red2")
# button1.place(x=600,y=150)


def about():
    
    window = tk.Toplevel()
    window.title("WELCOME")
    window.geometry('3000x3000')
    

    ##

    ##window.configure(background ="light green")
    ima = PhotoImage(file = 'C:\\Users\\sredd\\OneDrive\\Desktop\\covid\\18.png')
    label = tk.Label(window, image = ima)
    
    def covid():
        lb1=tk.Label(window, text="Clean your hands often. Use soap and water, or an alcohol-based hand rub.",font=("Century Gothic",20,"bold","italic"),foreground="black")
        lb1.place(x=300,y=300)
        lb1=tk.Label(window, text="Maintain a safe distance from anyone who is coughing or sneezing.",font=("Century Gothic",20,"bold","italic"),foreground="black")
        lb1.place(x=300,y=350)
        lb1=tk.Label(window, text="Wear a mask when physical distancing is not possible.",font=("Century Gothic",20,"bold","italic"),foreground="black")
        lb1.place(x=300,y=400)
        lb1=tk.Label(window, text="Cover your nose and mouth with your bent elbow or a tissue when you cough or sneeze.",font=("Century Gothic",20,"bold","italic"),foreground="black")
        lb1.place(x=300,y=450)
        lb2=tk.Label(window, text="If you have a fever, cough and difficulty breathing, seek medical attention." ,font=("Century Gothic",20,"bold","italic"),foreground="black")
        lb2.place(x=300,y=500)
        lb2=tk.Label(window, text="Stay home if you feel unwell. Stay home, stay safe." ,font=("Century Gothic",20,"bold","italic"),foreground="black")
        lb2.place(x=300,y=550)
        
        button2=Button(window,text="Click Here To Exit",command=window.destroy,font=("Century Gothic",18,"bold","italic"),foreground="white",background="red")
        button2.place(x=1200,y=650)


        

    button1=Button(window,text="Safety Measures",command=covid,font=("Century Gothic",18,"bold","italic"),foreground="white",background="green")
    button1.place(x=300,y=200)



    label.pack()
    window.mainloop()






        
    





button1=Button(window,text="Precautions",command=about,font=("Century Gothic",14,"bold","italic"),foreground="white",background="blue3")
button1.place(x=700,y=150)



def faq():
    
    window = tk.Toplevel()
    window.title("WELCOME")
    window.geometry('3000x3000')
    

    ##

    ##window.configure(background ="light green")
    ima = PhotoImage(file = 'C:\\Users\\sredd\\OneDrive\\Desktop\\covid\\img1.png')
    label = tk.Label(window, image = ima)
    def question1():
        lb1=tk.Label(window, text="Register on the Co-WIN Portal https://www.cowin.gov.in/home",font=("Century Gothic",14,"bold","italic"),foreground="black")
        lb1.place(x=600,y=200)
    def question2():
        
        lb2=tk.Label(window, text="Two vaccines that have been granted emergency use authorization by the Central Drugs",font=("Century Gothic",14,"bold","italic"),foreground="black")
        lb2.place(x=100,y=300)
        lb2=tk.Label(window, text="Standard Control Organization (CDSCO) in India are Covishield® (AstraZeneca'smanufactured by Serum Institute of India)",font=("Century Gothic",14,"bold","italic"),foreground="black")
        lb2.place(x=100,y=330)
       
       
       
       
    
   
    # lb1=tk.Label(window, text="FAQ",font=("Century Gothic",24,"bold","italic"),foreground="black")
    # lb1.place(x=1200,y=150)
    
        
    button1=Button(window,text="Where should I register for the vaccination?",command=question1,font=("Century Gothic",14,"bold","italic"),foreground="black")
    button1.place(x=600,y=100)
    button2=Button(window,text="Which COVID-19 vaccines are licensed in India?",command=question2,font=("Century Gothic",14,"bold","italic"),foreground="black")
    button2.place(x=100,y=100)
    button3=Button(window,text="Click here to Exit",command=window.destroy,font=("Century Gothic",14,"bold","italic"),foreground="black")
    button3.place(x=1000,y=500)
    

    label.pack()
    window.mainloop()





    
button1=Button(window,text="FAQ",command=faq,font=("Century Gothic",14,"bold","italic"),foreground="white",background="royal blue")
button1.place(x=1200,y=150)



button1=Button(window,text="Click here to Exit",command =window.destroy,font=("Century Gothic",18,"bold","italic"),foreground="white",background="red")
button1.place(x=1200,y=450)
label.pack()
window.mainloop()
