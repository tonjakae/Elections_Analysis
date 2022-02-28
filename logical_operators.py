# Use the "and" operator to determine if two counties, Arapahoe and El Paso, are in the list of counties
counties = ["Arapahoe", "Denver", "Jefferson"]
if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso are not in the list of counties.")
# The output code will be: Arapahoe or El Paso is not in the list of counties. (El Paso is not in the list)
# Next, check if EITHER are in the list
if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso is in the list of countiers.")
else:
    print("Arapahoe and El Paso are not in the list of counties.")
# The output code will be: Arapahoe or El Paso is in the list of counties
