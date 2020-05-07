from flask import Flask, request, jsonify, Response
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash
from bson import json_util
from bson.objectid import ObjectId
from flask_cors import CORS
#descargar la libreria pip install -U flask-cors

app = Flask(__name__)
app.config['MONGO_URI']='mongodb://localhost/shop'
mongo=PyMongo(app)

@app.route('/user', methods=['POST'])
def create_user():
    #receiving data
    username=request.json['username']
    password=request.json['password']
    email=request.json['email']

    if username and email and password:
        hashed_password=generate_password_hash(password)
        id = mongo.db.users.insert(
            {'username': username, 'email':email,'password':hashed_password}
        )
        response={
            'id': str(id),
            'username':username,
            'password':hashed_password,
            'email':email
        }
        return response
    else:
        return not_found()

    return {'message':"data received"}

@app.route('/user', methods=['GET'])
def get_users():
    users=mongo.db.users.find()
    response=json_util.dumps(users)
    return Response(response, mimetype='application/json')

@app.route('/user/<id>', methods=['GET'])
def get_user(id):
    user=mongo.db.users.find_one({'_id': ObjectId(id)})
    response=json_util.dumps(user)
    return Response(response, mimetype='application/json')

@app.route('/user/<id>', methods=['DELETE'])
def delete_user(id):
    mongo.db.users.delete_one({'_id': ObjectId(id)})
    response=jsonify({'message':'User '+id+' was succesfully deleted'})
    return response

@app.route('/user/<id>', methods=['PUT'])
def update_user(id):
    username=request.json['username']
    password=request.json['password']
    email=request.json['email']

    if username and email and password:
        hashed_password=generate_password_hash(password)
        id = mongo.db.users.update_one({'_id': ObjectId(id)},{'$set':{
            'username': username, 'email':email,'password':hashed_password
        }})
        response = jsonify({'message':'User was update succesfully'})
        return response

@app.errorhandler(404)
def not_found(error=None):
    message = jsonify({
        'message':'Resource not found: ' + request.url,
        'status':404
    })
    message.status_code=404
    return message

if __name__ == "__main__":
    app.run(debug=True)

