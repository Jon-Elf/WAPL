# WAPL documentation

## установка Raspberry OS на флешку
    1. Подключите вашу флешку к компютеру.
    2. Для начала вам нужно установить на флешку ОС Raspberry pi, 
       в этом вам поможет Raspberry pi imager  
       https://www.raspberrypi.com/software/
    3. Откройте Raspberry pi imager
    4. Выберите ОС Raspberry pi Lite
    5. Выберите вашу флешку
    6. Нажмите кнопку write
    7. Подождите, пока ОС установится на вашу флешку

    
## Установка приложения
    8. Найдите на флешке папку home
    9. Скачайте репозиторий, вставьте его в папку home
    10. Переставьте флешку в raspberry, подключите монитор, и
        сточник питания, клавиатуру и интернет.
    11. У вас начнёт загружаться raspberry. Подождите, 
        пока всё загрузится. По умолчанию логин pi, пароль raspberry
    12. Зайдите в папку с приложением: cd WAPL
    13. Скачайте утилиту pip: sudo apt install python3-pip
    14. Скачайте supervisor: sudo apt install supervisor
    15. Скачайте все требуемые модули: pip install -r requirements.txt
        (Если хотите в дальнейшем подключится к raspberry удалённо через SSH): 
        sudo systemctl enable sshsudo systemctl start ssh
    
## Включение
    13. Пропишите в терминале команду supervisord
    
## Подключение
    14. Что бы узнать айпи raspberry, пропишите команду: ip a
    15. Что бы подключиться к веб-интерфейсу, перейдите по этой ссылке: https//x.x.x.x:8000/, 
        где x.x.x.x - айпи raspberry. 
    16. Логин - admin,  пароль - 123pass321. Вы можете изменить это зайдя на https//x.x.x.x:8000/admin.
        
