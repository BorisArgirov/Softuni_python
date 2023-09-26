chicken_menu_number = int(input())
fish_menu_number = int(input())
vegetarian_menu_number = int(input())

chicken_menu = 10.35
fish_menu = 12.40
vegetarian_menu = 8.15

total_fee_menus = (chicken_menu_number * chicken_menu) + (fish_menu_number * fish_menu) + (vegetarian_menu_number * vegetarian_menu)
dessert = total_fee_menus * 0.20
delivery = 2.50
total_fee = total_fee_menus + dessert + delivery
print(total_fee)

