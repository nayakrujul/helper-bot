import argparse
import random
import datetime
import pytz

def randint():
    parser = argparse.ArgumentParser(prog='randint',
                                     description ='HelperBot by nayakrujul: generate a random number between a and b')
    parser.add_argument('a', metavar='a', type=int, nargs=1, help='the minimum value of the random number')
    parser.add_argument('b', metavar='b', type=int, nargs=1, help='the maximum value of the random number')
    args = parser.parse_args()
    print(random.randint(args.a[0], args.b[0]))

def output():
    parser = argparse.ArgumentParser(prog='output',
                                 description ='HelperBot by nayakrujul: evaluate a python expression and output')
    parser.add_argument('exp', metavar='exp', type=str, nargs=1, help='the expression to evaluate and output')
    args = parser.parse_args()
    try:
        print(eval(args.exp[0], {'exec': None, 'eval': None, 'open': None}))
    except Exception as e:
        print('\033[1;31mSomething went wrong:', e, '\033[0m')
 
def timein():
    parser = argparse.ArgumentParser(prog='timein',
                                 description ='HelperBot by nayakrujul: get the current time in the given timezone')
    parser.add_argument('tz', metavar='tz', type=str, nargs=1, help='the timezone to output the time in')
    args = parser.parse_args()

    try:
        dt = datetime.datetime.now(pytz.timezone(args.tz[0]))
        print(dt.strftime('%d/%m/%Y %H:%M:%S %Z %z'))
    except Exception as e:
        print('\033[1;31mSomething went wrong:', e, '\033[0m')
