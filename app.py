from flask import Flask, redirect

from flask_login import LoginManager

from flask_socketio import SocketIO

from config import Config

from models.models import db, User

from routes.auth_routes import auth

from routes.task_routes import task

app = Flask(__name__)

app.config.from_object(Config)

db.init_app(app)

socketio = SocketIO(app, async_mode='threading')

login_manager = LoginManager()

login_manager.init_app(app)

login_manager.login_view = 'auth.login'


@login_manager.user_loader
def load_user(user_id):

    return User.query.get(int(user_id))


@app.route('/')
def home():

    return redirect('/login')


app.register_blueprint(auth)

app.register_blueprint(task)


if __name__ == '__main__':

    with app.app_context():

        db.create_all()

    socketio.run(app, debug=True)