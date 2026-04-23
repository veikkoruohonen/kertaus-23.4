kirjasto = {
    "Kirja1": ["Kirjailija1", 2000, "Fiktio"],
    "Kirja2": ["Kirjailija2", 2010, "Draama"]
}

# Haku
print(kirjasto["Kirja1"][0])  # kirjailija
print(kirjasto["Kirja2"][2])  # genre

# Muokkaus
kirjasto["Kirja1"][2] = "Sci-fi"

# Lisäys
kirjasto["Kirja3"] = ["Kirjailija3", 2020, "Fantasia"]

# Poisto
del kirjasto["Kirja2"]

# Tulostus
print("\nPäivitetty kirjasto:")
for k, v in kirjasto.items():
    print(k, v)