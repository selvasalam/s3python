with open('source.txt', 'r') as source_file:
    content = source_file.read()

with open('desti.txt', 'w') as dest_file:
    dest_file.write(content)

print("Contents copied from source.txt to desti.txt")
