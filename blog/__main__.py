'''
Main file, runs app.
'''

from blog.models import User
from blog.views import views
from blog.auth import auth
from blog.dashboard import dashboard
from blog import app

from flask_login import LoginManager

app.register_blueprint(views, url_prefix='/')
app.register_blueprint(auth, url_prefix='/')
app.register_blueprint(dashboard, url_prefix='/dashboard')

login_manager = LoginManager()
login_manager.login_view = 'auth.login_get'
login_manager.init_app(app)


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


FLASK_PORT = 8081

if __name__ == "__main__":
    app.run(debug=True, port=FLASK_PORT)
