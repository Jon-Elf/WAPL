# WAPL

**WAPL - Веб интерфейс для полива растений. Можно создавать точки полива, настроить автоматический полив.
	   Написан на python, использует фреймворк Django. Используется встроенный в Django веб-сервер, 
	   он не предназначен для больших нагрузок.**

## WAPL установка


### установка Raspberry OS на флешку
- Подробная инструкция [здесь](https://www.raspberrypi.com/documentation/computers/getting-started.html#setting-up-your-raspberry-pi). Советуется скачать Raspberry OS Lite
    
### Установка приложения
- Переставьте флешку в raspberry, подключите монитор, сточник питания, клавиатуру и интернет
- У вас начнёт загружаться raspberry. Подождите, пока всё загрузится. Запустите терминал. По умолчанию логин pi, пароль raspberry
- Скачайте все необходимые инструменты: sudo apt install python3-pip python3-venv supervisor git
- Скачайте проект: git clone https://github.com/jon-elf/WAPL
- Зайдите в каталог WAPL: cd WAPL
- Создайте виртуальное окружение: python3 -m venv wapl_env
- Активируйте виртуальное окружение: source wapl_venv/bin/activate
- Скачайте все требуемые модули: pip install -r requirements.txt
- Создайте базу данных: python3 mysite/manage.py migrate
- Создайте симлинк для корректной работы конфига: sudo ln -s /home/pi/WAPL/supervisor_programs.conf /etc/supervisor/conf.d/
- Деактивируйте виртуальное окружение: deactivate
    
### Включение, подключение, выключение, создание админа
- Запустить supervisor: sudo systemctl start supervisor (supervisor управляет сервером и обработчиком команд, он необходим)
- Запустить сервер: sudo supervisorctl start wapl_server do_actions
- Выключить сервер: sudo supervisorctl stop wapl_server do_actions
- Создать админа: python3 WAPL/mysite/manage.py createsuperuser (Email писать не обязательно)

Что бы подключиться к веб-интерфейсу, перейдите по этой ссылке: https//x.x.x.x:8000/, 
где x.x.x.x - IP-адрес raspberry. 
Что бы узнать IP-адрес raspberry, нужно выполнить эту команду: ip a

	
    
#### Примечание
При первом запуске supervisor'а есть вероятность того, что он не увидит конфиг. (Версия 5.10 raspberry pi OS lite, supervisor 4.1.0)
Что бы проверить, что всё работает правильно, выполните команду 'sudo supervisorctl status'
Если вы увидели что-то вроде этого, то всё в порядке.
```
    do_actions                       RUNNING
    wapl_server                      RUNNING
```
Если же нет, то вам необходимо перезапустить supervisor. Выполните 'systemctl reload supervisor'.
Всё должно заработать.
    
    
 ## Обновление
 Что бы обновиться, нужно выполнить команду 'git pull' находясь в папке WAPL.

        
