import pycps;

# Create a connection to a Clusterpoint dawtabase.
con = pycps.Connection('tcp://cloud-eu-0.clusterpoint.com:9007', 'nexthack', 'rituraj.tc@gmail.com', 'clusterpoint', '794')
doc = {'title': 'goal', 'text': 'second text.' , 'Start': "1525-05-2015"}
con.insert({5111: doc})

