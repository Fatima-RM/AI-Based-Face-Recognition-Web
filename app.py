from flask import Flask, request, render_template, session, redirect
import face_recognition
import cv2
import numpy as np
import base64
import pickle
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def home():
    return redirect('/login')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.get_json()
        image_data = data['image'].split(',')[1]
        img_bytes = base64.b64decode(image_data)
        np_arr = np.frombuffer(img_bytes, np.uint8)
        img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

        # Load known encodings
        with open("encodings.pickle", "rb") as f:
            data = pickle.load(f)
        known_face_encodings = data["encodings"]
        known_face_names = data["names"]
        print(len(data['encodings']), data['names'])
        name = recognize_face_from_image(img, known_face_encodings, known_face_names)
        print(f"[DEBUG] Recognized name: {name}")
        if name != "Unknown":
            session['user'] = name
            return "success"
        else:
            print("[DEBUG] Face not recognized")
        return "Face not recognized", 403

    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect('/login')
    return f"Welcome, {session['user']}!"

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')

def recognize_face_from_image(img, known_face_encodings, known_face_names, threshold=0.42):
    # Resize for speed
    small_img = cv2.resize(img, (0, 0), fx=0.25, fy=0.25)
    rgb_img = cv2.cvtColor(small_img, cv2.COLOR_BGR2RGB)

    face_locations = face_recognition.face_locations(rgb_img)
    face_encodings = face_recognition.face_encodings(rgb_img, face_locations)
    print(f"[DEBUG] Faces detected: {len(face_encodings)}")

    for face_encoding in face_encodings:
        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)
        best_distance = face_distances[best_match_index]

        print(f"[DEBUG] Closest distance: {best_distance:.4f}")
        
        if best_distance < threshold:
            return known_face_names[best_match_index]

    return "Unknown"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
