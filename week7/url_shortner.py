import math
import sys
import itertools
from flask import Flask
from flask import request
from flask import Response
from flask import jsonify
from flask import abort
from flask import redirect

app = Flask(__name__)
#counter = itertools.count()
#counter.next()
counter = 100

# db for saving all the short urls
db = {}
LONG_URL_KEY = "long:%s"
SHORT_URL_KEY = "short:%s"
ID_KEY = "id:%s"

BASE = 62
UPPERCASE_OFFSET = 55
LOWERCASE_OFFSET = 61
DIGIT_OFFSET = 48
BASE_URL = 'http://localhost:5000'
"""
base62 encoder is used from https://gist.github.com/bhelx/778542
"""
def true_ord(char):
    """
    Turns a digit [char] in character representation
    from the number system with base [BASE] into an integer.
    """
    
    if char.isdigit():
        return ord(char) - DIGIT_OFFSET
    elif 'A' <= char <= 'Z':
        return ord(char) - UPPERCASE_OFFSET
    elif 'a' <= char <= 'z':
        return ord(char) - LOWERCASE_OFFSET
    else:
        raise ValueError("%s is not a valid character" % char)

def true_chr(integer):
    """
    Turns an integer [integer] into digit in base [BASE]
    as a character representation.
    """
    if integer < 10:
        return chr(integer + DIGIT_OFFSET)
    elif 10 <= integer <= 35:
        return chr(integer + UPPERCASE_OFFSET)
    elif 36 <= integer < 62:
        return chr(integer + LOWERCASE_OFFSET)
    else:
        raise ValueError("%d is not a valid integer in the range of base %d" % (integer, BASE))


def saturate(key):
    """
    Turn the base [BASE] number [key] into an integer
    """
    int_sum = 0
    reversed_key = key[::-1]
    for idx, char in enumerate(reversed_key):
        int_sum += true_ord(char) * int(math.pow(BASE, idx))
    return int_sum


def dehydrate(integer):
    """
    Turn an integer [integer] into a base [BASE] number
    in string representation
    """
    
    # we won't step into the while if integer is 0
    # so we just solve for that case here
    if integer == 0:
        return '0'
    
    string = ""
    while integer > 0:
        remainder = integer % BASE
        string = true_chr(remainder) + string
        integer /= BASE
    return string

class InvalidUsage(Exception):
    status_code = 400
    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv

class DuplicateIDException(Exception):
    pass

@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response

@app.route("/<string:link_id>")
def get_short_link(link_id):
    db_id = saturate(link_id)
    if db_id not in db:
        abort(404)

    short_url, long_url = db[db_id]
    return redirect(long_url, code=302)

@app.route("/", methods=['POST'])
def create_short_link():
    if not request.is_json:
        raise InvalidUsage('Invalid Request, please post valid json', status_code=400)

    content = request.get_json()
    url = content.get("url", None)
    friendly_id = content.get("id", None)
    if not url:
        raise InvalidUsage('Invalid Request, url is missing in post', status_code=400)

    try:
        short_url = __create_short_url(url, friendly_id)
    except DuplicateIDException, e:
        return "id:%s already exists"%friendly_id, 409

    return short_url, 201
        
def __create_short_url(long_url, friendly_id=None):
    id_key = ID_KEY % friendly_id
    long_url_key = LONG_URL_KEY % long_url
    if friendly_id and id_key in db:
        raise DuplicateIDException("%s id already exists" % friendly_id)

    global counter
    counter += 1
    id = counter
    short_url = dehydrate(id)
    db[id] = (short_url, long_url)
    if friendly_id:
        db[id_key] = (short_url, long_url)
    db[long_url_key] = (short_url, long_url)
    return "%s/%s" %  (BASE_URL, short_url)
