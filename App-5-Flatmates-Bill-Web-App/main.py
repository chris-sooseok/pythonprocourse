from flask import Flask, render_template, request
from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from flatmates_bill import flat

# __name__ is the name of current file
app = Flask(__name__)


class HomePage(MethodView):

    def get(self):
        return render_template('index.html')


class BillFormPage(MethodView):

    def get(self):
        bill_form = BillForm()
        return render_template(template_name_or_list='bill_form_page.html'
        , bill_form=bill_form)


class ResultsPage(MethodView):

    def post(self):
        billform = BillForm(request.form)
        amount = float(billform.amount.data)
        period = billform.period.data

        name1 = billform.name1.data
        days_in_house1 = float(billform.days_in_house1.data)

        name2 = billform.name2.data
        days_in_house2 = float(billform.days_in_house2.data)

        the_bill = flat.Bill(amount, period)
        flatmate1 = flat.Flatmate(name1, days_in_house1)
        flatmate2 = flat.Flatmate(name2, days_in_house2)


        return render_template('results.html',
        name1=flatmate1.name,
        name2=flatmate2.name,
        amount1=flatmate1.pays(the_bill, flatmate2),
        amount2=flatmate2.pays(the_bill, flatmate1))


class BillForm(Form):
    amount = StringField('Bill Amount: ')
    period = StringField('Bill Period: ')

    name1 = StringField('Name: ')
    days_in_house1 = StringField('Days in House: ')

    name2 = StringField('Name: ')
    days_in_house2 = StringField('Days in House: ')

    button = SubmitField('Calculate')

app.add_url_rule('/', view_func=HomePage.as_view('home_page'))
app.add_url_rule('/bill_form', view_func=BillFormPage.as_view('bill_form_page'))
app.add_url_rule('/results', view_func=ResultsPage.as_view('results_page'))

app.run(debug=True)