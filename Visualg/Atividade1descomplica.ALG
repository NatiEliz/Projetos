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

escreval("1) Qual � o seu nome?: ")
leia(nome)
escreval("")

escreval("2) Qual � a sua idade?(xx): ")
leia(idade)
escreval("")

escreval("3) Qual � a sua altura?(x.xx): ")
leia(altura)
escreval("")

escreval("4) Qual � a cidade onde voc� mora?: ")
leia(cidade)
escreval("")
escreval("")

escreval(" -------- Dados Informados: ")
escreval("-> ", nome,";")
escreva("->", idade," anos --")
               se idade >= 18 entao
                  escreval("  Mensagem: Voc� j� � um adulto, vida o agora e sinta a felicidade dentro de voc�!!!;")
               senao
                    se idade >= 13 entao
                       escreval("  Mensagem: Voc� � um adolescente, seja voc� mesmo! Se ame!;")
                    senao
                         se idade >=5 entao
                            escreval("  Mensagem: Voc� � uma crian�a, aproveite cada minuto!!!;")
                         senao
                              se ((idade >=1) ou (i)) entao
                                 escreval("  Mensagem: Voc� � um beb�, aben�oado seja!!!;")
                              senao
                                   escreval("Erro, informe uma idade valida!!")
                         fimse
                     fimse
                  fimse
               fimse

escreval("->", altura,";")
escreval("-> ", cidade,";")

Fimalgoritmo