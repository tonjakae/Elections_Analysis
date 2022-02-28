# How many votes did you get? Declare the my_votes variable equal to an input function.
#  Wrap the input function with int(). converts input from user to an integer or use float() to convert user data to a floating-point decimal
my_votes = int(input("How many votes did you get in the election?"))
# Total votes in the election. Declare the total_votes variable equal to an input function. Wrap the input function with int().
total_votes = int(input("What is the total votes in the election?"))
# Calculate the percentage of votes you received.
# Calculate percentage by dividing the users' votes by total votes and multiplying by 100 (*)
percentage_votes = (my_votes / total_votes) * 100
# Create a print statement. Must convert percentage_votes from int to a string
print("I received " + str(percentage_votes)+"% of the total votes,")
