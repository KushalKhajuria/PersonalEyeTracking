import cv2

class ManualAdditions:
    def __init__(self, collection, font):
        self.collection = collection
        self.font = font

    def testAccuracy(self, image):
        color = (0, 0, 255)
        yes_point = (240, 360)
        no_point = (900, 360)

        l_c_ll_deltax = self.collection.l_c_x - self.collection.l_ll_x
        l_c_rr_deltax = self.collection.l_rr_x - self.collection.l_c_x
        r_c_ll_deltax = self.collection.r_c_x - self.collection.r_ll_x
        r_c_rr_deltax = self.collection.r_rr_x - self.collection.r_c_x

        if l_c_ll_deltax + r_c_ll_deltax < l_c_rr_deltax + r_c_rr_deltax:
            cv2.putText(image, 'YES', yes_point, self.font, 3, color, 3, cv2.LINE_AA)
        else:
            cv2.putText(image, 'NO', no_point, self.font, 3, color, 3, cv2.LINE_AA)

    def lineThroughMiddle(self, image):
        start_point = (640, 0)
        end_point = (640, 720)
        color = (0, 255, 0)
        thickness = 9

        image = cv2.line(image, start_point, end_point, color, thickness)

    def putEyeDots(self, frame, font, color):
        for i in range(len(self.collection.key_landmarks)):
            for j in range(2):
                cv2.putText(frame, '.', self.collection.key_landmarks[i][j], font, 1, color, 3, cv2.LINE_AA)