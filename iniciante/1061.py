dia_inicial_str = input()
dia_inicial = [int(x) for x in dia_inicial_str.split() if x.isdigit()]

hora_inicial_str = input()
hora_inicial = [int(x) for x in hora_inicial_str.split() if x.isdigit()]

dia_final_str = input()
dia_final = [int(x) for x in dia_final_str.split() if x.isdigit()]

hora_final_str = input()
hora_final = [int(x) for x in hora_final_str.split() if x.isdigit()]

hh_i, mm_i, ss_i = hora_inicial
hh_f, mm_f, ss_f = hora_final

inicio_segundos = hh_i*3600 + mm_i*60 + ss_i
fim_segundos = (dia_final[0] - dia_inicial[0])*86400 + hh_f*3600 + mm_f*60 + ss_f

if fim_segundos > inicio_segundos:
    duracao = fim_segundos - inicio_segundos
elif fim_segundos < inicio_segundos:
    duracao = (fim_segundos + 24*3600) - inicio_segundos
elif fim_segundos == inicio_segundos:
    duracao = 24*3600

dias = duracao // 86400
resto = duracao % 86400
horas = resto // 3600
resto = resto % 3600
minutos = resto // 60
resto = resto % 60
segundos = resto


print(f"{dias} dia(s)\n" +
      f"{horas} hora(s)\n" +
      f"{minutos} minuto(s)\n" +
      f"{segundos} segundo(s)")
