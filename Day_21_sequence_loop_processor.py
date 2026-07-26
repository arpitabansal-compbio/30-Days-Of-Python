# Day_21_sequence_loop_processor.py
from typing import List, Dict, Any

def normalize_sequence(raw_dna: str) -> str:
    """Lecture 0: Cleans sequence whitespace and enforces uppercase mapping."""
    return raw_dna.strip().upper()

def evaluate_sequence_batch(sequence_metadata: List[str]) -> List[Dict[str, Any]]:
    """
    Lecture 1 & 2: Loops through raw sequence records and uses 
    conditional gates to calculate base lengths and track quality targets.
    """
    parsed_records: List[Dict[str, Any]] = []
    
    # Lecture 2: Loop engine parsing the sequence dataset line-by-line
    for index, raw_record in enumerate(sequence_metadata):
        clean_entry = raw_record.strip()
        
        # Lecture 1: Conditional gate to drop empty or malformed strings
        if not clean_entry or ":" not in clean_entry:
            continue
            
        try:
            # Slicing metadata at the delimiter
            sample_id, raw_sequence, raw_q_score = clean_entry.split(":")
            
            # Lecture 0: Variable assignment and string normalization methods
            dna_sequence = normalize_sequence(raw_sequence)
            
            # Explicit type casting from string to math float for quality parameters
            phred_score = float(raw_q_score.strip())
            
            # Lecture 1: Conditional logic evaluation gate
            if phred_score >= 30.0:
                quality_status = "HIGH_QUALITY_PASS"
            elif 0.0 <= phred_score < 30.0:
                quality_status = "LOW_QUALITY_FAIL"
            else:
                quality_status = "OUT_OF_BOUNDS_ERROR"
                
            parsed_records.append({
                "Batch_Index": index + 1,
                "Sample_ID": sample_id.strip().upper(),
                "Sequence_Length_BP": len(dna_sequence),
                "Mean_Phred_Score": phred_score,
                "QC_Verdict": quality_status
            })
            
        except ValueError:
            # Gracefully bypasses any numeric casting data traps
            continue
            
    return parsed_records

if __name__ == "__main__":
    # Biological text data stream input
    raw_sequence_stream = [
        "Patient_BRCA2_01 :  atgcgtacgtagctagc  : 38.5",
        "   ",  # Empty row anomaly
        "Patient_BRAF_02 : taggctagctagctagc : 18.2",
        "Patient_UNKNOWN_03 : atgctagctagc : CORRUPT_SCORE"  # Value casting trap
    ]
    
    # Execute loop processing run
    analysis_output = evaluate_sequence_batch(raw_sequence_stream)
    
    print("[RUN LOG] Day 21 Pure Genomic Verification Run Successful:")
    for record in analysis_output:
        print(record)

