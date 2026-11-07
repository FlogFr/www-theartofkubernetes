Operator ou pas Operator ? Avantages et limites des Operators Kubernetes
########################################################################

:lang: fr
:date: 2024-08-01
:modified: 2026-11-07
:slug: operator-or-not-operator
:category: Kubernetes
:tags: kubernetes, operator, operators kubernetes, crd, administration, architecture, infrastructure
:authors: Florian Grignon
:seo_title: Operators Kubernetes : avantages, limites et bons usages
:description: Les Operators automatisent la gestion d'applications dans Kubernetes. Avantages, risques et cas où les utiliser : l'avis de l'auteur de The Art of Kubernetes.
:summary: Le modèle d'Operator occupe une place centrale dans l'écosystème Kubernetes en automatisant la gestion d'applications complexes au sein du cluster. Mais faut-il en déployer partout ? Avantages, limites et recommandations.
:logo: logo-operator.webp

Kubernetes est conçu pour prendre en charge tout type d'application conteneurisée de
manière performante et résiliente. Sa flexibilité constitue un atout majeur : elle lui
permet d'étendre ses fonctionnalités afin de supporter les divers services et outils d'une
plateforme, tout en optimisant l'utilisation des ressources d'infrastructure d'une
entreprise.

Gérer le cycle de vie des applications dans Kubernetes
======================================================

Les outils intégrés à une plateforme facilitent la gestion du cycle de vie des applications
et des services. Par exemple, un bon système de déploiement continu (CD) permet de gérer
efficacement les déploiements au sein de votre parc.

Un autre système de gestion du cycle de vie des applications s'est imposé dans
l'écosystème Kubernetes : celui des **Operators**. Ces derniers occupent désormais une place
centrale en automatisant la gestion d'applications complexes directement au sein du
cluster Kubernetes.

Comme je le développe dans `The Art of Kubernetes </>`__, Kubernetes et son écosystème
permettent de définir des plateformes efficaces pour chaque entreprise, avec les outils
adaptés pour gérer le cycle de vie des applications et des services. Pour des raisons que
je vais détailler, je recommande pourtant de recourir aux Operators uniquement dans des cas
spécifiques. Dans d'autres situations, vous pouvez facilement gérer le service vous-même ou
opter pour un service externalisé.

Qu'est-ce qu'un Operator Kubernetes ?
=====================================

Un Operator est une extension de Kubernetes qui encapsule la logique opérationnelle d'une
application spécifique dans des contrôleurs personnalisés, en s'appuyant sur des
*Custom Resource Definitions* (CRD), une fonctionnalité de Kubernetes qui permet de définir
de nouvelles ressources. C'est en quelque sorte un « opérateur humain » codifié, capable de
gérer des tâches complexes telles que le déploiement, la mise à jour, la sauvegarde, la
restauration et même la mise à l'échelle de l'application, le tout de manière automatisée.

Un Operator surveille ces ressources personnalisées et réagit aux événements associés en
exécutant des actions prédéfinies pour gérer l'état de l'application. Il gère ainsi le
cycle de vie d'une application ou d'un service, *stateful* ou *stateless*, de son
installation à sa désinstallation, en passant par ses différents états fonctionnels. Il
ajoute une couche de logique supplémentaire entre l'administrateur et l'application, ce qui
nécessite des droits élevés, au minimum équivalents à ceux de l'administrateur du service
concerné.

Prenons l'exemple de l'Operator PostgreSQL `CloudNativePG <https://cloudnative-pg.io/>`__.
Il met à disposition de l'administrateur du cluster des CRD comme ``Cluster``, ``Backup``
ou ``ScheduledBackup``. Pour déployer un cluster PostgreSQL à l'intérieur de votre cluster
Kubernetes, il suffit de créer un objet ``Cluster`` dans l'API Kubernetes avec les bons
paramètres, puis de laisser l'Operator faire sa magie : il déploiera les Pods, Services et
PersistentVolumes nécessaires pour obtenir un cluster PostgreSQL fonctionnel.

L'automatisation, une arme à double tranchant
=============================================

L'avantage principal des Operators réside dans leur capacité à automatiser des tâches
complexes qui, autrement, nécessiteraient une intervention humaine. Par exemple, la mise à
jour d'une base de données *stateful*, avec toutes ses spécificités, peut être entièrement
gérée par un Operator, minimisant ainsi les risques d'erreurs.

.. pull-quote::

   Si les Operators automatisent l'exploitation d'un service, ils posent également un défi
   en déléguant les décisions critiques à un logiciel plutôt qu'à un expert humain.

Cependant, ce même avantage peut se transformer en inconvénient : l'administrateur risque
de se reposer entièrement sur l'Operator et de perdre la connaissance approfondie de la
logique de l'application. Il pourrait alors négliger la documentation et ne plus maîtriser
suffisamment l'application pour la déployer et la maintenir en état de fonctionnement, ce
qui pourrait avoir des conséquences graves en cas de problème majeur. L'opérateur humain
doit rester expert des services qu'il administre.

C'est un peu comme balayer la poussière sous le tapis : la poussière est toujours là, et
vous risquez toujours d'y être allergique. Il n'existe pas de raccourci pour maîtriser un
logiciel et atteindre un haut niveau de service : cela nécessite une solide expertise, de
la pratique, ainsi qu'un investissement en temps.

.. pull-quote::

   Les choix que vous déléguez à un Operator ne vous exemptent pas d'en assumer les
   conséquences, qu'elles soient positives ou négatives.

Standardisation et reproductibilité : une promesse trompeuse ?
==============================================================

Les Operators jouent un rôle essentiel dans la standardisation de la gestion des
applications et des services, en garantissant que les meilleures pratiques sont appliquées
de manière cohérente à travers différents environnements. Cette reproductibilité s'avère
particulièrement utile dans des contextes multi-environnements ou
`multi-clusters <{filename}multi-cluster.rst>`__, où il est crucial que les applications
soient déployées et maintenues de manière uniforme.

Cette standardisation peut cependant s'avérer trompeuse. En ajoutant une couche automatisée
qui gère le cycle de vie du logiciel, comment être certain que ce logiciel se trouve dans
le même état dans deux environnements différents ? Cela devient presque impossible si vous
ne contrôlez pas l'ensemble de l'état de l'Operator, qui dépend de tout l'environnement. Cela
pose un réel problème dans les environnements d'intégration continue (CI), où la
reproductibilité et l'idempotence sont des notions essentielles pour garantir la fiabilité
des résultats.

Des Operators qui ne couvrent pas tous les besoins
==================================================

Les Operators disponibles ne couvrent pas nécessairement l'ensemble des besoins
opérationnels d'une application. Il est donc possible qu'un Operator limite votre capacité à
maintenir le service dans un état pleinement fonctionnel. Une migration de l'application
ou du service est-elle prise en compte par l'Operator ? Et même si c'est le cas,
préférez-vous effectuer la migration à l'aide d'un Operator automatisé ou d'un opérateur
humain ?

Résilience : qui décide en cas d'incident ?
===========================================

En automatisant la gestion des erreurs et en surveillant continuellement l'état des
applications, les Operators contribuent à améliorer la disponibilité et la résilience des
services. Un Operator peut par exemple détecter un dysfonctionnement et prendre
automatiquement des mesures correctives, comme le redémarrage d'un composant défaillant ou
la restauration à partir d'une sauvegarde.

Mais là encore, le choix de la résolution des dysfonctionnements est laissé à un composant
logiciel plutôt qu'à un expert de l'application. Cette automatisation peut entraîner
l'application dans un état non seulement indésirable, mais aussi problématique, sans
possibilité de retour en arrière.

Le vrai intérêt : des Operators sur mesure pour vos applications
================================================================

Je vais probablement m'écarter de ce que vous avez déjà entendu à propos des Operators,
mais je pense que leur efficacité et leur utilité résident dans les **Operators
personnalisés pour vos propres applications**. En développant un Operator adapté à vos
besoins, vous pouvez l'utiliser facilement comme un service au sein de votre plateforme
Kubernetes, sans dépendre de nombreux outils tiers. La logique de gestion du cycle de vie de
vos applications étant intégrée dans l'Operator, vous pouvez instancier votre application
aisément pour la tester depuis une autre plateforme.

Attention cependant : le développement d'un Operator peut s'avérer complexe et nécessite une
compréhension approfondie de Kubernetes. Cette complexité peut constituer une barrière à
l'adoption, en particulier pour les petites équipes ou les entreprises qui ne disposent pas
des compétences nécessaires en interne.

Maintenance et charge cognitive : le coût caché des Operators
=============================================================

Comme tout composant logiciel de votre cluster, un Operator doit être maintenu, mis à jour
et corrigé en cas de bugs ou de vulnérabilités. Cela implique un effort de maintenance
continu, qui peut devenir coûteux si l'Operator est complexe ou s'il doit évoluer avec
l'application qu'il gère. Cet effort doit également être pris en compte dans les cas
critiques, comme une migration de l'application.

Pour les équipes qui gèrent déjà un grand nombre d'outils et de services, l'ajout
d'Operators peut aussi contribuer à une surcharge cognitive. Comprendre et gérer les
différents Operators déployés dans un cluster peut devenir complexe, en particulier lorsque
chacun a ses propres configurations et comportements.

Conclusion : utiliser les Operators avec parcimonie
===================================================

Les Operators sont aujourd'hui très (voire trop) répandus : plus de 277 étaient déjà
référencés sur `OperatorHub <https://operatorhub.io/>`__ en 2024, et il est désormais possible
de déployer presque n'importe quel composant logiciel open source avec un Operator. Il est
cependant crucial de bien peser les avantages et les inconvénients d'un Operator par
rapport à d'autres méthodes pour gérer le cycle de vie d'un composant logiciel.

Je vous recommande donc d'utiliser les Operators avec parcimonie : principalement pour
transformer vos propres applications en services au sein d'une plateforme, et dans les cas
où vous n'avez pas d'autre choix.
