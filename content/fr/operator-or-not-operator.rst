Operator ou ne pas Operator, telle est la question
##################################################

:lang: fr
:date: 2024-08-01
:modified: 2024-08-01
:tags: kubernetes, operator, administration, architecture, infrastructure
:category: kubernetes
:logo: logo-operator.webp
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

        <p class="text-justify text-lg text-400">Nous constatons que Kubernetes est conçu pour prendre en charge tout type d’application conteneurisée de manière performante et résiliente. Sa flexibilité constitue un atout majeur, permettant à Kubernetes d'étendre ses fonctionnalités afin de supporter divers services et outils d’une plateforme, tout en optimisant l’utilisation des ressources d’infrastructure d’une entreprise. Les outils intégrés à une plateforme facilitent la gestion du cycle de vie des applications et des services. Par exemple, un bon système de déploiement continu (CD) permet de gérer efficacement les déploiements au sein de votre parc.</p>

        <p class="text-justify text-lg text-400">Un autre système de gestion du cycle de vie des applications, qui s'est imposé dans l'écosystème Kubernetes, est celui des Operators. Ces derniers occupent désormais une place centrale en automatisant la gestion d'applications complexes directement au sein du cluster Kubernetes.</p>
      </div>
    </div><!--end container-->
  </section>

  <section class="relative md:py-8 py-8 bg-slate-50 dark:bg-slate-800" id="services">
      <div class="container relative">
          <div class="grid grid-cols-1 pb-6 text-center">
              <h3 class="font-semibold text-2xl leading-normal mb-4">Les Operators sont une autre manière de gérer le cycle de vie des applications et services au sein d’un cluster.</h3>
          </div>
      </div>
  </section>

  <section class="relative md:py-8 py-8">
    <div class="container relative">
      <div class="grid grid-cols-1 grid-rows-1">
        <p class="text-justify text-lg text-400">Techniquement, un Operator automatise les interventions manuelles de l'administrateur d’une application en encapsulant la logique opérationnelle d'une application spécifique dans des contrôleurs personnalisés, souvent en s'appuyant sur des Custom Resource Definitions (CRD). Ainsi, il abstrait complètement la gestion du cycle de vie et l’automatisation de tâches complexes pour les applications.</p>
        <p class="text-justify text-lg text-400">En pratique, un Operator permet de gérer le cycle de vie d’une application ou d’un service, qu'il soit stateful ou stateless, de son installation à sa désinstallation, en passant par ses différents états fonctionnels. Il ajoute une couche supplémentaire de logique entre l'administrateur et l’application, ce qui nécessite des droits élevés, au minimum équivalents à ceux de l’administrateur du service concerné.</p>
        <p class="text-justify text-lg text-400">Comme nous l'avons observé tout au long de cet ouvrage, Kubernetes et son écosystème permettent de définir des plateformes efficaces pour chaque entreprise. Cela signifie que Kubernetes, associé aux outils disponibles pour gérer le cycle de vie des applications et des services, offre une solution performante.</p>
        <p class="text-justify text-lg text-400">Pour des raisons que je vais détailler, je recommande de recourir aux Operators uniquement dans des cas spécifiques. Dans d'autres situations, vous pouvez facilement gérer le service vous-même ou opter pour un service externalisé.</p>
        <p class="text-justify text-lg text-400">Ce post explore les avantages et les inconvénients des Operators, qui sont devenus incontournables pour de nombreuses entreprises souhaitant tirer le meilleur parti de Kubernetes.</p>
      </div>
    </div><!--end container-->
  </section>

  <section class="relative md:py-8 py-8 bg-slate-50 dark:bg-slate-800" id="services">
      <div class="container relative">
          <div class="grid grid-cols-1 pb-6 text-center">
              <h3 class="font-semibold text-2xl leading-normal mb-4">En automatisant la gestion des erreurs et en surveillant continuellement l'état des applications, les Operators contribuent à améliorer la disponibilité et la résilience des services.</h3>
          </div>
      </div>
  </section>

  <section class="relative md:py-8 py-8">
    <div class="container relative">
      <div class="grid grid-cols-1 grid-rows-1">
        <p class="text-justify text-lg text-400">Un Operator est une extension de Kubernetes qui encapsule la logique opérationnelle d'une application spécifique. C'est en quelque sorte un "opérateur humain" codifié, capable de gérer des tâches complexes telles que le déploiement, la mise à jour, la sauvegarde, la restauration et même la mise à l’échelle de l’application, le tout de manière automatisée. Les Operators sont construits sur la base des Custom Resource Definitions (CRDs), une fonctionnalité de Kubernetes qui permet de définir de nouvelles ressources personnalisées. Un Operator surveille ces ressources et réagit aux événements associés en exécutant des actions prédéfinies pour gérer l'état de l'application. Prenons l’exemple de l’Operator PostgreSQL CloudNativePG. Les CRD suivants seront mis à disposition de l’administrateur du cluster : Cluster, Backup, ScheduleBackup… Pour déployer un cluster PostgreSQL à l’intérieur de votre cluster Kubernetes, il suffit de créer un objet CRD Cluster dans l’API Kubernetes avec les bons paramètres, puis de laisser l’Operator faire sa magie. L’Operator déploiera ensuite les Pods, Services et PersistentVolumes nécessaires pour obtenir un cluster PostgreSQL fonctionnel au sein du cluster.</p>
      </div>
    </div><!--end container-->
  </section>

  <section class="relative md:py-8 py-8 bg-slate-50 dark:bg-slate-800" id="services">
      <div class="container relative">
          <div class="grid grid-cols-1 pb-6 text-center">
              <h3 class="font-semibold text-2xl leading-normal mb-4">Si les Operators automatisent l’exploitation d’un service, ils posent également un défi en déléguant les décisions critiques à un logiciel plutôt qu'à un expert humain.</h3>
          </div>
      </div>
  </section>

  <section class="relative md:py-8 py-8">
    <div class="container relative">
      <div class="grid grid-cols-1 grid-rows-1">
        <p class="text-justify text-lg text-400">L'avantage principal des Operators réside dans leur capacité à automatiser des tâches complexes qui, autrement, nécessiteraient une intervention humaine. Par exemple, la mise à jour d'une base de données stateful, avec toutes ses spécificités, peut être entièrement gérée par un Operator, minimisant ainsi les risques d'erreurs. Cependant, ce même avantage peut aussi se transformer en inconvénient, car l'administrateur risque de se reposer entièrement sur l'Operator, perdant ainsi la connaissance approfondie de la logique de l’application. Il pourrait alors négliger la documentation et ne plus avoir la connaissance suffisante de l’application pour déployer et maintenir l'application en état fonctionnel, ce qui pourrait avoir des conséquences graves en cas de problème majeur. L’administrateur, ou opérateur humain, doit rester experte des services qu’il ou elle administre.</p>
      </div>
    </div><!--end container-->
  </section>

  <section class="relative md:py-8 py-8 bg-slate-50 dark:bg-slate-800" id="services">
      <div class="container relative">
          <div class="grid grid-cols-1 pb-6 text-center">
              <h3 class="font-semibold text-2xl leading-normal mb-4">Les choix que vous déléguez à un Operator ne vous exemptent pas d’en assumer les conséquences, qu’elles soient positives ou négatives.</h3>
          </div>
      </div>
  </section>

  <section class="relative md:py-8 py-8">
    <div class="container relative">
      <div class="grid grid-cols-1 grid-rows-1">
        <p class="text-justify text-lg text-400">C’est un peu comme balayer la poussière sous le tapis : la poussière est toujours là, et vous risquez toujours d’y être allergique. Il n’existe donc pas de raccourci pour maîtriser un logiciel et atteindre un haut niveau de service : cela nécessite une solide expertise, de la pratique, ainsi qu’un investissement en temps.</p>
        <p class="text-justify text-lg text-400">Les Operators jouent un rôle essentiel dans la standardisation de la gestion des applications et des services, garantissant que les meilleures pratiques sont appliquées de manière cohérente à travers différents environnements. Cette reproductibilité s'avère particulièrement utile dans des contextes multi-environnements ou multi-clusters, où il est crucial que les applications soient déployées et maintenues de manière uniforme. Cependant, cette standardisation peut s'avérer trompeuse. En effet, en ajoutant une couche automatisée qui gère le cycle de vie du logiciel, comment pouvez-vous être certain que ce logiciel se trouve dans le même état dans deux environnements différents ? Cela devient presque impossible si vous ne contrôlez pas l'ensemble de l'état de l’Operator, qui dépend de tout l’environnement. Cela pose un réel problème dans les environnements d'intégration continue (CI), où la reproductibilité et l’idempotence sont des notions essentielles pour garantir la fiabilité des résultats.</p>
        <p class="text-justify text-lg text-400">De plus, les Operators disponibles pour les applications ne couvrent pas nécessairement l'ensemble des besoins opérationnels. Il est donc envisageable qu'un Operator limite vos capacités à maintenir le service dans un état pleinement fonctionnel. Par exemple, une migration de l’application ou du service est-elle prise en compte par l’Operator ? Et même dans le cas où cela serait le cas, préférez-vous effectuer la migration à l'aide d'un Operator automatisé ou bien d'un opérateur humain ?</p>
        <p class="text-justify text-lg text-400">En automatisant la gestion des erreurs et en surveillant continuellement l'état des applications, les Operators contribuent à améliorer la disponibilité et la résilience des services. Par exemple, un Operator peut détecter un dysfonctionnement et prendre automatiquement des mesures correctives, telles que le redémarrage d'un composant défaillant ou la restauration à partir d'une sauvegarde. Cependant, cela peut également constituer un désavantage, car le choix de la résolution des dysfonctionnements est laissé à un composant logiciel plutôt qu’à un expert de l’application. Cette automatisation peut entraîner l’application dans un état non seulement indésirable, mais aussi problématique, sans possibilité de retour en arrière.</p>

        <p class="text-justify text-lg text-400 mt-6">Je vais probablement m'écarter de ce que vous avez déjà entendu à propos des Operators, mais je pense que leur efficacité et leur utilité résident dans les Operators personnalisés pour vos applications. En développant un Operator spécifiquement adapté à vos besoins, vous pouvez l'utiliser facilement comme un service au sein de votre plateforme Kubernetes, sans dépendre de nombreux outils tiers. La logique de gestion du cycle de vie de vos applications étant intégrée dans l’Operator, vous pouvez instancier votre application aisément pour la tester depuis une autre plateforme. Attention cependant, le développement d’un Operator peut s’avérer complexe et nécessite une compréhension approfondie de Kubernetes. Cette complexité peut constituer une barrière à l'adoption, en particulier pour les petites équipes ou les entreprises qui ne disposent pas des compétences nécessaires en interne.</p>
        <p class="text-justify text-lg text-400">Comme tout composant logiciel dans votre cluster, un Operator doit être maintenu, mis à jour et corrigé en cas de bugs ou de vulnérabilités. Cela implique un effort de maintenance continu, qui peut devenir coûteux si l'Operator est complexe ou s'il doit évoluer avec l'application qu'il gère. Cet effort doit également être pris en compte dans les cas critiques, comme par exemple une migration de l’application.</p>
        <p class="text-justify text-lg text-400">Pour les équipes qui gèrent déjà un grand nombre d'outils et de services, l'ajout d'Operators peut contribuer à une surcharge cognitive. Comprendre et gérer les différents Operators déployés dans un cluster peut devenir complexe, en particulier lorsque chaque Operator a ses propres configurations et comportements spécifiques.</p>
        <p class="text-justify text-lg text-400 mt-6">Les Operators sont aujourd'hui très (voire trop) répandus. Plus de 277 sont listés sur OperatorHub à la disposition de la communauté Kubernetes. Il est désormais possible de déployer presque n’importe quel composant logiciel open-source avec un Operator. Cependant, il est crucial de bien peser les avantages et les inconvénients de l’utilisation d’un Operator par rapport à d’autres méthodes pour gérer le cycle de vie d’un composant logiciel.</p>
      </div>
    </div><!--end container-->
  </section>

  <section class="relative md:py-8 py-8">
    <div class="container relative">
      <div class="grid grid-cols-1 grid-rows-1">
        <p class="text-justify text-lg text-400">Je vous recommande donc d’utiliser les Operators avec parcimonie, principalement pour transformer vos applications en services au sein d’une plateforme, ainsi que dans les cas où vous n’auriez d’autre choix.</p>
      </div>
    </div><!--end container-->
  </section>

