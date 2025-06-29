# AI-Based-Face-Recognition-Web

A modern, AI-powered, web-based facial recognition login system. This project demonstrates how to build a secure face authentication mechanism for web applications using Python, Flask, face_recognition, and OpenCV.

---

## Contributors

- [Fatima-RM](https://github.com/Fatima-RM)
- [Usman-Azhar](https://github.com/Usman-Azhar)

---

## Table of Contents

- [Features](#features)
- [How It Works](#how-it-works)
- [Directory Structure](#directory-structure)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Setup Known Faces](#setup-known-faces)
  - [Run the Web App](#run-the-web-app)
- [Usage](#usage)
- [Contributors](#contributors)
- [Future Improvements](#future-improvements)
- [License](#license)

---

## Features

- **Face Recognition Login:** Users log in using their webcam; the system recognizes their faces against a pre-built database.
- **Personalized Dashboard:** Authenticated users are greeted by name.
- **Session Management:** User sessions are tracked for secure access.
- **Logout Functionality:** Users can securely end their sessions.
- **Easy Addition of New Users:** Add face images to the dataset and regenerate encodings.
- **Extensible Backend:** Designed for simple addition of features like web-based registration, multi-factor authentication, and database integration.
- **Educational Example:** Code is clear and heavily commented for learning purposes.

---

## How It Works

### 1. Face Data Preparation

- Store reference images for each user in `known_faces/<user_name>/`.
- Run `generate_encodings.py` to process images and create `encodings.pickle` containing facial feature vectors and corresponding names.

### 2. Web Application

- **Login Page:** The user’s webcam image is captured in-browser and sent to the Flask backend.
- **Face Recognition:** The backend decodes the image, extracts facial features, and compares them to the known encodings using the `face_recognition` library.
- **Authentication:** If a match is found within a set threshold, the user is logged in and redirected to a personalized dashboard.
- **Session Management:** User session state is handled using Flask’s session mechanism.
- **Logout:** The session is cleared and the user is redirected to the login page.

### 3. Core Code Highlights

- `app.py` handles all routing and face authentication logic.
- `generate_encodings.py` pre-processes user images to create face encodings.
- Facial recognition uses a distance threshold for reliable matching.
- The system is modular and ready for further feature integration.

---

## Directory Structure

```
├── app.py                       # Flask web app: handles routes and authentication
├── generate_encodings.py        # Script to process known faces and generate encodings
├── encodings.pickle             # Serialized face encodings and names
├── known_faces/                 # Directory of user folders with images
│   └── <username>/              # Each user has a folder of face images
│       └── <image1>.jpg
├── templates/
│   └── login.html               # HTML for login page (webcam capture)
├── static/                      # (Optional) CSS/JS for frontend
├── README.md
```

---

## Getting Started

### Prerequisites

- Python 3.7+
- [Flask](https://flask.palletsprojects.com/)
- [face_recognition](https://github.com/ageitgey/face_recognition)
- OpenCV (`cv2`)
- Numpy

Install dependencies:

```bash
pip install flask face_recognition opencv-python numpy
```

---

### Setup Known Faces

1. **Create folders for each user in `known_faces/` and add their face images:**

   ```
   known_faces/
   ├── Alice/
   │   ├── alice1.jpg
   │   └── alice2.jpg
   └── Bob/
       ├── bob1.jpg
       └── bob2.jpg
   ```

2. **Generate face encodings:**

   ```bash
   python generate_encodings.py
   ```

   This creates or updates `encodings.pickle`.

---

### Run the Web App

```bash
python app.py
```
Then open your browser to [http://localhost:5000](http://localhost:5000).

---

## Usage

- Go to the login page.
- Allow webcam access when prompted.
- The system will capture your face and attempt to recognize you.
- If successful, you’ll be greeted on the dashboard.
- Click logout to end your session.

---

## Future Improvements

- **User Registration via Web:** Allow users to add themselves directly from the web interface.
- **Database Integration:** Store user data and face encodings persistently in a DB.
- **Enhanced Security:** Add rate limiting and multi-factor authentication.
- **Detailed Dashboard:** Provide profile management and login history.
- **Mobile Support:** Make the UI friendly for mobile browsers.

---

## License

This project is for educational use. For production, review, secure, and extend the code as needed.

---
