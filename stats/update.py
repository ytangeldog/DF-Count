with open('temp.txt', 'r') as file:
  tempnum = file.read().strip()
with open('stats.txt', 'a') as file:
  file.write(f'\n{tempnum}')
with open('temp.txt', 'w') as file:
  tempnum = file.write('0')
