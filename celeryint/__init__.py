from .celery import app as celery_app # celery.py da yaratilgan app, unda port va backend url'i va tasklar joylashgan faylga yo'l ko'rsatilgan

__all__ = ("celery_app", ) # Bu yordamida Django har safar ishga tushganida Celery'ni o'ziga initialize qiladi. Buni Djangoga ko'rsatish shart chunki u Celery'ni avtomatik ravishda o'ziga qo'shib keta olmaydi
