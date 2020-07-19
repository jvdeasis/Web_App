# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 17:26:29 2020

@author: jonat
"""

from flask import (
    Bluepring, flash, g, redirect, render_template, request, url_for)

from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('blog', __name__)

