import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import cv2
from functions import *

import json
import requests
import random


class Video:
    def __init__(self):
        self.base_options = mp.tasks.BaseOptions
        
        self.face_model_path = 'face_landmarker_v2_with_blendshapes.task'
        self.FaceLandmarker = mp.tasks.vision.FaceLandmarker
        self.FaceLandmarkerOptions = mp.tasks.vision.FaceLandmarkerOptions

        self.face_options = self.FaceLandmarkerOptions(
            base_options=self.base_options(model_asset_path=self.face_model_path),
            output_face_blendshapes=True,
            output_facial_transformation_matrixes=True,
            num_faces=1
        )

        self.face_landmarker = self.FaceLandmarker.create_from_options(self.face_options)

        #***********************

        self.pose_model_path = 'pose_landmarker.task'
        self.PoseLandmarker = mp.tasks.vision.PoseLandmarker
        self.PoseLandmarkerOptions = mp.tasks.vision.PoseLandmarkerOptions

        self.pose_options = self.PoseLandmarkerOptions(
            base_options=self.base_options(model_asset_path=self.pose_model_path),
            output_segmentation_masks = True
        )
        
        self.pose_landmarker = vision.PoseLandmarker.create_from_options(self.pose_options)

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
        start_detecting = False

        while cap.isOpened():

            if cv2.waitKey(1) & 0xFF == ord('s'):
                start_detecting = True #does nothing for now

            ret, frame = cap.read()
            image = cv2.flip(frame, 1)
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            image = mp.Image(image_format=mp.ImageFormat.SRGB, data=image)
            
            face_landmarker_result = self.face_landmarker.detect(image)

            self.l_c_x = int(face_landmarker_result.face_landmarks[0][468].x * 1270) #1440
            self.l_c_y = int(face_landmarker_result.face_landmarks[0][468].y * 720) #900
            self.r_c_x = int(face_landmarker_result.face_landmarks[0][473].x * 1270)
            self.r_c_y = int(face_landmarker_result.face_landmarks[0][473].y * 720)

            self.l_l_x = int(face_landmarker_result.face_landmarks[0][469].x * 1270)
            self.l_l_y = int(face_landmarker_result.face_landmarks[0][469].y * 720)
            self.r_l_x = int(face_landmarker_result.face_landmarks[0][474].x * 1270)
            self.r_l_y = int(face_landmarker_result.face_landmarks[0][474].y * 720)

            self.l_t_x = int(face_landmarker_result.face_landmarks[0][470].x * 1270)
            self.l_t_y = int(face_landmarker_result.face_landmarks[0][470].y * 720)
            self.r_t_x = int(face_landmarker_result.face_landmarks[0][475].x * 1270)
            self.r_t_y = int(face_landmarker_result.face_landmarks[0][475].y * 720)

            self.l_r_x = int(face_landmarker_result.face_landmarks[0][471].x * 1270)
            self.l_r_y = int(face_landmarker_result.face_landmarks[0][471].y * 720)
            self.r_r_x = int(face_landmarker_result.face_landmarks[0][476].x * 1270)
            self.r_r_y = int(face_landmarker_result.face_landmarks[0][476].y * 720)

            self.l_b_x = int(face_landmarker_result.face_landmarks[0][472].x * 1270)
            self.l_b_y = int(face_landmarker_result.face_landmarks[0][472].y * 720)
            self.r_b_x = int(face_landmarker_result.face_landmarks[0][477].x * 1270)
            self.r_b_y = int(face_landmarker_result.face_landmarks[0][477].y * 720)

            self.l_ll_x = int(face_landmarker_result.face_landmarks[0][33].x * 1270)
            self.l_ll_y = int(face_landmarker_result.face_landmarks[0][33].y * 720)
            self.l_rr_x = int(face_landmarker_result.face_landmarks[0][133].x * 1270)
            self.l_rr_y = int(face_landmarker_result.face_landmarks[0][133].y * 720)

            self.r_ll_x = int(face_landmarker_result.face_landmarks[0][362].x * 1270)
            self.r_ll_y = int(face_landmarker_result.face_landmarks[0][362].y * 720)
            self.r_rr_x = int(face_landmarker_result.face_landmarks[0][263].x * 1270)
            self.r_rr_y = int(face_landmarker_result.face_landmarks[0][263].y * 720)

            self.updateVariables()

            #**************************************************************************

            image = cv2.cvtColor(image.numpy_view(), cv2.COLOR_RGB2BGR)

            self.putEyeDots(image, self.FONT, self.COLOR)

            cv2.namedWindow('image', cv2.WINDOW_NORMAL) #cv2.WINDOW_AUTOSIZE or cv2.WINDOW_NORMAL if you want to resize
            cv2.resizeWindow('image', 1440, 810)

            start_point = (640, 0)
            end_point = (640, 720)
            color = (0, 255, 0)
            thickness = 9

            image = cv2.line(image, start_point, end_point, color, thickness)

            self.testAccuracy(image)

            cv2.imshow('image', image)

            if cv2.waitKey(1) & 0xFF == ord('q'):

                cv2.imwrite('image.jpg', image)

                frame = np.zeros(shape=[900, 1440, 3], dtype=np.uint8)

                self.putEyeDots(frame, self.FONT, self.COLOR)

                cv2.imshow(f'eye frame {num}', frame)

                num+=1

                # break

        cap.release()
        cv2.destroyAllWindows()        

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
