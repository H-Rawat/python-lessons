# dictionary = {key: expression for (key, value) in iterable}

# example 1
cities_in_f = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}
cities_in_c = {key: round((value - 32) * (5/9)) for (key, value) in cities_in_f.items()}
print(cities_in_c)

# example 2
weather = {'New York': 'snowing', 'Boston': 'sunny', 'Los Angeles': 'sunny', 'Chicago': 'cloudy'}
sunny_weather = {key: value for (key, value) in weather.items() if value == 'sunny'}
print(sunny_weather)

# example 3
cities_in_f = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}
desc_cities = {key: ('WARM' if value > 40 else 'COLD') for (key, value) in cities_in_f.items() }
print(desc_cities)

# example 4
cities = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}

def check_temp(value):
    if (value > 70): return "HOT"
    else: return "COLD"

desc_cities = {key: check_temp(value) for (key, value) in cities.items() }
print(desc_cities)
