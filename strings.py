strings = ['This', 'list', 'is', 'now', 'all', 'together']
sentence = ''

for i in range(5):
    sentence += strings[i] + ' '
sentence += strings[-1]

print(sentence)
print(' '.join(strings))

