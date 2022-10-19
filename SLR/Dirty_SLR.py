# from logging import root
from tkinter import *
from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np

# Create simple linear regression model for sequence prediction
data=[i for i in range(101)]
x=[]
y=[]

for i in range(len(data)):
    end=i+1
    if end>=len(data):break
    x.append(data[i:end])
    y.append(data[end])

x=np.array(x)
y=np.array(y)

# Tkinter GUI for for fresh predictions
model=LinearRegression()
model.fit(x,y)
root=Tk()

root.geometry('500x200')
root.configure(bg='pink')

root.title('A Dirty Simple Linear regression')

# Integer Input
num=IntVar()
ent=Entry(root,textvariable=num,justify='center',font='Stencil_Std 13')
ent.grid(column=0,row=0,columnspan=2,rowspan=2,sticky='NSEW')

# Entry Label
lab_ent=Label(root)
lab_ent.grid(column=3,row=0,columnspan=2,rowspan=2)
lab_ent.config(background='Blue',foreground="black",text="Enter the value to predict",font=('Bold'))

# Label to display the prediction
lab=Label(root)
lab.grid(column=0,row=3,columnspan=2,rowspan=2,sticky='NSEW')

# Label to display Prediction
lab_ent=Label(root)
lab_ent.grid(column=3,row=3,columnspan=2,rowspan=2,sticky='NSEW')
lab_ent.config(background='Blue',foreground="black",text="The Predicted Value",font=('Bold'),borderwidth=5,border=2)


def l(event):
    value=num.get()
    predict=model.predict(np.array(value).reshape(1,-1))
    print(predict)
    lab.config(text=round(predict[0],1),background='yellow',font=('Bold'))

ent.bind('<Key-Return>',l)
# def lab_value(event):
#     lab.set
    

root.mainloop()