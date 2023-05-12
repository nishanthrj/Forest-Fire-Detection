import cv2
import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
from twilio.rest import Client
from playsound import playsound
from decouple import config

message_sent = False

model = load_model("./model.h5")

video = cv2.VideoCapture(0)

name = ["Peace", "FIREEEE"]


def send_message():
    account_sid = config("ACCOUNT_SID")
    auth_token = config("AUTH_TOKEN")
    
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="Forest Fire detected.",
        from_=config("FROM"),
        to=config("TO")
    )
    print(message.sid)
    print("Fire Detected")
    print("SMS Sent!")


while True:
    success, frame = video.read()
    if not success:
        break
    
    img = cv2.resize(frame, (128, 128))
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    pred = model.predict(img)
    p = int(pred[0][0])
    cv2.putText(frame, str(name[p]), (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 1)
    
    if p == 1:
        if not message_sent:
            send_message()
            message_sent = True
        print("FIREEEEEE")
        playsound("beep.mp3")
    else:
        print("Peace")
    
    cv2.imshow("Video Feed", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

video.release()
cv2.destroyAllWindows()
