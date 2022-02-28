# so far you have learned to print a string or sentence between quotes
print("Hello World!")
# and a string with integer values converted to a string using concatenation with the + sign
interest = (5000)
print("Your interest for the year is $" + str(interest))

# F-strings: Formatted String Literals
# Begins with an f followed by a string wrapped in quotes
# Uses curly braces {} to add variables or expressions to the f-string

# Original code
my_votes = int(input("How many votes did you get in the election?"))
total_votes = int(input("What is the total votes in the election?"))
percentage_votes = (my_votes / total_votes) * 100
print("I received " + str(percentage_votes)+"% of the total votes.")

# Edit code using an F-String:
my_votes = int(input("How many votes did you get in the election?"))
total_votes = int(input("What is the total votes in the election?"))
print(f"I received {my_votes / total_votes * 100}% of the total votes.")

# Inside the curly braces of the last line the f-string perfoms the calculation!
# So there is no need to convert percentage_votes


# Using F-Strings with Dictionaries.
# Modify Skill Drill Exercise
# Original Code
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")

# Edit code using an F-String:
for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")

# Skill Drill (add a thousandths separator to the f-string)
for county, voters in counties_dict.items():
    print(f"{county} county has {voters:,} registered voters.")


# Multiline F-Strings
candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes / total_votes * 100}% of the total votes.")

print(message_to_candidate)

# Format Floating-Point Decimals
# Edit above code to format floating-point decimals and thousandths separators (,)
candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

print(message_to_candidate)

