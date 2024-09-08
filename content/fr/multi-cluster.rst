Multi Cluster Kubernetes
########################

:lang: fr
:date: 2024-09-15
:modified: 2024-09-15
:tags: kubernetes, multi-cluster, multi cluster, architecture, infrastructure, k8s
:category: kubernetes
:slug: multi-cluster-kubernetes
:authors: Florian Grignon
:summary: Kubernetes, grâce à son architecture hautement modulable, flexible et extensible permet facilement de mettre en place une architecture multi clusters pour répondre à des besoins spécifiques.
:timeread: 15 min

.. raw:: html

  <section class="relative md:py-24 py-16"><!-- Section Auteur -->
    <div class="container relative">
      <div class="grid grid-cols-1 grid-rows-1">
        <h6 class="text-teal-500 text-sm font-semibold uppercase mb-2">Florian Grignon, le 15/09/2024</h6>
        <h3 class="font-semibold text-2xl leading-normal mb-4">Multi Cluster Kubernetes</h3>
        <p class="text-justify text-lg text-400">Dans cet article du blog The Art of Kubernetes, nous abordons un sujet avancé : l'architecture multi-cluster. Nous allons le simplifier tout en supposant que le lecteur maîtrise déjà bien les bases de Kubernetes.</p>

        <h4 class="font-semibold text-2xl leading-normal mb-4">L’architecture de l’infrastructure, reflet des besoins métiers et applicatifs</h4>
        <p class="text-justify text-lg text-400">Il est désormais courant de disposer de plusieurs environnements pour gérer le cycle de vie des applications. L’environnement de test permet, comme son nom l’indique, de valider fonctionnellement les applications. Un environnement de pré-production teste les processus de déploiement, tandis qu’un environnement d’intégration vérifie des fonctionnalités spécifiques. Un environnement de performance, quant à lui, teste la robustesse de l’application en conditions réelles de charge.</p>
        <p class="text-justify text-lg text-400">Idéalement, chaque environnement doit être le plus proche possible de la production afin de garantir des résultats pertinents. En parallèle, il est essentiel d’isoler ces environnements pour éviter tout impact négatif, tel que des tests de performance perturbant une application en production. Comme expliqué dans notre livre, les Namespaces Kubernetes permettent une isolation logique des objets de l’API Kubernetes, mais ils ne suffisent pas toujours à isoler complètement les outils et services de la plateforme. La solution la plus simple consiste alors à provisionner un cluster Kubernetes distinct pour chaque environnement. Ainsi, chaque cluster représente un environnement avec ses applications, outils, et services.</p>
        <p class="text-justify text-lg text-400">Si des contraintes budgétaires existent, il est possible de mutualiser certains outils entre plusieurs environnements ou de déployer des versions allégées, comme des APIs simulées. Cependant, tant que ces clusters ne communiquent pas entre eux, nous ne sommes pas encore dans une architecture multi-cluster à proprement parler.</p>
        <h4 class="font-semibold text-2xl leading-normal mb-4">Qu'est-ce qu'une architecture multi-cluster ?</h4>
        <p class="text-justify text-lg text-400">Une architecture multi-cluster consiste en un ensemble de clusters Kubernetes qui communiquent entre eux. Le cas le plus simple est celui d’une répartition de charge entre deux clusters, comme lors d’une migration. Prenons un exemple : vous souhaitez migrer de votre cluster basé à Londres (cluster-lon-1) vers un cluster à Paris (cluster-par-1) pour des raisons de conformité au RGPD. Vous provisionnez un nouveau cluster à Paris et commencez à répartir la charge de travail entre les deux sites. Le projet Kubestellar vous permet justement de spécifier, via une API Kubernetes centrale, quels objets déployer sur chaque cluster, facilitant ainsi la migration de la charge de Londres à Paris. Ce type d’usage est souvent temporaire, le temps de la migration, et vise à décommissionner l’ancien cluster une fois la transition effectuée. D'autres méthodes de migration sont également décrites en détail dans le livre.</p>
        <h4 class="font-semibold text-2xl leading-normal mb-4">Autres cas d’usage du multi-cluster</h4>
      </div>
    </div><!--end container-->
  </section>

  <section class="relative"><!-- Section Auteur -->
      <div class="container relative">
        <div class="grid grid-cols-1 pb-6 text-center">
            <img src="/images/Diag MultiCluster Hub and Spoke.png" width="100%" class="shadow dark:shadow-gray-700" alt="Fonctionnalités de Kubernetes" >
        </div>
      </div>
  </section>

  <section class="relative md:py-24 py-16">
    <div class="container relative">
      <div class="grid grid-cols-1 grid-rows-1">
        <p class="text-justify text-lg text-400">Un autre scénario fréquent est celui du multi-cloud ou du cloud hybride. Dans ces configurations, l’idée est de répartir la charge de travail sur deux fournisseurs de cloud, afin de tirer parti des avantages propres à chacun. Le Special Interest Group (SIG) Kubernetes "multicluster" propose des solutions d’extension des clusters pour gérer la répartition de la charge et la communication entre clusters via les systèmes ServiceImport et ServiceExport. Le fonctionnement de la répartition est similaire à celui de Kubestellar, avec une API Kubernetes centrale et des contrôleurs (WorkController) sur chaque cluster pour répliquer les objets.</p>
        <p class="text-justify text-lg text-400">Enfin, un cas d’usage courant du multi-cluster est l’architecture satellitaire, où les clusters sont déployés au plus proche des utilisateurs finaux afin de traiter et stocker les données localement. Ce besoin se rencontre souvent dans les entreprises cherchant à optimiser la performance des applications tout en minimisant les délais de traitement. Pour plus de détails sur ce sujet, je vous invite à consulter notre autre article dédié.</p>
        <h4 class="font-semibold text-2xl leading-normal mb-4">Conclusion</h4>
        <p class="text-justify text-lg text-400">Grâce à sa modularité, sa flexibilité et son extensibilité, Kubernetes a su évoluer pour répondre à des besoins variés, notamment en matière d’architecture multi-cluster. Que ce soit pour la migration de charges, l’utilisation de plusieurs fournisseurs cloud, ou la proximité avec les utilisateurs finaux, Kubernetes offre des solutions simples et efficaces, parfaitement adaptées aux enjeux des entreprises modernes.</p>
      </div>
    </div><!--end container-->
  </section>
