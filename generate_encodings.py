import face_recognition
import cv2
import os
import pickle

image_folder = 'known_faces'
known_encodings = []
known_names = []

# Loop through each subfolder (each person's name)
for person_name in os.listdir(image_folder):
    person_folder = os.path.join(image_folder, person_name)
    
    # Check if it is a folder
    if not os.path.isdir(person_folder):
        continue
    
    # Loop through each image in the person's folder
    for file in os.listdir(person_folder):
        img_path = os.path.join(person_folder, file)
        img = face_recognition.load_image_file(img_path)
        
        # Check if the face is detected
        encodings = face_recognition.face_encodings(img)
        if len(encodings) > 0:
            enc = encodings[0]
            known_encodings.append(enc)
            known_names.append(person_name)  # Use folder name as the person's name
        else:
            print(f"Warning: No face found in {img_path}")

# Save the encodings
with open('encodings.pickle', 'wb') as f:
    pickle.dump({'encodings': known_encodings, 'names': known_names}, f)
