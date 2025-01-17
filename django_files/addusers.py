import os
import django
from myapp.models import UserData

class AddUsers:
    def __init__(self):
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eyetracking.settings')
        django.setup()

    def add_x_y_data(self, x, y):
        user = UserData.objects.create(username="Kushal", l_c_x = x, l_c_y = y)

    def print_data(self):
        users = UserData.objects.all()
        for user in users:
            print(user.id, user.l_c_x, user.l_c_y)