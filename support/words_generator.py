# -*- coding: utf-8 -*-
import random

__author__ = 'elhe'

SAMPLE = ('Google', 'Yandex', u'Гуглить', u'оксфорд', 'learning')


def random_word():
    return random.choice(SAMPLE)