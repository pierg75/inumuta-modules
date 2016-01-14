# coding=utf8
"""
slap.py - plambri
Copyright 2016 Pierguido Lambri

Licensed under the Eiffel Forum License 2.
"""
from __future__ import unicode_literals
from sopel.config.types import StaticSection, ValidatedAttribute
from sopel.module import commands
# from sopel.module import rate, rule, commands
# from sopel.tools import Identifier
import random
import json
import os
import re

reSlapped = re.compile(r'\$slapped')
reSlapper = re.compile(r'\$slapper')


class SlapSection(StaticSection):
    db_file = ValidatedAttribute('dbfile', json.loads)

    def setup(bot):
        bot.config.define_section('slap', SlapSection)

    def configure(config):
        config.define_section('slap', SlapSection, validate=False)
        config.slap.configure_setting('dbfile', 'File for the slap db')


@commands('slap')
def slap(bot, trigger):
    """Command to slap someone
    """
    print("%s", trigger)
    nslapper = trigger.nick
    if trigger.group(2):
        nslapped = trigger.group(2).strip().split()[0]

    print("%s", nslapper)
    print("%", bot.config.slap.dbfile)
    # try:
    with open(os.path.expanduser(bot.config.slap.dbfile)) as f:
        slap_list = list(f)
        slap = random.choice(slap_list)
        bot.say("%s" % reSlapped.sub(nslapped, reSlapper.sub(nslapper, slap)))

    # except:
    #    print("Error while slapping")
    #    return
