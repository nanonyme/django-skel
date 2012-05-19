from __future__ import absolute_import
from .common import application
from twisted.web.wsgi import WSGIResource
from twisted.internet import reactor
application = WSGIResource(reactor, reactor.getThreadPool(), application)
                        
