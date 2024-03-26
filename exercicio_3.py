"""
#### Exercício 3 - Identificar se a variante está no gene BRCA1 - Versão 2.

Receba 3 inputs do usuário:
1) O cromossomo de uma variante. Ele virá escrito como texto e da seguinte forma "chr1", "chr2", etc.
2) A posição dessa variante. Será um número inteiro.
3) O genoma de referência dessa variante. Considere só 2 opções possíveis, "hg19" e "hg38".

Responda:
"Sim" se ela estiver no BRCA1.
"Não" se ela não estiver.

Considere que a variante está no gene BRCA1 se estiver no cromossomo 17 (chr17), e:
1) Se a posição estiver no intevalo de 41196312 a 41277500, caso o genoma de referência seja o "hg19".
2) Se a posição estiver no intevalo de 43044295 a 43125483, caso o genoma de referência seja o "hg38".

Obs: Tirei a Location daqui: https://grch37.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000012048;r=17:41196312-41277500

Exemplos:

----------------------------------

Digite o cromossomo: chr17
Digite a posição: 41196313
Digite o genoma de referência: hg38

Resposta:
Não


----------------------------------

Digite o cromossomo: chr17
Digite a posição: 41196313
Digite o genoma de referência: hg19

Resposta:
Sim

----------------------------------

Digite o cromossomo: chr17
Digite a posição: 43044299
Digite o genoma de referência: hg38

Resposta:
Sim

----------------------------------

Digite o cromossomo: chr2
Digite a posição: 43044299
Digite o genoma de referência: hg38

Resposta:
Não

"""

# Resolução

cromossomo = input("Digite o cromossomo: ")
print(cromossomo)
posição = int(input("Digite a posição: "))
print(posição)
referência = input("Digite o genoma de referência: ")
print(referência)
BRCA1 = cromossomo == ('chr17') and 41196312 <= posição <= 41277500 and referência == 'hg19'
print(BRCA1) 
BRCA2 = cromossomo == ('chr17') and 43044295 <= posição <= 43125483 and referência == 'hg38' 


if BRCA1 :
    print('Sim')
elif BRCA2 :
    print('Sim')
else:
    print('Não')
