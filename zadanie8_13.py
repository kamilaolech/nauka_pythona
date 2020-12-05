atomy = [{'nazwa': 'wodor', 'grupa': 1, 'okres': 1},
 {'nazwa': 'hel', 'grupa': 2, 'okres': 1}]

for i in atomy:
    print(i['nazwa'] + ' - grupa: ' + str(i['grupa']) + ' okres: ' + str(i['okres']))

suma_walencyjnych=0
for i in atomy:
    suma_walencyjnych+=i['grupa']
  
print('Suma elektronow walencyjnych: ' + str(suma_walencyjnych))
  
 
