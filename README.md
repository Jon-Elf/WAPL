# WAPL installation

## установка Raspberry OS на флешку
    1. Подключите вашу флешку к компютеру.
    2. Для начала вам нужно установить на флешку ОС Raspberry pi, 
       в этом вам поможет Raspberry pi imager  
       https://www.raspberrypi.com/software/
    3. Откройте Raspberry pi imager
    4. Выберите ОС Raspberry pi Lite (Находится во вкладке other)
    5. Выберите вашу флешку
    6. Нажмите кнопку write
    7. Подождите, пока ОС установится на вашу флешку

    
## Установка приложения
    8. Переставьте флешку в raspberry, подключите монитор, и
        сточник питания, клавиатуру и интернет.
    9. У вас начнёт загружаться raspberry. Подождите, 
        пока всё загрузится. По умолчанию логин pi, пароль raspberry
    10. скачайте все необходимые инструменты: sudo apt install python3-pip supervisor git
    11. скачайте проект: git clone https://github.com/Jon-Elf/WAPL
    12. Зайдите в папку с приложением: cd WAPL
    13. Скачайте все требуемые модули: pip install -r requirements.txt
    14. Создайте симлинк для корректной работы конфига: sudo ln -s /home/pi/WAPL/supervisor_programs.conf /etc/supervisor/conf.d/
    
    (Если хотите в дальнейшем подключится к raspberry удалённо через SSH): 
    sudo systemctl enable ssh
    sudo systemctl start ssh
    
## Включение
    14. Запустите проект: sudo systemctl start supervisor
    
## Подключение
    15. Что бы узнать айпи raspberry, пропишите команду: ip a
    16. Что бы подключиться к веб-интерфейсу, перейдите по этой ссылке: https//x.x.x.x:8000/, 
        где x.x.x.x - айпи raspberry. 
    17. Логин - admin,  пароль - 123pass321. Вы можете изменить это зайдя на https//x.x.x.x:8000/admin.
        
