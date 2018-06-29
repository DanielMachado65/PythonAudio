import urllib 
import json
import os
from flask import flask, request, make_response

# Flask app shout start in global layot
app = Flask(__name__)

@app.route('/webhook', method=['POST'])
def webhook():
	req  = request.get_json(silent=True, force=True)
	print('Request: ')
	print(json.dumps(req, indent=4))
	res = makeWebhookResult(req)