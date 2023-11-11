number_pairs = int(input())
final_dictionary = {}

for pairs in range(number_pairs):

    name = input()
    grade = float(input())
    if name not in final_dictionary:
        final_dictionary[name] = []
    final_dictionary[name].append(float(grade))

to_remove = [name for name, grades in final_dictionary.items() if sum(grades) / len(grades) < 4.50]

for name in to_remove:
    del final_dictionary[name]

for names, grades in final_dictionary.items():
    average_grade = sum(grades) / len(grades)
    print(f"{names} -> {average_grade:.2f}")