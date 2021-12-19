balance = 320000
annualInterestRate = 0.2

init_bal = balance
MonthInt = annualInterestRate/12
lowerbound = balance/12
upperbound = (balance*(1+MonthInt)**12)/12

# print(lowerbound)
# print(upperbound)

MinPayGuess = (lowerbound+upperbound)/2

# print(MinPayGuess)
cycle = 0

while abs(init_bal) > 0.1:
    cycle += 1
    MonthCount = 0
    init_bal = balance

    while MonthCount < 12:
        MonthCount += 1
        UnpaidBal = init_bal - MinPayGuess
        init_bal = UnpaidBal + (UnpaidBal*MonthInt)
        # print(f'{"Month "}{MonthCount}{" Balance is: "}{init_bal}')

    if init_bal > 0.1:
        # if ending balance is too high, then MinPayGuess was too low
        # set lowerbound to last guess
        # print("Too Low")
        lowerbound = MinPayGuess
        MinPayGuess = round(((lowerbound+upperbound)/2),2)

    elif init_bal < -.1:
        # if ending balance is too low, then MinPayGuess was too high
        # set upperbound to last guess
        # print("Too High")
        upperbound = MinPayGuess
        MinPayGuess = round(((lowerbound+upperbound)/2),2)

print(("Lowest Payment: "),end="")
print(MinPayGuess)
# print(f'{"It took "}{cycle}{" tries"}')







