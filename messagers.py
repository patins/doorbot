import tornado.httpclient
import tornado.escape

class ConsoleMessager:
    def send_message(self, message):
        print("MESSAGE: {}".format(message))

http_client = tornado.httpclient.AsyncHTTPClient()

class GroupMeMessager:
    def __init__(self, botId):
        self.botId = botId
    def send_message(self, message):
        http_client.fetch(self._make_send_message_request(message))
    def _make_send_message_request(self, message):
        data = {'bot_id': self.botId, 'text': message}
        headers = {'Content-Type': 'application/json; charset=UTF-8'}
        return tornado.httpclient.HTTPRequest("https://api.groupme.com/v3/bots/post",
                method='POST', headers=headers, body=tornado.escape.json_encode(data))
