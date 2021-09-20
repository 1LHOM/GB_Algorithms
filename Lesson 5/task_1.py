"""
1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4
квартала (т.е. 4 отдельных числа) для каждого предприятия.. Программа должна определить
среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий, чья
прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже
среднего.
"""


def avg_company_revenue():
    n = int(input('Enter number of companies: '))
    companies_dict = {}
    higher_than_average = {}
    less_than_average = {}
    average_revenue = 0

    for i in range(n):
        name = input(f'Enter {i+1} company name: ')
        companies_dict[f"{name}"] = [int(input(f'Enter revenue amount for {_ + 1} quarter: ')) for _ in range(4)]

    for value in companies_dict.values():
        average_revenue += sum(value)
    average_revenue /= n

    for k, v in companies_dict.items():
        if sum(v) > average_revenue:
            higher_than_average[k] = sum(v)
        else:
            less_than_average[k] = sum(v)

    print(f'{companies_dict}')
    print(f'Average revenue value is: {average_revenue}')
    print(f'These companies earned more than average:\n\t{higher_than_average}')
    print(f'These companies earned less than average:\n\t{less_than_average}')

    return higher_than_average, less_than_average


avg_company_revenue()
