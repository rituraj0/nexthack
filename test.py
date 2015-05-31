import pycps;
import uuid
from pycps.query import *
import xml.etree.ElementTree as ET
import json
import hashlib;

print( uuid.uuid1() );

def convert2json(document):
	root = ET.fromstring(document);
	data = {}
	for child in root:
		#if( child.tag == "id"):
		#	continue;
		data[child.tag]=child.text;
	#json_data = json.dumps(data);
	print( data);

def fetchFromDB(type):
	con = pycps.Connection('tcp://cloud-eu-0.clusterpoint.com:9007', 'nexthack', 'rituraj.tc@gmail.com', 'clusterpoint', '794')	
	response = con.search(term ( and_terms(type) , 'onup') );
	answer = []
	for id, document in response.get_documents(doc_format='string').items():
		answer.append(convert2json(document));
	return answer;
# Create a connection to a Clusterpoint dawtabase.

con = pycps.Connection('tcp://cloud-eu-0.clusterpoint.com:9007', 'nexthack', 'rituraj.tc@gmail.com', 'clusterpoint', '794')
print("Cneection");
doc = {'onup':'on' ,'title': 'Test', 'text': 'First text.' , 'Start': "15-05-2015" , "Name":"yxz" , "url": "www.google.com"};

hash_object = hashlib.sha512(b'Hello World')
print( hash_object.hexdigest() );
con.insert({ hash_object.hexdigest(): doc})

fetchFromDB("on");


