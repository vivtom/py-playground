# Write a program that reads a file called data.txt, counts how many words are in it, and prints the total word count.

with open ('data.txt', 'r') as file:
    content = file.read()
    words = content.split()
    count = len(words)
print(count)