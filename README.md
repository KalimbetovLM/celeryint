Celery'ni integratsiya qilamiz
Men pipenv virtual muhiti, VS code kodlash muhiti va Windows OS da bu ishlarni amalga oshirdim
Muallif: Lazizbek Kalimbetov
Aloqaga chiqish: 
    t.me://captainlazizbek
    lazizkalimbetov@gmail.com

Step 1.  Boshlash

    Pipenv dasturlash muhitini o'rnatamiz va ishga tushiramiz. Buning uchun siz loyihangiz joylashgan papkaga CMD yoki Powershell'da kirasiz. Quyidagi buyruqlarni kiriting:

        pip install pipenv     
        pipenv shell           
        
    Agar o'rnatish chog'ida Already satisfied(yoki shunga o'xshash) xatolik chiqsa buning yechimi boshqa projectingizdan pipenv.exe 
    faylini ko'chirib olib joriy loyiha papkasiga ctrl + v qiling (faqat pipenv.exe'ning o'zini) va muhitni qayta ishga tushiring

Step 2.  Celeryni o'rnatish

    Celery'ni o'rnating:

        pipenv install celery

    O'rnatilganini tekshirish uchun bir nechta usullar:

       1. python show celery
       2. pipenv show celery

Step 3.  RabbitMQ va Erlang'ni Chocolatey yordamida o'rnatish

    RabbitMQ'ni o'rnating. Bu jarayon e'tiborni talab qiladi. Biz RabbitMQ'ni uning sahifasidan emas, balki CMD'da Chocolatey usuli bilan o'rnatamiz. Shunisi soddaroq. Buning uchun siz Командная строка'dan chiqib ketib uni admnistrator nomidan ishga tushirishingiz kerak( Запуск от имени админстратора ). Shundan so'ng joriy loyiha papkasiga qaytib pipenv'ni ishga tushiring(pipenv shell). Quyidagi buyruqni kiriting:

        choco install rabbitmq

    Chocolatey RabbitMQ ishlashi uchun kerak bo'luvchi barcha paketlarni(jumladan Erlang'ni ham) yuklab oladi va kerakli joylarga o'rnatadi. 

Step 4.  Fayllarni tartibga keltirish

    Django'dagi loyihaga kirib barcha kerakli settinglarni o'rnating. Xususan:
        celeryint/celery.py
        celeryint/__init__.py
        celeryint/settings.py --> 128-129-qatorlar
        tasks/tasks.py
    Ushbu fayllarda nima nima uchun kerakligi to'liq(yoki noto'liq) bayon etilgan

Step 5.  RabbitMQ Server'ni ishga tushirish

    RabbitMQ serverini ishga tushiring. Buning uchun Пуск'dagi rabbitmq-server startdan aslo foydalanmang. Agar foydalangan bo'lsangiz uni o'chiring. Uning pastida rabbitmq-server stopga kiring. Shunda u o'chadi. Keyin esa Total Commander'da rabbitmq-server ni toping. Default holatda u c:\Program Files\RabbitMQ Server\rabbitmq_server\sbin da joylashgan bo'ladi.
    Ushbu fayldan rabbitmq-server nomli faylni adminstrator nomidan ishga tushiring(Запуск от имени адмистратора).
    Agar CMD ochilsa va u yerda Starting Broker.... chiqsa demak RabbitMQ serveri ishga tushdi. Agar CMD ochilsa va o'z-o'zidan qayta yopilsa demak sizning Пуск yordamida ishga tushirgan rabbitmq-server'ingiz hali ham ishlamoqda. Пускка qaytib borib uni o'chiring(qanday o'chirish yuqorida(Step 5.) ko'rsatilgan). Keyin rabbitmq-server'ni adminstrator nomidan(Запуск от имени адмистратора)ishga tushiring. 

Step 6.  Celeryni ishga tushirish

    Endi faqatgina Celeryning o'zini ishga tushirish qoldi. Buning uchun loyihangizning o'zida joylashgan terminalda:

        celery -A celeryint worker -l INFO --pool=solo

    buyrug'ini bering. Buyruqdagi celery buyruq aynan Celery'ga tegishliligini, -A esa undan keyingi so'z project nomi ekanligini(Mening holatimda loyiha nomi celeryint, sizning holatingizda bu o'zgarishi mumkin. Muhimi siz aynan django-admin startproject yordamida ishga tushirgan loyihangiz nomini kiritishingiz kerak, app nomini emas), -l INFO esa ishlar qanday ketayotgani haqida ma'lumotlar ekranda aks etishini(bu ixtiyoriy), --pool=solo esa Windows'ning bir vaqtning o'zida bir qancha vazifalar bajarishini anglatadi. Buyruqning eng muhim qismi celery -A celeryint worker --pool=solo. Qolganlari ixtiyoriy. --pool=solo'ning muqobillari ham mavjud, xususan eventlet yoki gevent( jievent gevent emas). Ulardan birini pipenv install gevent/evetlet buyrug'i yordamida o'rnating. Celery'ni ishga tushirish haqidagi buyruq quyidagicha o'zgaradi. 

        celery -A celeryint worker -l INFO -P gevent/eventlet

    Demak, Celeryga qaytamiz. Yuqoridagi buyruqlarni ishga tushirganingizdan so'ng, Celery ishga tushishi kerak. Agar sizga xatolik qaytsa,xususan:
    [2024-04-16 19:01:53,442: ERROR/MainProcess] consumer: Cannot connect to amqp://guest:**@127.0.0.1:5672//: [WinError 10061] Подключение не установлено, т.к. конечный компьютер отверг запрос на подключение.
    Trying again in 2.00 seconds... (1/100)
    xatolik qaytsa RabbitMQ serveri ishga tushmagan yoki noto'g'ri ishga tushgan. Bu holatda Step 5. ni qayta takrorlang.
    Agarda Celery hech qanday xatoliksiz ishga tushsa tabriklayman, Celery muvaffaqiyatli integratsiya qilindi. Lekin uni tekshirib ko'rish zarar qilmaydi.

Step 7.  Tekshiruv

    CMD'da quyidagi buyruqni ishga tushiring:

        python manage.py shell

    Shundan so'ng Django ORM ishga tushadi. tasks.py faylidan(Step 4. ni eslang) tasklarni import qiling:

        >>> from tasks.tasks import hello_world
        >>> helo_world()

    Agar funksiya ishlasa Celery butunlay ishga tushdi. Endi xursand bo'lishingiz mumkin.







