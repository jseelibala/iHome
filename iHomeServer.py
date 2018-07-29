from flask import Flask,request
from flask_ask import Ask, statement, question, session
import os
import logging
app = Flask(__name__)
ask = Ask(app, "/ihome")
emsg="I did not get that. Please repeat it once more"
logging.basicConfig(filename='/home/jseelibala/mysite/logs/iHomeServer.log',format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logging.info("iHomeServer Started")

#Program Starts here
@app.route("/send")
def wservice():
    ms = request.args.get("msg")
    os.system("/home/jseelibala/.virtualenvs/myvirtualenv/bin/python3 /home/jseelibala/mysite/pubmsg.py "+ms)
    return 'Published ' + ms

@ask.launch
def start_skill():
    welcome_message = 'Hello there, Welcome to iHome by Vishal of N P S. How may I help you today?'
    return question(welcome_message).simple_card(title='Welcome!', content='Hello there, Welcome to iHome. How may I help you today?')

@ask.intent("EjectDVDPlayer")
def eject():
    message = 'Ok, Ejecting the DVD Player. What else?'
    os.system("/home/jseelibala/.virtualenvs/myvirtualenv/bin/python3 /home/jseelibala/mysite/pubmsg.py eject")
    return question(message).simple_card(title='DVD Player ejected', content='Your DVD Player has been ejected')

@ask.intent("play")
def play():
    message = 'Ok, Pressing play. What else?'
    os.system("/home/jseelibala/.virtualenvs/myvirtualenv/bin/python3 /home/jseelibala/mysite/pubmsg.py play")
    return question(message).simple_card(title='DVD Player play', content='Your DVD Player is being played')

@ask.intent("pause")
def pause():
    message = 'Ok, Pressing pause. What else?'
    os.system("/home/jseelibala/.virtualenvs/myvirtualenv/bin/python3 /home/jseelibala/mysite/pubmsg.py pause")
    return question(message).simple_card(title='DVD Player paused', content='Your DVD Player has been paused')

@ask.intent("stop")
def stop():
    message = 'Ok, Pressing stop. What else?'
    os.system("/home/jseelibala/.virtualenvs/myvirtualenv/bin/python3 /home/jseelibala/mysite/pubmsg.py stop")
    return question(message).simple_card(title='DVD Player stoped', content='Your DVD Player has been stoped')

@ask.intent("okbutton")
def ok():
    message = 'Ok, Pressing ok'
    os.system("/home/jseelibala/.virtualenvs/myvirtualenv/bin/python3 /home/jseelibala/mysite/pubmsg.py ok")
    return question(message).simple_card(title='DVD Player OK', content='Pressing OK')

@ask.intent("notustand")
def ustand():
    message = 'Sorry, I did not get that. Please Repeat it once more'
    return question(message).simple_card(title='Did not get that', content='Sorry, I did not get that. Please Repeat it once more')

@ask.intent("AMAZON.StopIntent")
def exit():
    message = 'Thanks for using iHome. Have a Nice Day!'
    return statement(message).simple_card(title='Thank You', content='Thank You for using iHome')

@ask.intent("iHomeOn", mapping={'name': 'device'})
def ondevice(name):
    global emsg
    logging.info("In iHomeOn Intent. Name is:"+name)
    if name == None:
        return question(emsg)
    else:
        name = name.replace(" ","")
        name = name.replace(".","")
        name.lower()
        if name == "livingroomfan":
            message = 'Ok, turning on the Living room Fan. What else?'
            os.system("/home/jseelibala/.virtualenvs/myvirtualenv/bin/python3 /home/jseelibala/mysite/pubmsg.py bon")
            return question(message).simple_card(title='Turning on Living room fan', content='Turning on living room fan')
        elif name == "bedroomfan":
            message = 'Ok, turning on the Bedroom Fan. What else?'
            os.system("/home/jseelibala/.virtualenvs/myvirtualenv/bin/python3 /home/jseelibala/mysite/pubmsg.py fanonbroom")
            return question(message).simple_card(title='Turning on Bedroom fan', content='Turning on Bedroom fan')
        elif name == "dvdplayer":
            message = 'Ok, turning on the DVD Player. What else?'
            os.system("/home/jseelibala/.virtualenvs/myvirtualenv/bin/python3 /home/jseelibala/mysite/pubmsg.py onoff")
            return question(message).simple_card(title='Turning on DVD Player', content='Turning on DVD Player')
        elif name == "livingroomlight":
            message = 'Ok, turning on the Living Room Light. What else?'
            os.system("/home/jseelibala/.virtualenvs/myvirtualenv/bin/python3 /home/jseelibala/mysite/pubmsg.py fanonlroom")
            return question(message).simple_card(title='Turning on Living room light', content='Turning on Living room light')
        else:
            return question(emsg)


@ask.intent("iHomeOff", mapping={'name': 'device'})
def offdevice(name):
    global emsg
    logging.info("In iHomeOff Intent. Name is:"+name)
    if name == None:
        return question(emsg)
    else:
        name = name.replace(" ","")
        name = name.replace(".","")
        name.lower()
        if name == "livingroomfan":
            message = 'Ok, turning off the Living room Fan. What else?'
            os.system("/home/jseelibala/.virtualenvs/myvirtualenv/bin/python3 /home/jseelibala/mysite/pubmsg.py boff")
            return question(message).simple_card(title='Turning off Living room fan', content='Turning off living room fan')
        elif name == "bedroomfan":
            message = 'Ok, turning off theBedroom Fan. What else?'
            os.system("/home/jseelibala/.virtualenvs/myvirtualenv/bin/python3 /home/jseelibala/mysite/pubmsg.py fanoffbroom")
            return question(message).simple_card(title='Turning off Bedroom fan', content='Turning off Bedroom fan')
        elif name == "dvdplayer":
            message = 'Ok, turning off the DVD Player. What else?'
            os.system("/home/jseelibala/.virtualenvs/myvirtualenv/bin/python3 /home/jseelibala/mysite/pubmsg.py onoff")
            return question(message).simple_card(title='Turning off DVD Player', content='Turning off DVD Player')
        elif name == "livingroomlight":
            message = 'Ok, turning off the Living Room Light. What else?'
            os.system("/home/jseelibala/.virtualenvs/myvirtualenv/bin/python3 /home/jseelibala/mysite/pubmsg.py fanofflroom")
            return question(message).simple_card(title='Turning off Living room light', content='Turning off Living room light')
        else:
            return question(emsg)





if __name__ == '__main__':
	app.run(debug=True)
