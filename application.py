#!/usr/bin/env python
try:
    import web
except ImportError:
    print "No server"
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
    try:
        app = web.application(urls, globals())
    except NameError:
        print ""

    sender.startSender()
    
    # Servidor en localhost:8080
    try:
        app.run()
    except NameError:
           print "" 
