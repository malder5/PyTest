from model.group import Group
from random import randrange
import random
import string
import os
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/groups.json"

for o, a in opts:
        if o == "-n":
            n=int(a)
        elif o=="-f":
            f = a


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
    for i in range(n)]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', f)

with open(file, 'w') as out:
    jsonpickle.set_encoder_options('json', indent=2)
    out.write(jsonpickle.encode(testdata))

