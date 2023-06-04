from flask import Flask, render_template
from bridge import get_ip, get_data
#import os

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret key"

@app.route('/', methods=["GET", "POST"])
def trap():
    data = get_data(get_ip())
    return render_template('main.html', data=data)

if __name__ == "__main__":
    app.run()
    #app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)