import os


#print(os.getcwd())

os.chdir("/Users/valentin/Documents/VHS Kurse/Automatisierung mit Python/Demo Ordner")

#print(os.getcwd())

print(os.listdir())

for file in os.listdir():
    if file.startswith("."):
        continue
    print(file)

    #if file.endswith(".dmg"):
        # Hier wird eine Datei gelöscht
        #print("Datei " + file + " wird gelöscht!")
        #os.remove(file)

    if ".pdf" in file:
        filename, file_type = os.path.splitext(file)

        thema, kapitel = filename.split("-")

        print("Thema: " + thema + " Kapitel: " + kapitel)

        new_file = kapitel + " - " + thema + file_type

        os.renames(file, new_file)




