from telegram import MessageEntity


def edit_message(update, context, text, **kwargs):
    context.bot.edit_message_text(
        text=text,
        chat_id=update.callback_query.message.chat_id,
        message_id=update.callback_query.message.message_id,
        **kwargs
    )


def reply_or_edit(update, context, text, **kwargs):
    if update.callback_query and update.message.text:
        edit_message(update, context, text, **kwargs)
    else:
        with_reply = True
        for entity in update.effective_message.entities:
            if entity.type == MessageEntity.BOT_COMMAND:
                with_reply = False

        if with_reply:
            update.message.reply_text(text, reply_to_message_id=update.message.message_id, **kwargs)
        else:
            update.message.reply_text(text, **kwargs)
