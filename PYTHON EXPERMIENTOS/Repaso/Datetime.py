from datetime import *

#date(año, mes, dia)

#time(hora, minutos, segundos, microsegundos)

#datetime(año, mes, dia, hora, minutos, segundos, microsegundos)

d = date.today()
t = datetime.now()
print(d)
print(t)
print(d.year)
print(d.month)
print(d.day)
print(t.hour)
print(t.second)
print(t.weekday(), '\n')

print(t.strftime('%d-%m-%Y'))
print(t.strftime('%A, %d %B, %y'))
print(t.strftime('%H:%M:%S'))
print(t.strftime('%H horas, %M minutos y %S segundos'))