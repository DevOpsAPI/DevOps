resource "digitalocean_kubernetes_cluster" "games-cluster" {
  name    = "games-cluster"
  region  = "ams3"  # Update to your preferred region
  version = "1.29.5-do.0" # Update to your preferred version
  registry_integration = true

  node_pool {
    name       = var.droplet_name
    size       = "s-2vcpu-2gb" # Adjust based on your needs
    node_count = 1
  }
}

resource "kubernetes_deployment" "games_app" {
  depends_on = [digitalocean_kubernetes_cluster.games-cluster]
  metadata {
    name = "games-app"
  }

  spec {
    replicas = 5

    selector {
      match_labels = {
        app = "games-app"
      }
    }

    template {
      metadata {
        labels = {
          app = "games-app"
        }
      }

      spec {
        container {
          name  = "games-app"
          image = "registry.digitalocean.com/devopsapi/api:1.1"
          env {
            name  = "MYSQL_HOST"
            value = var.db_host
          }
          env {
            name  = "MYSQL_DB"
            value = var.db_name
          }
          env {
            name  = "MYSQL_PORT"
            value = var.db_port
          }
          env {
            name  = "MYSQL_USER"
            value = var.db_user
          }
          env {
            name  = "MYSQL_PASSWORD"
            value = var.db_password
          }
          port {
            container_port = 8080
          }
        }
      }
    }
  }
}

resource "kubernetes_service" "games_app_service" {
  depends_on = [kubernetes_deployment.games_app]
  metadata {
    name = "games-app-service"
  }

  spec {
    selector = {
      app = "games-app"
    }
    port {
      port        = 80
      target_port = 8080
    }
    type = "LoadBalancer"
  }
}

resource "helm_release" "kube_prometheus_stack" {
  depends_on = [kubernetes_deployment.games_app]
  name       = "kube-prometheus-stack"
  repository = "https://prometheus-community.github.io/helm-charts"
  chart      = "kube-prometheus-stack"

  set {
    name  = "grafana.enabled"
    value = "true"
  }
}

resource "kubernetes_service" "prometheus_lb" {
  depends_on = [ helm_release.kube_prometheus_stack ]
  metadata {
    name = "prometheus-grafana-lb"
  }
  spec {
    selector = {
      "app.kubernetes.io/name" = "grafana"
      "app.kubernetes.io/instance" = "kube-prometheus-stack"
    }
    port {
      port        = 80
      target_port = 3000
    }
    type = "LoadBalancer"
  }
}

