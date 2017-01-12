from time import time
from logging import getLogger
import datetime
from ipware.ip import get_ip

class LoggingMiddleware(object):
    def __init__(self):
        # arguably poor taste to use django's logger
        self.logger = getLogger('django.request')

    def process_request(self, request):
        request.timer = time()
        return None

    def process_response(self, request, response):    
    	x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    	if x_forwarded_for:
        	ip = x_forwarded_for.split(',')[0]
    	else:
        	ip = request.META.get('REMOTE_ADDR')    	
        self.logger.info(
            '[%s] [REQUESTED URL : %s %s ] %s (%.1fs)',            
            datetime.datetime.now().strftime("%d/%b/%Y %H:%M:%S"),
            request.method,       
            ''.join([
            ip,
            request.get_full_path(),
        	]),
            response.status_code,
            time() - request.timer
        )
        return response