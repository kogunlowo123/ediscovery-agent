# eDiscovery Agent

[![CI](https://github.com/kogunlowo123/ediscovery-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/kogunlowo123/ediscovery-agent/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Category**: Legal | **Cloud**: MULTI-CLOUD | **LLM**: gpt-4o

eDiscovery agent that manages document collection and preservation, applies search and review workflows, performs technology-assisted review, tracks custodian compliance, and generates production reports.

---

## Domain-Specific Tools

| Tool | Description |
|------|-------------|
| `initiate_hold` | Initiate legal hold and notify custodians |
| `collect_documents` | Collect documents from specified data sources |
| `run_tar` | Run technology-assisted review on document collection |
| `track_custodian_compliance` | Track custodian acknowledgment and compliance with legal hold |
| `generate_production` | Generate document production in required format |

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/api/v1/ediscovery/analyze` | Analyze |
| `POST` | `/api/v1/ediscovery/search` | Search |
| `POST` | `/api/v1/ediscovery/generate` | Generate document |
| `GET` | `/api/v1/ediscovery/track` | Track status |
| `POST` | `/api/v1/ediscovery/report` | Generate report |

## Features

- Ediscovery
- Compliance
- Audit Trail

## Integrations

- Relativity
- Logikcull
- Ironclad
- Docusign Clm
- Westlaw

## Architecture

```
ediscovery-agent/
├── src/
│   ├── agent/              # Domain-specific agent logic
│   │   ├── ediscovery_agent_agent.py  # Main agent with domain tools
│   │   ├── tools.py        # 5 domain-specific tools
│   │   └── prompts.py      # Expert system prompts
│   ├── api/                # FastAPI routes
│   │   └── routes/
│   │       ├── domain.py   # 5 domain-specific endpoints
│   │       └── health.py   # Health check
│   ├── connectors/         # 5 integration connectors
│   ├── config/             # Settings and configuration
│   ├── models/             # Domain-specific Pydantic schemas
│   ├── rag/                # RAG pipeline
│   ├── mcp/                # MCP server
│   └── a2a/                # Agent-to-agent protocol
├── tests/
├── infrastructure/         # Terraform, K8s, Helm, Docker
├── dashboard/              # Next.js frontend
└── docs/                   # Architecture and deployment docs
```

## Quick Start

```bash
# Install
pip install -e ".[dev]"

# Run
make dev

# Test
make test

# Docker
docker compose up -d
```

## Primary Service

**Legal Tech Platform + LLM + Document Management**

---

Built as part of the Enterprise AI Agent Platform.
