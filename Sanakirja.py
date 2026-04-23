henkilot = {
    "John": ["John", 30, "Engineer"],
    "Emily": ["Emily", 25, "Artist"],
    "Anna": ["Anna", 22, "Student"]
}

# Haku
print(henkilot["John"][0], henkilot["John"][1])
print(henkilot["Emily"][2])

# Muokkaus
henkilot["Anna"][2] = "Teacher"
henkilot["James"] = ["James", 28, "Writer"]

# Lisäys
henkilot["Sophia"] = ["Sophia", 35, "Doctor"]

# Poisto
del henkilot["Emily"]

# Tulostus
print("\nLopullinen sanakirja:")
for k, v in henkilot.items():
    print(k, v)