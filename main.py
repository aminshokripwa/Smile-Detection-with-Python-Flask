from flask import request, Flask
import cv2
import numpy as np
from keras.models import load_model

app = Flask(__name__)

width = 800
height = 600
blue = (255, 0, 0)
# load the haar cascade face detector
face_detector = cv2.CascadeClassifier("haar_cascade/haarcascade_frontalface_default.xml")
# load our trained model
model = load_model("model")

@app.route('/api/v1/face', methods=['POST'])
def test():
    f = request.files.get('image')
    if f is None:
        return '["message": "Please Upload an image","status": false]"', 422
    if f.filename.split('.')[0] != 'jpg' and f.filename.split('.')[0] == 'jpeg' :
        return '["message": "Please upload only jpg file","status": false]"', 422

    #upload image to server
    imagefile = request.files.get('imagefile')
    imagefile.save('./image.jpg')
    # load the image, resize it, and convert it to grayscale
    image = cv2.imread("./image.jpg")
    image = cv2.resize(image, (width, height))
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # detect faces in the grayscale image
    face_rects = face_detector.detectMultiScale(gray, 1.1, 8)

    # loop over the face bounding boxes
    for (x, y, w, h) in face_rects:
        cv2.rectangle(image, (x, y), (x + w, y + h), blue, 2)
        # extract the region of the face from the grayscale image
        roi = gray[y:y + h, x:x + w]
        roi = cv2.resize(roi, (32, 32))
        roi = roi / 255.0
        # add a new axis to the image
        # previous shape: (32, 32), new shape: (1, 32, 32)
        roi = roi[np.newaxis, ...]
        # apply the smile detector to the face roi
        prediction = model.predict(roi)[0]
        label = "Smiling" if prediction >= 0.5 else "Not Smiling"

        #cv2.putText(image, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, blue, 2)
    #cv2.imshow("image", image)
    print(label)
    cv2.waitKey(0)
    return '["message": '+label+',"status": true]"', 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)