import os
from flask import Flask, render_template, send_from_directory

# initialization
app = Flask(__name__)

# controllers
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/today')
def today():
    return render_template('index.html')

@app.route('/company/amazon')
def amazon():
    return render_template('index.html')

@app.route('/company/apple')
def apple():
    return render_template('index.html')

@app.route('/company/facebook')
def facebook():
    return render_template('index.html')

@app.route('/company/google')
def google():
    return render_template('index.html')

@app.route('/company/microsoft')
def microsoft():
    return render_template('index.html')

@app.route('/company/samsung')
def samsung():
    return render_template('index.html')

@app.route('/company/twitter')
def twitter():
    return render_template('index.html')

@app.route('/tech/ai')
def ai():
    return render_template('index.html')

@app.route('/tech/bigdata')
def bigdata():
    return render_template('index.html')

@app.route('/tech/cloud')
def cloud():
    return render_template('index.html')

@app.route('/tech/ecommerce')
def ecommerce():
    return render_template('index.html')

@app.route('/tech/vr')
def vr():
    return render_template('index.html')

@app.errorhandler(404)
def page_not_foun(e):
    return render_template('404.html'), 404

# launch
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)