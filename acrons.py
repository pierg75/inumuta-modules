# coding=utf8
"""
acrons.py - Willie (Sopel) Acronyms Module
Copyright 2015 Pierguido Lambri
Licensed under the Eiffel Forum License 2.

http://willie.dftba.net
"""
from __future__ import unicode_literals
from willie import web, tools
from willie.module import NOLIMIT, commands, example, rule
import urllib2
import lxml.html

@commands('acron')
@example('.acron IOT')
def acron(bot, trigger):

    # Get the page asked
    if trigger.group(2) is None:
        bot.reply("What do you want me to look up?")
        return NOLIMIT
    
    url = "http://www.acronymfinder.com/"
    full_url = url+trigger.group(2)+".html"
    acron_page   = urllib2.urlopen(full_url).read()


    # Decode the html page
    html   = lxml.html.fromstring(acron_page)

    # Get only the class we need (the page has multiple classes from the most known
    # to the the least known meaning of the acronyms 
    r5 = html.xpath('//a[@class="r5"]')
    r4 = html.xpath('//a[@class="r4"]')
    r3 = html.xpath('//a[@class="r3"]')

    # Got through all the classes we have and add to a list
    list_acron = []

    for elem in r5:
        means = elem.values()
        list_acron.append(means[2])

    for elem in r4:
        means = elem.values()
        list_acron.append(means[2])

    # Let's print only the first 5 elements (some times we get less than 5 
    # elements so we need to check the length of the lsit)
    if len(list_acron) > 5:
        counter = 0 
        while counter < 5:
            bot.say(list_acron[counter])
            counter +=1
    else:
        for el in range(len(list_acron)):
            bot.say(list_acron[el])

    
