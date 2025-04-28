# DIOGO_MORTIMER_DDF_TECH_042025

# To do:
- [x] Choose a database
- [x] Load data on dadosfera's platform
- [x] Catalog the data dictionary (Bonus: using dadosfera's API)
- [ ] Organize the data in a data lake
- [ ] Make a data quality report with soda-core lib (Bonus: Define and implement a Common Data Model)
- [ ] Create a dashboard with at least 5 different visualizations

# Item 1 - Base de Dados

Para este case técnico, será utilizada a base de dados NYC Taxi and Limousine Commission (TLC) [Yellow Taxi Trip Records in February 2025](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page). Esta base de dados inclui informações de viagens realizadas por táxis amarelos na cidade de Nova Iorque no mês de Fevereiro de 2025. Estas informações podem ser úteis para uma empresa que deseja entrar no mercado de aplicativos de carona e precisa conhecer os padrões de viagens como horários e locais de maior demanda para se posicionar de forma estratégica.

# Item 2 - Integração com a Dadosfera

# Item 3 - Exploração
## Dicionário de Dados
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
