Algoritmo "ProcedimentosParametros"
// Descrição   : Multiplicação como uso de Procedimento (Parâmetro)
// Autor(a)    : Natália Eliz de Sousa Chagas
// Data atual  : 08/05/2024
PROCEDIMENTO atividade_pratica(a,b: inteiro)
VAR
   aux: inteiro
INICIO
   aux <- a * b
   resp <- aux
FIMPROCEDIMENTO
Var
   resp, c, d: inteiro
Inicio
   escreval("---------- Atividade Procedimentos com Parametros ----------")
   escreval("----------------------- Descomplica ------------------------")
   escreval("------------------------------------------------------------")
   escreval("")

   escreva("Digite um número inteiro: ")
   leia(c)

   escreva("Digite outro número inteiro: ")
   leia(d)

   atividade_pratica(c,d)

   escreval("")
   escreval("A multiplicação de", c, " e", d, " é:", resp)
   escreval("")
Fimalgoritmo