import os
import time
import remotecontrol1
from gpiozero import LED

from google.cloud import pubsub_v1


fan=LED(14)
fan2=LED(15)
bulb = LED(18)
os.environ['GOOGLE_APPLICATION_CREDENTIALS']='/home/pi/<INSERT NAME OF CREDENTIALS JSON FILE>.json'
subscriber = pubsub_v1.SubscriberClient()
subscription_path = 'projects/rpiir-208011/subscriptions/mySubscription'

def callback(message):
    cmd=message.data.decode()
    print('Received message: {}'.format(message))
    print('data is:',cmd)
    if cmd == "onoff":
         os.system("irsend SEND_ONCE SONY_RMT_B104P KEY_POWER")
    if cmd == "eject":
         os.system("irsend SEND_ONCE SONY_RMT_B104P KEY_EJECT")
    if cmd == "play":
         os.system("irsend SEND_ONCE SONY_RMT_B104P KEY_PLAY")
    if cmd == "pause":
         os.system("irsend SEND_ONCE SONY_RMT_B104P KEY_PAUSE")
    if cmd == "stop":
         os.system("irsend SEND_ONCE SONY_RMT_B104P KEY_STOP")
    if cmd == "ok":
         os.system("irsend SEND_ONCE SONY_RMT_B104P KEY_OK")
    if cmd == "fanonbroom":
         fan.on()
    if cmd == "fanoffbroom":
         fan.off()
    if cmd == "fanonlroom":
         fan2.on()
    if cmd == "fanofflroom":
         fan2.off()
    if cmd == "bon":
         bulb.on()
    if cmd == "boff":
         bulb.off()
    if cmd == "halt":
         message.ack()
         os.system("sudo poweroff")

    message.ack()

subscriber.subscribe(subscription_path, callback=callback)

# The subscriber is non-blocking, so we must keep the main thread from
# exiting to allow it to process messages in the background.
print('Listening for messages on {}'.format(subscription_path))
while True:
