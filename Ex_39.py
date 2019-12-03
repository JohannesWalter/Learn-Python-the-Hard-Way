# Dictionaries, Oh Lovely Dictionaries

# create a mapping of state to abbreviation

states ={
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# create a sbasic set of states and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# add some more cities

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities

print('-' * 10)
print("NY State has: ", cities['NY'])
print("OR State has: ", cities['OR'])

# print some states
print('-' * 10)
print("Michigan's abbreviation is: ", states["Michigan"])
print("Floridas's abbreviation is: ", states["Florida"])

# print every abbreviation
print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {cities}")

# now do both at the same time
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated as {abbrev}")
    print(f"and has a city {cities[abbrev]}")

print('-' * 10)

# safely get an abbreviation by state that might not be there

state = states.get('Texas')

if not state:
    print("Sorry no Texas.")

# get a city with a default value
city = cities.get('TX', 'Does not exist')
print(f"The city for the state 'TX' is: {city}")

