import tornado.ioloop

class DoorController:
    def __init__(self, unlock_time):
        self.current_timeout = None
        self.unlock_time = unlock_time
    def lock(self):
        pass
    def _unlock(self):
        pass
    def unlock(self):
        if self.current_timeout:
            tornado.ioloop.IOLoop.instance().remove_timeout(self.current_timeout)
        self._unlock()
        self.current_timeout = tornado.ioloop.IOLoop.instance().call_later(self.unlock_time, self.lock)
    def is_locked(self):
        pass

class ConsoleDoorController(DoorController):
    def __init__(self, unlock_time):
        self.locked = True
        super().__init__(unlock_time)
    def lock(self):
        if not self.locked:
            print("locking")
        self.locked = True
    def _unlock(self):
        if self.locked:
            print("unlocking")
        self.locked = False
    def is_locked(self):
        return self.locked

class PiDoorController(DoorController):
    def __init__(self, pin, unlock_time):
        import pigpio
        self.pi = pigpio.pi()
        self.pin = pin
        super().__init__(unlock_time)
    def lock(self):
        self.pi.write(self.pin, 1)
    def _unlock(self):
        self.pi.write(self.pin, 0)
    def is_locked(self):
        return self.pi.read(self.pin) == 1
