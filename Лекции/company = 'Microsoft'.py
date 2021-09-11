countries_temperature = [
    ['Thailand', [75.2, 77, 78.8, 73.4, 68, 75.2, 77]],
    ['Germany', [57.2, 55.4, 59, 59, 53.6, 55.4, 57.2]],
    ['Russia', [35.6, 37.4, 39.2, 41, 42.8, 39.2, 35.6]],
    ['Poland', [50, 50, 53.6, 57.2, 55.4, 55.4, 51.8]],
]


for country in countries_temperature:
    avg = 0
    for temp in country[1]:
        avg = avg + (temp - 32) * 5 / 9
    print(avg / len(country[1]))