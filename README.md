# [Descomplicando o Prometheus](https://www.linuxtips.io/course/descomplicando-prometheus) - O LIVRO

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

&nbsp;

**ACESSE O LIVRO GRATUITAMENTE [CLICANDO AQUI](https://livro.descomplicandoprometheus.com.br)**

&nbsp;

### Conteúdo do Livro

- **[DAY-1](pt/src/day-1/README.md) - Em revisão...**
    - [Por que precisamos de ferramentas como o Prometheus?](pt/src/day-1/README.md#por-que-precisamos-de-ferramentas-como-o-prometheus)
    - [O que é monitorar?](pt/src/day-1/README.md#o-que-e-monitorar)
        - [O monitoramento e a observabilidade](pt/src/day-1/README.md#o-monitoramento-e-a-observabilidade)
    - [O que é o Prometheus?](pt/src/day-1/README.md#o-que-e-o-prometheus)
        - [A arquitetura do Prometheus](pt/src/day-1/README.md#a-arquitetura-do-prometheus)
    - [Instalando o Prometheus](pt/src/day-1/README.md#instalando-o-prometheus)
        - [Executando o Prometheus em um node Linux](pt/src/day-1/README.md#executando-o-prometheus-em-um-node-linux)
        - [Instalação do Prometheus no Linux](pt/src/day-1/README.md#instalação-do-prometheus-no-linux)
    - [A sua lição de casa](pt/src/day-1/README.md#a-sua-lição-de-casa)
    - [Desafio do Day-1](pt/src/day-1/README.md#desafio-do-day-1)
    - [Final do Day-1](pt/src/day-1/README.md#final-do-day-1)

- **[DAY-2](pt/src/day-2/README.md) - Em revisão...**
    - [O Data Model do Prometheus](pt/src/day-2/README.md#o-data-model-do-prometheus)
    - [As queries do Prometheus e o PromQL](pt/src/day-2/README.md#as-queries-do-prometheus-e-o-promql)
    - [O nosso primeiro exporter](pt/src/day-2/README.md#o-nosso-primeiro-exporter)
    - [Nosso Primeiro Exporter no Container](pt/src/day-2/README.md#nosso-primeiro-exporter-no-container)
    - [Os Targets do Prometheus](pt/src/day-2/README.md#os-targets-do-prometheus)
    - [Visualizando as métricas do nosso primeiro exporter](pt/src/day-2/README.md#visualizando-as-métricas-do-nosso-primeiro-exporter)
    - [Conhecendo um pouco mais sobre os tipos de dados do Prometheus](pt/src/day-2/README.md#conhecendo-um-pouco-mais-sobre-os-tipos-de-dados-do-prometheus) 
    - [gauge: Medidor](pt/src/day-2/README.md#gauge-medidor)
    - [counter: Contador](pt/src/day-2/README.md#counter-contador)
    - [summary: Resumo](pt/src/day-2/README.md#summary-resumo)
    - [histogram: Histograma](pt/src/day-2/README.md#histogram-histograma)
    - [Chega por hoje!](pt/src/day-2/README.md#chega-por-hoje)
    - [Lição de casa](pt/src/day-2/README.md#lição-de-casa)

- **[DAY-3](pt/src/day-3/README.md) - Em revisão...**
    - [Criando o nosso segundo exporter](pt/src/day-3/README.md#criando-o-nosso-segundo-exporter)
        - [Criando o nosso exporter usando Go](pt/src/day-3/README.md#criando-o-nosso-exporter-usando-go)
        - [Adicionando o nosso exporter no container](pt/src/day-3/README.md#adicionando-o-nosso-exporter-no-container)
        - [Adicionando o novo Target no Prometheus](pt/src/day-3/README.md#adicionando-o-novo-target-no-prometheus)
    - [As Funções](pt/src/day-3/README.md#as-funções)
    - [A função rate](pt/src/day-3/README.md#a-função-rate)
    - [A função irate](pt/src/day-3/README.md#a-função-irate)
    - [A função delta](pt/src/day-3/README.md#a-função-delta)
    - [A função increase](pt/src/day-3/README.md#a-função-increase)
    - [A função sum](pt/src/day-3/README.md#a-função-sum)
    - [A função count](pt/src/day-3/README.md#a-função-count)
    - [A função avg](pt/src/day-3/README.md#a-função-avg)
    - [A função min](pt/src/day-3/README.md#a-função-min)
    - [A função max](pt/src/day-3/README.md#a-função-max)
    - [A função avg_over_time](pt/src/day-3/README.md#a-função-avg_over_time)
    - [A função sum_over_time](pt/src/day-3/README.md#a-função-sum_over_time)
    - [A função max_over_time](pt/src/day-3/README.md#a-função-max_over_time)
    - [A função min_over_time](pt/src/day-3/README.md#a-função-min_over_time)
    - [A função stddev_over_time](pt/src/day-3/README.md#a-função-stddev_over_time)
    - [A função by](pt/src/day-3/README.md#a-função-by)
    - [A função without](pt/src/day-3/README.md#a-função-without)
    - [A função histogram_quantile e quantile](pt/src/day-3/README.md#a-função-histogram_quantile-e-quantile)
    - [Praticando e usando as funções](pt/src/day-3/README.md#praticando-e-usando-as-funções)
    - [Operadores](pt/src/day-3/README.md#operadores)
        - [Operador de igualdade](pt/src/day-3/README.md#operador-de-igualdade)
        - [Operador de diferença](pt/src/day-3/README.md#operador-de-diferença)
        - [Operador de maior que](pt/src/day-3/README.md#operador-de-maior-que)
        - [Operador de menor que](pt/src/day-3/README.md#operador-de-menor-que)
        - [Operador de maior ou igual que](pt/src/day-3/README.md#operador-de-maior-ou-igual-que)
        - [Operador de menor ou igual que](pt/src/day-3/README.md#operador-de-menor-ou-igual-que)
        - [Operador de multiplicação](pt/src/day-3/README.md#operador-de-multiplicação)
        - [Operador de divisão](pt/src/day-3/README.md#operador-de-divisão)
        - [Operador de adição](pt/src/day-3/README.md#operador-de-adição)
        - [Operador de subtração](pt/src/day-3/README.md#operador-de-subtração)
        - [Operador de modulo](pt/src/day-3/README.md#operador-de-modulo)
        - [Operador de potenciação](pt/src/day-3/README.md#operador-de-potenciação)
        - [Operador de agrupamento](pt/src/day-3/README.md#operador-de-agrupamento)
        - [Operador de concatenação](pt/src/day-3/README.md#operador-de-concatenação)
        - [Operador de comparação de strings](pt/src/day-3/README.md#operador-de-comparação-de-strings)
        - [Chega de operadores por hoje](pt/src/day-3/README.md#chega-de-operadores-por-hoje)
    - [O Node Exporter](pt/src/day-3/README.md#o-node-exporter)
        - [Os Collectors](pt/src/day-3/README.md#os-collectors)
        - [Instalação do Node Exporter no Linux](pt/src/day-3/README.md#instalação-do-node-exporter-no-linux)
        - [Adicionando o Node Exporter no Prometheus](pt/src/day-3/README.md#adicionando-o-node-exporter-no-prometheus)
        - [Habilitando novos collectors no Node Exporter](pt/src/day-3/README.md#habilitando-novos-collectors-no-node-exporter)
    - [Algumas queries capturando métricas do Node Exporter](pt/src/day-3/README.md#algumas-queries-capturando-métricas-do-node-exporter)
    - [O Grafana](pt/src/day-3/README.md#o-grafana)
    - [Instalação do Grafana](pt/src/day-3/README.md#instalação-do-grafana)
    - [Adicionando o Prometheus como Data Source](pt/src/day-3/README.md#adicionando-o-prometheus-como-data-source)
    - [Criando o nosso primeiro Dashboard](pt/src/day-3/README.md#criando-o-nosso-primeiro-dashboard)
    - [Chega por hoje!](pt/src/day-3/README.md#chega-por-hoje)
    - [Lição de casa](pt/src/day-3/README.md#lição-de-casa)
    - [Referências](pt/src/day-3/README.md#referências)

- **[DAY-4](pt/src/day-4/README.md) - Em revisão...**
    - [O que iremos ver hoje?](pt/src/day-4/README.md#o-que-iremos-ver-hoje)
    - [Conteúdo do Day-4](pt/src/day-4/README.md#conteúdo-do-day-4)
    - [O Grafana](pt/src/day-4/README.md#o-grafana)
    - [Instalando o Grafana](pt/src/day-4/README.md#instalando-o-grafana)
    - [Adicionando o Prometheus como Data Source](pt/src/day-4/README.md#adicionando-o-prometheus-como-data-source)
    - [Criando o nosso primeiro Dashboard](pt/src/day-4/README.md#criando-o-nosso-primeiro-dashboard)
    - [Alertmanager](pt/src/day-4/README.md#alertmanager)
    - [Instalando o Alertmanager](pt/src/day-4/README.md#instalando-o-alertmanager)

- **[DAY-5](pt/src/day-5/README.md) - Em revisão...**

- **[DAY-6](pt/src/day-6/README.md) - Em revisão...**
    - [O que iremos ver hoje](pt/src/day-6/README.md#o-que-iremos-ver-hoje)
    - [Conteúdo do Day-6](pt/src/day-6/README.md#conteúdo-do-day-6)
    - [O que é o kube-prometheus](pt/src/day-6/README.md#o-que-é-o-kube-prometheus)
    - [Instalando o nosso cluster Kubernetes](pt/src/day-6/README.md#instalando-o-nosso-cluster-kubernetes)
    - [Instalando o Kube-Prometheus](pt/src/day-6/README.md#instalando-o-kube-prometheus)
    - [Acessando o Grafana](pt/src/day-6/README.md#acessando-o-grafana)
    - [Acessando o Prometheus](pt/src/day-6/README.md#acessando-o-prometheus)
    - [Acessando o AlertManager](pt/src/day-6/README.md#acessando-o-alertmanager)
    - [Chega por hoje!](pt/src/day-6/README.md#chega-por-hoje)
    - [Lição de casa](pt/src/day-6/README.md#lição-de-casa)

- **[DAY-7](pt/src/day-7/README.md) - Em revisão...**
    - [O que iremos ver hoje?](pt/src/day-7/README.md#o-que-iremos-ver-hoje)
    - [Conteúdo do Day-7](pt/src/day-7/README.md#conteúdo-do-day-7)
    - [Os ServiceMonitors](pt/src/day-7/README.md#os-servicemonitors)
    - [Criando um ServiceMonitor](pt/src/day-7/README.md#criando-um-servicemonitor)
    - [Os PodMonitors](pt/src/day-7/README.md#os-podmonitors)
    - [Criando um PodMonitor](pt/src/day-7/README.md#criando-um-podmonitor)
    - [Criando nosso primeiro alerta](pt/src/day-7/README.md#criando-nosso-primeiro-alerta)
    - [O que é um PrometheusRule?](pt/src/day-7/README.md#o-que-é-um-prometheusrule)
        - [Criando um PrometheusRule](pt/src/day-7/README.md#criando-um-prometheusrule)
    - [Chega por hoje!](pt/src/day-7/README.md#chega-por-hoje)
    - [Lição de casa](pt/src/day-7/README.md#lição-de-casa)

- **[DAY-8](pt/src/day-8/README.md) - Em revisão...**
    - [O que iremos ver hoje?](pt/src/day-8/README.md#o-que-iremos-ver-hoje)
    - [Conteúdo do Day-8](pt/src/day-8/README.md#conteúdo-do-day-8)
    - [Vamos brincar com as métricas do Kubernetes](pt/src/day-8/README.md#vamos-brincar-com-as-métricas-do-kubernetes)
        - [O que podemos saber sobre os nodes do nosso cluster?](pt/src/day-8/README.md#o-que-podemos-saber-sobre-os-nodes-do-nosso-cluster)
        - [Quantos nós temos no nosso cluster?](pt/src/day-8/README.md#quantos-nós-temos-no-nosso-cluster)
        - [Qual a quantidade de CPU e memória que cada nó tem?](pt/src/day-8/README.md#qual-a-quantidade-de-cpu-e-memória-que-cada-nó-tem)
        - [O nó está disponível para receber novos pods?](pt/src/day-8/README.md#o-nó-está-disponível-para-receber-novos-pods)
        - [Qual a quantidade de informação que cada nó está recebendo e enviando?](pt/src/day-8/README.md#qual-a-quantidade-de-informação-que-cada-nó-está-recebendo-e-enviando)
        - [Quantos pods estão rodando em cada nó?](pt/src/day-8/README.md#quantos-pods-estão-rodando-em-cada-nó)
    - [Agora vamos saber se o nosso cluster está com problemas](pt/src/day-8/README.md#agora-vamos-saber-se-o-nosso-cluster-está-com-problemas)
        - [O que podemos saber sobre os pods do nosso cluster?](pt/src/day-8/README.md#o-que-podemos-saber-sobre-os-pods-do-nosso-cluster)
        - [Quantos pods estão rodando no nosso cluster?](pt/src/day-8/README.md#quantos-pods-estão-rodando-no-nosso-cluster)
        - [Quantos pods estão com problemas?](pt/src/day-8/README.md#quantos-pods-estão-com-problemas)
        - [Verificar os pods e os limites de memória e CPU configurados](pt/src/day-8/README.md#verificar-os-pods-e-os-limites-de-memória-e-cpu-configurados)
        - [Verificar se o cluster está com problemas relacionados ao disco](pt/src/day-8/README.md#verificar-se-o-cluster-está-com-problemas-relacionados-ao-disco)
        - [Verificar se o cluster está com problemas relacionados a memória](pt/src/day-8/README.md#verificar-se-o-cluster-está-com-problemas-relacionados-a-memória)
    - [E como saber se meus deployments estão com problemas?](pt/src/day-8/README.md#e-como-saber-se-meus-deployments-estão-com-problemas)
        - [Quantos deployments estão rodando no meu cluster?](pt/src/day-8/README.md#quantos-deployments-estão-rodando-no-meu-cluster)
        - [Quantos deployments estão com problemas?](pt/src/day-8/README.md#quantos-deployments-estão-com-problemas)
        - [Qual o status dos meus deployments?](pt/src/day-8/README.md#qual-o-status-dos-meus-deployments)
    - [E como saber se meus serviços estão com problemas?](pt/src/day-8/README.md#e-como-saber-se-meus-serviços-estão-com-problemas)
        - [Quantos serviços estão rodando no meu cluster?](pt/src/day-8/README.md#quantos-serviços-estão-rodando-no-meu-cluster)
        - [Todos os meus serviços estão com endpoints?](pt/src/day-8/README.md#todos-os-meus-serviços-estão-com-endpoints)
        - [Todos os meus serviços estão com endpoints ativos?](pt/src/day-8/README.md#todos-os-meus-serviços-estão-com-endpoints-ativos)
    - [Como eu posso modificar as configurações do meu Prometheus?](pt/src/day-8/README.md#como-eu-posso-modificar-as-configurações-do-meu-prometheus)
        - [Definindo o nosso Prometheus](pt/src/day-8/README.md#definindo-o-nosso-prometheus)
        - [Definindo o nosso Alertmanager](pt/src/day-8/README.md#definindo-o-nosso-alertmanager)

- **[DAY-9](pt/src/day-9/README.md) - Em revisão...**
    - [O que iremos ver hoje?](#o-que-iremos-ver-hoje)
    - [Conteúdo do Day-9](#conteúdo-do-day-9)
    - [O que é Relabeling?](#o-que-é-relabeling)
    - [Como funciona o Relabeling?](#como-funciona-o-relabeling)
    - [Exemplos de uso do Relabeling](#exemplos-de-uso-do-relabeling)
        - [ Removendo uma métrica baseado em uma label](#-removendo-uma-métrica-baseado-em-uma-label)
        - [Junta duas labels em uma só](#junta-duas-labels-em-uma-só)
        - [Adicionando uma nova label](#adicionando-uma-nova-label)
        - [Armazenando somente métricas específicas](#armazenando-somente-métricas-específicas)
        - [Mapeando todas as labels do Kubernetes](#mapeando-todas-as-labels-do-kubernetes)
    - [As meta labels do Prometheus](as-metas-labels-do-prometheus)


### Como adquirir o treinamento?

Para adquirir o treinamento [Descomplicando o Prometheus](https://www.linuxtips.io/course/descomplicando-prometheus) você deverá ir até a loja da [LINUXtips](https://www.linuxtips.io/).

Para ir até o treinamento, [CLIQUE AQUI](https://www.linuxtips.io/course/descomplicando-prometheus).


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

Lembrando que o treinamento está disponível na plataforma da escola da LINUXtips,para acessa-la [CLIQUE AQUI](https://linuxtips.io).


**Bons estudos!**

