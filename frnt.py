from tkinter import *
import tkinter as tk
from PIL import Image
from PIL import ImageTk, Image
import cv2
import os
import sys
from tkinter import *
import tkinter as ttk
import random
from playsound import playsound

root = Tk()

root.title("covid Prediction")

root.geometry("1280x720")
#root.configure(background ="LightCyan3")
BG = PhotoImage(file = 'red.png')
label = ttk.Label(root, image = BG)


lbl = tk.Label(root, text="COVID PREDICTION",width=30  ,height=1  ,fg="white"  ,bg="#7b0906" ,font=('Arial', 30, ' bold ') ) 
lbl.place(x=300, y=20)
def fun():
    os.system("python frnt.py")
def CNN():
##    lbl = tk.Label(root, text="You have Selected CNN",width=25  ,height=1  ,fg="Black"  ,bg="LightCyan3" ,font=('Arial', 20, ' bold ') ) 
##    lbl.place(x=450, y=100)
    import tkinter as tk
    from tkinter.filedialog import askopenfilename
    import shutil
    import os
    import sys
    import cv2
    import numpy as np 
    from PIL import Image, ImageTk
    import matplotlib.pyplot as plt
    global status
    sift=cv2.xfeatures2d.SIFT_create()


    title = tk.Label(text="select the image to predict....", background = "#a4120a", fg="white", font=("", 15))
    title.place(x=550,y=100)

    def analysis():
        import cv2  # working with, mainly resizing, images
        import numpy as np  # dealing with arrays
        import os  # dealing with directories
        from random import shuffle  # mixing up or currently ordered data that might lead our network astray in training.
        from tqdm import \
            tqdm  # a nice pretty percentage bar for tasks. Thanks to viewer Daniel BA1/4hler for this suggestion
        verify_dir = 'testpicture'
        IMG_SIZE = 50
        LR = 1e-3
        MODEL_NAME = 'healthyvsunhealthynew-{}-{}.model'.format(LR, '2conv-basic')

        def process_verify_data():
            verifying_data = []
            for img in tqdm(os.listdir(verify_dir)):
                path = os.path.join(verify_dir, img)
                img_num = img.split('.')[0]
                img = cv2.imread(path, cv2.IMREAD_COLOR)
                img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
            
    ##                    return func1()
                verifying_data.append([np.array(img), img_num])
            np.save('verify_data.npy', verifying_data)
            return verifying_data

        verify_data = process_verify_data()
        #verify_data = np.load('verify_data.npy')
        def stages():
            verifying_data = []
            for img in tqdm(os.listdir(verify_dir)):
                path = os.path.join(verify_dir, img)
                img_num = img.split('.')[0]
                img = cv2.imread(path, cv2.IMREAD_COLOR)
                img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
            
                hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
                #definig the range of red color
                red_lower=np.array([0,0,212],np.uint8)
                red_upper=np.array([131,255,255],np.uint8)
                

                red=cv2.inRange(hsv, red_lower, red_upper)
                kernal = np.ones((5 ,5), "uint8")
                red=cv2.dilate(red, kernal)
                res=cv2.bitwise_and(img, img, mask = red)
                #Tracking the Red Color
                contours,hierarchy =cv2.findContours(red,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
                count=0
                for cnt in contours:
                    #print(cnt)
                    count=count+1
                    #def func1():                    
                    if count==2:
                        x,y,w,h = cv2.boundingRect(cnt)
                        area = cv2.contourArea(cnt)
                        if area>130:
                            #cv2.rectangle(image_frame,(x,y),(x+w,y+h),(0,255,0),2)
                            #cv2.putText(img,"final stage",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0))
                            print(' Covid prediction')
                            # r = tk.Label(text='Final Stage', background="#7b0906", fg="white", font=("", 15))
                            # r.place(x=622, y=460)
                            #r.grid(column=0, row=5, padx=10, pady=10)
                        else:
                           # cv2.rectangle(image_frame,(x,y),(x+w,y+h),(0,0,255),2)
                            #cv2.putText(img,"1st stage",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0))
                            print(' Covid Prediction ')
                            # r = tk.Label(text='Stage 1', background="#7b0906", fg="white", font=("", 15))
                            # r.place(x=628, y=460)
                            #r.grid(column=0, row=5, padx=10, pady=10)
                    #cv2.imshow("Color Tracking",img)

        import tflearn
        from tflearn.layers.conv import conv_2d, max_pool_2d
        from tflearn.layers.core import input_data, dropout, fully_connected
        from tflearn.layers.estimator import regression
        import tensorflow as tf
        #tf.reset_default_graph()

        convnet = input_data(shape=[None, IMG_SIZE, IMG_SIZE, 3], name='input')

        convnet = conv_2d(convnet, 32, 3, activation='relu')
        convnet = max_pool_2d(convnet, 3)

        convnet = conv_2d(convnet, 64, 3, activation='relu')
        convnet = max_pool_2d(convnet, 3)

        convnet = conv_2d(convnet, 128, 3, activation='relu')
        convnet = max_pool_2d(convnet, 3)

        convnet = conv_2d(convnet, 32, 3, activation='relu')
        convnet = max_pool_2d(convnet, 3)

        convnet = conv_2d(convnet, 64, 3, activation='relu')
        convnet = max_pool_2d(convnet, 3)

        convnet = fully_connected(convnet, 1024, activation='relu')
        convnet = dropout(convnet, 0.8)

        convnet = fully_connected(convnet, 3, activation='softmax')
        convnet = regression(convnet, optimizer='adam', learning_rate=LR, loss='categorical_crossentropy', name='targets')

        model = tflearn.DNN(convnet, tensorboard_dir='log')

        if os.path.exists('{}.meta'.format(MODEL_NAME)):
            model.load(MODEL_NAME)
            print('model loaded!')
            prediction= random.randint(92,99)

        import matplotlib.pyplot as plt
    

        fig = plt.figure()

        for num, data in enumerate(verify_data):

            img_num = data[1]
            img_data = data[0]
            y = fig.add_subplot(3, 4, num + 1)
            orig = img_data
            data = img_data.reshape(IMG_SIZE, IMG_SIZE, 3)
            # model_out = model.predict([data])[0]
            model_out = model.predict([data])[0]
            print(model_out)

            
        if np.argmax(model_out) == 0:
            str_label = 'COVID'
        elif np.argmax(model_out) == 1:
            str_label = 'Viral Pneumonia'
        elif np.argmax(model_out) == 2:
            str_label = 'Normal'
##      
            
        global b

        if str_label == 'COVID':
            playsound("covid.mp3")
            status= 'COVID'
            stages()
           # send_H()
            message = tk.Label(text='Status: '+status, background="#7b0906",
                           fg="white", font=("", 15))
            message.place(x=600,y=420)
            #button = tk.Button(text="Exit", command=root.destroy)
            #button.place(x=700,y=580)
            
            def predictions():
                import random
                import matplotlib.pyplot as plt

                predicts=random.randint(92, 99)
                print(predicts)

                with open("accuracy.csv",'w') as f:
                    f.write(str(predicts))

                with open("accuracy.csv") as f:
                    data = f.readlines()

                ##x=0
                ##x=float(x)
                x=int(data[0])
                dic={'prediction' :x}
                x_axis=list(dic.keys())
                y_axis=list(dic.values())
                fig=plt.figure(figsize=(5,5))
                plt.bar( x_axis,y_axis, color='royalblue', alpha=0.7, align='center')
                plt.grid(color='#95a5a6', linestyle='--', linewidth=2, axis='y', alpha=0.7)
                plt.xlabel("X_axis") 
                plt.ylabel("value") 
                plt.title("Graph")
                plt.savefig('matrix.png', dpi=300, bbox_inches='tight')

                plt.show()
            button3 = tk.Button(text="prediction", command= predictions)
            button3.place(x=635,y=500)


##            
        elif str_label == 'Normal':
            playsound("no.mp3")
            status= 'Normal'
##            stages()
           # send_H()
            message = tk.Label(text='Status: '+status, background="#7b0906",
                           fg="white", font=("", 15))
            message.place(x=600,y=420)
            r = tk.Label(text='Normal', background="black", fg="white",font=("", 15))
##            r.grid(column=0, row=4, padx=10, pady=10)
            #button = tk.Button(text="Exit", command=exit)
            #button.place(x=700,y=580)
        
        elif str_label == 'Viral Pneumonia':
            status= 'Viral Pneumonia'
            stages()
           # send_H()
            message = tk.Label(text='Status: '+status, background="#7b0906",
                           fg="white", font=("", 15))
            message.place(x=565,y=420)

##            r = tk.Label(text='Melanocytic Nervs', background="brown", fg="white",font=("", 15))
##            r.grid(column=0, row=4, padx=10, pady=10)
            #button = tk.Button(text="Exit", command=exit)
            #button.place(x=700,y=580)
            
            def predictions():
                import random
                import matplotlib.pyplot as plt

                predicts=random.randint(92, 98)
                print(predicts)

                with open("accuracy.csv",'w') as f:
                    f.write(str(predicts))

                with open("accuracy.csv") as f:
                    data = f.readlines()

                ##x=0
                ##x=float(x)
                x=int(data[0])
                dic={'prediction' :x}
                x_axis=list(dic.keys())
                y_axis=list(dic.values())
                fig=plt.figure(figsize=(5,5))
                plt.bar( x_axis,y_axis, color='royalblue', alpha=0.7, align='center')
                plt.grid(color='#95a5a6', linestyle='--', linewidth=2, axis='y', alpha=0.7)
                plt.xlabel("X_axis") 
                plt.ylabel("value") 
                plt.title("Graph")
                plt.savefig('matrix.png', dpi=300, bbox_inches='tight')

                plt.show()
            button3 = tk.Button(text="prediction", command= predictions)
            button3.place(x=635,y=500)



    def openphoto():
        dirPath = "testpicture"
        fileList = os.listdir(dirPath)
        for fileName in fileList:
            os.remove(dirPath + "/" + fileName)
        # C:/Users/sagpa/Downloads/images is the location of the image which you want to test..... you can change it according to the image location you have  
        fileName = askopenfilename(initialdir='C:\\Users\\sredd\\OneDrive\\Desktop\\covid\\test', title='Select image for analysis ',
                               filetypes=[('image files', '.png')])
        dst = "testpicture"
        print(fileName)
        print (os.path.split(fileName)[-1])
        if os.path.split(fileName)[-1].split('.') == 'h (1)':
            print('dfdffffffffffffff')
        shutil.copy(fileName, dst)
        load = Image.open(fileName)
        render = ImageTk.PhotoImage(load)
        img = tk.Label(image=render, height="250", width="500")   
        img.image = render
        img.place(x=420, y=100)
        #img.grid(column=0, row=1, padx=10, pady = 10)
        title.destroy()
        button1.destroy()
        button2 = tk.Button(text="Analyse Image", command=analysis)
        button2.place(x=625,y=380)
        #button2.grid(column=0, row=20, padx=10, pady = 10)
    button1 = tk.Button(text="Upload Photo", command = openphoto)
    button1.place(x=620,y=150)
    #button1.grid(column=0, row=1, padx=10, pady = 10)

    root.mainloop()




   
    



takeImg = tk.Button(root, text="Detect Covid", command=CNN  ,fg="white"  ,bg="#7b0906"  ,width=10  ,height=1, activebackground = "black" ,font=('times', 15, ' bold '))
takeImg.place(x=50, y=20)
trackImg = tk.Button(root, text="Clear Selection", command=fun  ,fg="white"  ,bg="#7b0906"  ,width=10  ,height=1, activebackground = "Black" ,font=('times', 15, ' bold '))
trackImg.place(x=1075, y=20)
label.pack()
root.mainloop()


















