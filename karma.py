# coding=utf8
"""
karma.py - maxpowa++
Copyright 2014 Max Gurela

Licensed under the Eiffel Forum License 2.
"""
from __future__ import unicode_literals
from willie.module import rate, rule, commands
from willie.tools import Identifier
import re


@rate(10)
@rule(ur'([\S]+?)\+\+')
def promote_karma(bot, trigger):
    """
    Update karma status for specify IRC user if get '++' message.
    """
    if (trigger.is_privmsg):
        return bot.say('People like it when you tell them good things.')

    names = re.findall('[\w][\S]+[\+\+]', trigger.raw)
    for name in names:
        who = name.split('+')[0].strip().split().pop()
        if (bot.db.get_nick_id(Identifier(who)) == bot.db.get_nick_id(Identifier(trigger.nick))):
            bot.say('You may not give yourself karma!')
            continue
        current_karma = bot.db.get_nick_value(who, 'karma')

        if not current_karma:
            current_karma = 0
        else:
            current_karma = int(current_karma)
        current_karma += 1

        bot.db.set_nick_value(who, 'karma', current_karma)
        bot.say(who + ' == ' + str(current_karma))


@rate(10)
@rule(ur'([\S]+?)\-\-')
def demote_karma(bot, trigger):
    """
    Update karma status for specify IRC user if get '--' message.
    """
    if (trigger.is_privmsg):
        return bot.say('Say it to their face!')

    names = re.findall('[\w][\S]+[\-\-]', trigger.raw)
    for name in names:
        who = name.split('+')[0].strip().split().pop()
        if (bot.db.get_nick_id(Identifier(who)) == bot.db.get_nick_id(Identifier(trigger.nick))):
            bot.say('You may not reduce yourself karma!')
            continue
        current_karma = bot.db.get_nick_value(who, 'karma')

        if not current_karma:
            current_karma = 0
        else:
            current_karma = int(current_karma)
        current_karma -= 1

        bot.db.set_nick_value(who, 'karma', current_karma)
        bot.say(who + ' == ' + str(current_karma))


@rate(10)
@rule(r'^([\S]+?)\=\=$')
def show_karma(bot, trigger):
    """
    Update karma status for specify IRC user if get '--' message.
    """
    current_karma = bot.db.get_nick_value(trigger.group(1), 'karma')
    if not current_karma:
        current_karma = 0
    else:
        current_karma = int(current_karma)

    bot.say(trigger.group(1) + ' == ' + str(current_karma))


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
