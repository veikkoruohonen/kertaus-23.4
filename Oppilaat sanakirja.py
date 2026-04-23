oppilaat = {
    "Matti": ["Matti", 1, "Matikka"],
    "Liisa": ["Liisa", 2, "Englanti"]
}

# Haku
print(oppilaat["Matti"][1])      # vuosiluokka
print(oppilaat["Liisa"][2])      # lempiaine

# Muokkaus
oppilaat["Matti"][2] = "Fysiikka"

# Lisäys
oppilaat["Teppo"] = ["Teppo", 3, "Historia"]

# Poisto
del oppilaat["Liisa"]

# Tulostus
print("\nPäivitetty sanakirja:")
for k, v in oppilaat.items():
    print(k, v)