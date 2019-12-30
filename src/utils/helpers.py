from telegram import MessageEntity, ChatMember, TelegramError


def edit_message(update, context, text, **kwargs):
    context.bot.edit_message_text(
        text=text,
        chat_id=update.callback_query.message.chat_id,
        message_id=update.callback_query.message.message_id,
        **kwargs
    )


def reply_or_edit(update, context, text, **kwargs):
    """
        Вернёт сообщение и было ли оно отредактировано. Если нет - отправлено новое.
    """

    if update.callback_query and update.message.text:
        return edit_message(update, context, text, **kwargs), True
    else:
        with_reply = True
        for entity in update.effective_message.entities:
            if entity.type == MessageEntity.BOT_COMMAND:
                with_reply = False

        if with_reply:
            return update.message.reply_text(text, reply_to_message_id=update.message.message_id, **kwargs), False
        else:
            return update.message.reply_text(text, **kwargs), False


def is_channel_member(context, channel, user):
    try:
        chat_member = context.bot.get_chat_member(channel, user.telegram_id)

        if chat_member.status not in [ChatMember.CREATOR, ChatMember.ADMINISTRATOR, ChatMember.MEMBER]:
            return False
    except TelegramError:
        return False

    return True
