Operator ou ne pas Operator, telle est la question
##################################################

:date: 2024-08-01
:modified: 2024-08-01
:tags: kubernetes, operator, administration, architecture, infrastructure
:category: kubernetes
:slug: operator-or-not-operator
:authors: Florian Grignon
:summary: L'un des atouts majeurs de Kubernetes réside dans sa capacité à être extensible et à s'adapter à une multitude de cas d'usage grâce à des abstractions avancées. Parmi celles-ci, le modèle d’Operator occupe une place centrale en automatisant la gestion d'applications complexes directement au sein du cluster Kubernetes.
:timeread: 15 min

.. raw:: html

  <section class="relative md:py-24 py-16"><!-- Section Auteur -->
    <div class="container relative">
      <div class="grid grid-cols-1 grid-rows-1">
        <h6 class="text-teal-500 text-sm font-semibold uppercase mb-2">Florian Grignon, le 01/08/2024</h6>
        <h3 class="font-semibold text-2xl leading-normal mb-4">Operator or not Operator, telle est la question</h3>

        <p class="text-justify text-lg text-400">L'un des atouts majeurs de Kubernetes réside dans sa capacité à être extensible et à s'adapter à une multitude de cas d'usage grâce à des abstractions avancées. Parmi celles-ci, le modèle d’Operator occupe une place centrale en automatisant la gestion d'applications complexes directement au sein du cluster Kubernetes. Un Operator encapsule la logique opérationnelle d'une application spécifique dans des contrôleurs personnalisés, souvent en s'appuyant sur des Custom Resource Definitions (CRD). Il facilite ainsi la gestion du cycle de vie et l’automatisation de tâches complexes pour les applications. En pratique, un Operator permet de gérer une application, qu'elle soit stateful ou stateless, de son installation à sa désinstallation, en passant par ses différents états fonctionnels. Cette automatisation remplace les interventions manuelles de l'administrateur de l'application, ajoutant ainsi une couche supplémentaire de logique entre l'administrateur et l’application, et requérant souvent des droits élevés, au minimum équivalents à ceux de l'administrateur. Pour des raisons que je vais détailler, je recommande de recourir aux Operators uniquement en dernier recours. Ce chapitre explore les avantages et les inconvénients de cette approche, devenue incontournable pour de nombreuses entreprises souhaitant tirer le meilleur parti de Kubernetes.</p>
      </div>
    </div><!--end container-->
  </section>

  <section class="relative md:py-24 py-16 bg-slate-50 dark:bg-slate-800" id="services">
      <div class="container relative">
          <div class="grid grid-cols-1 pb-6 text-center">
              <h3 class="font-semibold text-2xl leading-normal mb-4">En automatisant la gestion des erreurs et en surveillant continuellement l'état des applications, les Operators contribuent à améliorer la disponibilité et la résilience des services.</h3>
          </div>
      </div>
  </section>

  <section class="relative md:py-24 py-16">
    <div class="container relative">
      <div class="grid grid-cols-1 grid-rows-1">
        <p class="text-justify text-lg text-400">Un Operator est une extension de Kubernetes qui encapsule la logique opérationnelle d'une application spécifique. C'est en quelque sorte un "opérateur humain" codifié, capable de gérer des tâches complexes telles que le déploiement, la mise à jour, la sauvegarde, la restauration et même la mise à l’échelle de l’application, le tout de manière automatisée. Les Operators sont construits sur la base des Custom Resource Definitions (CRDs), une fonctionnalité de Kubernetes qui permet de définir de nouvelles ressources personnalisées. Un Operator surveille ces ressources et réagit aux événements associés en exécutant des actions prédéfinies pour gérer l'état de l'application. Prenons l’exemple de l’<a class="text-slate-400" href="https://operatorhub.io/operator/cloudnative-pg">Operator PostgreSQL CloudNativePG</a>. Les CRD suivants seront mis à disposition de l’administrateur du cluster : Cluster, Backup, ScheduleBackup… Pour déployer un cluster PostgreSQL à l’intérieur de votre cluster Kubernetes, il suffit de créer un CRD Cluster avec les bons paramètres, puis de laisser l’Operator faire sa magie. L’Operator déploiera ensuite les Pods, Services et PersistentVolumes nécessaires pour obtenir un cluster PostgreSQL fonctionnel au sein du cluster.</p>
        <p class="text-justify text-lg text-400">L'avantage principal des Operators réside dans leur capacité à automatiser des tâches complexes qui, autrement, nécessiteraient une intervention humaine. Par exemple, la mise à jour d'une base de données stateful, avec toutes ses spécificités, peut être entièrement gérée par un Operator, minimisant ainsi les risques d'erreurs et améliorant l'efficacité opérationnelle. Cependant, ce même avantage peut aussi se transformer en inconvénient, car l'administrateur risque de se reposer entièrement sur l'Operator, perdant ainsi la connaissance approfondie de la logique de l’application. Il pourrait alors négliger la documentation et ne plus avoir la connaissance suffisante de l’application pour déployer et maintenir l'application en état fonctionnel, ce qui pourrait avoir des conséquences graves en cas de problème majeur. De plus, les Operators disponibles pour les applications ne couvrent pas nécessairement l'ensemble des besoins opérationnels. Il est donc possible qu'un Operator limite vos capacités à maintenir l'application dans un état pleinement fonctionnel.</p>
        <p class="text-justify text-lg text-400">Les Operators permettent de standardiser la gestion des applications, en garantissant que les meilleures pratiques sont appliquées de manière cohérente à travers différents environnements. Cette reproductibilité est particulièrement utile dans des contextes multi-environnements ou multi-clusters, où il est essentiel que les applications soient déployées et maintenues de manière uniforme.</p>
        <p class="text-justify text-lg text-400">En automatisant la gestion des erreurs et en surveillant continuellement l'état des applications, les Operators contribuent à améliorer la disponibilité et la résilience des services. Par exemple, un Operator peut détecter un dysfonctionnement et prendre automatiquement des mesures correctives, telles que le redémarrage d'un composant défaillant ou la restauration à partir d'une sauvegarde. Cependant, cela peut également constituer un désavantage, car le choix de la résolution des dysfonctionnements est laissé à un composant logiciel plutôt qu’à un expert de l’application. Cette automatisation peut entraîner l’application dans un état non seulement indésirable, mais aussi problématique, sans possibilité de retour en arrière.</p>
        <p class="text-justify text-lg text-400">Le développement d’un Operator pour vos applications peut être utile pour automatiser les tâches opérationnelles. Cependant, le développement d’un Operator peut s’avérer complexe et nécessite une compréhension approfondie de Kubernetes. Cette complexité peut représenter une barrière à l'adoption, en particulier pour les petites équipes ou les entreprises qui ne disposent pas des compétences nécessaires en interne.</p>
        <p class="text-justify text-lg text-400">Comme tout composant logiciel dans votre cluster, un Operator doit être maintenu, mis à jour et corrigé en cas de bugs ou de vulnérabilités. Cela implique un effort de maintenance continu, qui peut devenir coûteux si l'Operator est complexe ou s'il doit évoluer avec l'application qu'il gère. Cet effort doit également être pris en compte dans les cas critiques, comme par exemple une migration de l’application. Une migration d’une application d’un cluster à un autre est-elle plus simple à gérer avec ou sans Operator ? Il est évident qu’il existe toujours des cas d’utilisation que nous pourrions oublier.</p>
      </div>
    </div><!--end container-->
  </section>

  <section class="relative md:py-24 py-16 bg-slate-50 dark:bg-slate-800" id="services">
      <div class="container relative">
          <div class="grid grid-cols-1 pb-6 text-center">
              <h3 class="font-semibold text-2xl leading-normal mb-4">L'ajout d'Operators peut contribuer à une surcharge cognitive.</h3>
          </div>
      </div>
  </section>

  <section class="relative md:py-24 py-16">
    <div class="container relative">
      <div class="grid grid-cols-1 grid-rows-1">
        <p class="text-justify text-lg text-400">Pour les équipes qui gèrent déjà un grand nombre d'outils et de services, l'ajout d'Operators peut contribuer à une surcharge cognitive. Comprendre et gérer les différents Operators déployés dans un cluster peut devenir complexe, en particulier lorsque chaque Operator a ses propres configurations et comportements spécifiques.</p>
        <p class="text-justify text-lg text-400">Les Operators sont aujourd'hui très (voire trop) répandus. Plus de 277 sont listés sur <a class="text-slate-400" href="https://operatorhub.io">https://operatorhub.io</a> à la disposition de la communauté Kubernetes. Il est désormais possible de déployer presque n’importe quel composant logiciel open-source avec un Operator. Cependant, il est crucial de bien peser les avantages et les inconvénients de l’utilisation d’un Operator par rapport à d’autres méthodes pour gérer le cycle de vie d’un composant logiciel.</p>
      </div>
    </div><!--end container-->
  </section>
