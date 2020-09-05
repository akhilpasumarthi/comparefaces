import PIL
from PIL import Image
import cv2 
import numpy as np
import face_recognition as fr
import time   

def verification(image,image2):
    profile_image = fr.load_image_file(image)
    profile_encoding = fr.face_encodings(profile_image)[0]
    status=[]
    video = cv2.VideoCapture(image2)
    t0 = time.time()
    
    while video.isOpened():
        check , frame = video.read()
        cv2.imshow('frame',frame)
    
        img = Image.fromarray(frame, 'RGB')
        img.save('my.jpg')
    
    
        live_image = fr.load_image_file('my.jpg')
        live_encoding = fr.face_encodings(live_image)[0]
        
        results = fr.compare_faces([profile_encoding],live_encoding)
        status.append(results)
        
        cv2.waitKey(2000)
        t1 = time.time()
    
      
        if t1-t0 >= 2:
            video.release()
            cv2.destroyAllWindows()
            
    return str(status[0])
status = verification('trump.jpeg','trump.webm')  
