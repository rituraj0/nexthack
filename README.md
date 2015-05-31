# nexthack
******** -Hackathon Project in  AngleHack- Hyderabad *********

Description:

	It is basically a web-app that keeps you updated about ongoing and upcoming hackathons. 
	This app crawls the internet , parse web pages , extract hackathon related information and 
	keep dumping into a CLUSTERPOINT no-sql database.

Technology used: 
	1) CLUSTERPOINT: to store huge dataset about hackathons 
	2) Heroku Cloud: to host this app 
	3) Flask : as backend 

WHY ClusterPOINT: 
	Initially i was using a database service(Say X. ) ,
	but X's performance is low compared to CLUSTERPOINT .
	Also , query on large database is very fast with CLUSTERPOINT . 
	so i decided to go with CLUSTERPOINT 

HOW TO USE:
	 I have also written an user friendly chrome extension ,
	 that fetches upcoming and ongoing hackathons from CLUSTERPOINT database and present it to USers.

	 a) Download chrome extension
	      https://github.com/rituraj0/nexthack/blob/master/chrome_extenstion.crx
	 b) Import it into Your chrome browser

Screen Shot:
	 	https://github.com/rituraj0/nexthack/blob/master/Screenshot.png

