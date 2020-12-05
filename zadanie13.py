atomy = {'nazwa': 'wodor',
          'grupa': '1',
          'okres': '1'}

print(atomy['nazwa'])
print(atomy['grupa'])

# co wypiszemy na ekran
#print(atomy['nieznany_klucz'])

# a co kiedy
#print(atomy.get['nieznany_klucz'])

for key in atomy:
    print("{0}:{1}".format(key, atomy[key]))
