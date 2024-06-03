with open('dfconnected/stats/temp.txt', 'r') as file:
  tempnum = file.read().strip()
with open('dfconnected/stats/stats.txt', 'a') as file:
  file.write(f'{tempnum}\n')
with open('dfconnected/stats/temp.txt', 'w') as file:
  tempnum = file.write('0')
