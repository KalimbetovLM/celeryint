from time import sleep
from celery import shared_task # aynan shu funksiya yordamida celery o'zi bajarishi kerak bo'lgan funksiyalarni ajratib oladi
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string #random matn tuzuvchi funksiya
import string

@shared_task # celery bajarish kerak bo'lgan funksiya oldidan qo'shib qo'yilishi kerak
def hello_world():
    # example function
    print("Hello world 1")

    sleep(5)

    print("Hello world 2")
    
    return "success"

@shared_task
def generate_accounts(total=2):
    # example function
    for i in range(total):
        username = 'user_{}'.format(get_random_string(10, string.ascii_letters))
        email = '{}@example.com'.format(username)
        password = get_random_string(50)
        User.objects.create_user(username=username, email=email, password=password)
    return '{} random users created with success!'.format(total)        

    
