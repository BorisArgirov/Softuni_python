filed_treshold = int(input())

solved_problems_count = 0
filed_times = 0
grades_sum = 0
last_problem = ''
has_filed = True

while filed_times < filed_treshold:
    problem_name = input()
    if problem_name == 'Enough':
        has_filed = False
        break
    grade = int(input())
    if grade <= 4:
        filed_times += 1
    grades_sum += grade
    solved_problems_count += 1
    last_problem = problem_name

if has_filed:
    print(f'You need a break, {filed_treshold} poor grades.')
else:
    print(f"Average score: {grades_sum / solved_problems_count :.2f}")
    print(f"Number of problems: {solved_problems_count}")
    print(f"Last problem: {last_problem}")