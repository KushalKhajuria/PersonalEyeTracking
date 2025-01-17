import mediapipe as mp
import cv2
import requests
import json
import numpy as np
# import axios
from django_files import addusers


class Video:
    def __init__(self):
        self.base_options = mp.tasks.BaseOptions
        self.face_model_path = './task_files/face_landmarker_v2_with_blendshapes.task'
        self.FaceLandmarker = mp.tasks.vision.FaceLandmarker
        self.FaceLandmarkerOptions = mp.tasks.vision.FaceLandmarkerOptions

        self.face_options = self.FaceLandmarkerOptions(
            base_options=self.base_options(model_asset_path=self.face_model_path),
            output_face_blendshapes=True,
            output_facial_transformation_matrixes=True,
            num_faces=1
        )

        self.face_landmarker = self.FaceLandmarker.create_from_options(self.face_options)

        self.key_landmarks = []

        self.l_c_x = None
        self.l_c_y = None
        self.r_c_x = None
        self.r_c_y = None

        self.l_l_x = None
        self.l_l_y = None
        self.r_l_x = None
        self.r_l_y = None

        self.l_t_x = None
        self.l_t_y = None
        self.r_t_x = None
        self.r_t_y = None

        self.l_r_x = None
        self.l_r_y = None
        self.r_r_x = None
        self.r_r_y = None

        self.l_b_x = None
        self.l_b_y = None
        self.r_b_x = None
        self.r_b_y = None

        self.l_ll_x = None
        self.l_ll_y = None
        self.r_ll_x = None
        self.r_ll_y = None

        self.l_rr_x = None
        self.l_rr_y = None
        self.r_rr_x = None
        self.r_rr_y = None

        self.l_c = None
        self.r_c = None

        self.l_l = None
        self.r_l = None

        self.l_t = None
        self.r_t = None

        self.l_r = None
        self.r_r = None

        self.l_b = None
        self.r_b = None

        self.l_ll = None
        self.r_ll = None

        self.l_rr = None
        self.r_rr = None

        self.c = None
        self.l = None
        self.t = None
        self.r = None
        self.b = None
        self.ll = None
        self.rr = None

        self.key_landmarks.append(self.c)
        self.key_landmarks.append(self.l)
        self.key_landmarks.append(self.l)
        self.key_landmarks.append(self.r)
        self.key_landmarks.append(self.b)
        self.key_landmarks.append(self.ll)
        self.key_landmarks.append(self.rr)

        self.COLOR = (255, 255, 255)
        self.FONT = cv2.FONT_HERSHEY_SIMPLEX

    def runVideo(self):
        cap = cv2.VideoCapture(0)
        num = 1
        # cv2.waitKey(0)
        self.regularFramesContinuous(cap)
        # self.infiniteBlackFramesDiscrete(cap, num)
        self.infiniteBlackFramesContinuous(cap, num)
        # self.oneBlackFrame(cap, num)
        self.endProgram(cap)
        # self.recordCoordinates(10, 20)

        application = addusers.AddUsers()

        lcx = self.key_landmarks[0][0][0]
        lcy = self.key_landmarks[0][0][1]

        application.add_x_y_data(lcx, lcy)

        application.print_data()

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

    def endProgram(self, cap):
        cap.release()
        cv2.destroyAllWindows()

    def regularFramesContinuous(self, cap):
        while cap.isOpened():
            self.regularFrame(cap, True)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    def infiniteBlackFramesDiscrete(self, cap, num):
        while cap.isOpened():
            self.blackFrame(cap, num, True)
            while True:
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    self.blackFrame(cap, num, True)
                    break
                if cv2.waitKey(1) & 0xFF == ord('s'):
                    return
            num+=1

    def infiniteBlackFramesContinuous(self, cap, num):
        while cap.isOpened():
            while True:
                self.blackFrame(cap, num, True)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
                if cv2.waitKey(1) & 0xFF == ord('s'):
                    return
            num+=1
            cv2.waitKey(0)

    def oneBlackFrame(self, cap, num):
        while cap.isOpened():
            self.blackFrame(cap, num, True)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cv2.waitKey(0)

    def readFrame(self, cap):
        ret, frame = cap.read()
        image = cv2.flip(frame, 1)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        return image

    def regularFrame(self, cap, display):
        image = self.readFrame(cap)
        image = mp.Image(image_format=mp.ImageFormat.SRGB, data=image)
        face_landmarker_result = self.face_landmarker.detect(image)
        image = cv2.cvtColor(image.numpy_view(), cv2.COLOR_RGB2BGR)
        self.UI(face_landmarker_result, image, display)

    def UI(self, face_landmarker_result, image, display):
        self.defineAndScale(face_landmarker_result, 1280, 720)
        self.putEyeDots(image, self.FONT, self.COLOR)
        self.lineThroughMiddle(image)
        self.testAccuracy(image)

        if display:
            self.UiDisplay(image)

    def UiDisplay(self, image):
        cv2.namedWindow('image', cv2.WINDOW_NORMAL) #cv2.WINDOW_AUTOSIZE, or cv2.WINDOW_NORMAL if you want to resize
        cv2.resizeWindow('image', 1440, 810)
        cv2.imshow('image', image)

    def blackFrame(self, cap, num, display):
        image = self.readFrame(cap)
        image = mp.Image(image_format=mp.ImageFormat.SRGB, data=image)
        face_landmarker_result = self.face_landmarker.detect(image)
        frame = np.zeros(shape=[720, 1280, 3], dtype=np.uint8) #900, 1440; 1693, 2880
        self.blackAndWhite(face_landmarker_result, frame, num, display)

    def blackAndWhite(self, face_landmarker_result, image, num, display):
        self.defineAndScale(face_landmarker_result, 1280, 720) #1493, 2560
        self.putEyeDots(image, self.FONT, self.COLOR)

        if display:
            self.blackAndWhiteDisplay(num, image)

    def blackAndWhiteDisplay(self, num, image):
        cv2.namedWindow(f'eye frame {num}', cv2.WINDOW_NORMAL)
        cv2.resizeWindow(f'eye frame {num}', 1440, 810)
        cv2.imshow(f'eye frame {num}', image)

    def putEyeDots(self, frame, font, color):
        for i in range(len(self.key_landmarks)):
            for j in range(2):
                cv2.putText(frame, '.', self.key_landmarks[i][j], font, 1, color, 3, cv2.LINE_AA)

    def updateVariables(self):
        self.l_c = (self.l_c_x, self.l_c_y)
        self.r_c = (self.r_c_x, self.r_c_y)

        self.l_l = (self.l_l_x, self.l_l_y)
        self.r_l = (self.r_l_x, self.r_l_y)

        self.l_t = (self.l_t_x, self.l_t_y)
        self.r_t = (self.r_t_x, self.r_t_y)

        self.l_r = (self.l_r_x, self.l_r_y)
        self.r_r = (self.r_r_x, self.r_r_y)

        self.l_b = (self.l_b_x, self.l_b_y)
        self.r_b = (self.r_b_x, self.r_b_y)

        self.l_ll = (self.l_ll_x, self.l_ll_y)
        self.r_ll = (self.r_ll_x, self.r_ll_y)

        self.l_rr = (self.l_rr_x, self.l_rr_y)
        self.r_rr = (self.r_rr_x, self.r_rr_y)

        self.c = (self.l_c, self.r_c)
        self.l = (self.l_l, self.r_l)
        self.t = (self.l_t, self.r_t)
        self.r = (self.l_r, self.r_r)
        self.b = (self.l_b, self.r_b)
        self.ll = (self.l_ll, self.r_ll)
        self.rr = (self.l_rr, self.r_rr)

        self.key_landmarks[0] = self.c
        self.key_landmarks[1] = self.l
        self.key_landmarks[2] = self.t
        self.key_landmarks[3] = self.r
        self.key_landmarks[4] = self.b
        self.key_landmarks[5] = self.ll
        self.key_landmarks[6] = self.rr

    def testAccuracy(self, image):
        color = (0, 0, 255)
        yes_point = (240, 360)
        no_point = (900, 360)

        l_c_ll_deltax = self.l_c_x - self.l_ll_x
        l_c_rr_deltax = self.l_rr_x - self.l_c_x
        r_c_ll_deltax = self.r_c_x - self.r_ll_x
        r_c_rr_deltax = self.r_rr_x - self.r_c_x

        if l_c_ll_deltax + r_c_ll_deltax < l_c_rr_deltax + r_c_rr_deltax:
            cv2.putText(image, 'YES', yes_point, self.FONT, 3, color, 3, cv2.LINE_AA)
        else:
            cv2.putText(image, 'NO', no_point, self.FONT, 3, color, 3, cv2.LINE_AA)

    def defineAndScale(self, face_landmarker_result, scale_x, scale_y):
        self.l_c_x = int(face_landmarker_result.face_landmarks[0][468].x * scale_x) #1440
        self.l_c_y = int(face_landmarker_result.face_landmarks[0][468].y * scale_y) #900
        self.r_c_x = int(face_landmarker_result.face_landmarks[0][473].x * scale_x)
        self.r_c_y = int(face_landmarker_result.face_landmarks[0][473].y * scale_y)

        self.l_l_x = int(face_landmarker_result.face_landmarks[0][469].x * scale_x)
        self.l_l_y = int(face_landmarker_result.face_landmarks[0][469].y * scale_y)
        self.r_l_x = int(face_landmarker_result.face_landmarks[0][474].x * scale_x)
        self.r_l_y = int(face_landmarker_result.face_landmarks[0][474].y * scale_y)

        self.l_t_x = int(face_landmarker_result.face_landmarks[0][470].x * scale_x)
        self.l_t_y = int(face_landmarker_result.face_landmarks[0][470].y * scale_y)
        self.r_t_x = int(face_landmarker_result.face_landmarks[0][475].x * scale_x)
        self.r_t_y = int(face_landmarker_result.face_landmarks[0][475].y * scale_y)

        self.l_r_x = int(face_landmarker_result.face_landmarks[0][471].x * scale_x)
        self.l_r_y = int(face_landmarker_result.face_landmarks[0][471].y * scale_y)
        self.r_r_x = int(face_landmarker_result.face_landmarks[0][476].x * scale_x)
        self.r_r_y = int(face_landmarker_result.face_landmarks[0][476].y * scale_y)

        self.l_b_x = int(face_landmarker_result.face_landmarks[0][472].x * scale_x)
        self.l_b_y = int(face_landmarker_result.face_landmarks[0][472].y * scale_y)
        self.r_b_x = int(face_landmarker_result.face_landmarks[0][477].x * scale_x)
        self.r_b_y = int(face_landmarker_result.face_landmarks[0][477].y * scale_y)

        self.l_ll_x = int(face_landmarker_result.face_landmarks[0][33].x * scale_x)
        self.l_ll_y = int(face_landmarker_result.face_landmarks[0][33].y * scale_y)
        self.l_rr_x = int(face_landmarker_result.face_landmarks[0][133].x * scale_x)
        self.l_rr_y = int(face_landmarker_result.face_landmarks[0][133].y * scale_y)

        self.r_ll_x = int(face_landmarker_result.face_landmarks[0][362].x * scale_x)
        self.r_ll_y = int(face_landmarker_result.face_landmarks[0][362].y * scale_y)
        self.r_rr_x = int(face_landmarker_result.face_landmarks[0][263].x * scale_x)
        self.r_rr_y = int(face_landmarker_result.face_landmarks[0][263].y * scale_y)

        self.updateVariables()

    def lineThroughMiddle(self, image):
        start_point = (640, 0)
        end_point = (640, 720)
        color = (0, 255, 0)
        thickness = 9

        image = cv2.line(image, start_point, end_point, color, thickness)