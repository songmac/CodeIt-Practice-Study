
with open('python_application/chicken.txt', 'r', encoding='utf-8') as f:
    count = 0
    amount = 0

    for line in f:
        sales_data = line.strip().split(': ')
        amount += int(sales_data[1])
        count += 1

    print(amount/count)
