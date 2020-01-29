
from twilio.rest import Client
import simplejson as json

class twilio_texter:
    def __init__(self,sid='none', token='none',number='none'):
        """
        This class uses Twilio to send a text message. Uses a JSON file to hook up account
        :param sid: Twilio account SID
        :param token: Twilio account token
        :param number: Twilio number
        """

        if sid == "none":
            with open('twilio_account.json') as f:
                config = json.load(f)
            sid = config['sid']
        if token == 'none':
            token = config['token']
        if number == 'none':

            self.number = config['number']
        else:
            self.number = number

        self.client = Client(sid, token)
        self.sid = sid
        self.token = token

    def send_text(self, num, message, test=False):
        """
        Sends a text with the given message to the given number
        :param num: Number to send a text to
        :param message: The message to send
        :param test: Whether or not this is a test. This prints the message that would be sent
        :return: Null
        """
        if test:
            print("Sending a text message to number '{0:s}'. The message reads as follows\n{1:s}".format(num,message))
        else:
            self.client.messages.create(body=message, from_=self.number, to=num)

    def write_to_json(self):
        """
        Writes your twilio account to a file

        :return: True if successful
        """
        f = open("twilio_account.json",'a')
        data = {"sid": self.sid, "token": self.token,"number": self.number}
        f.write(json.dumps(data))
        f.close()
        return True

if __name__ =="__main__":
    Texter = twilio_texter()
    Texter.send_text(num='+12064376030',message="Test",test=True)
    Texter.write_to_json()
    with open('twilio_account.json') as f:
        config = json.load(f)

        print('sid: {}'.format(config['sid']))
        print('token: {}'.format(config['token']))
        print('number: {}'.format(config['number']))

