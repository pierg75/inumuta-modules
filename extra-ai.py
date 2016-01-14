"""
extra-ai.py - Artificial Intelligence Module
Copyright 2015-2015, Pierguido Lambri
Licensed under the Eiffel Forum License 2.

http://sopel.chat
"""
from sopel.module import rule, priority, rate
import random
import time


@rate(30)
@rule('^\ +\/(j|join)\ \b')
def goodbye(bot, trigger):
    bot.reply('FAIL!')

@rate(30)
@rule('(^\ * (\/\ |\\)nick\ +)')
def goodbye(bot, trigger):
    bot.reply('FAIL!')

@rate(30)
@rule('(^(l[sl]|cd|pwd)\ +\b)')
def goodbye(bot, trigger):
    bot.reply('command not found')

@rate(30)
@rule('(?i)((sopel|TheGreatAbis)(\ |\?|\!|\.|))$')
def love(bot, trigger):
    respond = ['yes?', 'what\'s up?', 'uhm', 'whazzup?', 'doh!', 'yes love?','want a beer?','Yeap?']
    randtime = random.uniform(0, 3)
    time.sleep(randtime)
    bot.reply(random.choice(respond))


