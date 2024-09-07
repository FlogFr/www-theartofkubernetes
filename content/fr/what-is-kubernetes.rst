Qu'est-ce que Kubernetes ?
##########################

:lang: fr
:date: 2024-09-09
:modified: 2024-09-09
:tags: kubernetes, paas, platform as a service, architecture, infrastructure, k8s
:category: kubernetes
:slug: qu-est-ce-que-kubernetes
:authors: Florian Grignon
:summary: Kubernetes a 10 ans, et a bien évolué durant tout ce temps. Prenons 5 minutes pour voir ce qu'est devenu Kubernetes.
:timeread: 15 min

.. raw:: html

  <section class="relative md:py-24 py-16"><!-- Section Auteur -->
    <div class="container relative">
      <div class="grid grid-cols-1 grid-rows-1">
        <h6 class="text-teal-500 text-sm font-semibold uppercase mb-2">Florian Grignon, le 09/09/2024</h6>
        <h3 class="font-semibold text-2xl leading-normal mb-4">Qu'est-ce que Kubernetes ?</h3>


        <p class="text-justify text-lg text-400">Kubernetes est une technologie open-source relativement complexe mais accessible, initialement développée par Google, qui permet de distribuer des charges de travail sous forme de conteneurs sur une infrastructure. Cette solution est devenue incontournable dans toutes les infrastructures Cloud. Au cœur de Kubernetes se trouvent trois composants principaux (Kube API Server, Kube Scheduler et Kube Controller Manager) jouant le rôle de cerveau central, et deux composants (Kubelet et Kube Proxy) déployés sur chaque serveur de travail pour gérer les charges. Chacun de ces composants est hautement flexible, configurable et extensible, formant ensemble une distribution Kubernetes. Il est donc pertinent de considérer une distribution Kubernetes comme une distribution à part entière, au même titre qu’une distribution Linux.</p>
      </div>
    </div><!--end container-->
  </section>

  <section class="relative"><!-- Section Auteur -->
      <div class="container relative">
        <div class="grid grid-cols-1 pb-6 text-center">
            <img src="/images/Diag Kubernetes Features.png" width="100%" class="shadow dark:shadow-gray-700" alt="Fonctionnalités de Kubernetes" >
        </div>
      </div>
  </section>

  <section class="relative md:py-24 py-16">
    <div class="container relative">
      <div class="grid grid-cols-1 grid-rows-1">
        <p class="text-justify text-lg text-400">La technologie a considérablement évolué au cours des dix dernières années, offrant un éventail impressionnant de fonctionnalités. Certaines de ces fonctionnalités sont intégrées au cœur de Kubernetes (en bleu), d’autres nécessitent de la configuration et des greffons (en vert), tandis que certaines sont apportées par des extensions (en jaune). La grande force de Kubernetes réside dans sa modularité et son extensibilité, permettant une adaptation sur-mesure aux besoins spécifiques de chaque entreprise. Devenons des artisans de l’infrastructure en ajustant nos solutions pour qu’elles répondent précisément à nos exigences.</p>
      </div>
    </div>
  </section>

  <section class="relative md:py-24 py-16 bg-slate-50 dark:bg-slate-800" id="services">
      <div class="container relative">
          <div class="grid grid-cols-1 pb-6 text-center">
              <h3 class="font-semibold text-2xl leading-normal mb-4">Kubernetes est un outil remarquable pour la mise en place de plateformes.</h3>
          </div>
      </div>
  </section>

  <section class="relative md:py-24 py-16">
    <div class="container relative">
      <div class="grid grid-cols-1 grid-rows-1">
        <p class="text-justify text-lg text-400">Techniquement, une plateforme est un ensemble de services et d'outils qui supporte les applications de manière standardisée. Cependant, les avantages d'une plateforme vont bien au-delà de l'aspect technique. Elle devient une véritable interface de communication et un cadre organisationnel entre les équipes applicatives et les équipes infrastructure.</p>
        <p class="text-justify text-lg text-400">Il est donc crucial de définir minutieusement les besoins des applications, en collaboration étroite entre les équipes applicatives et infrastructure, afin d’y répondre de manière optimale grâce à une plateforme construite sur Kubernetes et son vaste écosystème.</p>
        <p class="text-justify text-lg text-400">Kubernetes est un projet extrêmement mature, qui, avec son écosystème riche, permet la mise en place de plateformes performantes au sein des entreprises, garantissant ainsi des niveaux de service exceptionnels.</p>
      </div>
    </div><!--end container-->
  </section><!--end section auteur-->
