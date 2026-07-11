print("--- Test 1: Calculating capital gain ---")
# implement this function according to the specification
# if you don't know how to compute the capital gain, you can always google it :]
# (its really simple dw)
def calculate_capital_gain(current_price, cost_basis, quantity):
    """ 
    Calculates the capital gain (current profit/loss one would make IF they sold now)
    Notes: Cost Basis = original price at time of investment

    Inputs:
        current_price: price of asset right now
        cost_basis: price asset was originally bought at
        quantity: quantity of asset bought

    Returns:
        profit/loss: positive or negative dollar value
    """
    return 0

gain = calculate_capital_gain(
    current_price=500,
    cost_basis=400,
    quantity=4
)

print(
"""
Capital gain of:
    current_price=500,
    cost_basis=400,
    quantity=4
Equals: """,
    gain
    )

if (gain == 400): print("Correct!")
else: print("...Wrong Value!")



print("\n--- Test 2: Real world Application ---")
# Here are the (actual) prices of the amazon stock along with their dates, which i got from a python script i wrote (and u can write soon :] )
# Let's calculate the current capital gain, depending on which month they purchased

# --- AMZN Open Prices for each month ---
amzn_price= [492.53578,	530.76052,	497.32036,	511.56014,	516.53863,	486.27449,	482.24247,	428.33252,	392.01092,	372.68281,	411.90784,	464.83999]
DATES   =   ["2025-07",	"2025-08",	"2025-09",	"2025-10",	"2025-11",	"2025-12",	"2026-01",	"2026-02",	"2026-03",	"2026-04",	"2026-05",	"2026-06"]
# index     ---[0]---	---[1]---	---[2]---	---[3]---	---[4]---	---[5]---	---[6]---	---[7]---	---[8]---	---[9]---	---[10]---	---[11]---

# buuut, we have a problem, for some reason, the numbers they give us have way too many decimal digits, more than we need
#       (* it was actually so much worse, i deleted the rest of the digits but it actually looked like this [217.2100067138672, 223.52000427246094 ...])
# so, before we work with this data, lets round these to the nearest 2 decimals.

print("\n\t--- 2a: Rounding ---")
# for each of the values in the amzn_price list, REPLACE the value with value rounded to 2 decimal places (for cents).

# WRITE CODE HERE



print("\tRounded values:", amzn_price)



print("\n\t--- 2b: The actual part ---")
# using the function made earlier, implement this to specifically get the capital for the amazon stock.

def amazon_capital_gain(month_purchased_index: int):
    """
    Calculate and return the capital using the existing data, using the purcchase month as the cost basis
    and the latest month as the current value.
    Inputs:
        month_purchased_index: the INDEX of the month the stock was purchased in
    """
    return 0

print("\tAmazon Capital Gain when bought in month 2", amazon_capital_gain(2))

print("\n\t--- 2c: Who counts months like that anyway? ---")
# In reality, it makes more sense to get the cost basis from the actual date, instead of some arbitrary index number.
# using the [list].index() function, change the function so that we instead give the text date of when the stock was purchased,
# and use that to find the real index


def amazon_capital_gain(month_purchased: str): # its a string now
    """
    Calculate and return the capital using the existing data, using the purcchase month as the cost basis
    and the latest month as the current value.
    Inputs:
        month_purchased: the DATE TEXT of the month the stock was purchased in i.e. '2020-01'
    """
    return 0


print("\tAmazon Capital Gain when bought on 2025-08", amazon_capital_gain("2025-08"))


print("\n\n--- EXTENSION ULTRA NIGHTMARE LEGENDARY DIFFICULTY TASK : ...A diversified portfolio ---")
# a good portfolio shouldnt just have one stock, so here is a portfolio stored as a multi level 'dictionary'

portfolio = {
    "AMZN": {
        "Bought": "2025-08",
        "Quanity": 5,
    },
    "NVDA": {
        "Bought": "2025-11",
        "Quantity": 14,
    },
    "MSFT": {
        "Bought": "2026-02",
        "Quantity": 8
    }
}

# if this looks confusing, thats because it is :/
# to access these values, look at these examples, its 2 dictionaries combined
portfolio["AMZN"]["Bought"] # 2025-08
portfolio["MSFT"]["Quantity"] # 8

# this means we need the prices for each of these stocks, which fortunately, are right here
# unfortunately, its in another dictionary.
# hey, atleast they're already rounded

prices = {
    "AMZN": [219.5, 217.21, 223.52, 217.36, 255.36, 233.22, 231.34, 238.31, 204.55, 210.44, 265.58, 266.29],
    "NVDA": [156.08, 173.86, 169.77, 185.0, 207.81, 174.54, 189.61, 186.97, 174.8, 175.8, 201.05, 215.73],
    "MSFT": [492.54, 530.76, 497.32, 511.56, 516.54, 486.27, 482.24, 428.33, 392.01, 372.68, 411.91, 464.84]
}

# the dates are the same, so you can still use the same DATES list, which ive copied here 

DATES   =   ["2025-07",	"2025-08",	"2025-09",	"2025-10",	"2025-11",	"2025-12",	"2026-01",	"2026-02",	"2026-03",	"2026-04",	"2026-05",	"2026-06"]
# index     ---[0]---	---[1]---	---[2]---	---[3]---	---[4]---	---[5]---	---[6]---	---[7]---	---[8]---	---[9]---	---[10]---	---[11]---


# now onto the task,
# calculate the capital gain for each of the investments in the portfolio, and using those values, sum them to get the total capital gain
# glhf

