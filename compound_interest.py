

def compound(amount, year_percent, months):
    months_percent = year_percent / 12
    for i in range(months):
        inc = amount / 100 * months_percent
        amount += inc
    return amount

print(compound(100000, 10, 12))


def compound(amount, year_percent, months):
    months_percent = year_percent / 12
    return amount * (1 + months_percent / 100) ** months
print(compound(100000, 10, 12))
