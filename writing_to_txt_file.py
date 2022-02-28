# Create a filename variable to a direct or indirect path to the file.
file_to_save = 'Module 3 - Python\Elections_Analysis\Analysis\election_analysis.txt'

# Use the open statement to open the file as a text file.
# After we create the file_to_save variable, we set the open(file_to_save, "w") to a filename variable, outfile.
outfile = open(file_to_save, "w")

# Write some data to the file.
# Then, we use the filename variable to write "Hello World" to the file using the write() function from the os module.
# outfile.write("Hello World")

# Close the file
# Lastly, we use outfile.close() to close the file.
# outfile.close()

# Write three counties to the file.

# Using the with statement open the file as a text file.  Remove # to use this code.
with open(file_to_save, "w") as txt_file:
    #txt_file.write("Arapahoe, ")
    #txt_file.write("Denver, ")
    #txt_file.write("Jefferson ")

# Or write it on one line.
# txt_file.write("Arapahoe, Denver, Jefferson")

# New Line Escape Sequence puts the counties on each line. Add a # to use the above code instead of this one.
    #txt_file.write("Arapahoe\nDenver\nJefferson")

# SKILL DRILL
    txt_file.write("Counties in the election\n------------------------\nArapahoe\nDenver\nJefferson")

# REMEMBER TO CLOSE YOUR FILE
outfile.close()