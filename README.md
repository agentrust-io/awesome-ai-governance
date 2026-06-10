# Awesome AI Agent Governance [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated list of tools, frameworks, standards, and resources for governing autonomous AI agents — covering safety, trust, identity, observability, and compliance across the agent lifecycle.

AI agents now hold real reach: email, CRMs, databases, financial systems. Guardrails at the content layer probably hold — but enterprises need to run on proof, not probability. This list tracks the tools and practices for making agents safe, auditable, and trustworthy in production.

## Contents

- [Governance Frameworks](#governance-frameworks)
- [Policy as Code](#policy-as-code)
- [LLM Safety & Guardrails](#llm-safety--guardrails)
- [Agent Frameworks with Governance Features](#agent-frameworks-with-governance-features)
- [Agent Identity & Attestation](#agent-identity--attestation)
- [Observability & Monitoring](#observability--monitoring)
- [Security Testing](#security-testing)
- [Standards & Specifications](#standards--specifications)
- [Research Papers](#research-papers)
- [Industry Reports & Guidance](#industry-reports--guidance)
- [Conferences & Communities](#conferences--communities)

## Governance Frameworks

*Dedicated platforms and control planes for governing AI agent behavior, enforcing policies, and maintaining trust at runtime.*

- [Agent Governance Toolkit (AGT)](https://github.com/microsoft/agent-governance-toolkit) - Production governance layer for autonomous agents with a policy enforcement kernel (<0.1ms p99), execution rings (Ring 0-3), cryptographic Merkle audit logs, and integrations across LangChain, CrewAI, AutoGen, Google ADK, and more. Python + .NET + Rust. Now stewarded by the Agentic AI Foundation. ★4000+
- [Agent Hypervisor](https://github.com/imran-siddique/agent-hypervisor) - Runtime supervisor for AI agents with execution rings, saga compensation, joint liability, and kill-switch controls.
- [Agent Manifest](https://github.com/agentrust-io/agent-manifest) - Hardware-anchored SDK that binds all 10 deployment artifacts (model, tools, policy, identity, etc.) into a single cryptographically signed manifest. Python + TypeScript.
- [Agent OS](https://github.com/imran-siddique/agent-os) - Kernel-level governance with POSIX-inspired primitives, policy interception, and OWASP Agentic Top 10 coverage. Integrates with LangChain, CrewAI, AutoGen, PydanticAI, and smolagents.
- [Agent SRE](https://github.com/imran-siddique/agent-sre) - Site reliability engineering for AI agents: SLOs, error budgets, chaos testing, circuit breakers, and cascading failure detection.
- [AgentMesh](https://github.com/imran-siddique/agent-mesh) - Zero-trust networking for AI agents with DID identity, behavioral trust scoring, delegation chains, and MCP governance proxy.
- [cMCP](https://github.com/agentrust-io/cmcp) - Confidential MCP Gateway. Hardware-attested policy enforcement for MCP tool calls — every tool invocation verified in silicon before execution.
- [Coral Server](https://github.com/Coral-Protocol/coral-server) - Agent coordination and trust server enabling safe multi-agent collaboration with structured communication protocols.
- [Cordum](https://github.com/cordum-io/cordum) - Agent control plane providing governance, lifecycle management, and policy enforcement for autonomous agents.
- [Gate22](https://github.com/aipotheosis-labs/gate22) - MCP gateway with role-based access control, audit logging, and fine-grained permission management for tool access.
- [IBM mcp-context-forge](https://github.com/IBM/mcp-context-forge) - Enterprise MCP gateway with context-aware guardrails, request routing, and compliance controls.
- [Invariant Guardrails](https://github.com/invariantlabs-ai/invariant) - Rule-based guardrails engine with policy-as-code, trace analysis, and real-time intervention for agentic applications.
- [LiteLLM](https://github.com/BerriAI/litellm) - Unified LLM gateway with spend tracking, rate limiting, guardrails, and access controls across 100+ LLM providers.
- [TRACE](https://github.com/agentrust-io/trace-spec) - Open attestation standard for agentic AI governance. Each agent action produces a verifiable compliance claim anchored in an append-only Merkle registry.
- [TrinityGuard](https://github.com/AI45Lab/TrinityGuard) - Multi-agent safety framework with three-layer defense for detecting and preventing unsafe agent behaviors.

## Policy as Code

*Language-level tools for expressing, validating, and enforcing authorization policies — applicable to agent capability bounds, tool access, and data permissions.*

- [Cedar](https://github.com/cedar-policy/cedar) - Amazon's policy language for fine-grained, type-safe access control. Used as the policy engine in the Agent Governance Toolkit. Fast, formally verified, and human-readable.
- [Casbin](https://github.com/casbin/casbin) - Cross-language authorization library supporting ACL, RBAC, and ABAC models. Available in Go, Python, Java, and more.
- [Open Policy Agent (OPA)](https://github.com/open-policy-agent/opa) - CNCF general-purpose policy engine. Decouples policy decisions from application logic using the Rego language. Widely deployed for Kubernetes and API authorization.
- [SpiceDB](https://github.com/authzed/spicedb) - Google Zanzibar-inspired database for fine-grained, relationship-based authorization. Useful for cross-agent and multi-tenant permission modeling.

## LLM Safety & Guardrails

*Input/output filtering, content safety, and prompt protection for LLM-powered agents.*

- [Arthur Shield](https://www.arthur.ai/product/shield) - Firewall for LLMs that detects hallucinations, toxicity, PII leakage, and prompt injection in real time.
- [Guardrails AI](https://github.com/guardrails-ai/guardrails) - Framework for structural, type, and quality guarantees on LLM outputs. Guardrails Hub provides community validators.
- [Hyperion](https://github.com/Salesforce/hyperion) - Framework for evaluating and improving robustness of LLM-based agents against adversarial attacks.
- [Lakera Guard](https://www.lakera.ai/) - Real-time API for detecting prompt injections, data leakage, toxic content, and other LLM security threats.
- [LLM Guard](https://github.com/protectai/llm-guard) - Input and output scanners covering toxicity, PII, prompt injection, invisible text, and code detection.
- [Meta Llama Guard](https://github.com/meta-llama/PurpleLlama) - Safety classifier models for filtering unsafe LLM inputs and outputs. Part of Meta's Purple Llama safety suite.
- [NVIDIA NeMo Guardrails](https://github.com/NVIDIA/NeMo-Guardrails) - Open-source toolkit for adding programmable guardrails to LLM-based conversational systems using Colang.
- [Rebuff](https://github.com/protectai/rebuff) - Prompt injection detection using multi-layer defense: heuristics, LLM analysis, and canary tokens.
- [Vigil](https://github.com/deadbits/vigil-llm) - LLM security scanner for detecting prompt injections using embedding similarity, heuristics, and canary tokens.

## Agent Frameworks with Governance Features

*Agent development frameworks that include governance, safety, or policy hooks.*

- [AgentScope](https://github.com/modelscope/agentscope) - Multi-agent platform with fault tolerance, agent-level monitoring, and configurable message validation.
- [AutoGen](https://github.com/microsoft/autogen) - Multi-agent conversation framework with human oversight, code execution sandboxing, and conversation policies.
- [CrewAI](https://github.com/crewAIInc/crewAI) - Multi-agent orchestration with role-based agents, task delegation, and configurable guardrails.
- [Dify](https://github.com/langgenius/dify) - LLM app development platform with content moderation, rate limiting, and annotation logging.
- [Google Agent Development Kit (ADK)](https://github.com/google/adk-python) - Google's agent framework with safety callbacks, evaluation tools, and multi-agent session management.
- [Haystack](https://github.com/deepset-ai/haystack) - End-to-end NLP framework with pipeline-based architecture supporting content filtering and validation.
- [LangChain](https://github.com/langchain-ai/langchain) - Composable framework with callbacks, tracing, and moderation chains for LLM applications.
- [LangGraph](https://github.com/langchain-ai/langgraph) - Stateful, multi-actor agent framework with human-in-the-loop and persistence built in.
- [LlamaIndex](https://github.com/run-llama/llama_index) - Data framework with observability callbacks, evaluation modules, and structured output guarantees.
- [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) - Official OpenAI SDK with built-in guardrails, input/output validation, and handoff controls.
- [PydanticAI](https://github.com/pydantic/pydantic-ai) - Agent framework with type-safe tool definitions, structured outputs, and dependency injection.
- [Semantic Kernel](https://github.com/microsoft/semantic-kernel) - Microsoft's AI orchestration SDK with plugin permission models, function filtering, and responsible AI hooks.
- [smolagents](https://github.com/huggingface/smolagents) - Hugging Face's lightweight agent library with sandboxed code execution and security controls.

## Agent Identity & Attestation

*Protocols and tools for establishing cryptographic identity, trust, and verifiable provenance for AI agents.*

- [Agent Card / AI Card](https://google.github.io/A2A/#/documentation?id=agent-card) - Specification for machine-readable agent capability and policy metadata, enabling discovery and trust decisions.
- [Agent Manifest](https://github.com/agentrust-io/agent-manifest) - Cryptographically signs all 10 deployment artifacts (model, tools, policy, identity, memory config, etc.) into a tamper-evident deployment record.
- [SPIFFE/SVID](https://spiffe.io/) - Secure Production Identity Framework for Everyone. Cryptographic workload identity applicable to agent-to-agent authentication.
- [TRACE](https://github.com/agentrust-io/trace-spec) - Trust Runtime Attestation and Compliance Evidence. Each governed action produces a cryptographic claim anchored in an append-only Merkle log.
- [W3C Decentralized Identifiers (DIDs)](https://www.w3.org/TR/did-core/) - W3C standard for decentralized, self-sovereign identifiers applicable to durable agent identity without centralized registries.

## Observability & Monitoring

*Platforms for tracing, monitoring, evaluating, and debugging AI agent behavior.*

- [AgentOps](https://github.com/AgentOps-AI/agentops) - Agent observability SDK with session replay, LLM cost tracking, compliance monitoring, and failure detection.
- [Arize / Phoenix](https://github.com/Arize-ai/phoenix) - Open-source AI observability with LLM tracing, evaluation, retrieval analysis, and experiment tracking.
- [Braintrust](https://www.braintrust.dev/) - Evaluation and monitoring platform with logging, scoring, and experiment comparison.
- [Datadog LLM Observability](https://www.datadoghq.com/product/llm-observability/) - Enterprise monitoring with trace clustering, cost attribution, and quality scoring.
- [Helicone](https://github.com/Helicone/helicone) - Open-source LLM observability with request logging, cost tracking, caching, and rate limiting.
- [Jaeger](https://www.jaegertracing.io/) - Open-source distributed tracing for monitoring agent workflows and debugging latency across services.
- [Langfuse](https://github.com/langfuse/langfuse) - Open-source LLM engineering platform with tracing, prompt management, evaluations, and cost tracking.
- [LangSmith](https://smith.langchain.com/) - LangChain's platform for debugging, testing, evaluating, and monitoring LLM applications.
- [MLflow](https://github.com/mlflow/mlflow) - Open-source ML lifecycle platform with experiment tracking, model registry, and LLM evaluation tools.
- [Prometheus](https://prometheus.io/) + [Grafana](https://grafana.com/) - Industry-standard metrics and visualization. Foundation for custom agent SLO dashboards.
- [Tuning Engines](https://github.com/cerebrixos-org/tuningengines) - Open-source AI control and evidence plane for agent, tool, MCP, and skill traffic. Records policy decisions, approvals, traces, runtime state, costs, and outcomes.
- [Weights & Biases](https://wandb.ai/) - ML experiment tracking with LLM tracing, evaluation pipelines, and model monitoring.

## Security Testing

*Scanners, red-teaming tools, and frameworks for testing the security of AI agents and LLMs.*

- [Counterfit](https://github.com/Azure/counterfit) - Azure's tool for assessing ML model security through adversarial attacks.
- [CyberSecEval](https://github.com/meta-llama/PurpleLlama/tree/main/CyberSecEval) - Meta's benchmark suite for LLM cybersecurity risks including insecure code generation and prompt extraction.
- [Garak](https://github.com/NVIDIA/garak) - LLM vulnerability scanner from NVIDIA. Probes for hallucination, data leakage, prompt injection, toxicity, and more.
- [HouYi](https://github.com/LLMSecurity/HouYi) - Prompt injection attack framework for testing LLM-integrated application security boundaries.
- [PyRIT](https://github.com/Azure/PyRIT) - Microsoft's Python Risk Identification Toolkit for red-teaming generative AI systems with automated attack strategies.
- [Snyk Agent Scan](https://github.com/snyk/agent-scan) - Security scanner for AI agents and MCP servers. Detects vulnerabilities in tool configurations, permissions, and data flows.

## Standards & Specifications

*Protocols, specifications, and regulatory frameworks relevant to agent governance and interoperability.*

- [Agent-to-Agent Protocol (A2A)](https://github.com/google/A2A) - Google-led open protocol for inter-agent communication, task delegation, and capability discovery.
- [CSA MCP Security Resource Center](https://cloudsecurityalliance.org/research/working-groups/model-context-protocol-security) - Cloud Security Alliance guidance for secure MCP implementations.
- [EU AI Act](https://artificialintelligenceact.eu/) - EU regulation classifying AI systems by risk with requirements for transparency, human oversight, and governance.
- [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) - Open protocol connecting LLMs to tools and data sources with standardized server/client architecture.
- [NIST AI Risk Management Framework](https://www.nist.gov/artificial-intelligence/executive-order-safe-secure-and-trustworthy-artificial-intelligence) - NIST framework for managing AI risk including governance and accountability.
- [OpenTelemetry](https://opentelemetry.io/) - Vendor-neutral observability standard for traces, metrics, and logs. Foundation for agent observability pipelines.
- [Oracle Agent Spec](https://github.com/oracle/agent-spec) - Enterprise agent interoperability specification with governance and management capabilities.
- [OWASP Agentic Applications Top 10 (2026)](https://genai.owasp.org/resource/agentic-ai-threats-and-mitigations/) - OWASP classification of the top 10 security risks in agentic AI: excessive agency, trust boundary failures, identity spoofing, and more.

## Research Papers

*Key academic works on agent safety, multi-agent governance, and trust in AI systems.*

- [A Survey on Large Language Model based Autonomous Agents](https://arxiv.org/abs/2308.11432) - Comprehensive survey of LLM-based agents covering architecture, capabilities, and safety.
- [Agent Safety: An Emerging Research Direction](https://arxiv.org/abs/2502.09689) - Analysis of safety challenges unique to autonomous AI agents beyond traditional LLM safety.
- [Constitutional AI: Harmlessness from AI Feedback](https://arxiv.org/abs/2212.08073) - Anthropic's methodology for training AI systems to be helpful, harmless, and honest using AI feedback.
- [Multi-Agent Safety: A Systematic Survey](https://arxiv.org/abs/2502.09859) - Survey of safety challenges in multi-agent systems including coordination failures and emergent behaviors.
- [Practices for Governing Agentic AI Systems](https://openai.com/index/practices-for-governing-agentic-ai-systems/) - OpenAI's whitepaper on governance practices: oversight, monitoring, and containment.
- [Reflexion: Language Agents with Verbal Reinforcement Learning](https://arxiv.org/abs/2303.11366) - Self-reflective agent architecture with implications for building self-correcting, safer agents.
- [The Landscape of Emerging AI Agent Architectures](https://arxiv.org/abs/2404.11584) - Survey of agentic architectures with analysis of governance-relevant design patterns.
- [The Rise and Potential of Large Language Model Based Agents: A Survey](https://arxiv.org/abs/2309.07864) - Survey covering agent construction, applications, and societal implications including safety.
- [Toolformer: Language Models Can Teach Themselves to Use Tools](https://arxiv.org/abs/2302.04761) - Foundational work on tool-using LLMs, relevant to understanding tool governance requirements.
- [Towards Autonomous AI Agents: A Safety-First Approach](https://arxiv.org/abs/2501.13649) - Framework for integrating safety constraints into autonomous agent design from the ground up.

## Industry Reports & Guidance

*Practitioner guides, threat models, and industry analyses for agent governance.*

- [Anthropic's Responsible Scaling Policy](https://www.anthropic.com/index/anthropics-responsible-scaling-policy) - Framework for responsible AI deployment with AI Safety Levels (ASL) and safety evaluation commitments.
- [CSA AI Safety Initiative](https://cloudsecurityalliance.org/research/working-groups/artificial-intelligence) - Cloud Security Alliance publications on AI safety and security best practices.
- [Google Secure AI Framework (SAIF)](https://safety.google/cybersecurity-advancements/saif/) - Conceptual framework for securing AI systems across the development and deployment lifecycle.
- [Microsoft Responsible AI Standard](https://www.microsoft.com/en-us/ai/responsible-ai) - Framework covering fairness, reliability, safety, and transparency in AI development.
- [MITRE ATLAS](https://atlas.mitre.org/) - Adversarial Threat Landscape for AI Systems. Adversary tactics and techniques against AI/ML systems, structured like ATT&CK.
- [OWASP Agentic AI Threats and Mitigations](https://genai.owasp.org/resource/agentic-ai-threats-and-mitigations/) - OWASP's threat catalog and mitigation strategies for agentic applications.
- [OWASP Top 10 for LLM Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/) - Top 10 security risks for LLM applications including prompt injection, insecure output handling, and supply chain vulnerabilities.

## Conferences & Communities

*Key venues for agent governance research, practice, and community discussion.*

- [AAMAS](https://www.aamas-conference.org/) - International Conference on Autonomous Agents and Multi-Agent Systems.
- [ACM FAccT](https://facctconference.org/) - ACM Conference on Fairness, Accountability, and Transparency in sociotechnical systems.
- [AI Safety Camp](https://aisafety.camp/) - Research program for AI safety and alignment.
- [Alignment Forum](https://www.alignmentforum.org/) - Community forum for AI alignment and safety research.
- [ICML](https://icml.cc/) - International Conference on Machine Learning, with safe and reliable ML tracks.
- [NeurIPS](https://neurips.cc/) - Leading ML conference with AI safety, alignment, and trustworthy ML workshops.
- [OWASP GenAI](https://genai.owasp.org/) - OWASP community for security guidance on generative AI and agentic applications.
- [r/agentic](https://www.reddit.com/r/agentic/) - Reddit community for autonomous AI agents, tools, and governance.

## Contributing

Contributions welcome! Please read the [contribution guidelines](CONTRIBUTING.md) and submit a PR. Open-source governance tools, research papers, and community resources are especially welcome.

---

*Maintained by [Imran Siddique](https://github.com/imran-siddique) — CPO at [Opaque Systems](https://opaque.co), creator of the [Agent Governance Toolkit](https://github.com/microsoft/agent-governance-toolkit), and contributor to OWASP ASI, CoSAI WS4, and the Agentic AI Foundation. The curator also maintains AGT, the agentrust-io tools (TRACE, cMCP, Agent Manifest), and the four component repos (Agent OS, AgentMesh, Agent SRE, Agent Hypervisor).*
