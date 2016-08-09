import tornado.web
import tornado.escape

def make_app(message_handler, controller, callback_url, backdoor_url):
    class BackdoorHandler(tornado.web.RequestHandler):
        def get(self):
            controller.unlock()
            self.write('unlocking')

    class GroupMeCallbackHandler(tornado.web.RequestHandler):
        def post(self):
            data = tornado.escape.json_decode(self.request.body)
            message = data.get('text', '')
            message_handler.handle_message(message)
            self.write("")

    routes = [(callback_url, GroupMeCallbackHandler)]

    if backdoor_url:
        routes.append((backdoor_url, BackdoorHandler))

    return tornado.web.Application(routes)
