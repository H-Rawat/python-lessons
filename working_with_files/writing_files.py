# text = 'Yoooo!!\nThis is some text\nHave a good one.'
# text = 'This text has been overwritten'
text = 'Have a nice day, sir'

# with open('text.txt', 'w') as file:
#     file.write(text)

with open('text.txt', 'a') as file:
    file.write(text)
