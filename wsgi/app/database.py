from app import app
from flask_pymongo import PyMongo
import os
from flask import jsonify

app.config['MONGO_DBNAME'] = os.environ['OPENSHIFT_APP_NAME']
app.config['MONGO_URI'] = os.environ['OPENSHIFT_MONGODB_DB_URL']+os.environ['OPENSHIFT_APP_NAME']
mongo = PyMongo(app)

# some comment!

@app.route('/database/collections', methods=['GET'])
def get_all_databases():
	return jsonify({'result' : mongo.db.collection_names()})
