import os

def genereer_bestandslijst(map_naam):
    if not os.path.isdir(map_naam):
        print(f"De map '{map_naam}' bestaat niet.")
        return

    bestanden = os.listdir(map_naam)
    met_naam = [bestand for bestand in bestanden if os.path.isfile(os.path.join(map_naam, bestand))]

    uitvoer_pad = os.path.join(map_naam, f"{map_naam}_bestand.txt")
    with open(uitvoer_pad, "w") as f:
        for bestand in met_naam:
            f.write(f"{bestand}\n")

    print(f"Bestandsnamen zijn opgeslagen in: {uitvoer_pad}")

if __name__ == "__main__":
    map_naam = input("Voer de naam van de map met afbeeldingen in: ")
    genereer_bestandslijst(map_naam)