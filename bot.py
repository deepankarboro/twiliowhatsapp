from flask import Flask, request
import requests
import os
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route('/')
def hello():
    return "Welcome to Whatsapp Search. Enter anything to search"

@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower() #Gets the incoming message from user and stores it.
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    if 'quote' in incoming_msg or 'daily quote' in incoming_msg or 'quotes' in incoming_msg or 'inspirational quotes' in incoming_msg:
        # return a quote
        r = requests.get('https://api.quotable.io/random')
        if r.status_code == 200:
            data = r.json()
            quote = f'{data["content"]} ({data["author"]})'
        else:
            quote = 'I could not retrieve a quote at this time, sorry.'
        msg.body(quote) #Putting the quote as reply in message body
        responded = True
    if 'dog' in incoming_msg or 'puppy' in incoming_msg or 'doggie' in incoming_msg:
        # return a dog pic
        contents = requests.get('https://random.dog/woof.json').json()
        url = contents['url']
        msg.media(url) #Putting dog image as reply in message body
        responded = True
    if 'cat' in incoming_msg:
        # return a cat pic
        b=msg.media('https://cataas.com/cat') #Putting cat image as reply in message body
        responded = True
    if not responded:
        msg.body('I only know about famous quotes, dogs and cats, sorry!')
    return str(resp) #Returning message response to user

if __name__ == '__main__':
    app.run()
