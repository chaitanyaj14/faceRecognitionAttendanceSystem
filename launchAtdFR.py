import os
from tkinter import Tk
from tkinter import Button
from tkinter import messagebox
import tkinter as tk
import haarCascade as hc

tkWindow = Tk()  
tkWindow.geometry('600x500')  
tkWindow.title('Face Recognition Attendance System')

label = tk.Label(tkWindow, 
                 text="ESG624 Pattern Recognition and Machine Learning",
                 font = "Verdana 10 bold")
label.pack()

def showMsg():  
    messagebox.showinfo('Message', 'You clicked the Submit button!')
    
def createYAML():
    faces,faceID=hc.labels_for_training_data('trainingImages')
    face_recognizer=hc.train_classifier(faces,faceID)
    face_recognizer.write('trainingData.yml')

def takeAtd():
    import takeAtd
    
def takeImage():
    import trainingCreator

def close_window (): 
    tkWindow.destroy()
    
def openExcel():
    os.startfile("attendance.xlsx")

sampleButton = Button(tkWindow,
	text = 'Instructions Guide',
    font = " bold ",
	command = showMsg, 
    width = 25)  
sampleButton.pack(padx=15, pady=15)

captureImgButton = Button(tkWindow,
	text = 'Capture Image',
    font = " bold ",
	command = takeImage, 
    width = 25)  
captureImgButton.pack(padx=15, pady=15) 

createYAMLButton = Button(tkWindow,
	text = 'Create YAML File',
    font = " bold ",
	command = createYAML, 
    width = 25)  
createYAMLButton.pack(padx=15, pady=15)  

startAtdButton = Button(tkWindow,
	text = 'Start Attendance',
    font = " bold ",
	command = takeAtd, 
    width = 25)  
startAtdButton.pack(padx=15, pady=15) 

openExlButton = Button(tkWindow,
	text = 'Display Excel',
    font = " bold ",
	command = openExcel, 
    width = 25)  
openExlButton.pack(padx=15, pady=15) 

closeButton = Button(tkWindow,
                     text="Close",
                     fg="red",
                     font = " bold ",
                     command = close_window, 
                     width = 25)
closeButton.pack(padx=15, pady=15)

label2 = tk.Label(tkWindow, 
                 text="Chaitanya Joshi -- SC19M001 -- M.Tech -- Geoinformatics",
                 font = "Verdana 8 bold italic")
label2.pack()

label3 = tk.Label(tkWindow, 
                 text="2019-21",
                 font = "Verdana 8 bold italic")
label3.pack()

  
tkWindow.mainloop()