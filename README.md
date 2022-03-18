# WAPL

**WAPL - Web interface for watering plants. You can create watering points, set up automatic watering.
	Written in python, uses the Django framework. Uses Django's built-in web server,
	it is not designed for heavy loads. Will only work on raspberry.**

## WAPL installation


### installing Raspberry OS on a flash drive
- detailed instruction [here](https://www.raspberrypi.com/documentation/computers/getting-started.html#setting-up-your-raspberry-pi). It is advised to download the Raspberry OS Lite
    
### Application installation
- connect the flash drive to raspberry, connect the monitor, power supply, keyboard and internet
- Your raspberry will start loading. Wait for everything to load. Launch terminal. Default login is 'pi', password is 'raspberry'
- **Run these commands::**
```
sudo apt install python3-pip python3-venv supervisor git
git clone https://github.com/jon-elf/WAPL
cd WAPL
python3 -m venv wapl_env
source wapl_env/bin/activate
pip install -r requirements.txt
python3 manage.py makemigrations wapl
python3 manage.py migrate
sudo ln -s /home/pi/WAPL/supervisor_programs.conf /etc/supervisor/conf.d/
deactivate
```
    
### Turning on, connecting, turning off
- Run supervisor: ```sudo systemctl start supervisor``` (supervisor manages the server and command handler, it is required)
- Turn on the server: ```sudo supervisorctl start wapl_wsgi do_actions```
- Turn off the server: ```sudo supervisorctl stop wapl_wsgi do_actions```

To connect to the web interface, follow this link: https//x.x.x.x:8000/, 
where x.x.x.x is raspberry IP-adress. 
To find out the IP address of the raspberry, you need to run this command: ```ip a```

	
    
#### Note
When you first start the supervisor, there is a chance that he will not see the config. (Version 5.10 raspberry pi OS lite, supervisor 4.1.0)
To check that everything is working correctly, run the command ```sudo supervisorctl status```
If you see something like this, then everything works.
```
    do_actions RUNNING
    wapl_server RUNNING
```
If not, then you need to restart supervisor. Run ```systemctl reload supervisor```
Everything should work.
    
    
 ## Updating
To update, you need to run the ```git pull``` command while you are in the WAPL folder.

        
