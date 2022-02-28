# Create an empty counties dictionary
counties_dict = {}
# Add the county "Arapahoe" to the dictionary as a key and the number of registered voters for "Arapahoe" as the values for this key
counties_dict["Arapahoe"] = 422829
# Add "Denver" and "Jefferson" the same way
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438
# Get the length of your dictionary (3)
len(counties_dict)
# Get all keys and values
counties_dict.items()
# Get all keys
counties_dict.keys()
# Get all values
counties_dict.values()
# Get a specific value (registered voters in "Denver")
counties_dict.get("Denver")
# You can also wrap key in brackets to get same data. 
counties_dict["Denver"]

