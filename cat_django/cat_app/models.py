from django.db import models
from django.contrib.auth.models import AbstractUser


class Users(AbstractUser):
    address = models.CharField(max_length=100)
    
    def __str__(self):
        return self.username
    
    
class Cats(models.Model):
    cat_owner = models.ForeignKey(
        to=Users,
        on_delete=models.CASCADE
    )
    cat_name = models.CharField(max_length=20)
    cat_age = models.CharField(max_length=2)
    COLORS = (
        ('Yello', 'Yello'),
        ('Black', 'Black'),
        ('White', 'White'),
        ('Orange', 'Orange')
    )
    cat_color = models.CharField(max_length=20, choices=COLORS, default='Yello')
    BREEDS = (
        ('Abyssinian', 'Abyssinian'),
        ('Maine-Coon', 'Maine-Coon'),
        ('Bengali', 'Bengali')
    )
    cat_breed = models.CharField(max_length=20, choices=BREEDS, default='Bengali')
    
    def __str__(self):
        return self.cat_name
    
    
class Messages(models.Model):
    message_owner = models.ForeignKey(
        to=Users,
        on_delete=models.CASCADE,
        related_name='owner_message'
    )
    where_message = models.ForeignKey(
        to=Users,
        on_delete=models.CASCADE,
        related_name='where_message'
    )
    message_name = models.CharField(max_length=20)
    message_content = models.CharField(max_length=50)
    message_create_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.message_name