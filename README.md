### For what?!
It is very convenient to launch the ssh tunnel at any time without access to a computer. 
This bot does not send a message to users who accidentally find this bot in Telegram.
3 buttons to choose from:
* Create ssh tunnel- and show the public address.
* Kill ngrok.
* Show public address ssh tunnel.
* 
*Created by default TCP from port 22.*
*Buttons in Russian, can be changed in the file utils.py*

### Install, start.

1. `clone https://github.com/Jagernau/telegram_ngrok_bot`
2. `cd telegram_ngrok_bot`
2. `python3.10 -m virtualenv env`
3. `source env/bin/activate`
4. `pip install -r requirements.txt`
5. `echo -e "NGROK_TOKEN=\nTELEGRAM_BOT_TOKEN=\nYOU_CHAT_ID=\nYOU_NAME=">todolist/.env`
    * In file `.env` put values.
    * NGROK_TOKEN= Specify a token of you ngrok account.
    * TELEGRAM_BOT_TOKEN= Insert telegram bot token.
    * YOU_CHAT_ID= Own telegram chat id.
    * YOU_NAME= First name telegram user.   
6. `python telegram_bot.py`


### Systemd.
```
[Unit]
Description=Ngrog_bot
After=network.target
Wants=network.target

[Service]
WorkingDirectory=/opt/my_projects/my_bots/
ExecStart=/opt/my_projects/my_bots/env/bin/python3.10 telegram_bot.py
Restart=always

[Install]
WantedBy=multi-user.target
```

*More pleasant automatically.*
*I accept ideas and corrections*
