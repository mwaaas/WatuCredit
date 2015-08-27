__author__ = 'Mwaaas'
__email__ = 'francismwangi152@gmail.com'
__phone_number__ = '+254702729654'

from django_ussd.ussd.handlers import *


class Welcome(Menu):

    prompt = "Welcome to Watu Credit\n"

    options = (
        MenuOption("sign up", "EnterName"),
    )


class EnterName(Input):

    next_handler = "EnterAge"

    prompt = "Enter your name\n"

    session_key = "name"

class EnterAge(Input):

    next_handler = 'ThankYou'

    prompt = "Enter your age\n"

    session_key = "age"

class ThankYou(Quit):

    def get_message(self, req):
        return "Thank you for registering your name is {0} age {1}".format(
            req.session["name"], req.session['age']
        )
