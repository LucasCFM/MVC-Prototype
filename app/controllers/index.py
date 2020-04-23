from flask import render_template
from app import views


def index():
    return render_template( 'index.html' )
