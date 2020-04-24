from flask import request

from app.controllers.message.actions import (
    addMessage, deleteMessage, listMessages
)


class MessageController(object):
    
    @staticmethod
    def index(data: dict = None):
        action = request.method
        if action is 'POST':
            return addMessage( data['content'] )
        elif action is 'DELETE':
            return deleteMessage( data['id'] )
        elif action is 'GET':
            return listMessages()
