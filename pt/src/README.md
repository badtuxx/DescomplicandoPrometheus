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

<details>
<summary class="summary">Clique aqui para expandir</summary>

- **[DAY-1](day-1/index.html) - Em revisão...**
    - [Por que precisamos de ferramentas como o Prometheus?](day-1/index.html#por-que-precisamos-de-ferramentas-como-o-prometheus)
    - [O que é monitorar?](day-1/index.html#o-que-e-monitorar)
        - [O monitoramento e a observabilidade](day-1/index.html#o-monitoramento-e-a-observabilidade)
    - [O que é o Prometheus?](day-1/index.html#o-que-e-o-prometheus)
        - [A arquitetura do Prometheus](day-1/index.html#a-arquitetura-do-prometheus)
    - [Instalando o Prometheus](day-1/index.html#instalando-o-prometheus)
        - [Executando o Prometheus em um node Linux](day-1/index.html#executando-o-prometheus-em-um-node-linux)
        - [Instalação do Prometheus no Linux](day-1/index.html#instalação-do-prometheus-no-linux)
    - [A sua lição de casa](day-1/index.html#a-sua-lição-de-casa)
    - [Desafio do Day-1](day-1/index.html#desafio-do-day-1)
    - [Final do Day-1](day-1/index.html#final-do-day-1)

- **[DAY-2](day-2/index.html) - Em revisão...**
    - [O Data Model do Prometheus](day-2/index.html#o-data-model-do-prometheus)
    - [As queries do Prometheus e o PromQL](day-2/index.html#as-queries-do-prometheus-e-o-promql)
    - [O nosso primeiro exporter](day-2/index.html#o-nosso-primeiro-exporter)
    - [Nosso Primeiro Exporter no Container](day-2/index.html#nosso-primeiro-exporter-no-container)
    - [Os Targets do Prometheus](day-2/index.html#os-targets-do-prometheus)
    - [Visualizando as métricas do nosso primeiro exporter](day-2/index.html#visualizando-as-métricas-do-nosso-primeiro-exporter)
    - [Conhecendo um pouco mais sobre os tipos de dados do Prometheus](day-2/index.html#conhecendo-um-pouco-mais-sobre-os-tipos-de-dados-do-prometheus) 
    - [gauge: Medidor](day-2/index.html#gauge-medidor)
    - [counter: Contador](day-2/index.html#counter-contador)
    - [summary: Resumo](day-2/index.html#summary-resumo)
    - [histogram: Histograma](day-2/index.html#histogram-histograma)
    - [Chega por hoje!](day-2/index.html#chega-por-hoje)
    - [Lição de casa](day-2/index.html#lição-de-casa)

- **[DAY-3](day-3/index.html) - Em revisão...**
    - [Criando o nosso segundo exporter](day-3/index.html#criando-o-nosso-segundo-exporter)
        - [Criando o nosso exporter usando Go](day-3/index.html#criando-o-nosso-exporter-usando-go)
        - [Adicionando o nosso exporter no container](day-3/index.html#adicionando-o-nosso-exporter-no-container)
        - [Adicionando o novo Target no Prometheus](day-3/index.html#adicionando-o-novo-target-no-prometheus)
    - [As Funções](day-3/index.html#as-funções)
    - [A função rate](day-3/index.html#a-função-rate)
    - [A função irate](day-3/index.html#a-função-irate)
    - [A função delta](day-3/index.html#a-função-delta)
    - [A função increase](day-3/index.html#a-função-increase)
    - [A função sum](day-3/index.html#a-função-sum)
    - [A função count](day-3/index.html#a-função-count)
    - [A função avg](day-3/index.html#a-função-avg)
    - [A função min](day-3/index.html#a-função-min)
    - [A função max](day-3/index.html#a-função-max)
    - [A função avg_over_time](day-3/index.html#a-função-avg_over_time)
    - [A função sum_over_time](day-3/index.html#a-função-sum_over_time)
    - [A função max_over_time](day-3/index.html#a-função-max_over_time)
    - [A função min_over_time](day-3/index.html#a-função-min_over_time)
    - [A função stddev_over_time](day-3/index.html#a-função-stddev_over_time)
    - [A função by](day-3/index.html#a-função-by)
    - [A função without](day-3/index.html#a-função-without)
    - [A função histogram_quantile e quantile](day-3/index.html#a-função-histogram_quantile-e-quantile)
    - [Praticando e usando as funções](day-3/index.html#praticando-e-usando-as-funções)
    - [Operadores](day-3/index.html#operadores)
        - [Operador de igualdade](day-3/index.html#operador-de-igualdade)
        - [Operador de diferença](day-3/index.html#operador-de-diferença)
        - [Operador de maior que](day-3/index.html#operador-de-maior-que)
        - [Operador de menor que](day-3/index.html#operador-de-menor-que)
        - [Operador de maior ou igual que](day-3/index.html#operador-de-maior-ou-igual-que)
        - [Operador de menor ou igual que](day-3/index.html#operador-de-menor-ou-igual-que)
        - [Operador de multiplicação](day-3/index.html#operador-de-multiplicação)
        - [Operador de divisão](day-3/index.html#operador-de-divisão)
        - [Operador de adição](day-3/index.html#operador-de-adição)
        - [Operador de subtração](day-3/index.html#operador-de-subtração)
        - [Operador de modulo](day-3/index.html#operador-de-modulo)
        - [Operador de potenciação](day-3/index.html#operador-de-potenciação)
        - [Operador de agrupamento](day-3/index.html#operador-de-agrupamento)
        - [Operador de concatenação](day-3/index.html#operador-de-concatenação)
        - [Operador de comparação de strings](day-3/index.html#operador-de-comparação-de-strings)
        - [Chega de operadores por hoje](day-3/index.html#chega-de-operadores-por-hoje)
    - [O Node Exporter](day-3/index.html#o-node-exporter)
        - [Os Collectors](day-3/index.html#os-collectors)
        - [Instalação do Node Exporter no Linux](day-3/index.html#instalação-do-node-exporter-no-linux)
        - [Adicionando o Node Exporter no Prometheus](day-3/index.html#adicionando-o-node-exporter-no-prometheus)
        - [Habilitando novos collectors no Node Exporter](day-3/index.html#habilitando-novos-collectors-no-node-exporter)
    - [Algumas queries capturando métricas do Node Exporter](day-3/index.html#algumas-queries-capturando-métricas-do-node-exporter)
    - [O Grafana](day-3/index.html#o-grafana)
    - [Instalação do Grafana](day-3/index.html#instalação-do-grafana)
    - [Adicionando o Prometheus como Data Source](day-3/index.html#adicionando-o-prometheus-como-data-source)
    - [Criando o nosso primeiro Dashboard](day-3/index.html#criando-o-nosso-primeiro-dashboard)
    - [Chega por hoje!](day-3/index.html#chega-por-hoje)
    - [Lição de casa](day-3/index.html#lição-de-casa)
    - [Referências](day-3/index.html#referências)

- **[DAY-4](day-4/index.html) - Em revisão...**
    - [O que iremos ver hoje?](day-4/index.html#o-que-iremos-ver-hoje)
    - [Conteúdo do Day-4](day-4/index.html#conteúdo-do-day-4)
    - [O Grafana](day-4/index.html#o-grafana)
    - [Instalando o Grafana](day-4/index.html#instalando-o-grafana)
    - [Adicionando o Prometheus como Data Source](day-4/index.html#adicionando-o-prometheus-como-data-source)
    - [Criando o nosso primeiro Dashboard](day-4/index.html#criando-o-nosso-primeiro-dashboard)
    - [Alertmanager](day-4/index.html#alertmanager)
    - [Instalando o Alertmanager](day-4/index.html#instalando-o-alertmanager)

- **[DAY-5](day-5/index.html) - Em revisão...**

- **[DAY-6](day-6/index.html) - Em revisão...**
    - [O que iremos ver hoje](day-6/index.html#o-que-iremos-ver-hoje)
    - [Conteúdo do Day-6](day-6/index.html#conteúdo-do-day-6)
    - [O que é o kube-prometheus](day-6/index.html#o-que-é-o-kube-prometheus)
    - [Instalando o nosso cluster Kubernetes](day-6/index.html#instalando-o-nosso-cluster-kubernetes)
    - [Instalando o Kube-Prometheus](day-6/index.html#instalando-o-kube-prometheus)
    - [Acessando o Grafana](day-6/index.html#acessando-o-grafana)
    - [Acessando o Prometheus](day-6/index.html#acessando-o-prometheus)
    - [Acessando o AlertManager](day-6/index.html#acessando-o-alertmanager)
    - [Chega por hoje!](day-6/index.html#chega-por-hoje)
    - [Lição de casa](day-6/index.html#lição-de-casa)

- **[DAY-7](day-7/index.html) - Em revisão...**
    - [O que iremos ver hoje?](day-7/index.html#o-que-iremos-ver-hoje)
    - [Conteúdo do Day-7](day-7/index.html#conteúdo-do-day-7)
    - [Os ServiceMonitors](day-7/index.html#os-servicemonitors)
    - [Criando um ServiceMonitor](day-7/index.html#criando-um-servicemonitor)
    - [Os PodMonitors](day-7/index.html#os-podmonitors)
    - [Criando um PodMonitor](day-7/index.html#criando-um-podmonitor)
    - [Criando nosso primeiro alerta](day-7/index.html#criando-nosso-primeiro-alerta)
    - [O que é um PrometheusRule?](day-7/index.html#o-que-é-um-prometheusrule)
        - [Criando um PrometheusRule](day-7/index.html#criando-um-prometheusrule)
    - [Chega por hoje!](day-7/index.html#chega-por-hoje)
    - [Lição de casa](day-7/index.html#lição-de-casa)

- **[DAY-8](day-8/index.html) - Em revisão...**
    - [O que iremos ver hoje?](day-8/index.html#o-que-iremos-ver-hoje)
    - [Conteúdo do Day-8](day-8/index.html#conteúdo-do-day-8)
    - [Vamos brincar com as métricas do Kubernetes](day-8/index.html#vamos-brincar-com-as-métricas-do-kubernetes)
        - [O que podemos saber sobre os nodes do nosso cluster?](day-8/index.html#o-que-podemos-saber-sobre-os-nodes-do-nosso-cluster)
        - [Quantos nós temos no nosso cluster?](day-8/index.html#quantos-nós-temos-no-nosso-cluster)
        - [Qual a quantidade de CPU e memória que cada nó tem?](day-8/index.html#qual-a-quantidade-de-cpu-e-memória-que-cada-nó-tem)
        - [O nó está disponível para receber novos pods?](day-8/index.html#o-nó-está-disponível-para-receber-novos-pods)
        - [Qual a quantidade de informação que cada nó está recebendo e enviando?](day-8/index.html#qual-a-quantidade-de-informação-que-cada-nó-está-recebendo-e-enviando)
        - [Quantos pods estão rodando em cada nó?](day-8/index.html#quantos-pods-estão-rodando-em-cada-nó)
    - [Agora vamos saber se o nosso cluster está com problemas](day-8/index.html#agora-vamos-saber-se-o-nosso-cluster-está-com-problemas)
        - [O que podemos saber sobre os pods do nosso cluster?](day-8/index.html#o-que-podemos-saber-sobre-os-pods-do-nosso-cluster)
        - [Quantos pods estão rodando no nosso cluster?](day-8/index.html#quantos-pods-estão-rodando-no-nosso-cluster)
        - [Quantos pods estão com problemas?](day-8/index.html#quantos-pods-estão-com-problemas)
        - [Verificar os pods e os limites de memória e CPU configurados](day-8/index.html#verificar-os-pods-e-os-limites-de-memória-e-cpu-configurados)
        - [Verificar se o cluster está com problemas relacionados ao disco](day-8/index.html#verificar-se-o-cluster-está-com-problemas-relacionados-ao-disco)
        - [Verificar se o cluster está com problemas relacionados a memória](day-8/index.html#verificar-se-o-cluster-está-com-problemas-relacionados-a-memória)
    - [E como saber se meus deployments estão com problemas?](day-8/index.html#e-como-saber-se-meus-deployments-estão-com-problemas)
        - [Quantos deployments estão rodando no meu cluster?](day-8/index.html#quantos-deployments-estão-rodando-no-meu-cluster)
        - [Quantos deployments estão com problemas?](day-8/index.html#quantos-deployments-estão-com-problemas)
        - [Qual o status dos meus deployments?](day-8/index.html#qual-o-status-dos-meus-deployments)
    - [E como saber se meus serviços estão com problemas?](day-8/index.html#e-como-saber-se-meus-serviços-estão-com-problemas)
        - [Quantos serviços estão rodando no meu cluster?](day-8/index.html#quantos-serviços-estão-rodando-no-meu-cluster)
        - [Todos os meus serviços estão com endpoints?](day-8/index.html#todos-os-meus-serviços-estão-com-endpoints)
        - [Todos os meus serviços estão com endpoints ativos?](day-8/index.html#todos-os-meus-serviços-estão-com-endpoints-ativos)
    - [Como eu posso modificar as configurações do meu Prometheus?](day-8/index.html#como-eu-posso-modificar-as-configurações-do-meu-prometheus)
        - [Definindo o nosso Prometheus](day-8/index.html#definindo-o-nosso-prometheus)
        - [Definindo o nosso Alertmanager](day-8/index.html#definindo-o-nosso-alertmanager)

- **[DAY-9](day-9/index.html) - Em revisão...**
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

</details>


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

