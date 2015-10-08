"""
extra-ai.py - Artificial Intelligence Module
Copyright 2015-2015, Pierguido Lambri
Licensed under the Eiffel Forum License 2.

http://sopel.chat
"""
from sopel.module import rule, priority, rate
import random
import time


@rule('^(join\ +|\ +\/j\ +)#')
@rate(30)
def goodbye(bot, trigger):
    bot.reply('FAIL!')

@rule('(^\ * (\/\ |\\)nick\ +)')
@rate(30)
def goodbye(bot, trigger):
    bot.reply('FAIL!')



#@rule('(^(l[sl]|cd|pwd)\ +\b)')
#@rate(30)
#def goodbye(bot, trigger):
#    bot.reply('command not found')


@rule('(?i)((sopel|TheGreatAbis)(\ |\?|\!|\.))')
@rate(30)
def love(bot, trigger):
    bot.reply("Yes love?")



