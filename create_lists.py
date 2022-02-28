counties = ["Arapahoe", "Denver", "Jefferson"]
# Print indexes 0 "Arapahoe" and 1 "Denver" stopping at 2 "Jefferson".
print(counties[0:2])
# Add "El Paso" to the counties list. This will add to the end of the list
counties.append("El Paso")
# Add "El Paso" to index (position) 2. This will add a second "El Paso" to the list
counties.insert(2, "El Paso")
# Remove "El Paso". This will remove the first instance of "El Paso" (index 2)
counties.remove("El Paso")
# Remove the other "El Paso" using pop().  This "El Paso" is the fourth item in the list (index 3)
counties.pop(3)
# Change "Jefferson" to "El Paso". "Jefferson" is the third item in the list (index 2)
counties[2] = "El Paso"


