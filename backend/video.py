import cv2
import requests
import json

from backend.data_handling.data_transmission import DataTransmission
from backend.data_handling.data_collection import DataCollection
from backend.display.frame_live_stream import ColoredLiveStream, BlackAndWhiteLiveStream, CombinedLiveStream

class Video:
    def __init__(self):

        self.cap = cv2.VideoCapture(0)

        self.collection = DataCollection()

        self.num = 1

        self.colorstream = ColoredLiveStream(self.cap, True, self.collection)
        self.bwstream = BlackAndWhiteLiveStream(self.cap, self.num, True, self.collection)
        self.combinedstream = CombinedLiveStream(self.cap, self.num, True, self.collection)

        self.transmission = DataTransmission(self.collection)

    def runVideo(self):
        # cv2.waitKey(0)
        self.colorstream.regularFramesContinuous()
        # self.infiniteBlackFramesDiscrete(cap, num)
        self.bwstream.infiniteBlackFramesContinuous()
        # self.oneBlackFrame(cap, num)
        self.endProgram()
        # self.recordCoordinates(10, 20)

        self.transmission.transmit()

        print("finished!")

    def recordCoordinates(self, x, y):
        session = requests.Session()

        url = "http://localhost:8000/post/"
        response = session.get(url)

        csrf_token = session.cookies.get('csrftoken')

        payload = json.dumps({
            "x-coordinate": x,
            "y-coordinate": y
        })

        headers = {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrf_token
        }

        response = session.post(url, headers=headers, data=payload)

        print(response.text)

    def endProgram(self):
        self.cap.release()
        cv2.destroyAllWindows()