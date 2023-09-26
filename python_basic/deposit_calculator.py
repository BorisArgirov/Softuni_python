deposit_amount = float(input())
deposit_term = int(input())
annual_interest_rate = float(input()) / 100

final_amount = deposit_amount + deposit_term * ((deposit_amount * annual_interest_rate) / 12)
print(final_amount)


#сума = депозирана сума + срок на депозита * ((депозирана сума * годишен лихвен процент ) / 12)