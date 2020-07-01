import os

folder = '_posts'
origin = ''
replacement = ''

fls = os.listdir(f'./{folder}/')

for file in fls:
  print(file)

  with open (f'./{folder}/{file}', 'r') as old:
    lines = old.readlines()
    new_lines = []
    for line in lines:
      if line.find(origin) != -1:
        line = line.replace(origin, replacement)
        print(line)
      new_lines.append(line)

    with open (f'./temp/{file}', 'w') as new:
      for line in new_lines:
        new.write(line)
