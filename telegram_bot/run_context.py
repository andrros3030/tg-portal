import os


class Context:
    def __int__(self):
        self.BOT_TOKEN = os.getenv('BOT_TOKEN')
        self.SUDO_USERS = [
            439133935,
        ]


global_context = Context()
global_context.__int__()
