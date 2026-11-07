# Content roadmap

Articles bring search traffic to the book. Each one targets one search intent, links to
other articles and to the book. Keep this file updated when an article is published or
planned.

## Published (fr)

| URL | Main keyword | Published | Updated |
| --- | ------------ | --------- | ------- |
| `/fr/qu-est-ce-que-kubernetes` | qu'est-ce que kubernetes | 2024-09-09 | 2026-11-07 |
| `/fr/multi-cluster-kubernetes` | kubernetes multi-cluster | 2024-09-15 | 2026-11-07 |
| `/fr/edge-computing-avec-kubernetes` | edge computing kubernetes | 2024-08-14 | 2026-11-07 |
| `/fr/operator-or-not-operator` | kubernetes operator | 2024-08-01 | 2026-11-07 |

## Ideas (stubs in `content/drafts/`)

Ordered by estimated search demand in French. Suggested angle: the book's point of view
(platform/PaaS thinking, pragmatism, few tools, high service levels).

| Draft file | Suggested title | Main keyword | Link to |
| ---------- | --------------- | ------------ | ------- |
| `what-is-k8s-cluster.rst` | Cluster Kubernetes : architecture et composants expliqués | cluster kubernetes | qu-est-ce-que-kubernetes |
| `helm-vs-kustomize.rst` | Helm ou Kustomize : comment choisir ? | helm vs kustomize | argocd-vs-flux |
| `argocd-vs-flux.rst` | Argo CD ou Flux : quel outil GitOps pour Kubernetes ? | argocd vs flux | helm-vs-kustomize, operator |
| `prometheus-grafana.rst` | Superviser Kubernetes avec Prometheus et Grafana | prometheus grafana kubernetes | kubernetes-autoscaler |
| `kubernetes-autoscaler.rst` | Autoscaling Kubernetes : HPA, VPA et Cluster Autoscaler | kubernetes autoscaling | prometheus-grafana |
| `what-is-k3s.rst` | K3s : la distribution Kubernetes légère (et quand l'utiliser) | k3s | microk8s, edge computing |
| `microk8s.rst` | MicroK8s, K3s, Kind : quelle distribution Kubernetes locale ? | microk8s | what-is-k3s |
| `service-mesh-istio.rst` | Service mesh et Istio : en avez-vous vraiment besoin ? | istio kubernetes | multi-cluster |
| `opa-gatekeeper.rst` | Sécuriser Kubernetes avec OPA Gatekeeper | opa gatekeeper | operator |
| `k8s-lens.rst` | Lens : l'IDE pour piloter vos clusters Kubernetes | kubernetes lens | |

`kubernetes-autoscaler.rst` was published as an empty placeholder until 2026-11; it was
moved to drafts (the URL `/fr/kubernetes-autoscaler` will be reused when it is written).

## Cadence

One article every 2–4 weeks is enough on a niche; quality and internal links matter more
than volume. Announce each article in the newsletter.
