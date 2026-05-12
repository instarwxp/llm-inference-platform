# LLM Inference Platform

A production-oriented multi-model LLM inference platform built with Ollama, Docker, and Kubernetes. Designed for self-hosted deployment with unified API access, monitoring, and auto-scaling.

> 🚧 **Status: Active Development** — Building in public. Follow along with the progress.

---

## Architecture

```
┌─────────────────────────────────────────────┐
│              Client Applications             │
└─────────────────┬───────────────────────────┘
                  │ HTTP REST API
┌─────────────────▼───────────────────────────┐
│              API Gateway (FastAPI)           │
│         Unified endpoint for all models      │
└──────┬──────────────────────┬───────────────┘
       │                      │
┌──────▼──────┐        ┌──────▼──────┐
│  Llama 3.2  │        │   Mistral   │
│  (Ollama)   │        │  (Ollama)   │
└─────────────┘        └─────────────┘
       │                      │
┌──────▼──────────────────────▼───────────────┐
│         Prometheus + Grafana                 │
│    Metrics: QPS / Latency / Memory Usage     │
└─────────────────────────────────────────────┘
```

---

## Features

- **Multi-model support** — Run and switch between multiple open-source LLMs (Llama 3.2, Mistral, and more)
- **Unified REST API** — Single endpoint regardless of which model is serving
- **Containerized** — Full Docker Compose setup for local development
- **Kubernetes-ready** — K8s manifests with HPA (Horizontal Pod Autoscaler)
- **Observability** — Prometheus metrics + Grafana dashboards out of the box
- **Self-hosted** — No API keys, no cloud costs, runs on your own hardware

---

## Tech Stack

| Component | Technology |
|---|---|
| LLM Runtime | [Ollama](https://ollama.ai) |
| API Gateway | FastAPI (Python) |
| Containerization | Docker + Docker Compose |
| Orchestration | Kubernetes (K8s) |
| Monitoring | Prometheus + Grafana |
| IaC | Terraform (AWS deployment) |

---

## Getting Started

### Prerequisites

- Docker & Docker Compose
- 8GB+ RAM (16GB recommended for multiple models)
- [Ollama](https://ollama.ai/download) installed

### Quick Start

```bash
# Clone the repository
git clone https://github.com/instarwxp/llm-inference-platform.git
cd llm-inference-platform

# Pull required models
ollama pull llama3.2
ollama pull mistral

# Start the platform
docker compose up -d

# Test the API
curl http://localhost:8000/health
```

### API Usage

```bash
# Send a prompt to the default model
curl -X POST http://localhost:8000/api/chat \
  -H "Content-Type: application/json" \
  -d '{"model": "llama3.2", "message": "Hello, how are you?"}'

# List available models
curl http://localhost:8000/api/models
```

---

## Project Roadmap

- [x] Local Ollama setup with llama3.2
- [x] WSL2 + Docker environment
- [ ] FastAPI gateway with model routing
- [ ] Docker Compose multi-service setup
- [ ] Prometheus metrics integration
- [ ] Grafana dashboard
- [ ] Kubernetes manifests + HPA
- [ ] Load testing & performance benchmarks
- [ ] Terraform AWS deployment

---

## Monitoring

Once running, access the dashboards at:

| Service | URL |
|---|---|
| API Gateway | http://localhost:8000 |
| Grafana | http://localhost:3000 |
| Prometheus | http://localhost:9090 |
| Ollama API | http://localhost:11434 |

---

## Performance Targets

| Metric | Target |
|---|---|
| P99 Latency | < 2000ms |
| Concurrent Requests | 20+ |
| Model Switch Time | < 5s |
| Uptime | 99.9% |

---

## Development Log

| Date | Milestone |
|---|---|
| 2026-05-12 | Project initialized, Ollama + Docker environment ready |

---

## About

Built by a DevOps/Infrastructure engineer transitioning into AI Infrastructure engineering. This project documents the journey of building production-grade LLM serving infrastructure from scratch.

**Skills demonstrated:** Linux · Docker · Kubernetes · CI/CD · Monitoring · Python · LLM Deployment

---

## License

MIT License — feel free to use this as a reference for your own LLM infrastructure projects.
