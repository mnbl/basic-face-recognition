import cv2
import os
import sqlite3

# Create a connection witn databse
conn = sqlite3.connect('facedb')
if conn != 0:
    print("Connection Successful")
else:
    print('Connection Failed')
    exit()

# Creating table if it doesn't already exists
conn.execute('''create table if not exists facedata ( id int primary key, name char(20) not null)''')

cam = cv2.VideoCapture(0)

face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# For each person, enter one numeric face id
face_id = input('\n Enter User Id and press "Enter" ==>  ')

# For each person, enter Name
face_name = input('\n Enter User Name and press "Enter" ==>  ')
try:
    conn.execute('''insert into facedata values ( ?, ?)''', (face_id, face_name))
    conn.commit()
except sqlite3.IntegrityError:
    print("\n ERROR! This id alreeady exists in database!")
    print("\n Try agian with new id\n")
    exit()

print("\n Initializing face capture. Look the camera and wait ...")

# Initialize individual sampling face count
count = 0

while(True):

    ret, img = cam.read()
    # img = cv2.flip(img, -1) # flip video image vertically
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:

        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
        count += 1

        # Save the captured image into the datasets folder
        cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])

        cv2.imshow('image', img)

    k = cv2.waitKey(100) & 0xff # Press 'ESC' for exiting video
    if k == 27:
        break
    elif count >= 30: # Take 30 face sample and stop video
         break

# Do a bit of cleanup
print("\n Your face is saved successfully")
print("\n Exiting Program")
cam.release()
cv2.destroyAllWindows()

# Exiting the connection
conn.close()
