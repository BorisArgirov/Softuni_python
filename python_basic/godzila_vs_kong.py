film_budget = float(input())
statist_count = int(input())
one_statist_clothing_price = float(input())

decor_sum = film_budget * 0.10
clothing_sum = statist_count * one_statist_clothing_price

if statist_count > 150:
    clothing_sum = clothing_sum - (clothing_sum * 0.10)

total_film_sum = decor_sum + clothing_sum
rest2 = film_budget - total_film_sum
rest1 = total_film_sum - film_budget

if decor_sum + clothing_sum > film_budget:
    print("Not enough money!\n" + f"Wingard needs {rest1:.2f} leva more.")

elif decor_sum + clothing_sum <= film_budget:
    print("Action!\n" + f"Wingard starts filming with {rest2:.2f} leva left.")


#15437.62
#186
#57.99

#9587.88
#222
#55.68

