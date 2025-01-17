from django.db import models
from decimal import Decimal

class UserData(models.Model):
    username = models.CharField(max_length=100)
    # age = models.IntegerField()
    # gender = models.CharField(max_length=10)

    l_c_x = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
    l_c_y = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
    r_c_x = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
    r_c_y = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))

    l_l_x = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
    l_l_y = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
    r_l_x = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
    r_l_y = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))

    l_t_x = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
    l_t_y = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
    r_t_x = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
    r_t_y = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))

    l_r_x = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
    l_r_y = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
    r_r_x = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
    r_r_y = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))

    l_b_x = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
    l_b_y = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
    r_b_x = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
    r_b_y = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))

    l_ll_x = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
    l_ll_y = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
    r_ll_x = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
    r_ll_y = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))

    l_rr_x = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
    l_rr_y = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
    r_rr_x = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
    r_rr_y = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))

    def __str__(self):
        return self.name

    # class Meta:
    #     app_label  = 'myapp'


