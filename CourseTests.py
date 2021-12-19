

# Variables
balance=1000
starting_balance = balance
balance = starting_balance
annualInterestRate = 0.2
MonthIntRate = annualInterestRate/12
monthlyPaymentRate = 0.04
MinPayment = 0
PayStep = 10
MonthCount = 0


# MonthIntRate = annualInterestRate/12

while balance > 0:
    MonthCount = 0
    balance = starting_balance
    MinPayment += PayStep
    # print(MinPayment)
    # print(balance)

    while MonthCount < 12:
        MonthCount += 1
        MinMonthPayment = monthlyPaymentRate*balance
        MonthlyUnpdBal = balance - MinPayment
        balance = MonthlyUnpdBal + (MonthIntRate * MonthlyUnpdBal)
        # print(f'{"Month " }{MonthCount}{" Remaining balance: "}{balance}')
        # print(MonthCount)


# print("Remaining balance: ", end="")
# print(round(balance, 2))
print(("Lowest payment: "), end="")
print(MinPayment)


print(f"{'Remaining balance: '}{round(balance,2)}")
# print("Remaining balance: ",end="")
# print(round(balance,2))
