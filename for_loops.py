# Practice creating for loops!
counties = "Arapahoe", "Denver", "Jefferson"
# Iterate through lists and tuples. 
# Declare 'county' as your variable in counties, and set equal to the first item in the list of counties, "Arapahoe".
for county in counties:
    print(county)
# Print each number using a for loop:
numbers = [0, 1, 2, 3, 4]
for num in numbers:
    print(num)
# Print the same output using range(). This simplifies the code from above,
for num in range(5):
    print(num)



# Iterate through a list by index. 
# You'll need to get the length of the list as an integer for the range() function.
for i in range(len(counties)):
    print(counties[i])

# Let's break it down
# The variable i is used to indicate the index, or the values 0, 1, and 2, in the length of the counties list. 
# The letter i is often used for simplicity, but any variable can be used.
# Inside the range() function, we get the length of the list of counties, which is the integer 3.
# Then, we iterate through the list, where the variable i is equal to 0 for the first index. 
# The 0 is passed into the print(counties[i]) statement, where i = 0, and "Arapahoe" is printed.
# This process is continued until all three items, or counties, in the list are printed to the screen.

# Iterate through a dictionary
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
# Get the keys of a dictionary
for county in counties_dict:
    print(county)
# We will get the counties printed to the screen

# Use the keys() method to iterate over a dictionary to get the keys
for county in counties_dict.keys():
    print(county)

# Get the values of a dictionary using values().
for voters in counties_dict.values():
    print(voters)

# Get the value of the key in the output.
for county in counties_dict:
    print(counties_dict[county])

# Return the same data using get().
for county in counties_dict:
    print(counties_dict.get(county))

# Get the Key-Value pairs of a dictionary.
for county, voters in counties_dict.items():
    print(county, voters)

# Skill Drill
# Output should say, Arapahoe county has 422829 registered voters. Etc.
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")


# Get each dictionary in a list of dictionaries using the standard format.
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)

# Iterate over the voting_data list of dictionaries and print the counties using range()
for i in range(len(voting_data)):
    print(voting_data[i]['county'])

# Get the values from a list of dictionaries (NESTED)
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

# Print only the county name from each dictionary
for county_dict in voting_data:
    print(county_dict['county'])
