ages = {'Meg':24, 'Caroline':19, 'Matt':29}

ages['Caroline'] = 20

ages['Carly'] = 16

ages['Carrington'] = 15

ages['Mena'] = 15

print(ages)

for name in ages:
    print(name)

print(ages['Matt'])

for name in ages:
    print(ages[name])

for name in ages:
    print(ages[name] + 1)

for name in ages:
    currentAge = ages[name]
    ages[name] = currentAge + 1
    print(ages[name])

print(ages)
