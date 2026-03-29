import pandas as pd  #atua como o motor de processamento (similar ao que o MapReduce ou Spark fazem em escalas maiores
import numpy as np

 # DATA LAKE (Fontes de Dados Variadas)
data_vendas = {
    'id_cliente': [101, 102, 103, 104, 105],
    'produto': ['Teclado RGB', 'Monitor 4K', 'Cadeira Gamer', 'Mouse Wireless', 'Monitor 4K'],
    'categoria': ['Periféricos', 'Monitores', 'Móveis', 'Periféricos', 'Monitores'],
    'cidade_cliente': ['São Paulo', 'Belo Horizonte', 'São Paulo', 'Curitiba', 'Belo Horizonte'],
    'valor': [250, 2500, 1200, 150, 2500]
}

df_vendas = pd.DataFrame(data_vendas) #o dicionário data_vendas e o pd.DataFrame representam o Data Lake.

 #LOGÍSTICA: Identificação de Locais para Novos CDs (Volume + Valor)
def analise_logistica(df): #resolve o problema dos "Centros de Distribuição (CDs) centralizados
    print("--- ANÁLISE LOGÍSTICA (Estratégia de CDs) ---")
    # Agrupa vendas por cidade para identificar demanda reprimida
    demanda_por_cidade = df.groupby('cidade_cliente')['valor'].sum().sort_values(ascending=False)
    print("Sugestão de prioridade para novos Centros de Distribuição:")
    print(demanda_por_cidade)
    print("-" * 45)

#  Motor de Recomendação (Velocidade + Variedade)
def recomendar_produto(id_cliente, df):
    #  histórico do cliente
    historico = df[df['id_cliente'] == id_cliente]
    
    if historico.empty:
        return "Cliente novo: Recomendar produtos mais vendidos (Trendings)."
    
    # Lógica: Recomendar itens da mesma categoria que ele ainda não comprou
    ultima_categoria = historico['categoria'].iloc[-1]
    recomendacoes = df[df['categoria'] == ultima_categoria]['produto'].unique()
    
    # Remove o que ele já comprou
    ja_comprados = historico['produto'].unique()
    final_sugestao = [p for p in recomendacoes if p not in ja_comprados]
    
    return final_sugestao if final_sugestao else f"Explorar nova categoria: {df['categoria'].unique()[0]}"

# --- funcionamento ---

#  Analisar Logística
analise_logistica(df_vendas)

#  Personalizar Experiência para o Cliente 102 (que comprou Monitor 4K em BH)
cliente_alvo = 102
print(f"Processando recomendações para o Cliente {cliente_alvo}...")
sugestoes = recomendar_produto(cliente_alvo, df_vendas)
print(f"Produtos recomendados: {sugestoes}")

#RESULTADO ESPERADO:

###Análise Logística: Onde investir?
#O programa somou todas as vendas e as agrupou por localização.
#O Insight: Belo Horizonte tem um faturamento de 5.000, que é mais do que o triplo de São Paulo (1.450).
#A Tomada de Decisão (6Vs - Valor): Se a empresa hoje tem CDs centralizados (ex: apenas em SP), ela está gastando muito com frete para enviar produtos para BH.
#Ação: A recomendação estratégica é abrir o próximo Centro de Distribuição em Belo Horizonte. Isso reduz o tempo de entrega e o custo logístico, atacando diretamente a reclamação de "atrasos na reposição".
#2. Processando recomendações para o Cliente 102
#Aqui o sistema aplicou o conceito de Personalização em Tempo Real.
#O Cenário: O Cliente 102 comprou um "Monitor 4K" (Categoria: Monitores).
#O Problema: No nosso banco de dados simulado, ele já comprou todos os monitores disponíveis.
#A Inteligência do Algoritmo: Em vez de mostrar o mesmo monitor que ele já possui (o que irritaria o cliente), o programa percebe que a categoria "Monitores" está esgotada para ele e sugere "Explorar nova categoria: Periféricos".
#3. Por que o resultado foi "Periféricos"?
#Isso demonstra o uso de Variedade e Análise Preditiva:
#Mix de Produtos: O sistema identifica que quem compra um monitor de alta performance (4K) geralmente precisa de periféricos (teclados, mouses) para completar o setup.
#Engajamento: Ao sugerir algo novo e complementar, você aumenta o Lifetime Value (valor que o cliente gasta ao longo do tempo) e resolve o problema de "clientes que não encontram o que desejam".