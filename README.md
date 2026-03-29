Big Data E-commerce Sync: Personalização e Logística
Este projeto é uma simulação de um ecossistema de Big Data. O objetivo é demonstrar como o processamento de grandes volumes de dados pode otimizar a logística e personalizar a experiência do usuário.

  Projeto
A empresa enfrentava dificuldades com sistemas tradicionais (Data Warehouses) que não processavam dados em tempo hábil. Os principais problemas eram:

Logística ineficiente: Centros de Distribuição centralizados e atrasos na reposição.

Falta de personalização: Clientes recebendo ofertas irrelevantes.

Dados Silados: Informações de lojas físicas, site e redes sociais não integradas.

Linguagem: Python 3.x

Manipulação de Dados: Pandas & Numpy (Simulando motores de processamento como Spark/MapReduce)

Arquitetura: Conceitos de Data Lake para armazenamento de múltiplas fontes.

Estratégia 6Vs: * Volume & Valor: Identificação de demanda regional para novos CDs.

Velocidade: Processamento de recomendações em tempo real.

Variedade: Cruzamento de dados transacionais com comportamento de navegação.

Exemplo de Output
Ao rodar a simulação, o sistema gera o seguinte relatório:

--- ANÁLISE LOGÍSTICA (Estratégia de CDs) ---
Sugestão de prioridade para novos Centros de Distribuição:
Belo Horizonte    5000
São Paulo         1450
Curitiba           150

---------------------------------------------
Processando recomendações para o Cliente 102...
Produtos recomendados: Explorar nova categoria: Periféricos.

O programa executa duas análises críticas baseadas em um Data Lake simulado:

Módulo de Inteligência Logística:

Analisa o faturamento por cidade.

Sugere a localização estratégica para o próximo Centro de Distribuição (CD) com base no ROI (Retorno sobre Investimento).

 Recomendação Personalizada:

Identifica o histórico de compra do cliente.

Filtra itens já adquiridos.

Sugere produtos de categorias complementares para aumentar o engajamento.
