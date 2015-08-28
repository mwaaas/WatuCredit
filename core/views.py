from django.http import HttpResponse
from django_ussd.ussd.core import UssdAppView, UssdRequest
from django_ussd.http.views import UssdSimulatorView
from .handlers import *

class WatuCreditUssd(UssdAppView):
    initial_handler='Welcome'
    initial_level='1'
    initial_input='30'

    def post(self, req):
        return UssdRequest(
            phone_number=req.POST['phoneNumber'].strip('+'),
                       session_id=req.POST['sessionId'],
                       input_=req.POST['text'],
                       service_code=req.POST['serviceCode'],
        )

    def ussd_response_handler(self, ussd_response):

        ussd_text = '{status} {text}'

        status = 'STOP'
        if ussd_response.status:
            status = 'CON'

        ussd_text = ussd_text.format(status=status,
                                     text=ussd_response.text)

        return HttpResponse(ussd_text)


class WatuCreditUssdSimulator(UssdSimulatorView):
    ussd_view = WatuCreditUssd
    ussd_view_url_name = 'watu_ussd'
    phoneNumber = 'phoneNumber'
    session_id = 'sessionId'
    input = 'text'
    language = 'LANGUAGE'
    login_required=False

    def response_handler(self, response):
        response_status, response_message = response.content.split(' ', 1)

        if response_status == 'STOP':
            return False, response_message
        return True, response_message