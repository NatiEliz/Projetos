Algoritmo "ProcedimentosParametros"
// Descri��o   : Multiplica��o como uso de Procedimento (Par�metro)
// Autor(a)    : Nat�lia Eliz de Sousa Chagas
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

   escreva("Digite um n�mero inteiro: ")
   leia(c)

   escreva("Digite outro n�mero inteiro: ")
   leia(d)

   atividade_pratica(c,d)

   escreval("")
   escreval("A multiplica��o de", c, " e", d, " �:", resp)
   escreval("")
Fimalgoritmo