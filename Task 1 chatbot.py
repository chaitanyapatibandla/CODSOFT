import re
import datetime

class Chatbot:
    def __init__(self):
        self.rules = [
            # If the user says "hello", the chatbot responds with "hi".
            (re.compile(r'hello', re.IGNORECASE), 'hi'),

            # If the user says "how are you?", the chatbot responds with "I'm good, thanks for asking."
            (re.compile(r'how are you', re.IGNORECASE), "I'm good, thanks for asking."),
            (re.compile(r'can i ask u some questions', re.IGNORECASE), "yes,ofcourse."),
            (re.compile(r'what is your name', re.IGNORECASE), "I'm a bot,but you can call me with any name."),
            (re.compile(r'what is your favourite food', re.IGNORECASE), "I don't like eating I'm a bot,obviously."),

            # If the user says "what's the time?", the chatbot responds with the current time.
            (re.compile(r'what is the time', re.IGNORECASE), lambda: f"The time is {datetime.datetime.now().strftime('%H:%M:%S')}."),
        ]

    def respond(self, user_input):
        for rule, response in self.rules:
            if rule.match(user_input):
                return response()
        return "I don't understand."

if __name__ == '__main__':
    chatbot = Chatbot()

    while True:
        user_input = input("> ")
        response = chatbot.respond(user_input)
        print(response)
