Edge computing avec Kubernetes : architectures et outils
########################################################

:lang: fr
:date: 2024-08-14
:modified: 2026-11-07
:slug: edge-computing-avec-kubernetes
:category: Kubernetes
:tags: kubernetes, edge computing, edge, kubeedge, open horizon, iot, architecture, infrastructure
:authors: Florian Grignon
:seo_title: Edge computing avec Kubernetes : architectures et outils
:description: Edge computing et Kubernetes : réduire la latence, gérer des sites distribués et choisir son architecture (multi-cluster, nœuds distants, KubeEdge).
:summary: Kubernetes est un outil puissant pour orchestrer des environnements décentralisés, où les ressources sont dispersées géographiquement et où la latence, la bande passante et la résilience sont critiques. Tour d'horizon des architectures possibles.
:logo: logo-edge.webp

Comment Kubernetes peut-il orchestrer des ressources dispersées au plus près des
utilisateurs ? Voici ce qu'il faut savoir sur l'edge computing et sur les architectures
possibles avec Kubernetes.

Qu'est-ce que l'edge computing ?
================================

L'edge computing, ou informatique en périphérie, est une approche décentralisée du
traitement des données : le calcul et le stockage sont effectués au plus près de la source
de production des données, plutôt que dans un centre de données centralisé. Cette
architecture permet de réduire la latence, d'améliorer la réactivité des applications et de
gérer les données plus efficacement en local, avant de les transférer éventuellement vers un
cloud centralisé pour un traitement approfondi ou un stockage à long terme.

En rapprochant la puissance de calcul des utilisateurs finaux, l'edge computing est
particulièrement adapté aux environnements qui nécessitent une prise de décision en temps
réel, comme l'Internet des objets (IoT), les véhicules autonomes ou les systèmes industriels
intelligents.

Réduire la latence en traitant les données localement
=====================================================

Netflix a été l'une des premières entreprises à installer des points de présence chez les
fournisseurs d'accès à Internet (FAI), avec son réseau
`Open Connect <https://openconnect.netflix.com/>`__ : les films et séries sont stockés au
plus près des utilisateurs, ce qui garantit une lecture optimale partout dans le monde.

Sans aller jusqu'à déployer des points de présence chez les FAI, ce qui n'est pas à la
portée de toutes les entreprises, une architecture edge peut être réalisée sur plusieurs
zones géographiques au sein de votre fournisseur d'infrastructure.

.. pull-quote::

   L'un des principaux avantages de l'edge computing réside dans sa capacité à réduire la
   latence en traitant les données localement.

Dans des secteurs tels que l'IoT, les véhicules autonomes ou les réseaux de capteurs
industriels, la rapidité de traitement est essentielle. En utilisant Kubernetes pour
orchestrer ces environnements, les entreprises peuvent déployer des microservices et des
applications conteneurisées directement en périphérie du réseau. Cette approche réduit les
temps de réponse et optimise l'utilisation de la bande passante, en évitant l'envoi de
volumes massifs de données vers des centres de données centraux.

Pourquoi Kubernetes est adapté à l'edge computing
=================================================

Kubernetes se révèle être un outil puissant pour orchestrer et gérer ces environnements
décentralisés, où les ressources sont dispersées géographiquement et où les exigences en
matière de latence, de bande passante et de résilience sont particulièrement critiques.

Il offre d'abord une grande **flexibilité** pour déployer et gérer des applications sur les
infrastructures hétérogènes typiques de l'edge. Que les ressources disponibles se trouvent
sur des serveurs locaux, des dispositifs IoT ou de petits datacenters régionaux, Kubernetes
maintient une gestion et une orchestration homogènes des conteneurs. Cette standardisation
facilite la scalabilité horizontale, essentielle dans un contexte où la capacité de réponse
doit s'adapter rapidement aux fluctuations de la demande.

Kubernetes renforce aussi la **résilience** des infrastructures edge en assurant une gestion
autonome des défaillances. En déployant des applications sur plusieurs nœuds en périphérie,
il garantit la continuité des services, même en cas de panne de l'un des nœuds. Cette
tolérance aux pannes est cruciale pour les applications critiques qui ne peuvent se
permettre aucun temps d'arrêt, comme la gestion des urgences ou les opérations
industrielles.

Quatre approches pour faire de l'edge computing avec Kubernetes
===============================================================

L'implémentation de l'edge computing avec Kubernetes peut prendre plusieurs formes, selon
les besoins de l'entreprise et l'architecture sous-jacente.

Des clusters Kubernetes en périphérie
-------------------------------------

La manière la plus directe consiste à déployer des points de présence sous forme de
clusters Kubernetes en périphérie, répartis sur différents sites, chacun autonome mais
interconnecté. Cette configuration est idéale lorsque chaque site a des exigences
spécifiques en matière de traitement des données, mais qu'une certaine coordination entre
les sites reste nécessaire. Les outils présentés dans notre article sur le
`multi-cluster Kubernetes <{filename}multi-cluster.rst>`__ s'appliquent alors directement.

Étendre un cluster avec des nœuds distants
------------------------------------------

Une autre approche consiste à étendre un cluster Kubernetes centralisé vers les périphéries
du réseau, en utilisant des nœuds distants pour exécuter les charges de travail propres à
l'edge. La répartition des charges de travail selon des règles métier est déjà
`implémentée et documentée dans Kubernetes
<https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/>`__. Cette méthode
permet de centraliser la gestion tout en déployant des services là où ils sont le plus
nécessaires.

Fédérer plusieurs clusters
--------------------------

La fédération de clusters est un cas particulier de gestion de plusieurs clusters :
Kubernetes permet de gérer plusieurs clusters distribués comme une seule entité cohérente.
Cette approche est particulièrement efficace pour orchestrer des déploiements
multi-régionaux, où les applications doivent être disponibles et réactives dans plusieurs
emplacements géographiques.

Des plateformes edge clés en main : KubeEdge et Open Horizon
------------------------------------------------------------

.. image:: /images/logo-kubeedge-240.webp
   :alt: Logo du projet KubeEdge
   :width: 240
   :height: 240
   :align: right

De nombreuses entreprises intègrent Kubernetes avec des plateformes edge spécialisées
telles que `KubeEdge <https://kubeedge.io/>`__ ou
`Open Horizon <https://lfedge.org/projects/open-horizon/>`__, conçues pour faciliter le
déploiement et la gestion des applications sur des infrastructures distribuées. Ces
plateformes ajoutent des fonctionnalités spécifiques aux contraintes de l'edge, comme la
gestion d'une connectivité réseau intermittente ou l'intégration avec des dispositifs IoT.

Si vous disposez des ressources en interne, il est également possible de développer votre
propre solution edge à partir de Kubernetes. Mais à ce stade, vous faites sans doute déjà
partie des experts de Kubernetes !

Conclusion
==========

L'edge computing avec Kubernetes ouvre la voie à des architectures plus réactives,
résilientes et flexibles, qui répondent aux exigences croissantes des entreprises en
matière de traitement des données en temps réel. Kubernetes permet non seulement de tirer
parti des avantages de l'edge computing, mais aussi de standardiser la gestion des
ressources à travers des infrastructures dispersées, tout en maintenant une cohérence
opérationnelle à l'échelle mondiale.
