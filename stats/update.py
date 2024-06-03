with open('stats/temp.txt', 'r') as file:
  tempnum = file.read().strip()
with open('stats/stats.txt', 'a') as file:
  file.write(f'\n{tempnum}')
with open('stats/temp.txt', 'w') as file:
  tempnum = file.write('0')
