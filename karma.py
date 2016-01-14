# coding=utf8
"""
karma.py - maxpowa++
Copyright 2014 Max Gurela

Licensed under the Eiffel Forum License 2.
"""
from __future__ import unicode_literals
from sopel.module import rate, rule, commands
from sopel.tools import Identifier
import re


@rate(10)
@rule(r'.*?\b[\S]+\+\+')
def promote_karma(bot, trigger):
    """
    Update karma status for specify IRC user if get '++' message.
    """
    if (trigger.is_privmsg):
        return bot.say('People like it when you tell them good things.')

    already_updated = []
    # print(trigger.raw)
    names = re.findall(r'\b[\S]+\+\+', trigger.raw)
    # print("%s names" % names)
    for name in names:
        who = name.split('++')[0].strip().split().pop()
        # print(who)
        if who in already_updated:
            continue
        else:
            if (bot.db.get_nick_id(Identifier(who)) ==
               bot.db.get_nick_id(Identifier(trigger.nick))):
                bot.say('You may not give yourself karma!')
                continue
            current_karma = bot.db.get_nick_value(who, 'karma')

            if not current_karma:
                current_karma = 0
            else:
                current_karma = int(current_karma)
            current_karma += 1

            bot.db.set_nick_value(who, 'karma', current_karma)
            bot.say('%s has now %s point of karma!' %
                    (who, str(current_karma)))
            # Let's filter out all the eventual duplicate occurences of ++
            # People are evil!!
            already_updated.append(who)


@rate(10)
@rule(r'.*?\b[\S]+\-\-')
def demote_karma(bot, trigger):
    """
    Update karma status for specify IRC user if get '--' message.
    """
    if (trigger.is_privmsg):
        return bot.say('Say it to their face!')

    already_updated = []
    # print(trigger.raw)
    names = re.findall(r'\b[\S]+\-\-', trigger.raw)
    # print("%s names" % names)
    for name in names:
        who = name.split('--')[0].strip().split().pop()
        if who in already_updated:
            continue
        else:
            if (bot.db.get_nick_id(Identifier(who)) ==
               bot.db.get_nick_id(Identifier(trigger.nick))):
                bot.say('You may not reduce yourself karma!')
                continue
            current_karma = bot.db.get_nick_value(who, 'karma')

            if not current_karma:
                current_karma = 0
            else:
                current_karma = int(current_karma)
            current_karma -= 1

            bot.db.set_nick_value(who, 'karma', current_karma)
            bot.say('%s has now %s point of karma!' %
                    (who, str(current_karma)))
            # Let's filter out all the eventual duplicate occurences of ++
            # People are evil!!
            already_updated.append(who)


""" Let's disable this for now, it doesn't work anyway
@rate(10)
@rule(r'\b[\S]+\=\=')
def show_karma(bot, trigger):
    \"\"\"
    Update karma status for specify IRC user if get '--' message.
    \"\"\"
    who = trigger.group(1).split('--')[0].strip().split().pop()
    current_karma = bot.db.get_nick_value(trigger.group(1), 'karma')
    if not current_karma:
        current_karma = 0
    else:
        current_karma = int(current_karma)

    bot.say(trigger.group(1) + ' == ' + str(current_karma))
"""


@commands('karma')
def karma(bot, trigger):
    """Command to show the karma status for specify IRC user.
    """
    nick = trigger.nick
    if trigger.group(2):
        nick = trigger.group(2).strip().split()[0]

    karma = bot.db.get_nick_value(nick, 'karma')
    if not karma:
        karma = '0'
    bot.say("%s == %s" % (nick, karma))
