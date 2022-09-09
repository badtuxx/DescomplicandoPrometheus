# [Descomplicando o Prometheus](https://www.linuxtips.io/products/descomplicando-o-prometheus) - O Treinamento


Em construção...

- **[DAY-1](day-1/README.md) - Em revisão...**
    - [Por que precisamos de ferramentas como o Prometheus?](day-1/README.md#por-que-precisamos-de-ferramentas-como-o-prometheus)
    - [O que é monitorar?](day-1/README.md#o-que-e-monitorar)
        - [O monitoramento e a observabilidade](day-1/README.md#o-monitoramento-e-a-observabilidade)
    - [O que é o Prometheus?](day-1/README.md#o-que-e-o-prometheus)
        - [A arquitetura do Prometheus](day-1/README.md#a-arquitetura-do-prometheus)
    - [Instalando o Prometheus](day-1/README.md#instalando-o-prometheus)
        - [Executando o Prometheus em um node Linux](day-1/README.md#executando-o-prometheus-em-um-node-linux)
        - [Instalação do Prometheus no Linux](day-1/README.md#instalação-do-prometheus-no-linux)
    - [A sua lição de casa](day-1/README.md#a-sua-lição-de-casa)
    - [Desafio do Day-1](day-1/README.md#desafio-do-day-1)
    - [Final do Day-1](day-1/README.md#final-do-day-1)

&nbsp;


- **[DAY-2](day-2/README.md) - Em revisão...**
- [O Data Model do Prometheus](day-2/README.md#o-data-model-do-prometheus)
- [As queries do Prometheus e o PromQL](day-2/README.md#as-queries-do-prometheus-e-o-promql)
- [O nosso primeiro exporter](day-2/README.md#o-nosso-primeiro-exporter)
  - [Nosso Primeiro Exporter no Container](day-2/README.md#nosso-primeiro-exporter-no-container)
- [Os Targets do Prometheus](day-2/README.md#os-targets-do-prometheus)
- [Visualizando as métricas do nosso primeiro exporter](day-2/README.md#visualizando-as-métricas-do-nosso-primeiro-exporter)
- [Conhecendo um pouco mais sobre os tipos de dados do Prometheus](day-2/README.md#conhecendo-um-pouco-mais-sobre-os-tipos-de-dados-do-prometheus) 
  - [gauge: Medidor](day-2/README.md#gauge-medidor)
  - [counter: Contador](day-2/README.md#counter-contador)
  - [summary: Resumo](day-2/README.md#summary-resumo)
  - [histogram: Histograma](day-2/README.md#histogram-histograma)
- [Chega por hoje!](day-2/README.md#chega-por-hoje)
- [Lição de casa](day-2/README.md#lição-de-casa)


&nbsp;

- **[DAY-3](day-3/README.md) - Em construção...**
    - [Criando o nosso segundo exporter](day-3/README.md#criando-o-nosso-segundo-exporter)
	- [Criando o nosso exporter usando Go](day-3/README.md#criando-o-nosso-exporter-usando-go)
	- [Adicionando o nosso exporter no container](day-3/README.md#adicionando-o-nosso-exporter-no-container)
	- [Adicionando o novo Target no Prometheus](day-3/README.md#adicionando-o-novo-target-no-prometheus)
- [As Funções](day-3/README.md#as-funções)
  - [A função rate](day-3/README.md#a-função-rate)
  - [A função irate](day-3/README.md#a-função-irate)
  - [A função delta](day-3/README.md#a-função-delta)
  - [A função increase](day-3/README.md#a-função-increase)
  - [A função sum](day-3/README.md#a-função-sum)
  - [A função count](day-3/README.md#a-função-count)
  - [A função avg](day-3/README.md#a-função-avg)
  - [A função min](day-3/README.md#a-função-min)
  - [A função max](day-3/README.md#a-função-max)
  - [A função avg_over_time](day-3/README.md#a-função-avg_over_time)
  - [A função sum_over_time](day-3/README.md#a-função-sum_over_time)
  - [A função max_over_time](day-3/README.md#a-função-max_over_time)
  - [A função min_over_time](day-3/README.md#a-função-min_over_time)
  - [A função stddev_over_time](day-3/README.md#a-função-stddev_over_time)
  - [A função by](day-3/README.md#a-função-by)
  - [A função without](day-3/README.md#a-função-without)
  - [A função histogram_quantile e quantile](day-3/README.md#a-função-histogram_quantile-e-quantile)
- [Praticando e usando as funções](day-3/README.md#praticando-e-usando-as-funções)
- [Operadores](day-3/README.md#operadores)
	- [Operador de igualdade](day-3/README.md#operador-de-igualdade)
	- [Operador de diferença](day-3/README.md#operador-de-diferença)
	- [Operador de maior que](day-3/README.md#operador-de-maior-que)
	- [Operador de menor que](day-3/README.md#operador-de-menor-que)
	- [Operador de maior ou igual que](day-3/README.md#operador-de-maior-ou-igual-que)
	- [Operador de menor ou igual que](day-3/README.md#operador-de-menor-ou-igual-que)
	- [Operador de multiplicação](day-3/README.md#operador-de-multiplicação)
	- [Operador de divisão](day-3/README.md#operador-de-divisão)
	- [Operador de adição](day-3/README.md#operador-de-adição)
	- [Operador de subtração](day-3/README.md#operador-de-subtração)
	- [Operador de modulo](day-3/README.md#operador-de-modulo)
	- [Operador de potenciação](day-3/README.md#operador-de-potenciação)
	- [Operador de agrupamento](day-3/README.md#operador-de-agrupamento)
	- [Operador de concatenação](day-3/README.md#operador-de-concatenação)
	- [Operador de comparação de strings](day-3/README.md#operador-de-comparação-de-strings)
	- [Chega de operadores por hoje](day-3/README.md#chega-de-operadores-por-hoje)
- [O Node Exporter](day-3/README.md#o-node-exporter)
	- [Os Collectors](day-3/README.md#os-collectors)
	- [Instalação do Node Exporter no Linux](day-3/README.md#instalação-do-node-exporter-no-linux)
	- [Adicionando o Node Exporter no Prometheus](day-3/README.md#adicionando-o-node-exporter-no-prometheus)
	- [Habilitando novos collectors no Node Exporter](day-3/README.md#habilitando-novos-collectors-no-node-exporter)
- [Algumas queries capturando métricas do Node Exporter](day-3/README.md#algumas-queries-capturando-métricas-do-node-exporter)
- [O Grafana](day-3/README.md#o-grafana)
  - [Instalação do Grafana](day-3/README.md#instalação-do-grafana)
  - [Adicionando o Prometheus como Data Source](day-3/README.md#adicionando-o-prometheus-como-data-source)
  - [Criando o nosso primeiro Dashboard](day-3/README.md#criando-o-nosso-primeiro-dashboard)
- [Chega por hoje!](day-3/README.md#chega-por-hoje)
- [Lição de casa](day-3/README.md#lição-de-casa)
- [Referências](day-3/README.md#referências)

- [DAY-4](day-4/README.md) - Em construção...

- [DAY-5](day-5/README.md) - Em construção...

&nbsp;

## O treinamento [Descomplicando o Prometheus](https://www.linuxtips.io/products/descomplicando-o-prometheus)

Pensamos em fazer um treinamento realmente prático. Um treinamento onde a pessoa consiga aprender os conceitos e toda a teoria com explicações interessantes e excelente didática, com exemplo e desafios práticos para que você consiga executar todo o conhecimento adquirido. Isso é muito importante para que você consiga fixar e explorar ainda mais o conteúdo do treinamento.
E por fim, vamos simular algumas conversas, para que pareça um pouco mais com o dia-a-dia no ambiente de trabalho.

Durante o treinamento vamos passar por todos os tópicos importantes do Prometheus, para que no final do treinamento você possua todo conhecimento e também toda a segurança para implementar e administrar o Prometheus em ambientes críticos e complexos.

Vamos entender o que é o Prometheus e como ele pode nos ajudar a monitorar nossas serviços e sistemas. Vamos aprender diversas formas de instalar e configurar o Prometheus, sempre visando a melhor performance e a cobertura de diversos cenários.
Vamos integra-lo com diversas ferramentas como o Grafana e o AlertManager, trazendo ainda mais poder ao Prometheus. 
Durante o treinamento iremos entender como criar queries performáticas e que consigam nos trazer as informações que precisamos.
Vamos aprender muito sobre exporters, rules e alerts.
Acreditamos que o melhor ambiente para ter o Prometheus sendo executado de maneira segura e em alta disponibilidade é dentro de clusters Kubernetes, portanto durante o treinamento seremos expostos a esse cenário com muita frequência, afinal esse treinamento é para te preparar para a vida real e ambientes reais.
Vamos aprender sobre a utilização de storage para persistir os dados coletas e também como configurar o Prometheus para se beneficiar de todo o dinamismo do service discovery.
Iremos aprender sobre como configurar e utilizar o Push Gateway e claro, aprender a monitorar o próprio Prometheus.

E claro, sempre trazendo exemplos de integrações e de caso de uso reais para ajudar a enriquecer ainda mais o treinamento.

Estamos prontos para iniciar a nossa viagem?

### O conteúdo programático

O conteúdo ainda será ajustado, e no final do treinamento teremos o conteúdo completo.

- Como monitorar sistemas e serviços
- O que é o Prometheus?
- Instalando e configurando o Prometheus
- Integrando com o Grafana
- Adicionando items de nossa infra no Prometheus
- Queries
- Funções
- Data Model do Prometheus
- Visualizando as métricas em dashboards
- Monitorando containers e outros hosts
- Exporters
- Criando o nosso exporter
- Rules
- Alertas
- Kubernetes e Prometheus
- Prometheus em HA
- Storage
- Service Discovery
- Prometheus e o Zabbix
- Push Gateway
- Exemplo de integrações
- Instalando e configurando o Prometheus (2)
- Monitorando o Prometheus

### Como adquirir o treinamento?

Para adquirir o treinamento [Descomplicando o Prometheus](https://www.linuxtips.io/products/descomplicando-o-prometheus) você deverá ir até a loja da [LINUXtips](https://www.linuxtips.io/).

Para ir até o treinamento, [CLIQUE AQUI](https://www.linuxtips.io/products/descomplicando-o-prometheus).


## A ideia do formato do treinamento

Ensinar Prometheus de uma forma mais real, passando todo o conteúdo de forma prática e trazendo uma conexão com o ambiente real de trabalho.

Esse é o primeiro treinamento sobre Prometheus de forma realmente prática, da vida real. Pois entendemos que prática é o conjunto de entendimento sobre um assunto, seguido de exemplos reais que possam ser reproduzidos e conectando tudo isso com a forma como trabalhamos.

Assim a definição de prática passa a ser um focada em o conhecimento da ferramenta e adicionando a realidade de um profissional no seu dia-a-dia aprendendo uma nova tecnologia, uma nova ferramenta.

Prepare-se para um novo tipo de treinamento, e o melhor, prepare-se para um novo conceito sobre treinamento prático e de aprendizado de tecnologia.

### As pessoas (personagens) no treinamento

Temos algumas pessoas que vão nos ajudar durante o treinamento, simulando uma dinâmica um pouco maior e ajudando na imersão que gostaríamos. 


Ainda estamos desenvolvendo e aprimorando os personagens e o enredo, portanto ainda teremos muitas novidades.


#### A Pessoa_X

A Pessoa_X é uma das pessoas responsáveis pela loja de meias Strigus Socket, que está no meio da modernização de seu infra e das ferramentas que são utilizadas.

Segundo uma pessoa que já trabalhou com a Pessoa_X, ela é a pessoa que está sempre procurando aprender para inovar em seu ambiente. Normalmente é através dela que surgem as novas ferramentas, bem como a resolução de um monte de problemas.

O nível de conhecimento dela é sempre iniciante quando ela entra em um novo projeto, porém ao final dele, ela se torna uma especialista e com uma boa experiência prática, pois ela foi exposta a diversas situações, que a fizeram conhecer a nova tecnologia muito bem e se sentindo muito confortável em trabalhar no projeto.

Pessoa_X, foi um prazer fazer essa pequena descrição sobre você! 

Seja bem-vinda nesse novo projeto e espero que você se divirta como sempre! 

Lembre-se sempre que eu, Jeferson, estarei aqui para apoiar você em cada etapa dessa jornada! Eu sou o seu parceiro nesse projeto e tudo o que você precisar nessa jornada! Bora!


#### A Pessoa_Lider_X

Iremos criando a personalidade dessa pessoa durante o treinamento.
O que já sabemos é que ela é a pessoa líder imediata da Pessoa_X, e que irá demandar a maioria das tarefas. E tem como o esteriótipo um líder meio tosco.

#### A Pessoa_Diretora_X

Líder imediato da Pessoa_Lider_X e que tem um sobrinho 'jênio' e que está ali, dando os seus pitacos no setor de tecnologia, por que ele 'mereceu', entendeu?


#### A Pessoa_RH_X

A pessoa responsável pelo RH da empresa, no decorrer do treinamento vamos faz
endo a história e características dela.


## Vamos começar?

Agora que você já conhece mais detalhes sobre o treinamento, acredito que já podemos começar, certo?

Lembrando que o treinamento está disponível na plataforma da escola da LINUXtips, que não é o mesmo endereço da [loja](https://www.linuxtips.io/), para acessar a escola [CLIQUE AQUI](https://school.linuxtips.io).


### O conteúdo

Como o treinamento é dividido em **days**, acesse o diretório correto para acessar o conteúdo completar do treinamento do **day** em que vc está estudando.

- [ACESSE O DAY-1](day-1/README.md)

Durante o dia de hoje, nós iremos focar em o que é o Prometheus e qual problema ele resolve.
Iremos entender os diferentes tipos de monitoramento e as diferenças entre eles.
Hoje é dia de conhecer a história do Prometheus e também a motivação para a sua criação lá na SoundCloud.
Vamos entender a arquitetura do Prometheus e como ele se relaciona com outros aplicativos.
E por fim, vamos instalar o Prometheus e fazer a nossa primeira configuração para o nosso mais novo serviço de monitoração.
Teremos ainda o nosso primeiro contato com a interface web do Prometheus e vamos criar a nossa primeira query.

- [ACESSE O DAY-2](day-2/README.md)

Seja muito bem-vinda e muito bem-vindo para o seu segundo dia de treinamento! Sim, eu considero esse livro um treinamento e não somente um guia de como obter o melhor do sensacional Prometheus!

Hoje nós vamos aprender como criar as nossa primeiras *queries* e para isso vamos precisar entender o modelo de dados que o Prometheus utiliza, vamos entender no detalhe o que é uma métrica para o Prometheus e vamos aprender como criar a nossa propria métrica e as nossas primeiras queries.

Vamos criar o nosso primeiro exporter utilizando Python Docker. Vamos entender os tipos de dados que o Prometheus utiliza, como utiliza-los e pra que servem.

Vamos conhecer as nossas primeiras funções para que possamos ter ainda mais poderes para criar as nossa queries PromQL.


- [ACESSE O DAY-3](day-3/README.md)
- [ACESSE O DAY-4](day-4/README.md)
- [ACESSE O DAY-5](day-5/README.md)


**Bons estudos!**

