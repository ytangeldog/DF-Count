with open('stats/temp.txt', 'r') as file:
  tempnum = file.read().strip()
with open('stats/stats.txt', 'a') as file:
  file.write(f'{tempnum}\n')
with open('stats/temp.txt', 'w') as file:
  tempnum = file.write('0')
