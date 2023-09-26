number_pack_pens = int(input())
number_pack_markers = int(input())
liters_cleaner = int(input())
discount_percentage = int(input())

price_pens = number_pack_pens * 5.80
price_markers = number_pack_markers * 7.20
price_cleaner = liters_cleaner * 1.20

total_amount = price_pens + price_markers + price_cleaner
discount_amount = total_amount - (total_amount * (discount_percentage / 100))
print(discount_amount)
