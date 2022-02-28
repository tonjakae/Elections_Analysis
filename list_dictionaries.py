# Create an empty list called voting_data
voting_data = []
# Add, or append, each dictionary to the voting_data list
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})
# Get length of voting_data
len(voting_data)
# Add "El Paso" and its registered voters, 461149, to the second position (third item)
voting_data.insert(2, {"county":"El Paso", "registered_voters": 461149})
# Remove "Arapahoe" and its voters from voting_data
voting_data.remove({"county":"Arapahoe", "registered_voters": 422829})
# Make "Denver" and its voters the third item in voting_data but keep "Jefferson" and its voters as the second item
voting_data.remove({"county":"Denver", "registered_voters": 463353})
voting_data.insert(2, {"county":"Denver", "registered_voters": 463353})
# Add "Arapahoe" and its voters to voting_data
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})