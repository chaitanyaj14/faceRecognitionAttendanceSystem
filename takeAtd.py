#import os
import cv2
import mysql.connector
import haarCascade as hc
import pandas as pd
from datetime import date
from openpyxl import load_workbook

today = date.today()
# dd-mm-YY
currentDate = today.strftime("%d-%m-%Y")
#dateOfAtd = [currentDate]

c = 0
p = 0
r = 0
k = 0

face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.read('trainingData.yml')
name = {#0 : ["Priyanka","SC19B010", "Aerospace"], 
        #1 : ["Kangana","SC19B020", "Avionics"], 
        0 : ["Chaitanya", "SC19M001", "Geoinformatics",c], 
        1 : ["Chaitanya", "SC19M001", "Geoinformatics",c],
        2 : ["Ruchita", "SC19M002", "Geoinformatics",r]}

#dataFrame = pd.DataFrame(columns = ["Name", "SC Code", "Department", "Confidence"])

cap=cv2.VideoCapture(0)

imgCount = 0


atCandidate = []
atCandidateUnique = []
count = 0
while True:
    ret,test_img=cap.read()# captures frame and returns boolean value and captured image
    faces_detected,gray_img=hc.faceDetection(test_img)



    for (x,y,w,h) in faces_detected:
      cv2.rectangle(test_img,(x,y),(x+w,y+h),(255,0,0),thickness=7)

    resized_img = cv2.resize(test_img, (1000, 700))
    cv2.imshow('face detection Tutorial ',resized_img)
    cv2.waitKey(10)

    

    for face in faces_detected:
        (x,y,w,h)=face
        roi_gray=gray_img[y:y+w, x:x+h]
        label,confidence=face_recognizer.predict(roi_gray)#predicting the label of given image
        print("Confidence:",confidence)
        print("Name:",name[label][0])
        print("SC Code:",name[label][1])
        print("Branch:",name[label][2])
        if name[label][0] == 'Chaitanya':
            c = c + 1
        elif name[label][0] == 'Priyanka':
            p = p + 1
        elif name[label][0] == 'Ruchita':
            r = r + 1
        else:
            k = k + 1
        
        imgCount = imgCount + 1
        # if imgCount == 199:
        #     break
        
        hc.draw_rect(test_img,face)
        predicted_name=name[label][0]
        hc.put_text(test_img,predicted_name,x,y)
        if confidence < 40:
           hc.put_text(test_img,predicted_name,x,y)
        else:
            atCandidate.append([name[label][0],
                                name[label][1],
                                name[label][2],
                                currentDate])
            for i in atCandidate:
                if i not in atCandidateUnique:
                    atCandidateUnique.append([name[label][0], 
                                              name[label][1], 
                                              name[label][2],
                                              currentDate])
                    
            atCandidate = []
    resized_img = cv2.resize(test_img, (1000, 700))
    cv2.imshow('face recognition tutorial ',resized_img)

    if cv2.waitKey(10) == ord('q'):
        break
    
    # if imgCount == 199:
    #         break

dataFrame = pd.DataFrame(atCandidateUnique[0:],columns = ["Name", "SC Code", "Department", "Date"])
dataFrame = dataFrame.rename(columns={'Department':'Branch'})


cap.release()
cv2.destroyAllWindows

#dataFrame['date'] = dateOfAtd

# Output To Excel
# from datetime import date

# today = date.today()

# # dd-mm-YY
# currentDate = today.strftime("%d-%m-%Y")
path = r"attendance.xlsx"

book = load_workbook(path)
writer = pd.ExcelWriter(path, engine = 'openpyxl')
writer.book = book

#dataFrame.to_excel("C:\\Drive\\Sem2\\ML\\FaceRecognition-master\\FaceRecognition-master\\output.xlsx",sheet_name=currentDate, engine='openpyxl') 
dataFrame.to_excel(writer, sheet_name=currentDate)
writer.save()
writer.close()


dataFrame = dataFrame.rename(columns={'SC Code':'sccode'})
# # Output To Database
# db = mysql.connector.connect(host = "localhost", 
#                               user="chaitanya", 
#                               passwd="mysql",
#                               database="attendance")

# cursor = db.cursor()

# # creating column list for insertion
# cols = "`,`".join([str(i) for i in dataFrame.columns.tolist()])

# # Insert DataFrame recrds one by one.
# for i,row in dataFrame.iterrows():
#     sql = "INSERT INTO `attendanceML` (`" +cols + "`) VALUES (" + "%s,"*(len(row)-1) + "%s)"
#     cursor.execute(sql, tuple(row))

#     # the connection is not autocommitted by default, so we must commit to save our changes
#     db.commit()

# # print(cursor.rowcount, "was inserted.")

# # Execute query
# sql = "SELECT DISTINCT name FROM `attendanceML` WHERE date = '20-03-2020' ORDER BY 'name'"
# cursor.execute(sql)

# # Fetch all the records
# result = cursor.fetchall()
# for i in result:
#     print(i)
    
# print(cursor.rowcount, "Rows")

# db.close()