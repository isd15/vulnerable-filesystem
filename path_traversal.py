filename = input("Enter file name: ")
with open(f"/etc/{filename}", "r") as file:  # Reads system files
    print(file.read())
