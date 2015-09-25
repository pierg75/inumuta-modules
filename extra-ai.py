"""
extra-ai.py - Artificial Intelligence Module
Copyright 2015-2015, Pierguido Lambri
Licensed under the Eiffel Forum License 2.

http://sopel.chat
"""
from sopel.module import rule, priority, rate
import random
import time


@rule('^join\ #')
@rate(30)
def goodbye(bot, trigger):
    bot.reply('FAIL!')

