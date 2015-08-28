__author__ = 'Mwaaas'
__email__ = 'francismwangi152@gmail.com'
__phone_number__ = '+254702729654'

from django_ussd.ussd.handlers import *


class Welcome(Menu):

    prompt = "Welcome to Watu Credit\n"

    options = (
        MenuOption("Take a loan", "LoanChoices"),
        MenuOption("Repay Loan", "RepayLoan"),
        MenuOption("About Us", "AboutUs")
    )


class LoanChoices(List):

    prompt = "You are qualified in the following loans:\n"

    items = (
        ListItem("Ksh 300", 300),
        ListItem("Ksh 200", 200),
        ListItem("Ksh 100", 100),
    )

    options = (
        MenuOption("Back", "Welcome"),
    )

    items_per_page = 5

    session_key = "amount"

    next_handler = "LoanSubmission"


class LoanSubmission(Quit):

    def get_message(self, req):
        return "We will process your loan of {} and " \
               "send you a text".format(req.session['amount'])

class RepayLoan(Input):

    prompt = "Enter amount you want to pay"

    session_key = "repay_amount"

    next_handler = "RepaySubmission"

class RepaySubmission(Quit):

    def get_message(self, req):
        return "Ksh {0} will be deducted in your mpesa account".format(
            req.session['repay_amount']
        )

class AboutUs(Menu):

    options = (
        MenuOption("Back", "Welcome"),
    )

    prompt = "Watu credit is an organisation that offers micro credits\n"