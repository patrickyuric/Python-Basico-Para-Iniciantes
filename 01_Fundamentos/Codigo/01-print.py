#Função print()
#Vs Code comando (Crtl + Shift + ') abre o terminal

#Código e saída esperada

# 1 - print()
print("Olá, mundo!") # Olá, mundo!

print('Este também é outro texto!') # Este também é outro texto!

# 2 - print() com variáveis
nome = "Patrick" # variável string
idade = 30       # variável int

print(nome) # Patrick
print(idade) # 30

# 3 - Combinar texto com variáveis
# É preciso converter númeroas para string(texto) utilizando a função srt()
# Perceba a necessidade de espaços
print("Olá, meu nome é " + nome + " e tenho " + str(idade) + " anos.")

# 4 - Usando vírgulas
# Não precisa converter para string
print("Olá, meu nome é", nome, "e tenho", idade,"anos.")

# 5 - Usando método f-string (Formatação literal de sting) - A partir da versão 3.6 do Python
print(f"Olá, meu nome é {nome} e tenho {idade} anos.") 

# 6 - Usando método .format()
print("Olá, meu nome é {} e tenho {} anos.".format(nome, idade))

# 7 - Separador e finalizador
# Sem separador
print("Item 1", "Item 2", "Item 3")  # Item 1 Item 2 Item 3

# Com separador '-'
print("Item 1", "Item 2", "Item 3", sep="-") # Item 1-Item 2-Item 3

## Sem finalizador
print("Item 1", "Item 2", "Item 3", sep="-") 
print("Fim da linha.") 

# Item 1-Item 2-Item 3
# Fim da linha.

## Com finalizador
print("Item 1", "Item 2", "Item 3", sep="-", end=". ") 
print("Fim da linha.") 

# Item 1-Item 2-Item 3. Fim da linha.

# Obs: O Finalizador padrão é o comando de pular linha (\n) o finalizador end="." diz que quando
# terminar a impressão em vez de pular linha será colocado um ponto final logo após o texto
# e não pulará linha a não ser que coloque novamente o comando como no exemplo abaixo

print("Item 1", "Item 2", "Item 3", sep="-", end=". \n") 
print("Fim da linha.") 

# tem 1-Item 2-Item 3.
# Fim da linha.

# Comando finalizador com símbolos 
print("Linha 01", end=" -\n")
print("Linha 02")

# 8 - Quebra de linha dentro do texto (\n)
print("Linha 01 \nLinha 02 \nLinha 03")

# 9 - Tabulação com separador \t
print("Item 1", "Item 2", "Item 3", sep="\t")

#Item 1	Item 2	Item 3

# Criar tabelas visuais sem bibliotecas externas
print("Nome\tIdade\tProfissão")
print("Kelly\t30\tBiomédica")
print("Vicente\t22\tCientista de Dados")
print("Patrick\t35\tProfessor")

# Nome	Idade	Profissão
# Kelly	30	Biomédica
# Vicente	22	Cientista de Dados
# Patrick	35	Professor