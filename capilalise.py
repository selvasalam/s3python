
with open('i.txt', 'r') as infile:
    content = infile.read()
capitalized_content = content.title()

with open('o.txt', 'w') as outfile:
    outfile.write(capitalized_content)

print("Capitalized text saved to o.txt")
