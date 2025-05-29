def voto(ano):
   idade = 2025 - ano
   resultados = ['Não vota', 'Voto opcional', 'Voto obrigatório']
   if idade < 16 :
      return resultados[0]
   elif 19 > idade >= 16 or idade > 45:
       return resultados[1]
   else:
       return resultados[2]

print(voto())
