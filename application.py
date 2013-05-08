#!/usr/bin/env python

import web
import urllib2 
import urllib 
import sender
import logging
import test

# Logger
logger = logging.getLogger('app')
handler = logging.FileHandler('/tmp/app.log');
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

urls = (
  "/test", "test.Test"
)


if __name__ == "__main__":
    app = web.application(urls, globals())
    #response = urllib2.urlopen(url)
    #print response.code
    #print response.info()['date']
    #print response.read()
    #response.close()

    sender.startSender()
    
    # Servidor en localhost:8080
    app.run()
