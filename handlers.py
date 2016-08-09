import time

class GroupMeMessageHandler:
    def __init__(self, messager, controller):
        self.last_sent = 0
        self.last_sent_lock = 0
        self.messager = messager
        self.controller = controller
    def handle_message(self, message):
        message = message.lower()
        if "unlock" in message:
            self.controller.unlock()
            if time.time() - self.last_sent > 10: # TODO move to config
                self.messager.send_message("Unlocking now")
                self.last_sent = time.time()
        """
        elif "lock" in message:
            locked_state = self.controller.is_locked()
            self.controller.lock()
            if time.time() - self.last_sent_lock > 4: # TODO move to config
                if locked_state:
                    self.messager.send_message("Already locked")
                else:
                    self.messager.send_message("Locking now")
                self.last_sent_lock = time.time()
        """
