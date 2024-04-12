from flask import Flask
from server import views

app = Flask(__name__)
app.register_blueprint(views, url_prefix="/")
app.register_blueprint(views, url_prefix="/fileUpload")

#/fileUpload

#for deployment
if __name__=='__main__':
    with app.app_context():
        app.run(debug=True,port=8000)
