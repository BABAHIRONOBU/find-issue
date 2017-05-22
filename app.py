import os
from flask import Flask, render_template, send_from_directory

# initialization
app = Flask(__name__)

# controllers
@app.route("/")
def hello():
    return render_template('index.html')

@app.errorhandler(404)
def page_not_foun(e):
    return render_template('404.html'), 404

# launch
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)