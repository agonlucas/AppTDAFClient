import web
import config
import time
import urllib2
import urllib
import json
from threading import Thread

def threadSender(url, i, t, n_req):
    num_request = 0
    #json_data = {'entityType': 'device', 'entityId': 'M2M-Device-Test', 'data': {'measure': 'temperature', 'value': 12, 'uom': 'Cel'}}
    json_data = {'entityType': 'device', 'entityId': 'M2M-Device-Test', 'data': 'Testing'}
    post_data = json.dumps(json_data)
     
    # POST
    while (num_request < n_req):
        print "Sending to %s in thread num %d\n" % (url,i)
        try:
            clen = len(post_data)
            headers = {'TransactionInfo': '69', 'Content-Type': 'application/json', 'Content-Lenght': clen}
            request = urllib2.Request(url, post_data, headers);
            result = urllib2.urlopen(request) 
            #print result.read()
            result.close()
        except urllib2.URLError, e: 
            print e.reason
        except urllib2.HTTPError, e: 
            print e.reason
        time.sleep(t)
        num_request += 1 

def startSender():
    url=config.url
    num_threads=config.threads
    time_thread=config.time/1000
    num_requests=config.requests
    for i in range(num_threads):
        t = Thread(target=threadSender, args=(url, i, time_thread, num_requests))
        t.start()
