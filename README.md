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
        !!! Все шаги нужно делать в точности как указано. То, что написано заглавными буквами пишите заглавными буквами !!!
    8. Переставьте флешку в raspberry, подключите монитор, сточник питания, клавиатуру и интернет.
    9. У вас начнёт загружаться raspberry. Подождите, пока всё загрузится. По умолчанию логин pi, пароль raspberry
    10. скачайте все необходимые инструменты: sudo apt install python3-pip supervisor git
    11. скачайте проект: git clone https://github.com/jon-elf/WAPL
    13. Скачайте все требуемые модули: pip install -r WAPL/requirements.txt
    14. Создайте базу данных: python3 WAPL/mysite/manage.py migrate
    15. Создайте симлинк для корректной работы конфига: sudo ln -s /home/pi/WAPL/supervisor_programs.conf /etc/supervisor/conf.d/
    
    (Если хотите в дальнейшем подключится к raspberry удалённо через SSH): 
    sudo systemctl enable ssh
    sudo systemctl start ssh
    
## Включение, подключение, выключение
    Запустить сервер: sudo systemctl start supervisor (Возможны сложности. Читайте пункт 'примечания')
    Выключить сервер: sudo systemctl stop supervisor
    
    Что бы подключиться к веб-интерфейсу, перейдите по этой ссылке: https//x.x.x.x:8000/, 
    где x.x.x.x - айпи raspberry. 
    Что бы узнать айпи raspberry можно прописать 'ip a'
    
### Примечания
    При первом запуске сервера есть вероятность того, что supervisor не увидит конфиг. (Версия 5.10 raspberry pi OS lite, supervisor 4.1.0)
    Что бы это проверить, выполните следущие шаги:
    1. Пропишите 'sudo supervisorctl'
    2. Пропишите 'status'
    3. Если вы увидели что-то вроде этого, то всё в порядке. Можете прописать 'quit'
        do_actions                       RUNNING
        wapl_server                      RUNNING
    4. Если же нет, то вам необходимо перезапустить supervisor. Пропишите 'quit', далее пропишите 'systemctl reload supervisor'.
       Всё должно заработать.
 

        
