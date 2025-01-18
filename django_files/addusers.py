import os
import django
from myapp.models import UserData

class AddUsers:
    def __init__(self):
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eyetracking.settings')
        django.setup()

    def add_x_y_data(self,
                     l_c_x,
                     l_c_y,
                     r_c_x,
                     r_c_y,

                     l_l_x,
                     l_l_y,
                     r_l_x,
                     r_l_y,

                     l_t_x,
                     l_t_y,
                     r_t_x,
                     r_t_y,

                     l_r_x,
                     l_r_y,
                     r_r_x,
                     r_r_y,

                     l_b_x,
                     l_b_y,
                     r_b_x,
                     r_b_y,

                     l_ll_x,
                     l_ll_y,
                     r_ll_x,
                     r_ll_y,

                     l_rr_x,
                     l_rr_y,
                     r_rr_x,
                     r_rr_y):
        user = UserData.objects.create(username="Kushal",
                                       l_c_x = l_c_x,
                                       l_c_y = l_c_y,
                                       r_c_x = r_c_x,
                                       r_c_y = r_c_y,

                                       l_l_x = l_l_x,
                                       l_l_y = l_l_y,
                                       r_l_x = r_l_x,
                                       r_l_y = r_l_y,

                                       l_t_x = l_t_x,
                                       l_t_y = l_t_y,
                                       r_t_x = r_t_x,
                                       r_t_y = r_t_y,

                                       l_r_x = l_r_x,
                                       l_r_y = l_r_y,
                                       r_r_x = r_r_x,
                                       r_r_y = r_r_y,

                                       l_b_x = l_b_x,
                                       l_b_y = l_b_y,
                                       r_b_x = r_b_x,
                                       r_b_y = r_b_y,

                                       l_ll_x = l_ll_x,
                                       l_ll_y = l_ll_y,
                                       r_ll_x = r_ll_x,
                                       r_ll_y = r_ll_y,

                                       l_rr_x = l_rr_x,
                                       l_rr_y = l_rr_y,
                                       r_rr_x = r_rr_x,
                                       r_rr_y = r_rr_y)

    def print_data(self):
        users = UserData.objects.all()
        for user in users:
            print(f"""
            id: {user.id}
            
            left eye center: ({user.l_c_x}, {user.l_c_y})
            right eye center: ({user.r_c_x}, {user.r_c_y})
            
            left eye left: ({user.l_l_x}, {user.l_l_y})
            right eye left: ({user.r_l_x}, {user.r_l_y})

            left eye top: ({user.l_t_x}, {user.l_t_y})
            right eye top: ({user.r_t_x}, {user.r_t_y})
            
            left eye right: ({user.l_r_x}, {user.l_r_y})
            right eye right: ({user.r_r_x}, {user.r_r_y})

            left eye bottom: ({user.l_b_x}, {user.l_b_y})
            right eye bottom: ({user.r_b_x}, {user.r_b_y})
            
            left eye left left: ({user.l_ll_x}, {user.l_ll_y})
            right eye left left: ({user.r_ll_x}, {user.r_ll_y})

            left eye right right: ({user.l_rr_x}, {user.l_rr_y})
            right eye right right: ({user.r_rr_x}, {user.r_rr_y})
            """)