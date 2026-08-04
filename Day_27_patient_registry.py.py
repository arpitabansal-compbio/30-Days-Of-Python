
# ==============================================================================
# DAY 27 PORTFOLIO MILESTONE: INT_BASED INDEX ERROR HANDLING GATE
# ==============================================================================

def execute_registry_audit() -> None:
    """
    Applies explicit try-except handling to isolate IndexError and ValueError
    exceptions during continuous array indexing searches inside a patient registry list.
    """
    # Pure clinical database array tracking sequential patient sample IDs
    patient_samples = ["SAMPLE_ID_104", "SAMPLE_ID_208", "SAMPLE_ID_309", "SAMPLE_ID_412"]
    
    print("[SYSTEM INVENTORY] Active genomic data block loaded.")
    
    try:
        user_choice = input("Enter patient record index slot to audit (0, 1, 2, or 3): ").strip()
        slot_index = int(user_choice)
        
        assigned_sample = patient_samples[slot_index]
        print(f"\nSUCCESS: Audit complete. Retrieved record node: '{assigned_sample}'")
        
    except IndexError:
        print("\n[CRITICAL ERROR] Target array index out of bounds.")
        print("Please restrict inputs to valid memory slots (0 to 3).")
        
    except ValueError:
        print("\n[CRITICAL ERROR] Incompatible data type. Integer entry required.")

if __name__ == "__main__":
    execute_registry_audit()

