from flask import Blueprint, request
from twilio.twiml.messaging_response import MessagingResponse

track_route = Blueprint('queue_track', __name__)


# noinspection PyUnusedLocal
@track_route.route('/queue/track', methods=['POST'])
def route():
    number = request.form['From']
    message_body = request.form['Body']
    response = MessagingResponse()

    # TODO: implementation
