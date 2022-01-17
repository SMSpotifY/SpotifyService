class Request:
    def __init__(self, user, service, request_type, data):
        self.our_user = user
        self.service = service
        self.request_type = request_type
        self.data = data

    @staticmethod
    def create_request(number, message_body):
        # FaunaService.getService().getUser(phone_number)
        # Request.parse_message(message_body)
        #
        pass

    @staticmethod
    def parse_message(message):
        word_list = message.split('')

        pass

