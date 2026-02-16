# Awesome Agent Ecosystem [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated list of tools, frameworks, and platforms integrated with the [Agent OS](https://github.com/imran-siddique/agent-os) + [AgentMesh](https://github.com/imran-siddique/agent-mesh) + [Agent SRE](https://github.com/imran-siddique/agent-sre) governance stack.

Only tools with working integrations are listed. If it's here, it works with our stack.

## Contents

- [The Stack](#the-stack)
- [Framework Integrations](#framework-integrations)
- [IDE & AI Assistant Extensions](#ide--ai-assistant-extensions)
- [Protocol Support](#protocol-support)
- [Observability & SRE Integrations](#observability--sre-integrations)
- [Alerting & Notifications](#alerting--notifications)
- [Industry Templates](#industry-templates)
- [Deployment & Infrastructure](#deployment--infrastructure)
- [Community Integrations](#community-integrations)

## The Stack

*The core governance-to-reliability platform.*

- [Agent OS](https://github.com/imran-siddique/agent-os) - Kernel architecture for AI agents with POSIX-inspired primitives, deterministic policy enforcement, and flight recorder audit logging.
- [AgentMesh](https://github.com/imran-siddique/agent-mesh) - Identity, trust, and networking layer for multi-agent systems with DID-based identity, delegation chains, reward scoring, and MCP governance proxy.
- [Agent SRE](https://github.com/imran-siddique/agent-sre) - Reliability engineering for AI agents with SLOs, error budgets, chaos testing, progressive delivery, cost guardrails, and incident management.

## Framework Integrations

*Agent frameworks with built-in Agent OS governance adapters.*

- [LangChain](https://github.com/langchain-ai/langchain) - Governed via `LangChainKernel().wrap(my_chain)` in Agent OS. AgentMesh LangChain integration for secure agents with policies. Agent SRE LangChain callback handler for SLI collection.
- [CrewAI](https://github.com/joaomdmoura/crewAI) - Governed via `CrewAIKernel().wrap(my_crew)` in Agent OS. AgentMesh CrewAI integration for multi-agent crew governance. Agent SRE CrewAI adapter for reliability monitoring.
- [AutoGen](https://github.com/microsoft/autogen) - Governed via `AutoGenKernel().wrap(autogen_agent)` in Agent OS. Agent SRE AutoGen adapter for SLO tracking.
- [LangGraph](https://github.com/langchain-ai/langgraph) - AgentMesh LangGraph integration with trust checkpoints for graph workflows. Agent SRE LangGraph adapter for reliability monitoring.
- [OpenAI Agents SDK](https://platform.openai.com/docs/agents) - Governed via `OpenAIAgentsSDKKernel().wrap(agent)` in Agent OS. Agent SRE OpenAI Agents SDK adapter for SLI collection.
- [OpenAI Assistants](https://platform.openai.com/docs/assistants) - Governed via `OpenAIKernel().wrap_assistant(assistant, client)` in Agent OS.
- [Semantic Kernel](https://github.com/microsoft/semantic-kernel) - Governed via `SemanticKernelWrapper().wrap(sk_kernel)` in Agent OS. Agent SRE Semantic Kernel adapter for kernel/plugin/function tracking.
- [OpenAI Swarm](https://github.com/openai/swarm) - AgentMesh Swarm integration with trust-verified handoffs between agents.
- [Dify](https://github.com/langgenius/dify) - AgentMesh trust middleware for Dify workflows via [agentmesh-integrations](https://github.com/imran-siddique/agentmesh-integrations/tree/master/dify). Agent SRE Dify adapter for workflow/node/HTTP request tracking.
- [LlamaIndex](https://github.com/run-llama/llama_index) - Agent OS and AgentMesh integrated via [LlamaIndex PR #20644](https://github.com/run-llama/llama_index/pull/20644). Agent SRE LlamaIndex callback handler for query/retriever/LLM tracking.

## IDE & AI Assistant Extensions

*Extensions that bring Agent OS governance into your development environment.*

- [MCP Server](https://www.npmjs.com/package/agentos-mcp-server) - Works with Claude Desktop, GitHub Copilot, and Cursor. Install with `npx agentos-mcp-server`. 10 tools for agent creation, policy enforcement, and compliance checking.
- [VS Code Extension](https://marketplace.visualstudio.com/items?itemName=agent-os.agent-os-vscode) - Real-time policy checks, enterprise features. Published on VS Code Marketplace.
- [GitHub Copilot Extension](https://github.com/imran-siddique/agent-os/tree/master/extensions/copilot) - GitHub Copilot extension with Vercel/Docker deployment.
- [JetBrains Plugin](https://github.com/imran-siddique/agent-os/tree/master/extensions/jetbrains) - IntelliJ, PyCharm, WebStorm plugin (Kotlin).
- [Cursor Extension](https://github.com/imran-siddique/agent-os/tree/master/extensions/cursor) - Cursor IDE extension with Composer integration.
- [Chrome Extension](https://github.com/imran-siddique/agent-os/tree/master/extensions/chrome) - Browser extension for GitHub, Jira, AWS, and GitLab.
- [GitHub CLI Extension](https://github.com/imran-siddique/agent-os/tree/master/extensions/github-cli) - `gh agent-os` CLI extension.
- [AgentMesh MCP Proxy](https://github.com/imran-siddique/agent-mesh) - Transparent governance proxy for any MCP server. Wraps Claude Desktop, Copilot, or Cursor tool access with policy enforcement, trust scoring, and audit logs.

## Protocol Support

*Standards and protocols with native integrations.*

- [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) - Agent OS MCP kernel server for Claude Desktop integration. AgentMesh trust-gated MCP server/client. Agent SRE MCP drift detection with tool schema fingerprinting. Agent SRE MCP server exposing 5 self-monitoring tools for reliability-aware agents.
- [Agent-to-Agent Protocol (A2A)](https://github.com/google/A2A) - AgentMesh full A2A adapter for inter-agent coordination. Agent SRE A2A-aware distributed tracing with W3C context propagation.
- [Inter-Agent Trust Protocol (IATP)](https://github.com/imran-siddique/agent-os/tree/master/modules/iatp) - Native sidecar trust protocol in Agent OS with typed IPC pipes. AgentMesh uses IATP for trust handshakes.
- [SPIFFE/SVID](https://spiffe.io/) - AgentMesh identity layer with SPIFFE workload identity and Agent CA.
- [Decentralized Identifiers (DIDs)](https://www.w3.org/TR/did-core/) - AgentMesh DID-based agent identity with Ed25519 keys.
- [OpenTelemetry](https://opentelemetry.io/) - Agent OS observability module with OTEL tracing. Agent SRE native OTLP export for all SLIs and traces with custom semantic conventions.

## Observability & SRE Integrations

*Monitoring and reliability tools with Agent SRE bridges.*

- [Prometheus](https://prometheus.io/) - Agent OS Prometheus metrics via observability module. Agent SRE native `/metrics` Prometheus text format endpoint with SLO gauges and counters.
- [Grafana](https://grafana.com/) - Pre-built dashboards in Agent OS production examples. Agent SRE pre-built Grafana dashboard JSON at `dashboards/agent-sre-overview.json` with SLO status, error budgets, burn rate, cost, and incidents panels.
- [Jaeger](https://www.jaegertracing.io/) - Distributed tracing in Agent OS production examples. Agent SRE OTLP-compatible span export.
- [Langfuse](https://langfuse.com/) - Agent SRE Langfuse integration for SLO scoring and cost observation export.
- [LangSmith](https://smith.langchain.com/) - Agent SRE LangSmith exporter with run tracing, evaluation feedback, and parent-child run support.
- [Arize / Phoenix](https://arize.com/) - Agent SRE Arize/Phoenix integration for span export and evaluation import.
- [Braintrust](https://www.braintrust.dev/) - Agent SRE Braintrust exporter for eval-driven monitoring and experiment tracking.
- [Helicone](https://helicone.ai/) - Agent SRE Helicone integration with header injection for proxy-based cost/latency tracking and SLO feedback logging.
- [Datadog](https://www.datadoghq.com/) - Agent SRE Datadog exporter for LLM monitoring metrics and events.
- [AgentOps](https://www.agentops.ai/) - Agent SRE AgentOps exporter for session recording and event tracking.
- [Weights & Biases](https://wandb.ai/) - Agent SRE W&B exporter for experiment tracking with SRE metrics and SLO data.
- [MLflow](https://mlflow.org/) - Agent SRE MLflow exporter for experiment logging with SLO evaluations and cost tracking.

## Alerting & Notifications

*Alert channels supported by Agent SRE AlertManager.*

- [Slack](https://slack.com/) - Agent SRE Slack webhook alerting with block-based messages, severity badges, and agent/SLO context.
- [PagerDuty](https://www.pagerduty.com/) - Agent SRE PagerDuty Events API v2 with dedup keys, trigger/resolve actions, and custom severity mapping.
- [OpsGenie](https://www.atlassian.com/software/opsgenie) - Agent SRE OpsGenie Alert API with priority mapping (P1-P5), agent tags, and SLO alias deduplication.
- [Microsoft Teams](https://www.microsoft.com/en-us/microsoft-teams) - Agent SRE Microsoft Teams incoming webhook with Adaptive Card format and severity-colored notifications.

## Industry Templates

*Production-ready governance templates for specific industries.*

- [Healthcare HIPAA](https://github.com/imran-siddique/agent-os/tree/master/examples/healthcare-hipaa) - Agent OS HIPAA-compliant agent governance template. AgentMesh [HIPAA example](https://github.com/imran-siddique/agent-mesh/tree/master/examples/03-healthcare-hipaa) with PHI protection and Merkle audit.
- [Finance SOC2](https://github.com/imran-siddique/agent-os/tree/master/examples/finance-soc2) - Agent OS SOC2-compliant agent governance template.
- [Customer Service](https://github.com/imran-siddique/agent-os/tree/master/examples/customer-service) - Agent OS customer support agent. AgentMesh [multi-agent customer service](https://github.com/imran-siddique/agent-mesh/tree/master/examples/02-customer-service) with delegation chains and trust handshakes.
- [DevOps Automation](https://github.com/imran-siddique/agent-mesh/tree/master/examples/04-devops-automation) - AgentMesh just-in-time DevOps credentials with ephemeral creds and capability scoping.
- [Legal Review](https://github.com/imran-siddique/agent-os/tree/master/examples/legal-review) - Agent OS legal document analysis agent.
- [Carbon Auditor](https://github.com/imran-siddique/agent-os/tree/master/examples/carbon-auditor) - Agent OS multi-model verification with Docker + Grafana + Prometheus + Jaeger.
- [DeFi Sentinel](https://github.com/imran-siddique/agent-os/tree/master/examples/defi-sentinel) - Agent OS real-time attack detection with full observability stack.
- [Pharma Compliance](https://github.com/imran-siddique/agent-os/tree/master/examples/pharma-compliance) - Agent OS pharmaceutical document analysis with compliance automation.
- [GitHub PR Review](https://github.com/imran-siddique/agent-mesh/tree/master/examples/05-github-integration) - AgentMesh code review agent with output policies, shadow mode, and trust decay.

## Deployment & Infrastructure

*Infrastructure tools with ecosystem support.*

- [Docker](https://www.docker.com/) - Agent OS Dockerfile and production example docker-compose stacks. AgentMesh multi-container deployment (server, sidecar, dev). Agent SRE Docker Compose with quickstart, LangChain monitor, and REST API services.
- [Kubernetes](https://kubernetes.io/) - AgentMesh GoverndAgent CRD and Kubernetes examples. Agent SRE AgentSLO and CostBudget CRDs, AgentRollout reconciler, Helm chart with Deployment/Service/CRD templates.
- [Helm](https://helm.sh/) - Agent SRE Helm chart at `deployments/helm/agent-sre` with configurable values.
- [GitHub Actions](https://github.com/features/actions) - Agent SRE canary deployment composite action at `.github/actions/canary-deploy/` for progressive delivery in CI/CD pipelines.
- [Gitpod](https://gitpod.io/) - Agent OS one-click browser development via [Open in Gitpod](https://gitpod.io/#https://github.com/imran-siddique/agent-os).

## Community Integrations

*Third-party projects that have integrated with the ecosystem.*

- [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) - Agent OS and AgentMesh featured in the awesome-llm-apps curated list.
- [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) - Agent OS MCP server listed in awesome-mcp-servers.
- [Microsoft agent-lightning](https://github.com/microsoft/agent-lightning/tree/main/contrib/recipes/agentos) - Agent OS recipe integrated in Microsoft's agent-lightning project.

## Contributing

Contributions welcome! If your tool integrates with Agent OS, AgentMesh, or Agent SRE, please read the [contribution guidelines](CONTRIBUTING.md) and submit a PR.
