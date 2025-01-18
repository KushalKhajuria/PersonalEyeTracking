class DataCollection:
    def __init__(self):
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