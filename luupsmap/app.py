from flask import Flask, render_template

from model import db

app = Flask(__name__)

# CONFIG
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://{user}:{pw}@{address}/{db}'.format(
    user='luups_map',
    pw='luups',
    address='localhost:5432',
    db='luups_map_dev'
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# DB
db.init_app(app)


@app.route('/', methods=['GET'])
def home():
    return render_template('main.html')


if __name__ == '__main__':
    app.run()
