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
    incoming_msg = request.values.get('Body', '').lower()
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
        msg.body(quote)
        responded = True
    if 'dog' in incoming_msg or 'puppy' in incoming_msg or 'doggie' in incoming_msg:
        # return a dog pic
        contents = requests.get('https://random.dog/woof.json').json()
        url = contents['url']
        msg.media(url)
        responded = True
    if 'cat' in incoming_msg or 'pussy' in incoming_msg:
        # return a cat pic
        b=msg.media('https://cataas.com/cat')
        responded = True
    if not responded:
        msg.body('I only know about famous quotes, dogs and cats, sorry!')
    return str(resp)


if __name__ == '__main__':
    #port = int(os.environ.get("PORT", 5000))
    #app.run(host='0.0.0.0', port=port)
    app.run()
    #app.run(host="localhost", port=5000, debug=True)
