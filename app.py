""" Converts each letter in text message to its corresponding NATO phonetic alphabet spelling, 

then texts result back to user. """

from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

def nato_convert(text):
    """
    Converts letters in word to NATO phonetic alphabet spelling.

    Parameters:
        text(string): body of text message sent by user
    Returns:
        NATO spelling of text message
    """

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

@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():
    """ Receives and returns text messages """

    # Get message user sent to Twilio number
    body = request.values.get('Body', None)

    # Start TwiML response
    resp = MessagingResponse()

    # Convert message to NATO spelling
    nato = nato_convert(body.lower())

    if nato:
        resp.message(nato)
    else:
        resp.message("Invalid character in message")

    return str(resp)

if __name__ == "__main__":
    app.run()