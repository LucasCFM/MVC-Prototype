from flask import render_template

from app.db import db
from app.models.message import Message


def addMessage(content: str):
    """ add a new message """

    with db.atomic():
        Message.create(content=content)


def deleteMessage(messageId: int):
    """ delete a message by id """

    with db.atomic():
        Message.delete_by_id(messageId)


def listMessages():
    """ retrieves all messages """

    messages = Message.select()
    return render_template( 'message.html' )
