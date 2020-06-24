from flask import Flask, render_template, url_for, make_response, redirect
app = Flask(__name__)

@app.route('/login')
def _login():
    """ Render the template for login screen """
    return render_template('login.html')

@app.route('/create_account')
def _create_account():
    """ Render the template for create_account screen """
    return render_template('create-account.html')

@app.route('/panel')
def _panel():
    """ Render the template for panel screen """
    return render_template('panel.html')

@app.route('/expenses')
def _expenses():
    """ Render the template for expenses screen """
    return render_template('expenses.html')

@app.route('/create_expense')
def _create_expense():
    """ Render the template for create expense screen """
    return render_template('create-expense.html')

@app.route('/categories')
def _categories():
    """ Render the template for Categories """
    return render_template('categories.html')

@app.route('/settings')
def _settings():
    """ Render the template for settings screen """
    return render_template('settings.html')

@app.route('/alerts')
def _alerts():
    """ Render the template for alerts screen """
    return render_template('alerts.html')

@app.route('/help')
def _help():
    """ Render the template for help screen """
    return render_template('help.html')

@app.route('/')
def redirect_default():
    """ Redirect to login like default page """
    response = make_response(redirect("/login"))
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0')
