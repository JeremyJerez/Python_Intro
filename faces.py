# Problem Set 0
#A series of exercises for CS50 hands-on projects
"""
This one it's my aproach on the making faces problem
"""

def main():

    msg = input("whatsap? ")
    o = convert(msg)
    print(o)

def convert(msg):
    y = msg.replace(':)', '🙂')
    z = y.replace(':(', '😐') # can be y too
    return z


main()
