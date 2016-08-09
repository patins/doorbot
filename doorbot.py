import tornado.ioloop
import config

from doors import ConsoleDoorController, PiDoorController
from messagers import GroupMeMessager, ConsoleMessager
from handlers import GroupMeMessageHandler
from web import make_app

if config.PI_PIN:
    controller = PiDoorController(config.PI_PIN, config.UNLOCK_TIME)
else:
    controller = ConsoleDoorController(config.UNLOCK_TIME)

if config.GROUPME_BOT_ID:
    messager = GroupMeMessager(config.GROUPME_BOT_ID)
else:
    messager = ConsoleMessager()

message_handler = GroupMeMessageHandler(messager, controller)

app = make_app(message_handler, controller, config.CALLBACK_URL, config.BACKDOOR_URL)

if __name__ == "__main__":
    app.listen(config.PORT)
    tornado.ioloop.IOLoop.current().start()
