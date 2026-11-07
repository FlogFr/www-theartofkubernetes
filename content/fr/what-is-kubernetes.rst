Qu'est-ce que Kubernetes ? Bien plus qu'un orchestrateur de conteneurs
######################################################################

:lang: fr
:date: 2024-09-09
:modified: 2026-11-07
:slug: qu-est-ce-que-kubernetes
:category: Kubernetes
:tags: kubernetes, k8s, conteneurs, cloud native, paas, platform as a service, architecture
:authors: Florian Grignon
:seo_title: Qu'est-ce que Kubernetes ? Bien plus qu'un orchestrateur
:description: Kubernetes n'est « qu'un » orchestrateur de conteneurs ? Découvrez pourquoi sa flexibilité et son extensibilité en font l'outil idéal pour bâtir une plateforme.
:summary: Depuis plus de dix ans, Kubernetes s'est imposé dans les entreprises. Pourtant, ce n'est « qu'un » orchestrateur de conteneurs. Prenons cinq minutes pour comprendre ce qui fait vraiment sa force.
:logo: logo-kubernetes.webp
:pdf: /assets/Article-Qu-est-ce-que-Kubernetes.pdf

Depuis quelques années, Kubernetes est présenté comme la technologie incontournable.
Pourtant, si l'on s'en tient à sa définition stricte, il ne s'agit « que » d'un
orchestrateur de conteneurs. Alors, pourquoi cette solution s'est-elle imposée comme
indispensable dans tant d'entreprises depuis plus de dix ans ?

La conteneurisation a transformé la gestion des infrastructures
===============================================================

La conteneurisation, couplée à l'architecture microservices, a profondément transformé le
paysage de la gestion des infrastructures. Elle a facilité la gestion du cycle de vie des
applications tout en rendant leur déploiement et leur évolution plus efficaces. Cette
architecture *Cloud Native* a progressivement remplacé les approches de virtualisation
traditionnelle, plus lourdes.

Kubernetes a été conçu pour orchestrer ces conteneurs, en mettant un accent particulier sur
la **résilience** et la **performance**. Il intègre des mécanismes permettant, par exemple,
de redémarrer automatiquement les conteneurs défaillants ou de faire évoluer dynamiquement
leur nombre pour absorber des pics de charge. Il est toutefois important de noter que
certains aspects comme la sécurité, bien qu'essentiels, ne sont pas fournis nativement par
Kubernetes.

.. figure:: /images/kubernetes-fonctionnalites.webp
   :alt: Les principales fonctionnalités de Kubernetes : résilience, scalabilité, haute disponibilité, déploiement automatique, stockage persistant, jobs, isolation des ressources, découverte de services, configuration des applications, extensibilité et répartition de charge.
   :width: 560
   :height: 410

   Les principales fonctionnalités de Kubernetes.

Flexibilité et extensibilité : les clés du succès de Kubernetes
===============================================================

Ce qui a véritablement permis à Kubernetes de surpasser ses concurrents réside dans sa
flexibilité et son extensibilité.

D'une part, Kubernetes offre une grande **flexibilité** grâce à son architecture modulaire,
qui permet de choisir et d'adapter ses composants en fonction des besoins spécifiques de
chaque entreprise. Par exemple, bien que Kubernetes définisse un modèle réseau à respecter,
il laisse une liberté totale quant à son implémentation via des solutions compatibles comme
`Cilium <https://cilium.io/>`__.

D'autre part, en tant que projet open source, Kubernetes bénéficie d'une communauté
dynamique qui développe rapidement des **extensions** pour enrichir ses fonctionnalités. Il
est ainsi extrêmement facile d'ajouter, par exemple, l'extension
`CoreDNS <https://coredns.io/>`__ pour permettre la découverte automatique des services au
sein du cluster.

Grâce à cette flexibilité et à cette extensibilité, Kubernetes répond non seulement aux
attentes d'une infrastructure Cloud Native moderne, mais garantit également un très haut
niveau de qualité de service.

De l'infrastructure à la plateforme (PaaS)
==========================================

L'association de l'architecture Cloud Native et de la puissance de Kubernetes change
fondamentalement la perception de l'infrastructure. Celle-ci n'est plus seulement un socle
technique pour faire fonctionner les applications : elle devient une véritable
**plateforme** capable de fournir des services et des outils standardisés.

Ces outils simplifient la gestion du cycle de vie des applications : l'intégration d'un
service de déploiement continu (*Continuous Delivery*), par exemple, permet de déployer
automatiquement les services applicatifs. Par ailleurs, des services prêts à l'emploi,
comme une base de données, peuvent être déployés facilement dans Kubernetes, notamment
grâce aux `Operators <{filename}operator-or-not-operator.rst>`__.

.. pull-quote::

   Kubernetes est bien plus qu'un simple orchestrateur de conteneurs : c'est un outil de
   choix pour la mise en œuvre de plateformes.

Aujourd'hui, il est possible d'implémenter des plateformes sur mesure, adaptées à chaque
entreprise et offrant des niveaux de service élevés. Une plateforme en tant que service
(*Platform as a Service*) ne représente pas seulement un atout technique, mais également un
levier organisationnel : elle constitue un cadre efficace de communication et de
collaboration entre les équipes applicatives et celles en charge de l'infrastructure.

En résumé
=========

Kubernetes est une solution technologique conçue pour gérer de manière résiliente et
performante des charges de travail conteneurisées. Grâce à son architecture flexible et
extensible, couplée à une infrastructure Cloud Native, il se positionne comme un outil de
choix pour la mise en œuvre de plateformes, et il excelle notamment dans la gestion du
cycle de vie des applications.

Dans `The Art of Kubernetes </>`__, j'explique comment devenir des artisans de
l'infrastructure, en affinant nos solutions pour optimiser l'infrastructure grâce à
Kubernetes.
