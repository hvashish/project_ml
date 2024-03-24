import os
import platform
import logging
import logging.config
import secrets
secret_key = secrets.token_hex(16)
# print('secrete_key:-',secret_key)
from flask import Flask


app = Flask(__name__)
app.secret_key = '82a3649f9d7059e5fa53a2248e031821'
from .views import views as views_blueprint