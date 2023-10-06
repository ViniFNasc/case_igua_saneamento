import streamlit as st
import seaborn as sns
import numpy as np
import pandas as pd
from collections import Counter
import requests
from plotly import figure_factory as ff, express as xp, graph_objects as go

#Funções
def bar(df, label, values, title):
    fig = xp.bar(data_frame=df, x=f"{label}", y=f"{values}", title=f"{title}")
    st.plotly_chart(figure_or_data=fig, theme="streamlit", use_container_width=True)

def pie(df, label, title):

    fig = xp.pie(data_frame=df, title=f"{title}", names=f"{label}")

    fig.update_traces(textposition="inside")
    fig.update_layout(uniformtext_minsize=10, uniformtext_mode="hide")

    st.plotly_chart(figure_or_data=fig, theme="streamlit", use_container_width=True)

def indicator(label, title):
    fig = go.Figure()
    fig = fig.add_trace(go.Indicator(value=label, title=f"{title}"))
    st.plotly_chart(figure_or_data=fig, theme="streamlit", use_container_width=True)

def table(df, columns_table=None):
    if columns_table is not None:
        df = df[columns_table]

    fig = ff.create_table(df, height_constant=15)
    st.plotly_chart(figure_or_data=fig, theme="streamlit")

def line(df, label, values, title):
    fig = xp.line(data_frame=df, x=f"{label}", y=f"{values}", title=f"{title}")
    st.plotly_chart(figure_or_data=fig, theme="streamlit", use_container_width=True)

def boxplot(df, values, title):
    fig = xp.box(df, y=values, title=title)
    st.plotly_chart(figure_or_data=fig, theme="streamlit", use_container_width=True)

def histogram(df, values, title):
    fig = xp.histogram(df, x=values, title=title)
    st.plotly_chart(figure_or_data=fig, theme="streamlit", use_container_width=True)


#Storyingtelling
# Título do aplicativo
st.title("Análise de score de crédito")

st.write('Eu, analista de dados em uma empresa financeira global, fui encarregado de analisar uma base de dados que a empresa coletou ao longo dos anos relacionado a crédito.')

st.write('Meu superior imediato pediu para que eu construa um sistema inteligente, a fim de segregar as pessoas em faixas de pontuação de crédito para reduzir os esforços manuais do time da Administração.')

st.write('Como um funcionário ligado, resolvi realizar uma inspeção e análise exploratória dos dados. Veremos o que os usuários nos reservou!')


st.subheader('Data Inspection and Previous Exploratory Data Analysis')

st.write('A base de dados recebida é relativamente grande, possuindo 100000 linhas e 28 colunas, sem dados duplicados. Além disso, nem todas as colunas estão preenchidas como no gráfico a seguir')


info_initial = pd.read_csv(fr'streamlit_view\bases_to_view\info_initial.csv')
info_initial['Qtd. Nulos'] = 100000 - info_initial['Non-Null_Count']

bar(df=info_initial,label='Column',values='Qtd. Nulos',title= 'Distribuição de valores nulos')

st.write('Podemos ver a quantidade de valores nulos, sendo liderados pelo Monthly_Inhand_Salary.')

st.write("""Além disso, o tipo de dados estaavam trocados em algumas colunas (estão como string mas deveriam ser numéricos), são elas: Age, Annual_Income, Monthly_Inhand_Salary, Num_Credit_Card, Interest_Rate, Num_of_Loan, Delay_from_due_date, Num_of_Delayed_Payment, Changed_Credit_Limit, Num_Credit_Inquiries, Outstanding_Debt, Credit_Utilization_Ratio, Total_EMI_per_month, Amount_invested_monthly e Monthly_Balance.""")

st.write("""Essas colunas foram previamentes tratadas para a realização da análise exploratória.""")

df_pre_trat = pd.read_csv(fr'streamlit_view\bases_to_view\df_pre_trat.csv')

st.write("""
         
         
         """)


columns = ['Age','Annual_Income','Monthly_Inhand_Salary','Num_Bank_Accounts','Num_Credit_Card','Credit_History_Age','Interest_Rate','Num_of_Loan','Delay_from_due_date',
            'Num_of_Delayed_Payment','Changed_Credit_Limit','Num_Credit_Inquiries','Outstanding_Debt','Credit_Utilization_Ratio','Total_EMI_per_month',
            'Amount_invested_monthly','Monthly_Balance']

for col in columns:
    histogram(df=df_pre_trat,values=f'{col}',title=f'Disribuição de {col}')
    boxplot(df=df_pre_trat,values=f'{col}',title=f'Boxplot de {col}')

    if col == 'Age':
        st.write("""Age possui muitas pessoas com idade que não fazem sentido (negativo e maior que 100 anos.)""")
    
    if col == 'Num_Bank_Accounts' or col == 'Num_Credit_Card':
        st.write(f'{col} possui valores que não fazem sentido para uma pessoa, ultrapassando mais de 1000.')


st.write("""Todas as colunas numéricas possuem outliers, porém algumas colunas fazem sentido ser mante-los, visto que está ligado com a diferença financeira das pessoas. A quantidade de pessoas com poder aquisitivo baixo é maior das que possuem poder aquisitivo alto, portanto quando se falar de crédito é possível que hajam discrepâncias""")

st.write("""Já quanto às variáveis categóricas temos: """)

columns_categ = ['Occupation','Credit_Mix','Payment_of_Min_Amount','Payment_Behaviour','Credit_Score']

for col in columns_categ:
    histogram(df=df_pre_trat,values=f'{col}',title=f'Disribuição de {col}')
    
    if col == 'Occupation':
        st.write("""Podemos observar o dado '______', possivelmente pessoas sem ocupação""")
    
    if col == 'Credit_Mix':
        st.write(f"Presença do dado '_', provavelmente uma fuga da regra de negócio")

    if col == 'Payment_Behaviour':
        st.write(f"Presença do dado '!@9#%8', provavelmente uma fuga da regra de negócio")

    if col == 'Credit_Score':
        st.write(f"E finalmente nosso Target (Credit_Score), visualmente desbalanceado.")



st.write('Como esperado, veio uma grande massa de dados e portando variadas fugas da regra de négocio (o usuário faz de tudo para dificultar a vida do programador, não é mesmo? risos)')

st.write('Dessa forma, se faz necessária a limpeza dos dados antes de prosseguir.')
st.write("""
         
         
         """)

st.subheader('Data Cleaning')

st.write('A partir do que foi observado na exploração de dados a limpeza seguiu os pontos a seguir:')
st.write('- Age: Remoção de outliers, há valores negativos e e exorbitantes que não fazem sentido')
st.write('- Occupation: Os dados descritos como "_______" serão consideradas pessoas desempregadas')
st.write('- Annual_Income: Embora haja outliers, o mesmo não significa que é um dado com alguma espécie de erro, mas sim uma pessoa capital alto, portanto será mantido')
st.write('- Monthly_Inhand_Salary: A renda mensal das pessoas possuem valores nulos, porem na coluna renda anual não há valores nulos, por tanto nesses casos a renda mensal será uma aproximação da anual dividida por 12. Aqui não serão removidos os outliers, pela mesma justificativa anterior.')
st.write('- Num_Bank_Accounts: Não faz sentido os valores negativos de quantidade de contas, portanto serão eliminados. Existem pessoas com quantidades exorbitantes de contas, o que não faz sentido. Dessaa forma, os outeliers serão removidos.')
st.write('- Num_Credit_Card: Mesmas considerações feitas para a quantidade de contas bancárias')
st.write('- Interest_Rate: Não serão removidos os outliers pois os dados podem ser verdadeiros, uma vez que pode existir pessoas individadas')
st.write('- Num_of_Loan: Não faz sentido haver quantidade negativa de empréstimos. Remoção dos outliers, visto que em alguns casos a quantidade de empréstimos que uma pessoa é exorbitante, o que não faz sentido já que é algo limitado.')
st.write('- Type_of_Loan: Os dados nulos serão preenchidos pela pela moda')
st.write('- Delay_from_due_date: Não faz sentido valores negativos. Remoção dos outliers não se faz necessária, uma vez que realmente existem pessoas que possuem dívidas em processo.')
st.write('- Num_of_Delayed_Payment: Nesta coluna existem valores nulos. Neste caso serão preenchidos com a mediana, uma vez que sofre menor influência de outliers. Remoção dos outliers não se faz necessária, visto que é possível que pessoas estejam a muito tempo em dívida.')
st.write('- Changed_Credit_Limit: Substituição de nulos pela mediana. Não serão removidos os outliers por haver a possibilidade de aumentos especiais no crédito.')
st.write('- Num_Credit_Inquiries: Substituindo nulos pela mediana. Sob a ótica que essas consultas são feitas pelo banco e com o intuito de avaliar aumento do crédito, quantidades de consultas exorbitantes não fazem sentido (remoção de outliers).')
st.write('- Credit_Mix: A coluns Credit_Mix possui um dado chamado "_" que pode ser um cliente sem classificação de crédito, dessa forma será mantido, apenas modificado o nome.')
st.write('- Outstanding_Debt: Não será feita a remoção dos outliers, pois faz sentido que clientes tenham grandes dívidas a serem pagas e não apenas um erro.')
st.write('- Credit_Utilization_Ratio: Remoção dos outliers não necessária, pois é uma variável que varia de perfil de cliente, não necessariamente um erro')
st.write('- Credit_History_Age: Substituir os valores nulos pela mediana.')
st.write('- Payment_of_Min_Amount: A coluna Payment_of_Min_Amount possui dados classificados como "NM". Aqui será assumido "NM" como pessoas que não possuem parcelas a serem pagas, dessa forma não há a necessidade de tratamento por estar aparentemente dentro da regra de negócio.')
st.write('- Total_EMI_per_month: Embora haja outilers faz sentido haver pessoas que devam mais, da mesma forma que um tipo de cliente pode pegar um grande emprestimo.')
st.write('- Amount_invested_monthly: Variável que depende do perfil do cliente, não necessariamente os outliers se tratam de um erro. Substituir nulos pela mediana')
st.write("""- Payment_Behaviour: Nesta coluna existem dados como '!@9#%8', no entanto é claro que se trata de uma fuga da regra de negócio, visto que as classficações a seguir fazem sentido entre si.
'High_spent_Small_value_payments' e 'Low_spent_Small_value_payments'
'High_spent_Medium_value_payments' e 'Low_spent_Medium_value_payments'
'High_spent_Large_value_payments' e 'Low_spent_Large_value_payments'

Portanto os dados '!@9#%8' será substituido pela moda""")
st.write('- Monthly_Balance: Variável com outliers, mas que não necessariamente é um erro, mas sim cliente com alto rendimento. Os valores nulos do balanço mensal podem ser aproximados atráves dos dados de entrada e saída.')


st.subheader('Training the Model and Results')

st.write('Essa tarefa que meu superior me passou trata-se de um problema de classificação, uma vez que o enfatizou a necessidade de "um sistema inteligente para segregar as pessoas.')
st.write('Serão utilizados dois métodos: árvore de decisão e random forest.')

st.write('Antes do treinamento, a fim de garantir o bom desempenho do modelo, as colunas catergóricas foram transformadas em númericas (a partir do LabelEncoder) e as colunas numéricas foram normalizadas em um escala (StandardScaler) para que não sofresse alta influência de dado maiores.')

st.write('Além disso, vimos que nosso target está desbalanceado, o que pode resultar em dados tendenciosos. A estratégia aqui adotada será o undersampling, a fim de utilizar apenas os dados da base, diferente do oversampling, que cria dados sintéticos.')


histogram(df=df_pre_trat,values=f'Credit_Score',title=f'Target antes do Undersampling')

dados_balanceados = pd.read_csv(fr'streamlit_view\bases_to_view\dados_balanceados.csv')
histogram(df=dados_balanceados,values=f'Credit_Score',title=f'Target depois do Undersampling')


st.write(fr'Além disso, foram reservados 30% dos dados para a validação do modelo.')

st.write('Os resultados estão a seguir: ')

st.text('Arvore de decisão: f1_score: 0.66')
st.text('Random Forest: f1_score: 0.77')

st.write('RandomForest demonstrou-se mais eficiente e forte correlação com o target (>0.7), portanto será utilizado para responder as questões a seguir.')
st.write('OBS: Foram testadas as features eliminando as correlacionadas e mantendo. Ao manter os resultados foram ligeiramente melhores (<5%).')

st.write('A influência das variáveis sob o target foram as seguintes:')

feature_influence = pd.read_csv(fr'streamlit_view/bases_to_view/feature_influencias.csv')

bar(df=feature_influence,label='Features',values='Influência',title= 'Influência das features sob o Target')

st.write('Além disso, a correlação entre as variáveis foram as seguintes: ')
correlation = fr'streamlit_view\bases_to_view\correlation.png'
st.image(correlation, caption='Correlação entre as Variáveis', use_column_width=True)

st.subheader('Answearing the Quetions')

st.write('1.	O que faz alguém ter um score maior ou menor?')
st.write("""
        O score é influenciado pelas variáveis a seguir:
         
            - Proporcional: idade do cliente, idade do histórico do cartão e comportamento de pagamento 
            - Inversamente Proporcional: quantidade de contas bancárias, quantidade de cartões de crédito, \nquantidade de empréstimo, quantidade de dias de atraso para o pagamento, variação percentual do limite do cartão, quantidade de consultas no cartão, dívida restante a ser paga e o \npagamento mínimo da parcela.
        
        """)


st.write('2.	A quantidade de empréstimos é relevante?')
st.write("""
        Não, está entre os cinco mais irrelevantes.
        """)

st.write('3.	O saldo mensal é relevante?')
st.write("""
        Não, pelo contrário, é o que menos influencia o Target.
        """)

st.write('4.	Que tipos de clientes são mais propensos a ficarem inadimplentes?')
st.write("""
        Os clientes mais propensos a ficarem inadimplentes são os que possuem maiores dívidas a serem pagas (Outstanding_Debt) e as variáveis que influencia positivamente essa variável são:

            - Quantidade de contas bancárias
            - Quantidade de cartões de créditos
            - Quantidade de empréstimos
            - Quantidade de dias de atraso do pagamento do empréstimo
            - Variação percentual no limite do cartão de crédito
            - Quantidade de consultas de cartão de crédito

        Portanto, as pessoas mais provavéis de de ficarem inadimplentes são aquelas que possuem maiores quantidade de contas bancárias, cartões de créditos, empréstimos, dias de atraso do pagamento, variação do limite do cartão e consultas de cartão.
        """)

st.write('5.	Qual informação mais influência no score?')
st.write("""
        A Coluna Outstanding_Debt (dívida restante a ser paga) é o que mais influencia o Score
        """)




