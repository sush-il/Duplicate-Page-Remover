from flask import Flask
from server import home

app = Flask(__name__)

home_blueprint = home()
app.register_blueprint(home_blueprint, url_prefix="/")


if __name__=='__main__':
    app.run(debug=True,port=8000)
