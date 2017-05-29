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
    return render_template('today.html')

@app.route('/company/amazon')
def amazon():
    return render_template('amazon.html')

@app.route('/company/apple')
def apple():
    return render_template('apple.html')

@app.route('/company/facebook')
def facebook():
    return render_template('facebook.html')

@app.route('/company/google')
def google():
    return render_template('google.html')

@app.route('/company/microsoft')
def microsoft():
    return render_template('microsoft.html')

@app.route('/company/samsung')
def samsung():
    return render_template('samsung.html')

@app.route('/company/twitter')
def twitter():
    return render_template('twitter.html')

@app.route('/tech/ai')
def ai():
    return render_template('ai.html')

@app.route('/tech/bigdata')
def bigdata():
    return render_template('bigdata.html')

@app.route('/tech/cloud')
def cloud():
    return render_template('cloud.html')

@app.route('/tech/ecommerce')
def ecommerce():
    return render_template('ecommerce.html')

@app.route('/tech/smart-device')
def smart_device():
    return render_template('ecommerce.html')

@app.route('/tech/security')
def security():
    return render_template('ecommerce.html')

@app.route('/tech/vr')
def tech_vr():
    return render_template('vr.html')

@app.route('/static')
def user_static():
    return render_template('static.html')

@app.route('/setting')
def user_setting():
    return render_template('setting.html')

@app.errorhandler(404)
def page_not_foun(e):
    return render_template('404.html'), 404

# launch
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
