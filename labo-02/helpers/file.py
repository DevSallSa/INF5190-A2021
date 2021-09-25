def write_file():
    file = open("log.txt", "w")
    file.write("Im writing this in log.txt")
    file.close()

def read_file():
    try:
        file = open("input")
        lines = file.readlines()
        for index, line in enumerate(lines):
            print(f"Ligne #{index}, contenu: {line}")
    except:
        print("The file 'input' doesn't exists")


# Utilisation
write_file()
read_file()
