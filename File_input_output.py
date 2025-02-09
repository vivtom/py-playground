'''Create a new file "practice.txt" using python. Add the following data in it:
Hi everyone
we are learning File 1/0
using Java.
I like programming in Java.'''


with open('practice.txt', 'w') as f:
    f.write('Hi everyone\nwe are learning File 1/0 ')
    f.write('using Java.\nI like programming in Java')

'''WAF that replace all occurrences of "java" with "python" in above file.'''

with open('practice.txt', 'r') as f:
    just_read = f.read()
    actual = just_read.replace('Java', 'python')
with open('practice.txt', 'w') as f:
    f.write(actual)


'''Search if the word "learning" exists in the file or not.'''

word = "learning"
with open ("practice.txt", "r") as f:
    data = f.read( )
if(data.find(word) != -1):
    print ("Found")
else:
    print("not found")
