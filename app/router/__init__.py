from flask import Blueprint

from app.controllers.index import index


api = Blueprint('api', __name__, template_folder='../views')

api.add_url_rule('/', 'index', index, methods=['GET'])
