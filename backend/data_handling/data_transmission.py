from django_files import addusers

class DataTransmission:
    def __init__(self, collection):
        self.collection = collection

    def transmit(self):
        application = addusers.AddUsers()

        application.add_x_y_data(
            self.collection.key_landmarks[0][0][0],
            self.collection.key_landmarks[0][0][1],
            self.collection.key_landmarks[0][1][0],
            self.collection.key_landmarks[0][1][1],

            self.collection.key_landmarks[1][0][0],
            self.collection.key_landmarks[1][0][1],
            self.collection.key_landmarks[1][1][0],
            self.collection.key_landmarks[1][1][1],

            self.collection.key_landmarks[2][0][0],
            self.collection.key_landmarks[2][0][1],
            self.collection.key_landmarks[2][1][0],
            self.collection.key_landmarks[2][1][1],

            self.collection.key_landmarks[3][0][0],
            self.collection.key_landmarks[3][0][1],
            self.collection.key_landmarks[3][1][0],
            self.collection.key_landmarks[3][1][1],

            self.collection.key_landmarks[4][0][0],
            self.collection.key_landmarks[4][0][1],
            self.collection.key_landmarks[4][1][0],
            self.collection.key_landmarks[4][1][1],

            self.collection.key_landmarks[5][0][0],
            self.collection.key_landmarks[5][0][1],
            self.collection.key_landmarks[5][1][0],
            self.collection.key_landmarks[5][1][1],

            self.collection.key_landmarks[6][0][0],
            self.collection.key_landmarks[6][0][1],
            self.collection.key_landmarks[6][1][0],
            self.collection.key_landmarks[6][1][1]
        )

        application.print_data()