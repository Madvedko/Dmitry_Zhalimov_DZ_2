positions = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
names = [p.split(' ')[-1].capitalize() for p in positions]
text = ', '.join(names)
print(f'Привет, {text}!')

