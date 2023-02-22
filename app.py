from flask import Flask, request
from db import add_image, add_like, add_dislike, get_data

app = Flask(__name__)


@app.route('/api/add-img/', methods=['POST'])
def home():
    if request.method == 'POST':
        data = request.get_json(force=True) # get data from request body
        photo_id = data['photo_id'] # get photo id 

        # add photo to database
        doc_id = add_image(photo_id)
        if doc_id:
            return {'doc_id': doc_id}
        return {'status': 400}


@app.route('/api/like/', methods=['POST'])
def like():
    if request.method == 'POST':
        data = request.get_json(force=True) # get data from request body
        doc_id = data['doc_id'] # get photo id
        chat_id = data['chat_id'] # get chat id

        # like photo
        if add_like(doc_id, chat_id):
            return {'status': 200}
        return {'status': 400}


@app.route('/api/dislike/', methods=['POST'])
def dislike():
    if request.method == 'POST':
        data = request.get_json(force=True) # get data from request body
        doc_id = data['doc_id'] # get photo id
        chat_id = data['chat_id'] # get chat id

        # like photo
        if add_dislike(doc_id, chat_id):
            return {'status': 200}
        return {'status': 400}
    

@app.route('/api/get-data/<doc_id>')
def get_data_view(doc_id: str):
    '''get data about img'''
    data = get_data(doc_id)
    if data:
        return data
    return {'status': 400}