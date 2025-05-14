# DIOGO_MORTIMER_DDF_TECH_042025

# To do:
- [x] Choose a database
- [x] Load data on dadosfera's platform
- [x] Catalog the data dictionary
- [ ] Organize the data in a data lake
- [ ] Make a data quality report with soda-core lib
- [x] Create a dashboard with at least 5 different visualizations

# Item 1 - Base de Dados

Para este case técnico, foi utilizada a base de dados NYC Taxi and Limousine Commission (TLC) [Yellow Taxi Trip Records in February 2025](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page). Esta base de dados inclui informações de viagens realizadas por táxis amarelos na cidade de Nova Iorque no mês de Fevereiro de 2025. Estas informações podem ser úteis para uma empresa que deseja se posicionar de forma estratégica e precisa conhecer padrões de viagens como horários e locais de maior demanda da cidade de Nova Iorque.

# Item 2 - Integração com a Dadosfera

A plataforma da Dadosfera apresentou um erro ao tentar integrar o arquivo parquet do dataset. e o arquivo CSV do dataset escolhido é maior que o tamanho máximo aceito. Por isso, foi necessário eliminar algumas colunas e linhas para que o arquivo ficasse num tamanho adequado. Foram excluídas linhas aleatórias para não criar viés no dataset e apenas colunas que não foram utilizadas na análise foram excluídas. o que possibilitou a utilização desse dataset reduzido sem mudanças significativas na conclusão da análise.

![image](https://github.com/user-attachments/assets/38810af7-74d7-40a2-9cc2-a61b802eb69b)
![image](https://github.com/user-attachments/assets/8d078fca-cbfd-4148-b39f-550be5168403)

# Item 3 - Explorar
## Dicionário de Dados
O dicionário abaixo foi feito enquanto o problema de integração da plataforma ainda não havia sido resolvido e portanto inclui todas as colunas do dataset.

| Campo | Descrição | Tipo | Formato | Exemplo | Observações |
|-------|------------|------|---------|-------------------|-------------|
| VendorID | Código indicando provedor TPEP de onde vem o registro. | int32 | - | Ex.: 1 | 1 = Creative Mobile Technologies, LLC<br>2 = Curb Mobility, LLC<br>6 = Myle Technologies Inc<br>7 = Helix |
| tpep_pickup_datetime | Data e horário de partida. | datetime64[us] | YYYY-MM-DD HH:MM:SS| Ex.: 2025-02-01 00:12:18 | - |
| tpep_dropoff_datetime | Data e horário de chegada. | datetime64[us] | YYYY-MM-DD HH:MM:SS| Ex.: 2025-02-01 00:32:33 | - |
| passenger_count | Número de passageiros no veículo. | float64 | - | Ex.: 3.0 | - |
| trip_distance | Distância percorrida em milhas | float64 | - | Ex.: 3.12 | - |
| RatecodeID | Código indicanco tipo de taxa de precificação. | float64 | - | Ex.: 1.0 | 1 = Standard rate<br>2 = JFK<br>3 = Newark<br>4 = Nassau or Westchester<br>5 = Negotiated fare<br>6 = Group ride<br>99 = Null/unknown |
| store_and_fwd_flag | Indica se o registro de viagem foi armazenado na memória do veículo antes de ser enviado (store and forward) por não possuía conexão com o servidor. | object | - | Ex.: N | Y = store and forward, N = não store and forward  |
| PULocationID | Zona de Táxi TLC onde a viagem iniciou. | int32 | - | Ex.: 246 | Valor entre 1 - 246. Tabela de referência csv disponível no site oficial. |
| DOLocationID | Zona de Táxi TLC onde a viagem encerrou. | int32 | - | Ex.: 79 | Valor entre 1 - 246. Tabela de referência csv disponível no site oficial. |
| payment_type | Código especificando método de pagamento pela viagem. | int64 | - | Ex.: 1 | 0 = Flex Fare trip<br>1 = Credit card<br>2 = Cash<br>3 = No charge<br>4 = Dispute<br>5 = Unknown<br>6 = Voided trip |
| fare_amount | Valor cobrado pela distância e tempo de viagem calculado pelo taxímetro. | float64 | - | Ex.: 19.8 | - |
| extra | Outras cobranças não categorizadas. | float64 | - | Ex.: 1.0 | - |
| mta_tax | Taxa aplicada automaticamente baseada na taxa do taxímetro usado. | float64 | - | Ex.: 0.5 | - |
| tip_amount | Gorjeta cobrada. | float64 | - | Ex.: 5.11 | Incluídas apenas gorjetas pagas por cartão de crédito. Gorjetas pagas em dinheiro físico não são registradas. |
| tolls_amount | Cobrança por pedágios. | float64 | - | Ex.: 0.0 | - |
| improvement_surcharge | Sobretaxa de melhoria cobrada no início da corrida. | float64 | - | Ex.: 1.0 | - |
| total_amount | Preço final cobrado dos passageiros. | float64 | - | Ex.: 30.66 | - |
| congestion_surcharge | Sobretaxa de congestionamento do Estade de Nova Iorque. | float64 | - | Ex.: 2.5 | - |
| Airport_fee | Taxa de aeroporto. | float64 | - | Ex.: 0.0 | Aplicada apenas para corridas iniciadas nos aeroportos LaGuardia e John F. Kennedy |
| cbd_congestion_fee | Valor cobrado por corrida para viagens que entram ou circulam na Zona de Alívio de Congestionamento da MTA (área central de Manhattan). | float64 | - | Ex.: 0.75 | - |

# Item 4 - Data Quality

# Item 7 - Análise dos Dados

## Análise das Categorias
### Embarques e Desembarques por Região de Nova Iorque
![Embarques por Região de Nova Iorque](https://github.com/user-attachments/assets/99f5f161-ebc3-4457-abbc-f41fa313e041)
![Desembarques por Região de Nova Iorque](https://github.com/user-attachments/assets/d09a75d7-63ff-4947-9d81-d91b4b4444b2)

A análise do total de embarques e desembarques em cada região de Nova Iorque ratifica a ideia preconcebida de que Manhattan detém a maior parte do movimento de pessoas na cidade e especifica o quão maior de fato é. Isto leva a crer que esta região deve ser priorizada, se necessário em detrimento das outras, para se instalar um negócio de caronas. 

### Embarques e Desembarques por Zona de Nova Iorque
![Embarques por Zona de Nova Iorque](https://github.com/user-attachments/assets/ca4770b4-3696-42b8-8537-4b7c333c733d)
![Desembarques por Zona de Nova Iorque](https://github.com/user-attachments/assets/16fa4923-7a1c-44c6-933e-c54ae6499e2e)

Além de levar às mesmas conclusões das análises de demanda por região, as análises por zona trouxeram um dado importante: boa parte da demanda de transporte vem dos aeroportos, principalmente JFK e LaGuardia, localizados na região do Queens. Logo, esta informação deve ser considerada pela empresa ao distribuir sua disponibilidade, mas ainda priorizando Manhattan. 

## Análise de Série temporal
### Embarques por dia ao longo do ano
![Embarques por dia ao longo do ano](https://github.com/user-attachments/assets/b8772ef3-83fd-4218-a008-6c5121f18e4d)

A série temporal de embarques ao longo do ano mostra que a demanda por caronas oscila ao longo do mês, com picos entre quintas feiras e sábados e portanto tornando esses dias mais importantes. Em contrapartida, Domingos e Segundas Feiras apresentam a menor demanda ao longo das semanas registradas.

### Média de Embarques por Hora do Dia
![Média de Embarques por Hora do Dia](https://github.com/user-attachments/assets/e5642dd1-767b-4699-bbd6-ebac6e06027c)

Pela série temporal de média de embarques por hora, podemos observar que a demanda é mínimia durante a madrugada, e cresce a partir das 6 horas da manhã até seu pico às 19 horas, tornando o intervalo das 16 até as 21 horas o mais relevante em questão de demanda.
