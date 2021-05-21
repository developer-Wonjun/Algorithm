words = input()
cro_word_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for cro in cro_word_list:
    words = words.replace(cro, '.')

print(words)
print(len(words))