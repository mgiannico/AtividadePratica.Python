#   ATIVIDADE PRÁTICA DE LÓGICA DE PROGRAMAÇÃO E ALGORITMOS - FACULDADE
#   LINGUAGEM PYTHON


# -------------------------------  EXERCÍCIO 1 --------------------------------------------------
print('Olá, bem-vindo (a) à loja da Mariana Galvão Giannico')

#Valor de cada produto
valorUnitario = float(input('Insira o valor do produto: R$ '))
#Quantidade de produtos desejada
quantidade = int(input('Insira a quantidade de produtos que deseja: '))
#Valor inicial da embalagem para frete
valorEmbalagem = 0

#Para quantidade de produtos maior ou igual a 0 e menor que 11
if (0 <= quantidade < 11):
    valorEmbalagem = 30
#Para quantidade de produtos maior ou igual a 11 e menor que 101
elif (11 <= quantidade < 101):
    valorEmbalagem = 60
#Para quantidade de produtos maior ou igual a 101 e menor que 1001
elif (101 <= quantidade < 1001):
    valorEmbalagem = 120
#Para quantidade de produtos maior ou igual a 1001
else:
    valorEmbalagem = 240

#O valor sem o custo da embalagem para frete
semCustoEmbalagem = valorUnitario * quantidade
#O valor com o custo da embalagem para o frete
comCustoEmbalagem = semCustoEmbalagem + valorEmbalagem
print('O valor sem a embalagem para o frete foi R${:.2f} ' .format(semCustoEmbalagem))
print('O valor com a embalagem para o frete foi R${:.2f} (O valor das embalagens para o frete foi de: R${:.0f})' .format(comCustoEmbalagem,valorEmbalagem))
print('Obrigada pela preferência, volte sempre! <3')





# -------------------------------  EXERCÍCIO 2 --------------------------------------------------
# Tabela de serviços oferecidos
print('********* Seja bem-vindo (a) à Sorveteria  da Mariana Galvão Giannico *********')
print('**************************** SERVIÇOS OFERECIDOS ******************************')
print('|_____________________________________________________________________________|')
print('|  CODIGO  |      DESCRIÇÃO       |    TAMANHO P  |  TAMANHO M |  TAMANHO G   |')
print('|          |                      |     500 ML    |   1000 ML  |   2000 ML    |')
print('|   "TR"   |   SABOR TRADICIONAIS |   R$   6,00   |  R$  10,00 |  R$  18,00   |')
print('|   "ES"   |   SABORES ESPECIAIS  |   R$   7,00   |  R$  12,00 |  R$  21,00   |')
print('|   "PR"   |   SABORES ESPECIAIS  |   R$   8,00   |  R$  14,00 |  R$  24,00   |')
print('|_____________________________________________________________________________|')

# Inserindo os valores
tamanho = ["P", "M", "G"]
codigos = {"TR": [6.00, 10.00, 18.00],
           "ES": [7.00, 12.00, 21.00],
           "PR": [8.00, 14.00, 24.00]}
compra = []

# Pedindo os dados
while True:
    qual_tamanho = input("Qual o tamanho do sorvete desejado (P/M/G)? ")
    qual_sabor = input("Qual o código do sorvete desejado(TR/ES/PR)? ")
    if qual_tamanho in tamanho and qual_sabor in codigos:
        pedido = codigos[qual_sabor][tamanho.index(qual_tamanho)]
        print('Você escolheu o Tamanho {} e o sabor {}. Com valor de: {}'.format(qual_tamanho, qual_sabor, pedido))
        compra.append(pedido)
        # Se o cliente quiser pedir mais alguma coisa ou não
        algo_mais = input("Deseja pedir algo mais?"
                          "\nDigite S para sim ou N para não. ")
        if algo_mais == "S":
            continue
        elif algo_mais == "N":
            break
    else:
        # Caso o tamanho e o código sejam inseridos errados
        print("TAMANHO ou CÓDIGO INVÁLIDO(S)!!!!!")
        continue

# Valor total da compra
print("Valor total da compra:", "R$", sum(compra))





# -------------------------------  EXERCÍCIO 3 --------------------------------------------------
#Inicio
def metragem_limpeza():
   print('-'*20, 'MENU 1 de 3 - Metragem da Limpeza', '-'*20)
   while True:
       try:
           metragemL = int(input('Insira a metragem da casa (m²): '))
           if (metragemL >= 30) and (metragemL <= 300):
               print('É necessário contratar 1 pessoa para a limpeza')
               print('O valor da metragem é:')
               return 60 + 0.3 * metragemL
           elif (metragemL >= 300) and (metragemL <= 700):
                print('É necessário contratar 2 pessoas')
                print('O valor da metragem é:')
                return 120 + 0.5 * metragemL
           else:
               print('Não aceitamos casas com metragem menor que 30m² ou maior que 700m²!!!')
               #Retorna para o inicio da pergunta
               continue

#Caso o usuario digite letras ou valores quebrados em vez de valores inteiros
       except ValueError:
           print('!'*20, 'Valores não inteiros não são aceitos','!'*20)
#Fim da função metragem_limpeza()


#Inicio da função tipo_limpeza()
def tipo_limpeza():
   print('-'*20, 'MENU 2 de 3 - Tipo de Limpeza', '-'*20)
   while True:
       tipoL = input('Escolha qual o tipo de limpeza: \n'+
                     'B – Básica - Indicada para sujeiras semanais ou quinzenais \n' +
                     'C – Completa - Indicada para sujeiras antigas e/ou não rotineiras \n' +
                     'Insira a opção desejada: ')
       tipoL = tipoL.lower()
       tipoL = tipoL.strip()
       if tipoL == 'b':
           print('Você selecionou a opção de Limpeza Básica')
           print('Com multiplicador de: ')
           return 1.00
       elif tipoL == 'c':
           print('Você selecionou a opção de Limpeza Completa')
           print('Com multiplicador de: ')
           return 1.30
       else:
           print('!'*30 , 'Opção inválida', '!'*30)
           #Voltar para o inicio da pergunta
           continue

#Fim da função tipo_limpeza()


#Inicio da função adicional_limpeza()
def adicional_limpeza():
   print('-'*20, 'MENU 3 de 3 - Adicional de Limpeza', '-'*20)
   acumulador = 0
   while True:
       adicionalL = input('Deseja mais algum adicional? \n' +
                         '0 - Não desejo mais nada (Encerrar) \n' +
                         '1 - Passar 10 peças de roupa - R$ 10.00 \n' +
                         '2 - Limpeza de um forno/micro-ondas - R$ 12.00 \n' +
                         '3 - Limpeza de uma geladeira/freezer - R$ 20.00 \n' +
                         'Insira a opção desejada: ')
       if adicionalL == '0':
           return acumulador
       elif adicionalL == '1':
           acumulador = acumulador + 10
          #Volta para o inicio do laço de repetição
           continue
       elif adicionalL == '2':
           acumulador = acumulador + 12
           #Volta para o inicio do laço de repetição
           continue
       elif adicionalL == '3':
           acumulador = acumulador + 20
           #Volta para o inicio do laço de repetição
           continue
       else:
           print('!'*30,'Opção inválida', '!'*30)

#Fim da função adicional_limpeza()


#Inicio do Main
def borda(s1):
   tam = len(s1)
   if tam:
       print('+','-' * tam, '+')
       print('|', s1, '|')
       print('+','-' * tam, '+')

borda('          Bem-vindo ao Serviços de Limpezas da Mariana Galvão Giannico         ')
print('*'*100)
metragem = metragem_limpeza()
print(metragem)
tipo = tipo_limpeza()
print(tipo)
adicional = adicional_limpeza()
print(adicional)
total = (metragem * tipo) + adicional
print('Valor total ficou: R$ {:.2f} (Metragem: R$ {:.2f} + Tipo de Limpeza R$ {:.2f} + Adicional R$ {:.2f})' .format(total, metragem, tipo, adicional))

borda('Obrigado pela preferência!')



# -------------------------------  EXERCÍCIO 4 --------------------------------------------------
#Boas-vindas ao usuário
print('-'*20, 'Bem-vindo ao Controle de Funcionários da Mariana Galvão Giannico', '-'*20)

#Início
listafuncionarios = []

#Cadastro de funcionarios
def cadastrarfuncionario(codigo):
 print('-'*20, 'Você selecionou a opção de Cadastrar funcionario', '-'*20)
 print('O código do funcionario é: {:0>3}'.format(codigo))

 nome = input('Entre com o nome do funcionario:')
 setor = input('Entre com o setor do funcionario:')
 salario = float(input('Entre com o salário R$ do funcionario:'))
 dicionariofuncionarios = {'codigo'   : codigo,
                        'nome' : nome,
                        'setor': setor,
                        'salario': salario}
 listafuncionarios.append(dicionariofuncionarios.copy())

#Consulta de funcionarios
def consultarfuncionario():
 while True:
   try:
     print('-'*20, 'Você Selecionou a Opção de Consultar funcionarios', '-'*20)
     opConsultar = int(input('Entre com a opção desejada\n1- Consultar todos os funcionarios\n2- Consultar funcionarios por Código\n3- Consultar funcionarios por setor\n4- Retornar\n-->'))
     if opConsultar == 1:
         #Consultar todos os funcionários
       print('-' * 20)
       for funcionarios in listafuncionarios:
           for key, value in funcionarios.items():
             print('{} : {}'.format(key,value))
             print('-' * 20)

     elif opConsultar == 2:
         #Consultar funcionarios por meio do código
       print('Você Selecionou a Opção funcionarios por Código')
       entrada = int(input('Digite o Código: '))
       print('-' * 20)
       for funcionarios in listafuncionarios:
         if(funcionarios['codigo'] == entrada):
           for key, value in funcionarios.items():
             print('{} : {}'.format(key,value))
             print('-' * 20)
     elif opConsultar == 3:
         #Consultar funcionarios por meio do setor
       print('Você Selecionou a Opção funcionarios por setor')
       entrada = input('Digite o setor: ')
       print('-' * 20)
       for funcionarios in listafuncionarios:
         if(funcionarios['setor'] == entrada):
           for key, value in funcionarios.items():
             print('{} : {}'.format(key,value))
             print('-' * 20)
     elif opConsultar == 4:
       break
     else:
       print('Opção inválida!!!')
       continue
#Caso o usuário insira um valor inválido
   except ValueError:
     print('Digite uma opção válida!!')
     continue

#Para remover um funcionario
def removerfuncionario():
   print('Você Selecionou o Remover funcionario')
   entrada = int(input('Digite o Código do funcionario que irá remover: '))
   for funcionarios in listafuncionarios:
     if(funcionarios['codigo'] == entrada):
       listafuncionarios.remove(funcionarios)
   else:
     print('Você removeu o código.')
     print('Bem-vindo ao Controle de Funcionários da Mariana Galvão Giannico')

registrofuncionarios = 0
while True:
   try:
     print('-'*49,'MENU PRINCIPAL', '-'*49)
     opcao = int(input('Digite a opção desejada:\n1- Cadastrar funcionarios\n2- Consultar funcionarios\n3- Remover funcionarios\n4- Sair\n-->'))
     if opcao == 1:
       registrofuncionarios = registrofuncionarios + 1
       cadastrarfuncionario(registrofuncionarios)
     elif opcao == 2:
       consultarfuncionario()
     elif opcao == 3:
       removerfuncionario()
     elif opcao == 4:
       print('Programa finalizado')
       break
     else:
       print('Digite somente uma das opções do MENU')
       continue

   except ValueError:
       print('Insira valores válidos!!!')
