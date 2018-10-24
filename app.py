from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

def nato_convert(text):
    letterToNato = {'a':'alpha', 'b':'bravo', 'c':'charlie', 'd':'delta', 'e':'echo', 
                    'f':'foxtrot', 'g':'golf', 'h':'hotel', 'i':'india','j':'juliett', 
                    'k':'kilo', 'l':'lima', 'm':'mike', 'n':'november', 'o':'oscar', 'p':'papa', 
                    'q':'quebec', 'r':'romeo', 's':'sierra', 't':'tango', 'u':'uniform', 'v':'victor', 
                    'w':'whiskey', 'x':'x-ray', 'y':'yankee', 'z':'zulu'}

    result_str = " "

    for char in text:
        if char == " ":
            result_str += "\n"
        elif char not in "abcdefghijklmnopqrstuvwxyz":
            return None
        else:
            result_str += letterToNato[char] + "\n"

    return result_str

@app.route("/")
def hello_world():
    return "Hello world"

@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():
    """Send a dynamic reply to an incoming text message"""
    # Get the message the user sent our Twilio number
    body = request.values.get('Body', None)

    # Start our TwiML response
    resp = MessagingResponse()

    nato = nato_convert(body.lower())

    if nato:
        resp.message(nato)
    else:
        resp.message("Invalid character in message!")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)