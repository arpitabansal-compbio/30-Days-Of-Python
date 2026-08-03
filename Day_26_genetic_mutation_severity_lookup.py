#=================================================
# GENETIC MUTATION IMPACT SEVERITY LOOKUP SYSTEM
#=================================================

print("Mutation Code | Severity Score (1-10)")

mutation_database = {
"BRCA1_185delAG": 9,
"TP53_R175H": 8,
"EGFR_L858R": 7,
"HBB_E6V": 5,
"HTT_CAG": 8
}

while True:
    mutation_code = input("Enter mutation code (or 'q' to quit): ")

    if mutation_code == 'q':
        break
    try:
        severity_score = mutation_database[mutation_code]
        print(f"Severity score for {mutation_code}: {severity_score}")
        if severity_score > 0 and severity_score <= 3:   
            print("LOW RISK MUTATION")
        elif severity_score > 3 and severity_score <= 6:
            print("MEDIUM RISK MUTATION")
        elif severity_score > 6 and severity_score <= 10:
            print("HIGH RISK MUTATION")

    except KeyError:
            print("Mutation code not found in the database.")
