import os, io
import json
from flask import Flask, request, jsonify, render_template, redirect, url_for, send_from_directory
from dotenv import load_dotenv
import requests
import uuid
import curlify
import arrow
from flask_socketio import SocketIO
import sys
import json
from people import friend
from item import item
import requests
from output_read import output_read


load_dotenv()
app = Flask(__name__, template_folder="dist",
            static_folder="dist", static_url_path="")
app.config['SECRET_KEY'] = 'secret!'
app.config['UPLOAD_FOLDER'] = os.getcwd()+'/dist'
socketio = SocketIO(app)
friendsList = {}

@app.route('/')
def main():
    return render_template('homepage.html')


@app.route('/v1/request-money', methods=['POST'])
def request_money():
    """Request Money Wrapper Function

    Takes the following body parameters:
        - amount {number}
        - contactName {string}
        - email {string}
        - memo {string, optional}
        - returnURL {string, optional}

    """
    data = request.data
    dataDict = json.loads(data)

    source_money_request_id = str(uuid.uuid4()).replace('-', '')
    response = requests.post(
        'https://gateway-web.beta.interac.ca/publicapi/api/v2/money-requests/send',
        headers={
            'accessToken': f"Bearer {os.getenv('ACCESS_TOKEN')}",
            'thirdPartyAccessId': os.getenv('THIRD_PARTY_ACCESS_ID'),
            'apiRegistrationId': os.getenv('API_REGISTRATION_ID'),
            'requestId': str(uuid.uuid4()),
            'deviceId': str(uuid.uuid4())
        },
        json={
            'sourceMoneyRequestId': source_money_request_id,
            'requestedFrom': {
                'contactName': dataDict['contactName'],
                'language': 'en',
                'notificationPreferences': [{
                    'handle': dataDict['email'],
                    'handleType': 'email',
                    'active': True
                }]
            },
            'amount': dataDict['amount'],
            'currency': 'CAD',
            'editableFulfillAmount': False,
            'requesterMessage': dataDict.get('memo', None),
            'expiryDate': arrow.utcnow().shift(hours=24).format('YYYY-MM-DDTHH:mm:ss') + '.835Z',
            'supressResponderNotifications': False
        })
    print(curlify.to_curl(response.request))

    return jsonify(json.loads(response.text)), response.status_code


@app.route('/v1/notifications', methods=['POST'])
def notifications():
    socketio.emit('notifications', {'data': request.data.decode("utf-8")})
    print(request.data)

    return ('', 202)

@app.route('/test', methods=['GET'])
def asdf():
	return render_template('test.html')

@app.route('/uploadPage', methods=['GET'])
def uploadPage():
	return render_template('/uploadPage.html')
	
@app.route('/fileUploader', methods=['POST'])
def upload_image():
	f = request.files['file']
	fileLocation = os.path.join(app.config['UPLOAD_FOLDER'], f.filename)
	f.save(fileLocation)
	detect_document(fileLocation)
	return render_template('/receiptVerify.html')
	
def detect_document(path):
	print("beginning docuument detection")
	file = open(os.path.join(app.config['UPLOAD_FOLDER'],'out.txt'),'w')
	
	"""Detects document features in an image."""
	from google.cloud import vision
	client = vision.ImageAnnotatorClient()
	
	with io.open(path, 'rb') as image_file:
		content = image_file.read()
		
	image = vision.types.Image(content=content)
	
	response = client.document_text_detection(image=image)
	
	for page in response.full_text_annotation.pages:
		for block in page.blocks:
			# file.write('\nBlock confidence: {}\n'.format(block.confidence))

			for paragraph in block.paragraphs:
				# file.write('Paragraph confidence: {}'.format(
				#     paragraph.confidence))

				for word in paragraph.words:
					word_text = ''.join([
						symbol.text for symbol in word.symbols
					])
					file.write('{} '.format(
						word_text))

					# for symbol in word.symbols:
					#     file.write('\tSymbol: {} (confidence: {})'.format(
					#         symbol.text, symbol.confidence))
				file.write('\n')
	file.close()
	
	items = list()
	prices = list()

	items = []
	prices = []
	output_read(items, prices)
	d = dict(zip(items,prices))
	file = open(os.path.join(app.config['UPLOAD_FOLDER'],'jsonItems.txt'),'w')
	print(json.dumps(d))
	file.write(str(d))
	file.close()


@app.route('/addfriend', methods=['GET'])
def addFriends():
	return render_template('/addfriend.html')

@app.route('/receiptDistribution', methods=['POST'])
def receiptDistribution():
	print("receipt distriadfpoksdlfkjad")
	data = request.form.to_dict()
	print(data)
	data = data['pTableData']
	with open('dist/jsontext.txt', 'w') as f:
		f.write(data)
    
    
    #################
    
	data = eval(data[1:-1])
	print(data)
	friends = list()
	for i in range(0,len(data)):
		friends.append( friend(data[i]['FirstName'],data[i]['LastName'],data[i]['Email']) )
    
	dish1 = item('1 Edamame', 9.00,13,12)
	dish2 = item('1 Kimo', 10.50,13,12)
	dish3 = item('1 A la Carte Sushi', 243.00,13,12)
	dish1.add_friend(friends)
	dish1.assign_prices()
	dish2.add_friend(friends)
	dish2.assign_prices()
	dish3.add_friend(friends)
	dish3.assign_prices()
	url = "https://mchacks6.appspot.com/v1/request-money"
	
	headers = {
    'Content-Type': "application/json",
    'cache-control': "no-cache",
    'Postman-Token': "d09e9d2c-cd69-429d-81b0-6669b3f7402e"
    }
	
	response_list = list(map(lambda x:requests.request("POST", url, data=x.interac_request(), headers=headers),friends))
	list(map(lambda x:print(x.text), response_list))
	
	return 'splitting.html'

    ##########################
@app.route('/splitting', methods=['GET'])
def splitting():
	return render_template('/confirm.html')


@app.route('/confirm', methods=['GET'])
def returnHome():
	return render_template('/homepage.html')


if __name__ == '__main__':
    socketio.run(app)
