from flask import Flask
from server import views

app = Flask(__name__)
app.register_blueprint(views, url_prefix="/")
app.config['SERVER_NAME'] = 'duplicate-page-remover.onrender.com'

#for deployment
if __name__=='__main__':
    with app.app_context():
        app.run(debug=False)


