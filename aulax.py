def mostra_menssagem():
    print("Bem vindo ao def do Python.")
if __name__ == '__main__':
    print('Mensagem antes da chamada da função.')
    mostra_menssagem()
    print('Mensagem depois da chamada da função.')
def mostra_menssagem_2(msg):
    print(msg)
if __name__ == '__main__':
    mostra_menssagem_2('Menssagem passada para a função.')
    var = input('Digite uma menssagem: ')
    mostra_menssagem_2(var)
--

def mostra_menssagem():
    print("Bem vindo ao def do Python.")
def mostra_menssagem_2(msg):
    print(msg)

if __name__ == '__main__':
    print('Mensagem antes da chamada da função.')
    mostra_menssagem()
    print('Mensagem depois da chamada da função.')
    mostra_menssagem_2('Menssagem passada para a função.')
    var = input('Digite uma menssagem: ')
    mostra_menssagem_2(var)
--
def valor(v_valor):
    print('Parâmetro recebido:', v_valor)
if __name__ == '__main__':
    valor(5)
    valor2 = 23.8
    valor(valor2)
    valor3 = -4
    valor(valor3)
--

def valor(v_valor):
    print('Parâmetro recebido:', v_valor)
if __name__ == '__main__':
    valor(5)
    valor(23.8)
    valor(-55)
--

def valor(v_valor):
    print('Parâmetro recebido:', v_valor)
if __name__ == '__main__':
    valor(5)
    valor_float = 23.8
    valor(valor_float)
    valor_negativo = int(input('Digite um valor negativo: '))
--

def mostra_menssagem():
    print('Bem vindo ao def do Python.')
def mostra_menssagem_2(msg):
    print(msg)
def mostra_dois_valores(valor1, valor2):
    print('Valor1:', valor1)
    print('Valor2:', valor2)
if __name__ == '__main__':
    print('Mensagem antes da chamada da função.')
    mostra_menssagem()
    print('Mensagem depois da chamada da função.')
    mostra_menssagem_2('Menssagem passada para a função.')
    mostra_dois_valores(5, 10)
--

def valor(v_valor):
    print('Parâmetro recebido:', v_valor)
if __name__ == '__main__':
    v_valor = int(input('Digite um valor negativo: '))
--

def retorna_soma(v1, v2): # A função recebe 2 parâmetros
    soma = v1 + v2        # A variável soma recebe o cálculo
    return soma           # Retorna o valor calculado

def retorna_soma2(v3, v4):
    soma2 = v3 + v4
    return soma2
# Fim da função

if __name__ == '__main__':
    valor1 = int(input('Digite o primeiro valor: '))
    valor2 = int(input('Digite o segundo valor: '))
    v_retorno = retorna_soma(valor1, valor2) # Chama a função
    print('soma =', v_retorno)

    valor3 = float(input('Digite o terceiro valor: '))
    valor4 = float(input('Digite o quarto valor: '))
    v_retorno2 = retorna_soma2(valor3, valor4) # Chama a função
    print('soma =', v_retorno2)
