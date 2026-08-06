# ==============================================================================
# DAY 28 PORTFOLIO MILESTONE: STANDARD LIBRARY RANDOM SELECTION UTILITY
# ==============================================================================

import random

def execute_random_residue_sampling() -> None:
    """
    Utilizes the standard built-in random library to safely select 
    and isolate individual amino acid residues from a verified control sequence.
    """
    # Define a standardized testing sequence block
    target_sequence = ["Alanine", "Arginine", "Asparagine", "Aspartate", "Cysteine"]
    
    print("[SYSTEM INVENTORY] Core library modules loaded successfully.")
    
    try:
        # Utilize the random choice method to extract one node from the array array
        sampled_residue = random.choice(target_sequence)
        
        # Generate an automated institutional tracker index number
        sample_id_token = random.randint(1000, 9999)
        
        print(f"\nSUCCESS: Isolation complete. Sample ID: [GALG-{sample_id_token}]")
        print(f"Retrieved Biomarker Node: '{sampled_residue}'")
        
    except IndexError:
        print("\n[CRITICAL ERROR] Extraction failed. Sequence array data structure is empty.")

if __name__ == "__main__":
    execute_random_residue_sampling()
