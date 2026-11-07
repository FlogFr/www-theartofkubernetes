Multi-cluster Kubernetes : pourquoi et comment gérer plusieurs clusters
#######################################################################

:lang: fr
:date: 2024-09-15
:modified: 2026-11-07
:slug: multi-cluster-kubernetes
:category: Kubernetes
:tags: kubernetes, multi-cluster, multicluster, hub and spoke, kubestellar, liqo, submariner, architecture, k8s
:authors: Florian Grignon
:seo_title: Multi-cluster Kubernetes : architectures et outils
:description: Pourquoi passer au multi-cluster Kubernetes et avec quels outils : modèle Hub and Spoke du SIG Multicluster, KubeStellar, Liqo et Submariner.
:summary: Grâce à son architecture modulaire, flexible et extensible, Kubernetes permet de mettre en place une architecture multi-cluster pour répondre à des besoins spécifiques. Pourquoi multiplier les clusters, et avec quels outils les gérer ?
:logo: logo-multicluster.webp
:pdf: /assets/Article-Kubernetes-Multi-Cluster.pdf

Il est possible que vous ressentiez le besoin de disposer de plusieurs clusters
Kubernetes. Cela implique, ni plus ni moins, d'avoir plusieurs *control planes*, donc
plusieurs cerveaux.

Pourquoi utiliser plusieurs clusters Kubernetes ?
=================================================

Le besoin le plus répandu est **l'isolation des ressources par environnement**. Il est
essentiel de bien définir ce que chaque environnement inclut ou exclut. Les équipes
applicatives auront besoin, au minimum, d'un environnement de développement, d'un
environnement de test fonctionnel, d'un environnement de pré-production (*staging*) et,
bien entendu, d'un environnement de production pour livrer le produit aux clients. Il est
également envisageable d'ajouter un environnement d'intégration, qui permet de vérifier la
compatibilité entre les différentes applications et leurs dépendances, ou encore un
environnement de performance, conçu pour tester la robustesse du produit dans des
conditions identiques à celles de la production, sans impacter les autres environnements.

Un autre besoin réside dans **l'isolation des données par zone géographique**. Il serait,
par exemple, non conforme de faire communiquer la charge de travail d'un cluster en Europe
avec celle d'un cluster situé aux États-Unis. Pour répondre à ce besoin, vous pouvez
instancier un cluster par zone, qui agit comme un isolant des données. C'est aussi une
approche courante pour faire de l'`edge computing avec Kubernetes
<{filename}edge-computing.rst>`__.

Répartir les charges de travail avec KubeStellar
================================================

Maintenant que vous disposez de plusieurs clusters, vous souhaiterez probablement répartir
vos charges de travail de manière optimisée entre ces différents environnements. Un outil
particulièrement intéressant pour cela est `KubeStellar <https://kubestellar.io/>`__. Il
présente l'avantage de ne nécessiter aucune modification de l'architecture de vos clusters
Kubernetes existants, et permet de centraliser la gestion de l'ensemble des ressources de
vos clusters depuis un point unique.

Fédérer ses clusters : le modèle Hub and Spoke du SIG Multicluster
==================================================================

Vous envisagez peut-être aussi d'interconnecter vos clusters, notamment pour mutualiser
certains services de vos plateformes afin de réduire les coûts. Un
`Special Interest Group (SIG) nommé Multicluster <https://multicluster.sigs.k8s.io/>`__ se
penche sur cette problématique et propose des recommandations, des bonnes pratiques ainsi
qu'une ligne de conduite pour y répondre.

L'idée centrale consiste à fédérer plusieurs clusters Kubernetes afin de gérer les charges
de travail de manière centralisée via une API Kubernetes unique. Dans cette approche, un
cluster joue le rôle de « Hub » (cluster central) et communique avec des clusters dits
« Spoke » (clusters satellites). Ce modèle de distribution, connu sous le nom de
`Hub and Spoke <https://en.wikipedia.org/wiki/Spoke%E2%80%93hub_distribution_paradigm>`__,
est soutenu par plusieurs extensions de l'API Kubernetes :

- une CRD **Work** représente une charge de travail constituée de plusieurs manifestes,
  ainsi que le cluster Spoke cible sur lequel elle doit être déployée. Un contrôleur, appelé
  *Work Controller*, prend en charge le déploiement de cette charge sur le cluster désigné ;
- les CRD **ServiceExport** et **ServiceImport** gèrent la partie réseau des services, en
  représentant respectivement l'exposition d'un service et son importation. Conceptuellement
  proches des objets Service, ils sont spécifiquement adaptés aux environnements
  multi-cluster.

.. figure:: /images/kubernetes-multi-cluster-hub-and-spoke.webp
   :alt: Architecture multi-cluster Kubernetes Hub and Spoke : des objets Work sont créés dans l'API du cluster Hub, les Work Controllers des clusters Spoke les déploient, et les services sont partagés via ServiceExport et ServiceImport.
   :width: 800
   :height: 500

   Fédération de clusters avec une architecture Hub and Spoke : les objets Work sont
   déployés dans l'API centrale et les contrôleurs des clusters satellites prennent en
   charge leur déploiement. Les Pods de clusters différents ne communiquent qu'au travers
   des services exposés par ServiceExport et ServiceImport.

Avantages et limites de l'approche Hub and Spoke
------------------------------------------------

Cette stratégie multi-cluster comporte plusieurs avantages notables. Tout d'abord, il
s'agit d'une solution portée par le projet Kubernetes, qui devrait donc continuer à évoluer
et à être maintenue dans les années à venir. Ensuite, elle peut être mise en place même
après le déploiement de plusieurs clusters, et peut ainsi être vue comme une amélioration
naturelle de votre infrastructure. Enfin, elle répond au besoin de distribution de charge
sur plusieurs localisations avec des exigences d'interconnexion moindres qu'une stratégie
d'extension de clusters.

Sa limite : les Pods des différents clusters ne communiquent pas directement entre eux. Il
est nécessaire de mettre en place le système ServiceExport / ServiceImport pour qu'ils
puissent interagir avec les services des autres clusters.

Interconnecter ses clusters : Liqo et Submariner
================================================

Il existe également d'autres solutions, certes moins « officielles », mais redoutablement
efficaces.

Liqo
----

Si vous avez besoin d'interconnecter vos clusters afin que les applications déployées sur
un cluster puissent découvrir les services d'un autre comme s'ils faisaient partie du même
cluster, `Liqo <https://docs.liqo.io/en/latest/introduction.html>`__ est un outil
minimaliste, open source et facile à prendre en main. Il permet également une certaine
gestion de la répartition des charges de travail entre les clusters interconnectés, et se
distingue par sa simplicité de déploiement, puisqu'il ne requiert aucune modification des
configurations existantes des clusters.

Intégrer plusieurs clusters hétérogènes, notamment gérés par différents fournisseurs Cloud,
peut toutefois rendre sa configuration et sa gestion plus complexes. De plus, la latence des
interconnexions réseau peut varier en fonction des distances géographiques entre les
clusters, ce qui impacte les performances des applications distribuées.

Submariner
----------

`Submariner <https://submariner.io/>`__, projet incubé par la CNCF, est spécialisé dans
l'interconnexion sécurisée et performante des clusters, mais sans gestion de charge
distribuée. Il a été développé pour répondre aux défis de la connectivité réseau dans des
environnements multi-cluster, et vise les déploiements qui nécessitent une communication
entre clusters tout en maintenant une stricte isolation réseau.

Submariner établit une connectivité transparente en configurant automatiquement des tunnels
sécurisés et performants : les Pods d'un cluster accèdent aux services d'un autre comme
s'ils étaient sur le même réseau. Ce qui le différencie, c'est son approche décentralisée,
qui ne nécessite aucun point de gestion central pour orchestrer la connectivité, ce qui
renforce la disponibilité du réseau.

D'un point de vue technique, Submariner repose sur des tunnels VPN chiffrés, utilisant des
technologies éprouvées comme IPsec ou WireGuard, qui garantissent une communication
sécurisée entre les clusters Kubernetes. Cette approche facilite l'extension des réseaux
tout en maintenant des niveaux de sécurité élevés.

Multi-cluster et Platform as a Service
======================================

Le concept de Platform as a Service (PaaS), au cœur de `The Art of Kubernetes </>`__, est
parfaitement compatible avec une architecture multi-cluster et vous laisse une certaine
liberté quant à son implémentation : une plateforme par cluster, ou seulement une partie de
la plateforme par cluster, en mutualisant certains services et outils sur d'autres
clusters.

Encore une fois, il est préférable de limiter au strict minimum le nombre d'outils et de
services d'une plateforme, ainsi que le nombre d'instances associées. Bien que plusieurs
outils de gestion permettent de gagner du temps dans l'exploitation des services, restez
vigilant quant à la complexité supplémentaire qu'ils ajoutent à la suite logicielle que
vous devrez maîtriser.

.. pull-quote::

   Adoptez une approche pragmatique : concentrez-vous sur les niveaux de service que la
   plateforme fournit, plutôt que sur la multiplication des outils, des services et des
   fonctionnalités.
