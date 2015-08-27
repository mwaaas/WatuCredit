from django.http import HttpResponse
from django_ussd.ussd.core import UssdAppView, UssdRequest
from django_ussd.http.views import UssdSimulatorView
from .handlers import *

class WatuCreditUssd(UssdAppView):
    initial_handler='Welcome'
    initial_level='1'
    initial_input='30'

    def get(self, req):
        return UssdRequest(req.GET['msisdn'],
                       req.GET['SESSIONID'],
                       req.GET['input'],
                       )

    def ussd_response_handler(self, ussd_response):
        response = HttpResponse(str(ussd_response))
        response['Freeflow'] = 'FB'
        if ussd_response.status:
            response['Freeflow'] = 'FC'
        return response


class WatuCreditUssdSimulator(UssdSimulatorView):
    ussd_view = WatuCreditUssd
    ussd_view_url_name = 'watu_ussd'
    phoneNumber = 'msisdn'
    session_id = 'SESSIONID'
    input = 'input'
    language = 'LANGUAGE'
    login_required=False

    def response_handler(self, response):
        response_status = response.headers.get('Freeflow', 'FC')
        response_message = response.content

        if response_status == 'FB':
            return False, response_message
        return True, response_message