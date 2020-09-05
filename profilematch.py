

import face_recognition as fr
 
def verification(image,image2):
    profile_image = fr.load_image_file(image)
    profile_encoding = fr.face_encodings(profile_image)[0]
    live_image = fr.load_image_file(image2)
    live_encoding = fr.face_encodings(live_image)[0]
    results = fr.compare_faces([profile_encoding],live_encoding)
        
    return results[0]
    





