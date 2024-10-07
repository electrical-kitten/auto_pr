from pathlib import Path

# print(str(Path('spam', 'bacon', 'eggs')))

# my_files = ['accounts.txt', 'details.csv', 'invite.docx']
# for filename in my_files:
#     print(Path(r'C:/Users/Al', filename))

print(Path('spam') / 'bacon' / 'eggs')
print(Path('spam') / Path('bacon/eggs'))
print(Path('spam') / Path('bacon', 'eggs'))
