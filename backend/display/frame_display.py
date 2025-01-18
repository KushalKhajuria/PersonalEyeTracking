import cv2
import mediapipe as mp
import numpy as np
from backend.display.maunual_additions import ManualAdditions

class DisplayFunctions:
    def __init__(self, cap, display, collection):
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

        self.COLOR = (255, 255, 255)
        self.FONT = cv2.FONT_HERSHEY_SIMPLEX

        self.cap = cap
        self.display = display
        self.collection = collection

        self.additions = ManualAdditions(collection, self.FONT)

    def readFrame(self, cap):
        ret, frame = cap.read()
        image = cv2.flip(frame, 1)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        return image

    def displayFrame(self, image, name):
        cv2.namedWindow(name, cv2.WINDOW_NORMAL) #cv2.WINDOW_AUTOSIZE, or cv2.WINDOW_NORMAL if you want to resize
        cv2.resizeWindow(name, 1440, 810)
        cv2.imshow(name, image)

class ColoredDisplay(DisplayFunctions):
    def __init__(self, cap, display, collection):
        super().__init__(cap, display, collection)

    def regularFrame(self):
        image = self.readFrame(self.cap)
        image = mp.Image(image_format=mp.ImageFormat.SRGB, data=image)
        face_landmarker_result = self.face_landmarker.detect(image)
        image = cv2.cvtColor(image.numpy_view(), cv2.COLOR_RGB2BGR)
        self.UI(face_landmarker_result, image, self.display, self.collection)

    def UI(self, face_landmarker_result, image, display, collection):
        collection.defineAndScale(face_landmarker_result, 1280, 720)
        self.additions.putEyeDots(image, self.FONT, self.COLOR)
        self.additions.lineThroughMiddle(image)
        self.additions.testAccuracy(image)

        if display:
            self.UiDisplay(image)

    def UiDisplay(self, image):
        self.displayFrame(image, "Image")

class BlackAndWhiteDisplay(DisplayFunctions):
    def __init__(self, cap, num, display, collection):
        super().__init__(cap, display, collection)
        self.num = num

    def blackFrame(self):
        image = self.readFrame(self.cap)
        image = mp.Image(image_format=mp.ImageFormat.SRGB, data=image)
        face_landmarker_result = self.face_landmarker.detect(image)
        frame = np.zeros(shape=[720, 1280, 3], dtype=np.uint8) #900, 1440; 1693, 2880
        self.blackAndWhite(face_landmarker_result, frame)

    def blackAndWhite(self, face_landmarker_result, image):
        self.collection.defineAndScale(face_landmarker_result, 1280, 720) #1493, 2560
        self.additions.putEyeDots(image, self.FONT, self.COLOR)

        if self.display:
            self.blackAndWhiteDisplay(self.num, image)

    def blackAndWhiteDisplay(self, num, image):
        self.displayFrame(image, f"eye frame {num}")

class CombinedDisplay(DisplayFunctions):
    def __init__(self, cap, num, display, collection):
        super().__init__(cap, display, collection)
        self.num = num

    def combinedDisplay(self, num, image):
        self.displayFrame(image, f"combined display frame {num}")