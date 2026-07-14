
"""
PATIENT GENETIC RISK ANALYZER
"""
# Patient details
patient_name = input("Patient name: ")
patient_age = int(input("Age: "))
patient_family_hitory = input("Family History: ")
patient_genetic_marker = input("Genetic marker: ").upper()
patient_lifestyle_score = int(input("Lifestyle score: "))

# Create the custom function to calculate risk score
def calculated_risk_score(patient_age, patient_family_hitory, patient_genetic_marker, patient_lifestyle_score):
    risk_score = 0
    if patient_age > 50:
        risk_score += 20
    if patient_family_hitory == "yes" and  patient_genetic_marker == "A":
        risk_score += 30
    if patient_lifestyle_score < 5:
        risk_score += 25
    return risk_score

# Main Program Interface: Gather clinical parameters
print("==================================================")
print("            GENETIC RISK ASSESSMENT")
print("==================================================")
print(patient_name.strip().title())
print( str(patient_age) + " years old")
print("Family History: " + patient_family_hitory.strip().lower())
print("Genetic Marker: " + patient_genetic_marker.strip())
print("Lifestyle Score: " + str(patient_lifestyle_score)  + "/10")

#calculate total risk score
total_risk_score = calculated_risk_score(patient_age, patient_family_hitory, patient_genetic_marker, patient_lifestyle_score)


# Classify and process recommendations based on the calculated risk
if total_risk_score < 30:
    risk_level = "LOW RISK"
    recommendation = "Maintain routine annual genomic screening intervals."
elif 30 <= total_risk_score <= 60:
    risk_level = "MODERATE RISK"
    recommendation = "Initiate bi-annual monitoring and lifestyle optimization."
else:
    risk_level_score = "HIGH RISK"
    recommendation = "ALERT: Immediate genetic counselling recommended."

print("RISK SCORE CALCULATED: " + str(total_risk_score))
print("RISK LEVEL: " + risk_level)
print("RECOMMENDATION: " + recommendation)
