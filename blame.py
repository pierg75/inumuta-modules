# coding=utf8
"""
blame.py - Don't blame $nickname :V
Copyright 2014 Max Gurela

Licensed under the Eiffel Forum License 2.
"""
from __future__ import unicode_literals
from willie.module import rule
import random


@rule('(die|blame|kill|beat|spit|hit|crash|batter|hammer|pound|thrash)(es|s)?.+$nickname')
def blame(bot, trigger):
    bot.action(random.choice(('dies a little inside', 'will survive!', 'drowns his sorrows in beer')))
