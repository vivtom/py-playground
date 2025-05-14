dict1 = {'mai':'me','tu':'you','mera': 'mine'}
word = input('which word u wanna lookup?')
if word in dict1:
    print(f'the meaning of {word} is {dict1[word]} in english')
else:
    print('there is no such word')