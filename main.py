#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork

import logging
from config import Config
from core import commands,handlers
from telegram.ext import Application,CommandHandler, MessageHandler, filters

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(Config.BOT_TOKEN).build()
    function = application.add_handler

    # on different commands - answer in Telegram
    function(CommandHandler("start", commands.start))
    function(CommandHandler("help", commands.help_command))
    function(CommandHandler("prova", commands.command_test))

    function(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, handlers.new_member))

    # Run the bot until the user presses Ctrl-C
    application.run_polling()


if __name__ == "__main__":
    main()