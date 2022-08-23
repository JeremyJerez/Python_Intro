# Problem Set 0
"""
A series of exercises for CS50 hands-on projects
This it's my approach on the Tip calculator Problem
"""
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    d_dollars = d.replace("$", "")
    return float(d_dollars)

def percent_to_float(p):
    p_money = p.replace("%", "")
    p_calculated = float(p_money) / 100
    return p_calculated


main()
