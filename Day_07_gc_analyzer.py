"""
GC CONTENT ANALYZER
"""
# Create a custom function
def calculate_gc_content(g_bases, c_bases, total_bases):
    gc_count = (g_bases + c_bases)
    gc_percentage = (gc_count / total_bases) * 100
    return gc_percentage

# Now ask user for input
g_bases = int(input("Enter number of Guanine(G) bases: "))
c_bases = int(input("Enter number of Cytosine(C) bases: "))
total_bases = int(input("Enter total number of bases: "))

# Call the function and catch the return result in the variable
calculated_result = calculate_gc_content(g_bases, c_bases, total_bases )

# Print clean formated output
print()
print(f"The GC content of your DNA sequence is {calculated_result}%")
