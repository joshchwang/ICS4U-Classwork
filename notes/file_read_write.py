with open("some_file.txt", "w") as f:
    contents = f.write("woop")

print(contents)

with open("some_file.txt", "r") as f:
    contents = f.read()

print(contents)
