from celery import Celery   # Celeryning asosiy modui
import os                   # Operational System moduli

os.environ.setdefault("DJANGO_SETTINGS_MODULE",'celeryint.settings') # Celery o'ziga kerakli config'larni qaysi fayldan topishiga ishora

app = Celery('celeryint',                   # Celery sozlamalari
             broker = 'amqp://localhost',   # Broker joylashgan url, bizning holatimizda RabbitMQ serverining url'i
             backend = 'amqp://localhost',            # Natijalar qaysi aks etishi kerak bo'lgan url 
             include=['tasks.tasks'])       # tasklar (@shared_tasks qo'shilgan funksiyalar)  joylashgan faylga yo'l

app.config_from_object('django.conf:settings', namespace='CELERY')  # django.conf.settings (settings.py) da Celery'ga tegishli settinglarni qanday topishga ishora. Bizning holatimizda CELERY bilan boshlangan barcha setting'lar Celery'ga tegishli
app.autodiscover_tasks() # Bu metod yordamida Celery o'ziga berilgan funksiyalarni avtomatik ravishda qidirib topadi. Ya'ni oldiga @shared_task qo'shib yozilgan funksiyalar

