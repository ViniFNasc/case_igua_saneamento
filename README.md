# case_igua_saneamento
Este diretório destina-se ao processo seletivo de analista de dado pleno da Igua Saneamento.

Todos os processos de tratamento, análise de dados e classificação estão no arquivo solution.ipynb


Respostas

1. O que faz alguém ter um score maior ou menor?
O score é influenciado pelas variáveis a seguir:

- Proporcional: Idade do cliente, idade do histórico do cartão e comportamento de pagamento 
- Inversamente Proporcional: quantidade de contas bancárias, quantidade de cartões de crédito, quantidade de empréstimo, quantidade de dias de atraso para o pagamento, variação percentual do limite do cartão, quantidade de consultas no cartão, dívida restante a ser paga e o pagamento mínimo da parcela.

2. A quantidade de empréstimos é relevante?
Não, está entre os cinco mais irrelevantes.

3. O saldo mensal é relevante?
Não, pelo contrário, é o que menos influencia o Target.

4. Que tipos de clientes são mais propensos a ficarem inadimplentes?
Os clientes mais propensos a ficarem inadimplentes são os que possuem maiores dívidas a serem pagas (Outstanding_Debt) e as variáveis que influenciam positivamente essa variável são:

- Quantidade de contas bancárias
- Quantidade de cartões de créditos
- Quantidade de empréstimos
- Quantidade de dias de atraso do pagamento do empréstimo
- Variação percentual no limite do cartão de crédito
- Quantidade de consultas de cartão de crédito

Portanto, as pessoas prováveis de ficarem inadimplentes são aquelas que possuem maiores quantidade de contas bancárias, cartões de créditos, empréstimos, dias de atraso do pagamento, variação do limite do cartão e consultas de cartão.

5. Qual informação mais influência no score?
A Coluna Outstanding_Debt (dívida restante a ser paga) é o que mais influencia o Score



by: Vinícius Francisco do Nascimento.