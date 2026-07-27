def clean_sequence(raw_dna):
    # Strip away all the outer whitespace noise
    return raw_dna.strip().upper()

def evaluate_samples(sample_list):
    clean_results = []
    
    # Loop through the rows one by one
    for sample in sample_list:
        if not sample or ":" not in sample:
            continue
            
        # Separate the name from the DNA sequence
        name, dna = sample.split(":")
        
        # Clean the sequence
        final_dna = clean_sequence(dna)
        
        # Simple conditional gate to check the length
        if len(final_dna) > 10:
            status = "Valid Sequence Group"
        else:
            status = "Sequence Too Short"
            
        clean_results.append({
            "Sample_Name": name.strip(),
            "DNA_Length": len(final_dna),
            "Status": status
        })
        
    return clean_results

if __name__ == "__main__":
    # A tiny dataset of raw genomic text rows
    raw_data = [
        "BRCA1_Sample :   atgctagctagctag ",
        "BRAF_Sample : tagc"
    ]
    
    output = evaluate_samples(raw_data)
    print(output)
