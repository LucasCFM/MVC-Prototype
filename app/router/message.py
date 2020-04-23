from flask import Blueprint

from app.controllers.message import MessageController


api = Blueprint('messageAPI', __name__, url_prefix='/message', template_folder='../views/message')

api.add_url_rule('/', 'messageCRUD', MessageController.index, methods=['GET', 'POST', 'DELETE'])
