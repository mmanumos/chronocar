from flask import Flask, render_template, url_for
app = Flask(__name__)


@app.route('/base')
def base():
    return render_template('base.html')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/page1')
def page1():
    return render_template('page1.html')


@app.route('/page2')
def page2():
    return render_template('page2.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
