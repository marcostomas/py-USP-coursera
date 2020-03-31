seg = int(input("Por favor, entre com o número de segundos que deseja converter"))

dia = seg // 60 // 60 // 24
hora = seg // 60 // 60
minuto = hora * 60
segundo = minuto * 60

print(dia, "dias", hora, "horas", minuto, "minutos e", segundo, "segundos")

print(dia)
print(hora)
print(minuto)
print(segundo)