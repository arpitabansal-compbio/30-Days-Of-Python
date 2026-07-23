# feat: implement a basic biological dictionary mapping sequence keys

# Initialize a structured dictionary storing genomic base pairings
dna_complement_map = {
    "A": "T",
    "T": "A",
    "C": "G",
    "G": "C"
}

print("=== DEPLOYING GENOMIC DICTIONARY MAP ENGINE ===")

# Retrieve and print specific values using direct string keys
print(f"The complement base for Adenine (A) is: {dna_complement_map['A']}")
print(f"The complement base for Cytosine (C) is: {dna_complement_map['C']}")

print("=== DICTIONARY STRUCTURE RETRIEVAL COMPLETED CLEANLY ===")
