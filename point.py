import pycps;

if __name__ == '__main__':
	print("Start");
# Create a connection to a Clusterpoint database.
con = pycps.Connection('tcp://cloud-eu-0.clusterpoint.com:9007', 'nexthack', 'rituraj.tc@gmail.com', 'clusterpoint', '794')
doc = {'title': 'Test', 'text': 'First text.' , 'Start': "15-05-2015"}
try:
	con.insert({5: doc})
	print("Insert successful")
except pycps.APIError as e:
	print(e)
	print("failed inserttion")l



	    fetch();
    resp = jsonify(result=posts)
    print("cool hare");
    '''
    con = pycps.Connection('tcp://cloud-eu-0.clusterpoint.com:9007', 'nexthack', 'rituraj.tc@gmail.com', 'clusterpoint', '794')
    for xy in resp["result"]["upcoming"]:
        con.insert({ uuid.uuid1(): xy});
    for xy in resp["result"]["ongoing"]:
        con.insert({ uuid.uuid1(): xy});
    '''
    resp.status_code = 200
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp