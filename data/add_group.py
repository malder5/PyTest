from model.group import Group
from random import randrange
import random
import string

constant = [
    Group(name='Name1', header='header1', footer='footer1'),
    Group(name='Name2', header='header2', footer='footer2')
]


def random_string(prefix, maxlen):
    symbols = string.ascii_letters+string.digits+ " " #+string.punctuation
    return prefix+''.join([random.choice(symbols) for i in range(randrange(maxlen))])

testdata = [
    Group(name='', header='', footer='')]+[
    Group(name=random_string('name', 10), header=random_string('header', 20), footer=random_string('footer', 20))
    for i in range(10)]

testdata2 = [
    Group(name=name, header=header, footer=footer)
    for name in ['', random_string('name', 10)]
    for header in ['', random_string('header', 20)]
    for footer in ['', random_string('footer', 20)]
]