from flask import Flask, render_template, url_for, request, redirect
app = Flask(__name__)


@app.route('/base')
def _base():
    return render_template('base.html')


@app.route('/login')
def _login():
    return render_template('login.html')


@app.route('/create_account')
def _create_account():
    return render_template('create-account.html')


@app.route('/panel')
def _panel():
    return render_template('panel.html')


@app.route('/expenses')
def _expenses():
    return render_template('expenses.html')


@app.route('/categories')
def _categories():
    return render_template('categories.html')


@app.route('/settings')
def _settings():
    return render_template('settings.html')


@app.route('/help')
def _help():
    return render_template('help.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
