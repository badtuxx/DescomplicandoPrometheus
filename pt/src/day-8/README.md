# Descomplicando o Prometheus

## DAY-8

### O que iremos ver hoje?


Durante o dia de hoje, nós iremos passear um pouco pelas métricas que estamos coletando do nosso cluster Kubernetes. A ideia hoje é brincar um pouco mais com PromQL para extrair o máximo de valor das métricas que estamos coletando.

Quando estamos utilizando o Kube-Prometheus, temos que saber que já temos dezenas de novas métricas que nos mostram detalhes do comportamento do nosso cluster.

Outro ponto importante do dia de hoje será conhecer um pouco mais no detalhe, onde e como podemos mudar as características do nosso Prometheus e do nosso AlertManager.

Quando instalamos o Kube-Prometheus, e por consequência o Prometheus Operator, nós estamos expandindo o Kubernetes, dando maiores poderes e funções que antes ele não tinha. Entre os novos poderes que o Kubernetes agora possui estão os recursos que já vimos, como o PodMonitor, ServiceMonitor e o PrometheusRule.

Hoje ainda iremos conhecer mais dois recursos que o Prometheus Operator nos dá, um recurso chamado Prometheus e outro chamado AlertManager. Mas não vou dar detalhes agora, somente durante o dia de hoje.


### Conteúdo do Day-8

<details>
<summary class="summary">DAY-8</summary>

- [Descomplicando o Prometheus](#descomplicando-o-prometheus)
  - [DAY-8](#day-8)
    - [O que iremos ver hoje?](#o-que-iremos-ver-hoje)
    - [Conteúdo do Day-8](#conteúdo-do-day-8)
      - [Vamos brincar com as métricas do Kubernetes](#vamos-brincar-com-as-métricas-do-kubernetes)
        - [O que podemos saber sobre os nodes do nosso cluster?](#o-que-podemos-saber-sobre-os-nodes-do-nosso-cluster)
          - [Quantos nós temos no nosso cluster?](#quantos-nós-temos-no-nosso-cluster)
          - [Qual a quantidade de CPU e memória que cada nó tem?](#qual-a-quantidade-de-cpu-e-memória-que-cada-nó-tem)
          - [O nó está disponível para receber novos pods?](#o-nó-está-disponível-para-receber-novos-pods)
          - [Qual a quantidade de informação que cada nó está recebendo e enviando?](#qual-a-quantidade-de-informação-que-cada-nó-está-recebendo-e-enviando)
        - [Quantos pods estão rodando em cada nó?](#quantos-pods-estão-rodando-em-cada-nó)
      - [Agora vamos saber se o nosso cluster está com problemas](#agora-vamos-saber-se-o-nosso-cluster-está-com-problemas)
        - [O que podemos saber sobre os pods do nosso cluster?](#o-que-podemos-saber-sobre-os-pods-do-nosso-cluster)
          - [Quantos pods estão rodando no nosso cluster?](#quantos-pods-estão-rodando-no-nosso-cluster)
          - [Quantos pods estão com problemas?](#quantos-pods-estão-com-problemas)
          - [Verificar os pods e os limites de memória e CPU configurados](#verificar-os-pods-e-os-limites-de-memória-e-cpu-configurados)
          - [Verificar se o cluster está com problemas relacionados ao disco](#verificar-se-o-cluster-está-com-problemas-relacionados-ao-disco)
          - [Verificar se o cluster está com problemas relacionados a memória](#verificar-se-o-cluster-está-com-problemas-relacionados-a-memória)
      - [E como saber se meus deployments estão com problemas?](#e-como-saber-se-meus-deployments-estão-com-problemas)
          - [Quantos deployments estão rodando no meu cluster?](#quantos-deployments-estão-rodando-no-meu-cluster)
          - [Quantos deployments estão com problemas?](#quantos-deployments-estão-com-problemas)
          - [Qual o status dos meus deployments?](#qual-o-status-dos-meus-deployments)
      - [E como saber se meus serviços estão com problemas?](#e-como-saber-se-meus-serviços-estão-com-problemas)
          - [Quantos serviços estão rodando no meu cluster?](#quantos-serviços-estão-rodando-no-meu-cluster)
          - [Todos os meus serviços estão com endpoints?](#todos-os-meus-serviços-estão-com-endpoints)
          - [Todos os meus serviços estão com endpoints ativos?](#todos-os-meus-serviços-estão-com-endpoints-ativos)
      - [Como eu posso modificar as configurações do meu Prometheus?](#como-eu-posso-modificar-as-configurações-do-meu-prometheus)
        - [Definindo o nosso Prometheus](#definindo-o-nosso-prometheus)
        - [Definindo o nosso Alertmanager](#definindo-o-nosso-alertmanager)

</details>

#### Vamos brincar com as métricas do Kubernetes

Muito bem, chegamos naquele momento que não precisaremos instalar mais nada, pelo menos por agora, pois já temos o nosso cluster Kubernetes com o Kube-Prometheus instalado.

O que vamos fazer agora é usufruir de todo o conhecimento já adquirido e também por todo o trabalho que já fizemos até esse momento.

Então agora é a hora de começar a brincar com as métricas e assim extrair informações sobre a saúde e performance do nosso cluster Kubernetes.

##### O que podemos saber sobre os nodes do nosso cluster?

Algumas métricas que podemos extrair sobre os nodes do nosso cluster são:

* Quantos nós temos no nosso cluster?
* Qual a quantidade de CPU e memória que cada nó tem?
* O nó está disponível para receber novos pods?
* Qual a quantidade de informação que cada nó está recebendo e enviando?
* Quantos pods estão rodando em cada nó?

Vamos responder essas quatro perguntas utilizando o PromQL e as métricas que estamos coletando do nosso cluster Kubernetes.

###### Quantos nós temos no nosso cluster?

Para responder essa pergunta, vamos utilizar a métrica `kube_node_info` que nos mostra informações sobre os nós do nosso cluster. Podemos utilizar a função `count` para contar quantas vezes a métrica `kube_node_info` aparece no nosso cluster.

```promql
count(kube_node_info)
```

No nosso cluster, temos 2  nós, então a resposta para essa pergunta é 2.

###### Qual a quantidade de CPU e memória que cada nó tem?

Para responder essa pergunta, vamos utilizar a métrica `kube_node_status_allocatable` que nos mostra a quantidade de CPU e memória que cada nó tem disponível para ser utilizado.

```promql
kube_node_status_allocatable
```

Aqui ele vai te trazer todas as informações sobre CPU, memória, pods, etc. Mas nós só queremos saber sobre CPU e memória, então vamos filtrar a nossa consulta para trazer apenas essas informações.

```promql
kube_node_status_allocatable{resource="cpu"}
kube_node_status_allocatable{resource="memory"}
```

Fácil, agora precisamos somente de um pouco de matemática para converter os valores referente a memória para gigabytes.

```promql
kube_node_status_allocatable{resource="memory"} / 1024 / 1024 / 1024
```

Pronto, agora ficou um pouco mais fácil de ler a quantidade de memória que temos em cada nó.

###### O nó está disponível para receber novos pods?

Para responder essa pergunta, vamos utilizar a métrica `kube_node_status_condition` que nos mostra o status de cada nó do nosso cluster.

```promql
kube_node_status_condition{condition="Ready", status="true"}
```

Com a consulta acima, estamos perguntando para métrica `kube_node_status_condition` se o nó está pronto para receber novos pods. Se o nó estiver pronto, ele vai retornar o valor 1, caso contrário, ele vai retornar o valor 0.

Isso porque estamos perguntando para a métrica `kube_node_status_condition` se o nó está com a condição `Ready` e se o status dessa condição é `true`, se mudassemos o status para `false`, ele iria retornar o valor 0. Simplão demais!

###### Qual a quantidade de informação que cada nó está recebendo e enviando?

Aqui vamos levar em consideração que estamos falando de trafego de rede, o quanto o nosso nó está recebendo e enviando de dados pela rede.

Para isso vamos utilizar a métrica `node_network_receive_bytes_total` e `node_network_transmit_bytes_total` que nos mostra a quantidade de bytes que o nó está recebendo e enviando.

```promql
node_network_receive_bytes_total
node_network_transmit_bytes_total
```

Perceba que a saída dessa consulta ela traz a quantidade de bytes por pod, mas nós queremos saber a quantidade de bytes por nó, então vamos utilizar a função `sum` para somar a quantidade de bytes que cada pod está recebendo e enviando.

```promql
sum by (instance) (node_network_receive_bytes_total)
sum by (instance) (node_network_transmit_bytes_total)
```

Pronto, dessa forma teriamos a quantidade de bytes que cada nó está recebendo e enviando. No meu caso, como somente tenho dois nodes, o resultado foram duas linhas, uma para cada nó, mostrando a quantidade de bytes que cada nó está recebendo e enviando.

Agora vamos converter esses bytes para megabytes, para ficar mais fácil de ler.

```promql
sum by (instance) (node_network_receive_bytes_total) / 1024 / 1024
sum by (instance) (node_network_transmit_bytes_total) / 1024 / 1024
```

Vamos para a próxima pergunta.

##### Quantos pods estão rodando em cada nó?

Para responder essa pergunta, vamos utilizar a métrica `kube_pod_info` que nos mostra informações sobre os pods que estão rodando no nosso cluster.

```promql
kube_pod_info
```

Caso eu queria saber o número de pods que estão rodando em cada nó, eu poderia utilizar a função `count` para contar quantas vezes a métrica `kube_pod_info` aparece em cada nó.

```promql
count by (node) (kube_pod_info)
```

Pronto, agora eu sei quantos pods estão rodando em cada nó. No meu caso o meu cluster está bem sussa, somente 9 pods em um nó e 10 no outro, um dia de alegriaaaaa!


#### Agora vamos saber se o nosso cluster está com problemas

Agora que já sabemos como extrair informações sobre a saúde e performance do nosso cluster Kubernetes, vamos aprender como podemos ser notificados caso o nosso cluster esteja com algum problema.

##### O que podemos saber sobre os pods do nosso cluster?

Algumas métricas que podemos extrair sobre os pods do nosso cluster são:

* Quantos pods estão rodando no nosso cluster?
* Quantos pods estão com problemas?
* Verificar os pods e os limites de memória e CPU configurados
* Verificar se o cluster está com problemas de espaço em disco
* Verificar se o cluster está com problemas de consumo de memória


###### Quantos pods estão rodando no nosso cluster?

Essa é fácil e já sabemos qual a métrica que vai nos ajudar a responder essa pergunta.

```promql
count(kube_pod_info)
```

Simples assim.

###### Quantos pods estão com problemas?

Para responder essa pergunta, vamos utilizar a métrica `kube_pod_status_phase` que nos mostra o status de cada pod do nosso cluster.

```promql
kube_pod_status_phase
```

Essa métrica irá nos mostrar o status de cada pod, se o pod está rodando, se ele está em erro, se ele está em execução, etc. Mas nós só queremos saber se o pod está em erro, então vamos filtrar a nossa consulta para trazer apenas os pods que estão em erro.

```promql
kube_pod_status_phase{phase="Failed"}
```

E se eu quiser saber o número de pods que estão em erro?

```promql
count(kube_pod_status_phase{phase="Failed"})
```

Vamos melhorar, eu quero saber o número de pods que estão em erro por namespace.

```promql
count by (namespace) (kube_pod_status_phase{phase="Failed"})
```

Ou ainda por nó.

```promql
count by (node) (kube_pod_status_phase{phase="Failed"})
```

Simples assim.

Os status que podemos utilizar são:
* `Pending`: Pod está aguardando para ser executado
* `Running`: Pod está sendo executado
* `Succeeded`: Pod foi executado com sucesso
* `Unknown`: Pod está em um estado desconhecido
* `Failed`: Pod foi executado e falhou

Agora é só escolher o que você quer saber e sair testando.

###### Verificar os pods e os limites de memória e CPU configurados

Para responder essa pergunta, vamos utilizar a métrica `kube_pod_container_resource_limits` que nos mostra os limites de memória e CPU que cada pod está utilizando.

```promql
kube_pod_container_resource_limits
```

Agora vamos filtrar a nossa consulta para trazer apenas os pods e os limites de memória e CPU configurados.

```promql
kube_pod_container_resource_limits{resource="memory"}
kube_pod_container_resource_limits{resource="cpu"}
```

Assim você consegue saber quais os limites de memória e CPU que cada pod está utilizando.

###### Verificar se o cluster está com problemas relacionados ao disco

Tem um status de node que é o `DiskPressure`, que significa que o nó está com problemas relacionados ao disco. Para saber se o nó está com esse status, vamos utilizar a métrica `kube_node_status_condition` que nos mostra o status de cada nó.

```promql
kube_node_status_condition{condition="DiskPressure", status="true"}
```

Se o valor retornado for 1, significa que o nó está com problemas relacionados ao disco, agora, se o valor for 0, significa que o nó está ok e você não precisa se preocupar.

###### Verificar se o cluster está com problemas relacionados a memória

Tem um status de node que é o `MemoryPressure`, que significa que o nó está com problemas relacionados a memória. Para saber se o nó está com esse status, vamos utilizar a métrica `kube_node_status_condition` que nos mostra o status de cada nó.

```promql
kube_node_status_condition{condition="MemoryPressure", status="true"}
```

Se o valor retornado for 1, se prepare, pois você vai precisar entender o que está pegando com o seu nó, ou seja, terá um dia de trabalho pela frente. :D

#### E como saber se meus deployments estão com problemas?

Algumas perguntas que podemos responder sobre os deployments do nosso cluster são:

* Quantos deployments estão rodando no meu cluster?
* Quantos deployments estão com problemas?
* Qual o status dos meus deployments?


###### Quantos deployments estão rodando no meu cluster?

Para responder essa pergunta, vamos utilizar a métrica `kube_deployment_status_replicas` que nos mostra o número de replicas que cada deployment está rodando.

```promql
kube_deployment_status_replicas
```

Assim ele traz a lista de todos os deployments e o número de replicas que cada um está rodando.

###### Quantos deployments estão com problemas?

Para responder essa pergunta, vamos utilizar a métrica `kube_deployment_status_replicas_unavailable` que nos mostra o número de replicas indisponíveis que cada deployment está rodando.

```promql
kube_deployment_status_replicas_unavailable
```

Se tudo estiver bem, o valor retornado será 0, caso contrário, o valor retornado será o número de replicas indisponíveis.

###### Qual o status dos meus deployments?

Para responder essa pergunta, vamos utilizar a métrica `kube_deployment_status_condition` que nos mostra o status de cada deployment.

```promql
kube_deployment_status_condition
```

Com a consulta acima, você consegue saber o status de cada deployment, se ele está ok, se ele está com problemas, etc.

Se quisermos saber a lista de deployments com problemas, podemos utilizar a seguinte consulta.

```promql
kube_deployment_status_condition{condition="Available", status="false"}
```

Assim, se o valor retornado for 1, significa que o deployment está com problemas, caso contrário, significa que o deployment está ok.

#### E como saber se meus serviços estão com problemas?

Algumas perguntas que podemos responder sobre os serviços do nosso cluster são:

* Quantos serviços estão rodando no meu cluster?
* Todos os meus serviços estão com endpoints?
* Todos os meus serviços estão com endpoints ativos?

Vamos responder cada uma delas.

###### Quantos serviços estão rodando no meu cluster?

Para responder essa pergunta, vamos utilizar a métrica `kube_service_info` que nos mostra o número de serviços que estão rodando no nosso cluster.

```promql
kube_service_info
```

Assim ele traz a lista de todos os serviços que estão rodando no nosso cluster, com o valor 1.

###### Todos os meus serviços estão com endpoints?

Para responder essa pergunta, vamos utilizar a métrica `kube_endpoint_address` que nos traz a lista de endpoints de cada serviço.

```promql
kube_endpoint_address
```

Agora para saber os endpoints para um determinado serviço, vamos utilizar a seguinte consulta.

```promql
kube_endpoint_address{endpoint="kube-dns"}
```

###### Todos os meus serviços estão com endpoints ativos?

Podemos ainda buscar por endpoints com o status `ready` igual a `false`, o que significa que o endpoint não está ativo.

```promql
kube_endpoint_address{ready="false"}
```

Se a lista for vazia, significa que todos os endpoints estão ativos!


Acho que já deu para brincar um pouco sobre as nossas métricas que estão vindo do Kubernetes! :D

Vamos brincar com algo novo agora!


#### Como eu posso modificar as configurações do meu Prometheus?

Quando fizemos a instalação do nosso kube-prometheus, nós criamos alguns Custom Resource Definitions (CRDs) em nosso cluster. Nós já vimos alguns deles como o `ServiceMonitor` e o `PrometheusRule`, porém o nosso foco agora será em dois outros CRDs que são o `Prometheus` e o `Alertmanager`.

O `Prometheus` é o nosso recurso que vai nos permitir configurar o Prometheus que está rodando em nosso cluster. Já o `Alertmanager` é o nosso recurso que vai nos permitir configurar o Alertmanager.

Vamos focar nessa primeira parte no `Prometheus`.

##### Definindo o nosso Prometheus

Como eu disse, o recurso `Prometheus` é o nosso recurso que vai nos permitir configurar o Prometheus, e assim customiza-lo para as nossas necessidades.

Esse arquivo é o arquivo que vem por padrão quando instalamos o kube-prometheus, ele fica dentro do diretório `manifests/` do nosso repositório do kube-prometheus e ele se chama `prometheus-prometheus.yaml`.


```yaml
apiVersion: monitoring.coreos.com/v1 # Versão da API
kind: Prometheus # Tipo do recurso, no caso, Prometheus
metadata: # Informações sobre o recurso
  labels: # Labels que serão adicionadas ao nosso Prometheus
    app.kubernetes.io/component: prometheus # Label que indica que o recurso é um Prometheus
    app.kubernetes.io/instance: k8s # Label que indica que o recurso é o Prometheus do nosso cluster
    app.kubernetes.io/name: prometheus # Label que indica que o recurso é um Prometheus
    app.kubernetes.io/part-of: kube-prometheus # Label que indica que o recurso é parte do kube-prometheus
    app.kubernetes.io/version: 2.42.0 # Label que indica a versão do Prometheus
  name: k8s # Nome do nosso Prometheus
  namespace: monitoring # Namespace onde o Prometheus vai ser criado
spec: # Especificações do nosso Prometheus
  alerting: # Configurações de alerta 
    alertmanagers: # Lista de alertmanagers que o Prometheus vai utilizar
    - apiVersion: v2 # Versão da API do Alertmanager
      name: alertmanager-main # Nome do Alertmanager
      namespace: monitoring # Namespace onde o Alertmanager está rodando
      port: web # Porta que o Alertmanager está rodando
  enableFeatures: [] # Lista de features que serão habilitadas no Prometheus, no caso, nenhuma
  externalLabels: {} # Labels que serão adicionadas a todas as métricas que o Prometheus coletar
  image: quay.io/prometheus/prometheus:v2.42.0 # Imagem do Prometheus
  nodeSelector: # Node selector que será utilizado para definir em qual node o Prometheus vai rodar
    kubernetes.io/os: linux # Node selector que indica que o Prometheus vai rodar em nodes com o sistema operacional Linux
  podMetadata: # Metadata que será adicionada aos pods do Prometheus
    labels: # Labels que serão adicionadas aos pods do Prometheus
      app.kubernetes.io/component: prometheus # Label que indica que o pod é um Prometheus
      app.kubernetes.io/instance: k8s # Label que indica que o pod é o Prometheus do nosso cluster
      app.kubernetes.io/name: prometheus # Label que indica que o pod é um Prometheus
      app.kubernetes.io/part-of: kube-prometheus # Label que indica que o pod é parte do kube-prometheus
      app.kubernetes.io/version: 2.42.0 # Label que indica a versão do Prometheus
  podMonitorNamespaceSelector: {} # Namespace selector que será utilizado para selecionar os pods que serão monitorados pelo Prometheus
  podMonitorSelector: {} # Selector que será utilizado para selecionar os pods que serão monitorados pelo Prometheus
  probeNamespaceSelector: {} # Namespace selector que será utilizado para selecionar os pods que serão monitorados pelo Prometheus
  probeSelector: {} # Selector que será utilizado para selecionar os pods que serão monitorados pelo Prometheus
  replicas: 2 # Número de réplicas que o Prometheus vai ter
  resources: # Recursos que serão utilizados pelo Prometheus
    requests: # Recursos mínimos que serão utilizados pelo Prometheus
      memory: 400Mi # Memória mínima que será utilizada pelo Prometheus
  ruleNamespaceSelector: {} # Namespace selector que será utilizado para selecionar as regras que serão utilizadas pelo Prometheus
  ruleSelector: {} # Selector que será utilizado para selecionar as regras que serão utilizadas pelo Prometheus
  securityContext: # Security context que será utilizado pelo Prometheus
    fsGroup: 2000 # ID do grupo que será utilizado pelo Prometheus
    runAsNonRoot: true # Indica que o Prometheus vai rodar como um usuário não root
    runAsUser: 1000 # ID do usuário que será utilizado pelo Prometheus
  serviceAccountName: prometheus-k8s # Nome da service account que será utilizada pelo Prometheus
  serviceMonitorNamespaceSelector: {} # Namespace selector que será utilizado para selecionar os serviços que serão monitorados pelo Prometheus
  serviceMonitorSelector: {} # Selector que será utilizado para selecionar os serviços que serão monitorados pelo Prometheus
  version: 2.42.0 # Versão do Prometheus
```

Esse arquivo é o arquivo que vem por padrão quando instalamos o kube-prometheus, ele fica dentro do diretório `manifests/` do nosso repositório do kube-prometheus.

No arquivo acima, eu já adicionei comentários para explicar o que cada parte do arquivo faz, espero que tenha ajudado no entendimento.

Caso você queira fazer alguma alteração no Prometheus que já está rodando, basta alterar esse arquivo e aplicar as alterações no cluster.

Vamos imaginar que você queira adicionar limites de utilização de memória e CPU no Prometheus, para isso, basta adicionar as seguintes linhas no arquivo.

```yaml
  resources: # Recursos que serão utilizados pelo Prometheus
    requests: # Recursos mínimos que serão utilizados pelo Prometheus
      memory: 400Mi # Memória mínima que será utilizada pelo Prometheus
      cpu: 500m # CPU mínima que será utilizada pelo Prometheus
    limits: # Recursos máximos que serão utilizados pelo Prometheus
      memory: 1Gi # Memória máxima que será utilizada pelo Prometheus
      cpu: 900m # CPU máxima que será utilizada pelo Prometheus
```

Preste atenção para adicionar esse conteúdo dentro do bloco `spec:` e com a mesma indentação.

Agora, vamos aplicar as alterações no cluster.

```bash
$ kubectl apply -f prometheus.yaml
```

Agora, vamos verificar se o Prometheus foi atualizado.

```bash
$ kubectl get pods -n monitoring prometheus-k8s-0 -o yaml | grep -A 10 resources:
  resources:
    limits:
      cpu: 900m
      memory: 1Gi
    requests:
      cpu: 500m
      memory: 400Mi
```

Como podemos ver, o Prometheus foi atualizado com os novos recursos.

Tem diversas outras configurações que podemos fazer no Prometheus, como por exemplo, adicionar regras para alertas, selectors para selecionar os pods que serão monitorados, etc.

Mas eu sugiro que você comece a testar e achar a melhor configuração para a sua necessidade. Mas lembre-se sempre, você precisa testar, você precisa explorar, você precisa aprender! Bora pra cima! 

##### Definindo o nosso Alertmanager

Da mesma forma como fizemos com o Prometheus, vamos conhecer o arquivo responsável por definir o nosso Alertmanager.

O arquivo abaixo é o arquivo que vem por padrão quando instalamos o kube-prometheus, ele fica dentro do diretório `manifests/` do nosso repositório do kube-prometheus, o nome dele é `alertmanager-alertmanager.yaml`.

```yaml

```yaml
apiVersion: monitoring.coreos.com/v1 # Versão da API do Alertmanager
kind: Alertmanager # Tipo do objeto que estamos criando
metadata: # Metadata do objeto que estamos criando
  labels: # Labels que serão adicionadas ao objeto que estamos criando
    app.kubernetes.io/component: alert-router # Label que indica que o objeto é um Alertmanager
    app.kubernetes.io/instance: main # Label que indica que o objeto é o Alertmanager principal
    app.kubernetes.io/name: alertmanager # Label que indica que o objeto é um Alertmanager
    app.kubernetes.io/part-of: kube-prometheus # Label que indica que o objeto é parte do kube-prometheus
    app.kubernetes.io/version: 0.25.0 # Label que indica a versão do Alertmanager
  name: main # Nome do objeto que estamos criando
  namespace: monitoring # Namespace onde o objeto que estamos criando será criado
spec: # Especificações do objeto que estamos criando
  image: quay.io/prometheus/alertmanager:v0.25.0 # Imagem que será utilizada pelo Alertmanager
  nodeSelector: # Selector que será utilizado para selecionar os nós que o Alertmanager vai rodar
    kubernetes.io/os: linux # Selector que indica que o Alertmanager vai rodar em nós Linux
  podMetadata: # Metadata que será adicionada aos pods do Alertmanager
    labels: # Labels que serão adicionadas aos pods do Alertmanager
      app.kubernetes.io/component: alert-router # Label que indica que o pod é um Alertmanager
      app.kubernetes.io/instance: main # Label que indica que o pod é o Alertmanager principal
      app.kubernetes.io/name: alertmanager # Label que indica que o pod é um Alertmanager
      app.kubernetes.io/part-of: kube-prometheus # Label que indica que o pod é parte do kube-prometheus
      app.kubernetes.io/version: 0.25.0 # Label que indica a versão do Alertmanager
  replicas: 3 # Número de réplicas que o Alertmanager vai ter
  resources: # Recursos que serão utilizados pelo Alertmanager
    limits: # Recursos máximos que serão utilizados pelo Alertmanager
      cpu: 100m # CPU máxima que será utilizada pelo Alertmanager
      memory: 100Mi # Memória máxima que será utilizada pelo Alertmanager
    requests: # Recursos mínimos que serão utilizados pelo Alertmanager
      cpu: 4m # CPU mínima que será utilizada pelo Alertmanager
      memory: 100Mi # Memória mínima que será utilizada pelo Alertmanager
  securityContext: # Security context que será utilizado pelo Alertmanager
    fsGroup: 2000 # ID do grupo que será utilizado pelo Alertmanager
    runAsNonRoot: true # Indica que o Alertmanager vai rodar como um usuário não root
    runAsUser: 1000 # ID do usuário que será utilizado pelo Alertmanager
  serviceAccountName: alertmanager-main # Nome da service account que será utilizada pelo Alertmanager
  version: 0.25.0 # Versão do Alertmanager
```

Adicionei também comentários para explicar o que cada parte do arquivo faz, assim fica fácil de você entender o que está acontecendo.
Sempre lembrando, veja sempre a documentação oficial para entender melhor o que cada configuração faz e todas as opções que você tem.

Caso você queira fazer alguma alteração no Alertmanager que já está rodando, basta alterar esse arquivo e aplicar as alterações no cluster com o comando abaixo.

```bash
$ kubectl apply -f alertmanager-alertmanager.yaml
```

Pronto, seu Alertmanager foi atualizado com as novas configurações, caso você tenha feito alguma alteração. hahah :D









