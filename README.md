# Awesome AI Agent Governance [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated list of tools, frameworks, standards, and resources for governing autonomous AI agents — covering safety, trust, identity, observability, and compliance across the agent lifecycle.

AI agents are moving from demos to production, but governance hasn't kept up. This list tracks the emerging landscape of tools and practices for making agents safe, auditable, and trustworthy.

## Contents

- [Our Stack](#our-stack)
- [Agent Governance Frameworks](#agent-governance-frameworks)
- [LLM Safety & Guardrails](#llm-safety--guardrails)
- [Agent Frameworks with Built-in Governance](#agent-frameworks-with-built-in-governance)
- [Standards & Specifications](#standards--specifications)
- [Observability & Monitoring](#observability--monitoring)
- [Security Tools](#security-tools)
- [Research Papers & Surveys](#research-papers--surveys)
- [Industry Reports & Guides](#industry-reports--guides)
- [Conferences & Communities](#conferences--communities)

## Our Stack

*Our open-source governance stack for AI agents — from kernel-level policy enforcement to multi-agent networking and reliability engineering.*

- [Agent OS](https://github.com/imran-siddique/agent-os) - Kernel-level governance for AI agents with policy enforcement, action interception, and OWASP Agentic Top 10 coverage. Integrates with LangChain, CrewAI, AutoGen, OpenAI, Google ADK, PydanticAI, and smolagents.
- [AgentMesh](https://github.com/imran-siddique/agent-mesh) - Zero-trust networking for AI agents with DID identity, trust scoring, delegation chains, and MCP governance proxy.
- [Agent SRE](https://github.com/imran-siddique/agent-sre) - Site reliability engineering for AI agents with SLOs, error budgets, chaos testing, circuit breakers, and cascading failure detection.
- [Agent Hypervisor](https://github.com/imran-siddique/agent-hypervisor) - Runtime governance for AI agents with execution rings, resource limits, saga compensation, joint liability, and kill switch.

## Agent Governance Frameworks

*Dedicated platforms and control planes for governing AI agent behavior, enforcing policies, and maintaining trust.*

- [Agent OS](https://github.com/imran-siddique/agent-os) - Kernel architecture for AI agents with POSIX-inspired primitives, deterministic policy enforcement, and flight recorder audit logging.
- [AgentMesh](https://github.com/imran-siddique/agent-mesh) - Identity, trust, and networking layer for multi-agent systems with DID-based identity, delegation chains, reward scoring, and MCP governance proxy.
- [Agent SRE](https://github.com/imran-siddique/agent-sre) - Reliability engineering for AI agents with SLOs, error budgets, chaos testing, progressive delivery, cost guardrails, and incident management.
- [Agent Hypervisor](https://github.com/imran-siddique/agent-hypervisor) - Hypervisor-grade isolation and resource management for untrusted AI agents.
- [IBM mcp-context-forge](https://github.com/IBM/mcp-context-forge) - MCP gateway with context-aware guardrails, request routing, and compliance controls for enterprise MCP deployments.
- [Cordum](https://github.com/cordum-io/cordum) - Agent control plane providing governance, lifecycle management, and policy enforcement for autonomous agents.
- [Gate22](https://github.com/aipotheosis-labs/gate22) - MCP gateway with role-based access control, audit logging, and fine-grained permission management for tool access.
- [TrinityGuard](https://github.com/AI45Lab/TrinityGuard) - Multi-agent safety framework with three-layer defense for detecting and preventing unsafe agent behaviors.
- [Coral Server](https://github.com/Coral-Protocol/coral-server) - Agent coordination and trust server enabling safe multi-agent collaboration with structured communication protocols.
- [LiteLLM](https://github.com/BerriAI/litellm) - Unified LLM gateway with spend tracking, rate limiting, guardrails, and access controls across 100+ LLM providers.
- [Invariant Guardrails](https://github.com/invariantlabs-ai/invariant) - Rule-based guardrails engine for agentic applications with policy-as-code, trace analysis, and real-time intervention.

## LLM Safety & Guardrails

*Input/output filtering, content safety, and prompt protection for LLM-powered agents.*

- [NVIDIA NeMo Guardrails](https://github.com/NVIDIA/NeMo-Guardrails) - Open-source toolkit for adding programmable guardrails to LLM-based conversational systems. Supports topical, safety, and security rails with Colang.
- [Meta Llama Guard](https://github.com/meta-llama/PurpleLlama) - Safety classifier models for filtering unsafe LLM inputs and outputs. Part of Meta's Purple Llama safety suite.
- [Guardrails AI](https://github.com/guardrails-ai/guardrails) - Framework for adding structural, type, and quality guarantees to LLM outputs. Guardrails Hub provides community validators.
- [Rebuff](https://github.com/protectai/rebuff) - Prompt injection detection framework using multi-layer defense including heuristics, LLM analysis, and canary tokens.
- [LLM Guard](https://github.com/protectai/llm-guard) - Input and output scanners for LLM interactions covering toxicity, PII, prompt injection, invisible text, and code detection.
- [Lakera Guard](https://www.lakera.ai/) - Real-time API for detecting prompt injections, data leakage, toxic content, and other LLM security threats.
- [Arthur Shield](https://www.arthur.ai/product/shield) - Firewall for LLMs that detects hallucinations, toxicity, PII leakage, and prompt injection in real time.
- [Vigil](https://github.com/deadbits/vigil-llm) - LLM security scanner for detecting prompt injections using embedding similarity, heuristics, and canary tokens.
- [Hyperion](https://github.com/Salesforce/hyperion) - Framework for evaluating and improving robustness of LLM-based agents against adversarial attacks.

## Agent Frameworks with Built-in Governance

*Agent development frameworks that include governance, safety, or policy features.*

- [LangChain](https://github.com/langchain-ai/langchain) - Composable framework for building LLM applications with support for callbacks, tracing, and moderation chains.
- [LangGraph](https://github.com/langchain-ai/langgraph) - Framework for building stateful, multi-actor agent applications with human-in-the-loop and persistence built in.
- [CrewAI](https://github.com/crewAIInc/crewAI) - Multi-agent orchestration framework with role-based agents, task delegation, and configurable guardrails.
- [AutoGen](https://github.com/microsoft/autogen) - Multi-agent conversation framework with support for human oversight, code execution sandboxing, and conversation policies.
- [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) - Official OpenAI SDK for building agents with built-in guardrails, input/output validation, and handoff controls.
- [Google Agent Development Kit (ADK)](https://github.com/google/adk-python) - Google's agent framework with built-in safety callbacks, evaluation tools, and multi-agent session management.
- [Semantic Kernel](https://github.com/microsoft/semantic-kernel) - Microsoft's AI orchestration SDK with plugin permission models, function filtering, and responsible AI hooks.
- [PydanticAI](https://github.com/pydantic/pydantic-ai) - Agent framework built on Pydantic with type-safe tool definitions, structured outputs, and dependency injection.
- [Haystack](https://github.com/deepset-ai/haystack) - End-to-end NLP framework with pipeline-based architecture supporting content filtering and validation components.
- [smolagents](https://github.com/huggingface/smolagents) - Hugging Face's lightweight agent library with sandboxed code execution and built-in security controls.
- [AgentScope](https://github.com/modelscope/agentscope) - Multi-agent platform with fault tolerance, agent-level monitoring, and configurable message validation.
- [Dify](https://github.com/langgenius/dify) - LLM app development platform with built-in content moderation, rate limiting, and annotation logging.
- [LlamaIndex](https://github.com/run-llama/llama_index) - Data framework for LLM applications with observability callbacks, evaluation modules, and structured output guarantees.

## Standards & Specifications

*Protocols, specifications, and standards relevant to agent governance, identity, and interoperability.*

- [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) - Open protocol for connecting LLMs to external tools and data sources. Defines server/client architecture for standardized tool access.
- [Agent-to-Agent Protocol (A2A)](https://github.com/google/A2A) - Google-led open protocol for inter-agent communication, task delegation, and capability discovery.
- [OWASP Agentic Applications Top 10 (2026)](https://genai.owasp.org/resource/agentic-ai-threats-and-mitigations/) - OWASP's classification of the top 10 security risks in agentic AI applications including excessive agency, trust boundary failures, and identity spoofing.
- [SPIFFE/SVID](https://spiffe.io/) - Secure Production Identity Framework for Everyone. Provides cryptographic identity to workloads, applicable to agent-to-agent authentication.
- [W3C Decentralized Identifiers (DIDs)](https://www.w3.org/TR/did-core/) - W3C standard for decentralized, self-sovereign identifiers. Applicable to agent identity management without centralized registries.
- [Agent Card / AI Card](https://google.github.io/A2A/#/documentation?id=agent-card) - Specification for machine-readable agent capability and policy metadata, enabling discovery and trust decisions.
- [Oracle Agent Spec](https://github.com/oracle/agent-spec) - Oracle's specification for enterprise agent interoperability with governance and management capabilities.
- [CSA MCP Security Resource Center](https://cloudsecurityalliance.org/research/working-groups/model-context-protocol-security) - Cloud Security Alliance working group providing security guidance for MCP implementations.
- [OpenTelemetry](https://opentelemetry.io/) - Vendor-neutral observability standard for traces, metrics, and logs. Foundation for agent observability.
- [NIST AI Risk Management Framework](https://www.nist.gov/artificial-intelligence/executive-order-safe-secure-and-trustworthy-artificial-intelligence) - NIST framework for managing risks in AI systems, including governance and accountability guidelines.
- [EU AI Act](https://artificialintelligenceact.eu/) - European Union regulation classifying AI systems by risk level with requirements for transparency, human oversight, and governance.

## Observability & Monitoring

*Platforms for tracing, monitoring, evaluating, and debugging AI agent behavior.*

- [Langfuse](https://github.com/langfuse/langfuse) - Open-source LLM engineering platform with tracing, prompt management, evaluations, and cost tracking.
- [LangSmith](https://smith.langchain.com/) - LangChain's platform for debugging, testing, evaluating, and monitoring LLM applications and agents.
- [Arize / Phoenix](https://github.com/Arize-ai/phoenix) - Open-source AI observability with LLM tracing, evaluation, retrieval analysis, and experiment tracking.
- [Braintrust](https://www.braintrust.dev/) - Evaluation and monitoring platform for AI products with logging, scoring, and experiment comparison.
- [Helicone](https://github.com/Helicone/helicone) - Open-source LLM observability platform with request logging, cost tracking, caching, and rate limiting.
- [AgentOps](https://github.com/AgentOps-AI/agentops) - Agent observability SDK with session replay, LLM cost tracking, compliance monitoring, and failure detection.
- [Tuning Engines](https://github.com/cerebrixos-org/tuningengines) - Open-source AI control and evidence plane for agent, tool, model, MCP, and skill traffic. Records policy decisions, approvals, traces, runtime state references, costs, and outcomes for governed agent operations.
- [Weights & Biases](https://wandb.ai/) - ML experiment tracking platform with LLM tracing, evaluation pipelines, and model monitoring.
- [MLflow](https://github.com/mlflow/mlflow) - Open-source platform for the ML lifecycle with experiment tracking, model registry, and LLM evaluation tools.
- [Datadog LLM Observability](https://www.datadoghq.com/product/llm-observability/) - Enterprise monitoring for LLM applications with trace clustering, cost attribution, and quality scoring.
- [Prometheus](https://prometheus.io/) + [Grafana](https://grafana.com/) - Industry-standard metrics collection and visualization. Common foundation for custom agent SLO dashboards.
- [Jaeger](https://www.jaegertracing.io/) - Open-source distributed tracing for monitoring agent workflows and debugging latency across services.

## Security Tools

*Scanners, red-teaming tools, and security testing frameworks for AI agents and LLMs.*

- [Snyk Agent Scan](https://github.com/snyk/agent-scan) - Security scanner for AI agents and MCP servers. Detects vulnerabilities in tool configurations, permissions, and data flows.
- [Garak](https://github.com/NVIDIA/garak) - LLM vulnerability scanner from NVIDIA. Probes for hallucination, data leakage, prompt injection, toxicity, and more.
- [python-can-shoot](https://github.com/nickcash/python-can-shoot) - MCP attack toolset demonstrating prompt injection, tool poisoning, and other MCP-specific attack vectors.
- [CyberSecEval](https://github.com/meta-llama/PurpleLlama/tree/main/CyberSecEval) - Meta's benchmark suite for evaluating LLM cybersecurity risks including insecure code generation and prompt extraction.
- [PyRIT](https://github.com/Azure/PyRIT) - Microsoft's Python Risk Identification Toolkit for red-teaming generative AI systems with automated attack strategies.
- [Counterfit](https://github.com/Azure/counterfit) - Azure's tool for assessing security of ML models through adversarial attacks.
- [HouYi](https://github.com/LLMSecurity/HouYi) - Prompt injection attack framework for testing LLM-integrated application security boundaries.
- [Prompt Injection Detector](https://github.com/protectai/rebuff) - Tools for detecting and preventing prompt injection attacks in LLM applications.

## Research Papers & Surveys

*Key academic works on agent safety, multi-agent governance, and trust in AI systems.*

- [A Survey on Large Language Model based Autonomous Agents](https://arxiv.org/abs/2308.11432) - Comprehensive survey of LLM-based autonomous agents covering architecture, capabilities, and safety considerations.
- [The Rise and Potential of Large Language Model Based Agents: A Survey](https://arxiv.org/abs/2309.07864) - Survey covering agent construction, applications, and societal implications including safety and governance.
- [Agent Safety: An Emerging Research Direction](https://arxiv.org/abs/2502.09689) - Analysis of unique safety challenges in autonomous AI agents beyond traditional LLM safety.
- [Practices for Governing Agentic AI Systems](https://openai.com/index/practices-for-governing-agentic-ai-systems/) - OpenAI's whitepaper on governance practices for agentic AI including oversight, monitoring, and containment.
- [Towards Autonomous AI Agents: A Safety-First Approach](https://arxiv.org/abs/2501.13649) - Framework for integrating safety constraints into autonomous agent design from the ground up.
- [Multi-Agent Safety: A Systematic Survey](https://arxiv.org/abs/2502.09859) - Survey of safety challenges specific to multi-agent systems including coordination failures and emergent behaviors.
- [Constitutional AI: Harmlessness from AI Feedback](https://arxiv.org/abs/2212.08073) - Anthropic's methodology for training AI systems to be helpful, harmless, and honest using AI feedback.
- [Toolformer: Language Models Can Teach Themselves to Use Tools](https://arxiv.org/abs/2302.04761) - Foundational work on tool-using LLMs, relevant to understanding tool governance requirements.
- [Reflexion: Language Agents with Verbal Reinforcement Learning](https://arxiv.org/abs/2303.11366) - Self-reflective agent architecture with implications for building self-correcting, safer agents.
- [The Landscape of Emerging AI Agent Architectures for Reasoning, Planning, and Tool Calling](https://arxiv.org/abs/2404.11584) - Survey of agentic architectures with analysis of governance-relevant design patterns.

## Industry Reports & Guides

*Practitioner guides, threat models, and industry analyses for agent governance.*

- [OWASP Agentic AI Threats and Mitigations](https://genai.owasp.org/resource/agentic-ai-threats-and-mitigations/) - OWASP's threat catalog and mitigation strategies for agentic AI applications.
- [OWASP Top 10 for LLM Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/) - OWASP's top 10 security risks for LLM applications including prompt injection, insecure output handling, and supply chain vulnerabilities.
- [CSA AI Safety Initiative](https://cloudsecurityalliance.org/research/working-groups/artificial-intelligence) - Cloud Security Alliance working group publications on AI safety and security best practices.
- [Anthropic's Responsible Scaling Policy](https://www.anthropic.com/index/anthropics-responsible-scaling-policy) - Framework for responsible AI deployment with defined AI Safety Levels (ASL) and safety evaluation commitments.
- [Google Secure AI Framework (SAIF)](https://safety.google/cybersecurity-advancements/saif/) - Google's conceptual framework for securing AI systems across the development and deployment lifecycle.
- [Microsoft Responsible AI Standard](https://www.microsoft.com/en-us/ai/responsible-ai) - Microsoft's framework for responsible AI development covering fairness, reliability, safety, and transparency.
- [MITRE ATLAS](https://atlas.mitre.org/) - Adversarial Threat Landscape for AI Systems. Knowledge base of adversary tactics and techniques against AI/ML systems.

## Conferences & Communities

*Key venues for agent governance research, practice, and community discussion.*

- [AAAI Conference on Artificial Intelligence](https://aaai.org/conference/aaai/) - Premier AI conference with tracks on AI safety, multi-agent systems, and responsible AI.
- [NeurIPS](https://neurips.cc/) - Leading ML conference with workshops on AI safety, alignment, and trustworthy ML.
- [ICML](https://icml.cc/) - International Conference on Machine Learning, featuring work on safe and reliable ML systems.
- [ACM FAccT](https://facctconference.org/) - ACM Conference on Fairness, Accountability, and Transparency in sociotechnical systems.
- [AAMAS](https://www.aamas-conference.org/) - International Conference on Autonomous Agents and Multi-Agent Systems, core venue for multi-agent governance.
- [AI Safety Camp](https://aisafety.camp/) - Research program bringing together researchers working on AI safety and alignment.
- [Alignment Forum](https://www.alignmentforum.org/) - Community forum for research and discussion on AI alignment and safety.
- [OWASP GenAI](https://genai.owasp.org/) - OWASP community focused on security guidance for generative AI and agentic applications.
- [r/agentic](https://www.reddit.com/r/agentic/) - Reddit community for discussion of autonomous AI agents, tools, and governance.

## Contributing

Contributions welcome! Please read the [contribution guidelines](CONTRIBUTING.md) and submit a PR. We especially welcome additions of open-source governance tools, research papers, and community resources.
