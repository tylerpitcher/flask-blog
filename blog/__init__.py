'''
An init file is required for this folder to be considered as a module.
'''

from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '69cae04b04756f65eabcd2c5a11c8c24'
