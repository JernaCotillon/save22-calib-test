first_names = ['Shan', 'Dao Ming', 'Hua Ze', 'Xi', 'Mei']
last_names = ['Cai', 'Si', 'Lei', 'Men', 'Zuo']

names = [('{} {}'.format(fName,last_names[lName]))  for lName, fName in enumerate(first_names)]
print (names)