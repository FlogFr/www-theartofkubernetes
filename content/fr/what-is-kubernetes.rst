Qu'est-ce que Kubernetes ?
##########################

:lang: fr
:date: 2024-09-09
:modified: 2024-09-09
:tags: kubernetes, paas, platform as a service, architecture, infrastructure, k8s
:category: kubernetes
:logo: logo-kubernetes.webp
:slug: qu-est-ce-que-kubernetes
:authors: Florian Grignon
:summary: Kubernetes a 10 ans, et a bien évolué durant tout ce temps. Prenons 5 minutes pour voir ce qu'est devenu Kubernetes.
:timeread: 15 min

.. raw:: html

  <section class="relative md:py-24 py-16"><!-- Section Auteur -->
    <div class="container relative">
      <div class="grid grid-cols-1 grid-rows-1">
        <h6 class="text-teal-500 text-sm font-semibold uppercase mb-2">
        Florian Grignon, le 09/09/2024
        <a href="/assets/Chapitre-Qu-est-ce-que-Kubernetes.pdf" class="h-8 px-4 text-[12px] tracking-wider inline-flex items-center justify-right font-medium rounded-md bg-teal-500 text-white uppercase">Version PDF</a>
        </h6>
        <h3 class="font-semibold text-2xl leading-normal mb-4">Qu'est-ce que Kubernetes ?</h3>

        <p class="text-justify text-lg text-400">Depuis quelques années, Kubernetes est présenté comme la technologie incontournable. Pourtant, si l'on s'en tient à sa définition stricte, il ne s'agit "que" d'un orchestrateur de conteneurs. Alors, pourquoi cette solution s'est-elle imposée comme indispensable dans tant d'entreprises depuis près de dix ans ?</p>

        <p class="text-justify text-lg text-400 mt-6">La conteneurisation, couplée à l'architecture microservices, a profondément transformé le paysage de la gestion des infrastructures. Elle a facilité la gestion du cycle de vie des applications tout en rendant leur déploiement et leur évolution plus efficaces. Cette architecture "Cloud Native" a progressivement remplacé les approches de virtualisation traditionnelle, plus lourdes. Kubernetes a été conçu pour orchestrer ces conteneurs, en mettant un accent particulier sur la résilience et la performance. Il intègre des mécanismes permettant, par exemple, de redémarrer automatiquement les conteneurs défaillants ou de faire évoluer dynamiquement leur nombre pour absorber des pics de charge. Il est toutefois important de noter que certains aspects comme la sécurité, bien qu'essentiels, ne sont pas fournis nativement par Kubernetes.</p>

        <p class="text-justify text-lg text-400 mt-6">Ce qui a véritablement permis à Kubernetes de surpasser ses concurrents réside dans sa flexibilité et son extensibilité. D'une part, Kubernetes offre une grande flexibilité grâce à son architecture modulaire, permettant ainsi de choisir et d’adapter ses composants en fonction des besoins spécifiques de chaque entreprise. Par exemple, bien que Kubernetes définisse un modèle réseau à respecter, il laisse une liberté totale quant à son implémentation via des solutions compatibles comme <a href="https://cilium.io/">Cilium</a>.</p>

        <p class="text-justify text-lg text-400 mt-6">D'autre part, en tant que projet open-source, Kubernetes bénéficie d'une communauté dynamique qui développe rapidement des extensions pour enrichir ses fonctionnalités. Il est ainsi extrêmement facile d'ajouter, par exemple, l'extension CoreDNS pour permettre la découverte automatique des services au sein du cluster.</p>

        <p class="text-justify text-lg text-400 mt-6">Grâce à cette flexibilité et cette extensibilité, Kubernetes répond non seulement aux attentes d'une infrastructure Cloud Native moderne, mais garantit également un très haut niveau de qualité de service.</p>

        <p class="text-justify text-lg text-400 mt-6">L'association de l'architecture Cloud Native et de la puissance de Kubernetes change fondamentalement la perception de l'infrastructure. Celle-ci n'est plus seulement un socle technique pour faire fonctionner les applications ; elle devient une véritable plateforme capable de fournir des services et des outils standardisés. Ces outils simplifient la gestion du cycle de vie des applications : l'intégration d'un service de déploiement continu (Continuous Delivery), par exemple, permet de déployer automatiquement les services applicatifs. Par ailleurs, des services prêts à l'emploi, comme une base de données, peuvent être déployés facilement dans Kubernetes.</p>

        <p class="text-justify text-lg text-400 mt-6">En somme, Kubernetes est bien plus qu’un simple orchestrateur de conteneurs : c’est une solution technologique conçue pour gérer de manière résiliente et performante des charges de travail conteneurisées. Grâce à son architecture flexible et extensible, couplée à une infrastructure Cloud Native, Kubernetes se positionne comme un outil de choix pour la mise en œuvre de plateformes. Il excelle notamment dans la gestion du cycle de vie des applications.</p>

        <p class="text-justify text-lg text-400 mt-6">Aujourd'hui, il est possible d'implémenter des plateformes sur mesure, adaptées à chaque entreprise, offrant des niveaux de service élevés. Une plateforme en tant que service (Platform as a Service) ne représente pas seulement un atout technique, mais également un levier organisationnel. Elle constitue un cadre efficace de communication et de collaboration entre les équipes applicatives et celles en charge de l'infrastructure.</p>

        <p class="text-justify text-lg text-400 mt-6">Dans <a href="https://theartofkubernetes.com/">The Art of Kubernetes</a>, j'explique comment nous pouvons devenir des artisans de l'infrastructure en affinant nos solutions pour optimiser l'infrastructure grâce à Kubernetes.</p>

      </div>
    </div>
  </section>
