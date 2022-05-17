#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork

from telegram import ForceReply

async def start(update, context) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_html(
        rf"Hi {user.mention_html()}!",
        reply_markup=ForceReply(selective=True),
    )


async def help_command(update, context) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("Help!")

async def command_test(update,context):
    bot = context.bot
    chat = update.effective_chat.id
    await bot.send_message(chat, "Ciao")