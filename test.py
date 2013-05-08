import web
import logging



class Test:

    def __init__(self):
        print ""

    def POST(self):
        print "Receive Test::POST %s\n" % web.data() 
        print "Receive Test::POST %s\n" % web.ctx.environ

 
