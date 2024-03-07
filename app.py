from flask import Flask, render_template
from routes.home import home_route ; from routes.user import user_route

app = Flask(__name__, template_folder='templates')

app.register_blueprint(home_route)
app.register_blueprint(user_route)

if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)