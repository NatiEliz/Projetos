Algoritmo "Atividade1_descomplica"
Var
nome, cidade: caractere;
idade: inteiro;
altura: real;

Inicio
escreval("-------------------- Primeira Atividade --------------------")
escreval("----------------------- Descomplica ------------------------")
escreval("------------------------------------------------------------")
escreval("")

escreval("1) Qual é o seu nome?: ")
leia(nome)
escreval("")

escreval("2) Qual é a sua idade?(xx): ")
leia(idade)
escreval("")

escreval("3) Qual é a sua altura?(x.xx): ")
leia(altura)
escreval("")

escreval("4) Qual é a cidade onde você mora?: ")
leia(cidade)
escreval("")
escreval("")

escreval(" -------- Dados Informados: ")
escreval("-> ", nome,";")
escreva("->", idade," anos --")
               se idade >= 18 entao
                  escreval("  Mensagem: Você já é um adulto, vida o agora e sinta a felicidade dentro de você!!!;")
               senao
                    se idade >= 13 entao
                       escreval("  Mensagem: Você é um adolescente, seja você mesmo! Se ame!;")
                    senao
                         se idade >=5 entao
                            escreval("  Mensagem: Você é uma criança, aproveite cada minuto!!!;")
                         senao
                              se ((idade >=1) ou (i)) entao
                                 escreval("  Mensagem: Você é um bebê, abençoado seja!!!;")
                              senao
                                   escreval("Erro, informe uma idade valida!!")
                         fimse
                     fimse
                  fimse
               fimse

escreval("->", altura,";")
escreval("-> ", cidade,";")

Fimalgoritmo