def escreva(txt):
    tam = len(txt) + 2
    print('-'*tam)
    print(f' {txt} ')
    print('-'*tam)


msg = str(input('Digite uma mensagem para virar título: '))
escreva(msg)