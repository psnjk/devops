# Monitoring report
  
## Lab 7
```docker-compose.yaml``` includes 4 services:
- Python application
- Promtail
- Loki
- Grafana
  
Loki is configured in Grafana at localhost:3000 :
![Loki](screenshots/grafana_loki_configured.png)
Logs example:
![Logs](screenshots/grafana_logs_example.png)

## Lab 7
### Internal docker logging with prometheus
Now ```docker-compose.yaml``` includes also prometheus service available at port ```9090```.
It uses ```host.docker.internal:9090``` for metrics.
Grafana Loki dashboard:
![Loki Dashboard](screenshots/loki_dashboard.png)
Grafana Prometheus dashboard:
![Loki Dashboard](screenshots/prometheus_docker_internal_metrics.png)