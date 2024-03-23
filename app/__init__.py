import os
import platform
import logging
import logging.config

from flask import Flask


app = Flask(__name__)

from .views import views as views_blueprint