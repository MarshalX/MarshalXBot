class Context:
    def __init__(self, bot_context, user):
        self.bot_context = bot_context
        self.bot = self.bot_context.bot
        self.user = user

    def __repr__(self):
        return f'<Context object>'
