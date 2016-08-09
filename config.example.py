GROUPME_BOT_ID = None # to send messages to groupme instead of console change this
PORT = 8000
CALLBACK_URL = r"/groupme_callback" # groupme doesn't provide signatures on callbacks so security through obscurity
BACKDOOR_URL = r"/backdoor" # set to none if you don't want a backdoor
UNLOCK_TIME = 10 # how long the door should be open for on an unlock command
PI_PIN = None # if you are using a raspberry pi set this to the GPIO pin
