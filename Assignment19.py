def max_visited_speciality(patient_data) :
    specialities = {
        "P" : "Pediatrics",
        "O" : "Orthopedics",
        "E" : "ENT"
    }
    speciality_count = {}
    for i in range(1, len(patient_data), 2) :
        speciality = patient_data[i]
        if speciality in speciality_count:
            speciality_count[speciality] += 1
        else :
            speciality_count[speciality] = 1
    max_speciality = max(speciality_count, key=speciality_count.get)
    return specialities[max_speciality]
patient_data = input("Enter patient data (e.g., 101,P,102,O,302,P,305,P) : ")
patient_data = patient_data.split(',')
result = max_visited_speciality(patient_data)
print(f"The medical speciality visited by the maximum number of patients is {result}")