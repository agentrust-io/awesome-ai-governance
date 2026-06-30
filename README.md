# Awesome AI Agent Governance [![Awesome](https://awesome.re/badge.svg)](https://awesome.re) [![Discord](https://img.shields.io/badge/Discord-Join-5865F2?logo=discord&logoColor=white&style=flat)](https://discord.gg/grgzFEHgkj)

> A curated list of tools, frameworks, standards, and resources for governing autonomous AI agents, covering safety, trust, identity, observability, and compliance across the agent lifecycle.

AI agents now hold real reach: email, CRMs, databases, financial systems. Guardrails at the content layer probably hold, but enterprises need to run on proof, not probability. This list tracks the tools and practices for making agents safe, auditable, and trustworthy in production.

## Contents

- [Governance Frameworks](#governance-frameworks)
- [End-to-End Governance: Software and Hardware](#end-to-end-governance-software-and-hardware)
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

- [Agent Governance Toolkit (AGT)](https://github.com/microsoft/agent-governance-toolkit) - Production governance layer for autonomous agents with a policy enforcement kernel (<0.1ms p99), execution rings (Ring 0-3), cryptographic Merkle audit logs, and integrations across LangChain, CrewAI, AutoGen, Google ADK, and more. Python + .NET + Rust. Now stewarded by the Agentic AI Foundation. Provides the software governance layer that integrates with hardware-attested enforcement via cMCP. ★4000+
- [Agent Hypervisor](https://github.com/imran-siddique/agent-hypervisor) - Runtime supervisor for AI agents with execution rings, saga compensation, joint liability, and kill-switch controls. **(Archived; folded into the [Agent Governance Toolkit](https://github.com/microsoft/agent-governance-toolkit).)**
- [Agent OS](https://github.com/imran-siddique/agent-os) - Kernel-level governance with POSIX-inspired primitives, policy interception, and OWASP Agentic Top 10 coverage. Integrates with LangChain, CrewAI, AutoGen, PydanticAI, and smolagents. **(Archived; folded into the [Agent Governance Toolkit](https://github.com/microsoft/agent-governance-toolkit).)**
- [Agent SRE](https://github.com/imran-siddique/agent-sre) - Site reliability engineering for AI agents: SLOs, error budgets, chaos testing, circuit breakers, and cascading failure detection. **(Archived; folded into the [Agent Governance Toolkit](https://github.com/microsoft/agent-governance-toolkit).)**
- [AgentMesh](https://github.com/imran-siddique/agent-mesh) - Zero-trust networking for AI agents with DID identity, behavioral trust scoring, delegation chains, and MCP governance proxy. **(Archived; folded into the [Agent Governance Toolkit](https://github.com/microsoft/agent-governance-toolkit).)**
- [Coral Server](https://github.com/Coral-Protocol/coral-server) - Agent coordination and trust server enabling safe multi-agent collaboration with structured communication protocols.
- [Cordum](https://github.com/cordum-io/cordum) - Agent control plane providing governance, lifecycle management, and policy enforcement for autonomous agents.
- [Gate22](https://github.com/aipotheosis-labs/gate22) - MCP gateway with role-based access control, audit logging, and fine-grained permission management for tool access.
- [IBM mcp-context-forge](https://github.com/IBM/mcp-context-forge) - Enterprise MCP gateway with context-aware guardrails, request routing, and compliance controls.
- [Invariant Guardrails](https://github.com/invariantlabs-ai/invariant) - Rule-based guardrails engine with policy-as-code, trace analysis, and real-time intervention for agentic applications.
- [LiteLLM](https://github.com/BerriAI/litellm) - Unified LLM gateway with spend tracking, rate limiting, guardrails, and access controls across 100+ LLM providers.
- [Phinq](https://github.com/phinq-co/phinq) - Open-source governance layer for autonomous AI agents. A proxy intercepts every LLM tool call, a deterministic classifier scores risk, and irreversible or high-risk actions are held for human approval (Telegram or CLI) before execution; every decision is written to a hash-chained, tamper-evident audit log. Also ships an in-process TypeScript SDK. TypeScript. MIT.
- [Regulus](https://github.com/neul-labs/regulus) - EU & UK compliance plane for Google ADK encoding 10 regulations (EU AI Act, GDPR, DORA, NIS2, EHDS, UK GDPR, FCA SYSC, PRA SS1/23, PRA SS2/21, NHS DSPT) and 6 governance frameworks as runtime ADK `BasePlugin` profiles; emits hash-chained audit envelopes with GRC adapters (ServiceNow IRM, OneTrust, MetricStream).
- [ScopeBlind protect-mcp](https://github.com/ScopeBlind/scopeblind-gateway) - Security gateway for MCP servers with Cedar policy enforcement (AWS Cedar via WASM), Ed25519-signed decision receipts, issuer-blind spending authority (VOPRF), and multi-agent swarm tracking. [Merged into AGT](https://github.com/microsoft/agent-governance-toolkit/pull/667).
- [TrinityGuard](https://github.com/AI45Lab/TrinityGuard) - Multi-agent safety framework with three-layer defense for detecting and preventing unsafe agent behaviors.

## End-to-End Governance: Software and Hardware

*Tools and platforms that combine software policy enforcement with hardware-attested execution. The software layer (Cedar policy, audit logs, agent identity) is measured into a Trusted Execution Environment so that the governance claims cannot be forged by a privileged operator, a compromised runtime, or a supply chain attack. The result is a compliance artifact that any third party can verify offline without trusting the operator.*

*The stack: AGT enforces Cedar policies at the software layer. cMCP carries those policies into the TEE. TRACE records the attested outcome. Agent Manifest binds all ten deployment artifacts into a hardware-sealed identity document. OPAQUE Systems provides the managed TEE runtime.*

- [Agent Manifest](https://github.com/agentrust-io/agent-manifest) - Signs all 10 agent deployment artifacts (system prompt, policy bundle, model identity, tool schemas, RAG corpus, memory baseline, decision trace, A2A delegation chain, build provenance, HITL approvals) into a single tamper-evident record. Hardware attestation via TPM, AMD SEV-SNP, Intel TDX, or OPAQUE Managed Runtime. Four conformance levels mapped to EU AI Act Art. 13-15, DORA, HIPAA, and FedRAMP. 197 conformance tests. Python + TypeScript. Developer preview, launching June 23 2026.
- [cMCP (Confidential MCP Gateway)](https://github.com/agentrust-io/cmcp) - MCP gateway running inside a TEE. The Cedar policy bundle is measured into hardware attestation before any code runs; the signing key never leaves the enclave. Every tool call produces a signed GatewayClaim bound to the hardware measurement. Supports TPM, AMD SEV-SNP, Intel TDX, NVIDIA H100 Confidential Compute, and OPAQUE Managed Runtime. Developer preview, launching June 23 2026.
- [OPAQUE Systems](https://opaque.co) - Managed TEE runtime providing the highest-assurance hardware backend for cMCP, TRACE, and Agent Manifest. Handles TEE provisioning, attestation key lifecycle, and enclave deployment. Produces TRACE records signed by OPAQUE's hardware root of trust. Commercial.
- [TRACE (Trust Runtime Attestation and Compliance Evidence)](https://github.com/agentrust-io/trace-spec) - Open attestation standard and Python SDK for agentic AI governance. Each agent run produces a signed EAT/JWT trust record binding model identity, policy version, TEE hardware evidence, and tool call transcript into a single artifact verifiable offline without calling the operator. Built on IETF RATS (RFC 9334), EAT (RFC 9711), SCITT, SLSA, and SPIFFE. Spec v0.1, launching June 23 2026.

## Policy as Code

*Language-level tools for expressing, validating, and enforcing authorization policies applicable to agent capability bounds, tool access, and data permissions.*

- [Casbin](https://github.com/casbin/casbin) - Cross-language authorization library supporting ACL, RBAC, and ABAC models. Available in Go, Python, Java, and more.
- [Cedar](https://github.com/cedar-policy/cedar) - Amazon's policy language for fine-grained, type-safe access control. Used as the policy engine in the Agent Governance Toolkit. Fast, formally verified, and human-readable.
- [Open Policy Agent (OPA)](https://github.com/open-policy-agent/opa) - CNCF general-purpose policy engine. Decouples policy decisions from application logic using the Rego language. Widely deployed for Kubernetes and API authorization.
- [SpiceDB](https://github.com/authzed/spicedb) - Google Zanzibar-inspired database for fine-grained, relationship-based authorization. Useful for cross-agent and multi-tenant permission modeling.

## LLM Safety & Guardrails

*Input/output filtering, content safety, and prompt protection for LLM-powered agents.*

- [ai-evaluation](https://github.com/future-agi/ai-evaluation) - Open-source LLM evaluation framework with 50+ metrics, LLM-as-Judge, and guardrail scanners (jailbreak, PII, injection).
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

*Protocols and tools for establishing cryptographic identity, trust, and verifiable provenance for AI agents. For hardware-attested agent identity and compliance records, see [End-to-End Governance: Software and Hardware](#end-to-end-governance-software-and-hardware).*

- [Agent Card / AI Card](https://google.github.io/A2A/#/documentation?id=agent-card) - Specification for machine-readable agent capability and policy metadata, enabling discovery and trust decisions.
- [Nobulex](https://github.com/arian-gogani/nobulex) - Bilateral receipt primitive for tamper-evident agent audit trails: two Ed25519 signatures per action (pre- and post-execution), hash-chained via JCS canonicalization (RFC 8785). The receipt-signing approach is [merged into AGT](https://github.com/microsoft/agent-governance-toolkit/pull/1333). MIT licensed.
- [SPIFFE/SVID](https://spiffe.io/) - Secure Production Identity Framework for Everyone. Cryptographic workload identity applicable to agent-to-agent authentication.
- [W3C Decentralized Identifiers (DIDs)](https://www.w3.org/TR/did-core/) - W3C standard for decentralized, self-sovereign identifiers applicable to durable agent identity without centralized registries.

## Observability & Monitoring

*Platforms for tracing, monitoring, evaluating, and debugging AI agent behavior.*

- [AgentOps](https://github.com/AgentOps-AI/agentops) - Agent observability SDK with session replay, LLM cost tracking, compliance monitoring, and failure detection.
- [Arize / Phoenix](https://github.com/Arize-ai/phoenix) - Open-source AI observability with LLM tracing, evaluation, retrieval analysis, and experiment tracking.
- [Braintrust](https://www.braintrust.dev/) - Evaluation and monitoring platform with logging, scoring, and experiment comparison.
- [Datadog LLM Observability](https://www.datadoghq.com/product/llm-observability/) - Enterprise monitoring with trace clustering, cost attribution, and quality scoring.
- [Future AGI](https://github.com/future-agi/future-agi) - Open-source self-hostable end-to-end agent engineering platform with tracing, evals, guardrails, and gateway.
- [Helicone](https://github.com/Helicone/helicone) - Open-source LLM observability with request logging, cost tracking, caching, and rate limiting.
- [Jaeger](https://www.jaegertracing.io/) - Open-source distributed tracing for monitoring agent workflows and debugging latency across services.
- [Langfuse](https://github.com/langfuse/langfuse) - Open-source LLM engineering platform with tracing, prompt management, evaluations, and cost tracking.
- [LangSmith](https://smith.langchain.com/) - LangChain's platform for debugging, testing, evaluating, and monitoring LLM applications.
- [MLflow](https://github.com/mlflow/mlflow) - Open-source ML lifecycle platform with experiment tracking, model registry, and LLM evaluation tools.
- [Prometheus](https://prometheus.io/) + [Grafana](https://grafana.com/) - Industry-standard metrics and visualization. Foundation for custom agent SLO dashboards.
- [traceAI](https://github.com/future-agi/traceAI) - Open-source OpenTelemetry-native tracing for LLM and agent apps with 50+ framework integrations.
- [Weights & Biases](https://wandb.ai/) - ML experiment tracking with LLM tracing, evaluation pipelines, and model monitoring.

## Security Testing

*Scanners, red-teaming tools, and frameworks for testing the security of AI agents and LLMs.*

- [Commit](https://getcommit.dev) - Supply chain trust scoring for npm, PyPI, Cargo, and Go packages. Scores maintainer concentration, OIDC publisher gaps, and release consistency to surface high-risk dependency patterns that vulnerability databases miss. CLI, GitHub Action, IDE hooks, REST API, and MCP server.
- [Counterfit](https://github.com/Azure/counterfit) - Azure's tool for assessing ML model security through adversarial attacks.
- [CyberSecEval](https://github.com/meta-llama/PurpleLlama/tree/main/CybersecurityBenchmarks) - Meta's benchmark suite for LLM cybersecurity risks including insecure code generation and prompt extraction.
- [Garak](https://github.com/NVIDIA/garak) - LLM vulnerability scanner from NVIDIA. Probes for hallucination, data leakage, prompt injection, toxicity, and more.
- [HouYi](https://github.com/LLMSecurity/HouYi) - Prompt injection attack framework for testing LLM-integrated application security boundaries.
- [PyRIT](https://github.com/Azure/PyRIT) - Microsoft's Python Risk Identification Toolkit for red-teaming generative AI systems with automated attack strategies.
- [Snyk Agent Scan](https://github.com/snyk/agent-scan) - Security scanner for AI agents and MCP servers. Detects vulnerabilities in tool configurations, permissions, and data flows.

## Standards & Specifications

*Protocols, specifications, and regulatory frameworks relevant to agent governance and interoperability.*

- [Agent-to-Agent Protocol (A2A)](https://github.com/google/A2A) - Google-led open protocol for inter-agent communication, task delegation, and capability discovery.
- [CoSAI Risk Map v1](https://github.com/cosai-oasis/secure-ai-tooling) - Coalition for Secure AI's component-level risk taxonomy for agentic AI systems: 23 components, 35 controls, 36 risks (including 6 agentic-specific), 10 personas, 8 lifecycle stages. Cross-walks to MITRE ATLAS, NIST AI RMF, STRIDE, OWASP LLM Top 10, ISO 22989, and EU AI Act. Launched June 2026.
- [CSA Agentic Trust Framework](https://github.com/massivescale-ai/agentic-trust-framework) - Cloud Security Alliance / MassiveScale framework defining 5 Core Elements (Identity, Behavior, Data Governance, Segmentation, Incident Response) with 25 requirements across a 4-tier maturity model (Intern, Junior, Senior, Principal). Public Review Draft v0.9.1 (April 2026). Two conformance tiers: ATF Compatible / ATF Certified.
- [CSA MCP Security Resource Center](https://modelcontextprotocol-security.io/) - Cloud Security Alliance community project for securing MCP servers and AI agents: hardening guides, audit database, and vulnerability database.
- [CSA Non-Human Identity & Agentic AI Governance v1](https://labs.cloudsecurityalliance.org/research/csa-whitepaper-nonhuman-identity-agentic-ai-governance-v1-cs/) - Cloud Security Alliance whitepaper recommending a 6-field NHI registry (Identity, Owning Team, Business Purpose, Systems Accessed, Privilege Scope, Expiration/Review Date) for managing non-human and agentic identities. Published May 2026.
- [EU AI Act](https://artificialintelligenceact.eu/) - EU regulation classifying AI systems by risk with requirements for transparency, human oversight, and governance.
- [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) - Open protocol connecting LLMs to tools and data sources with standardized server/client architecture.
- [NIST AI 600-1 (GenAI Profile)](https://www.nist.gov/itl/ai-risk-management-framework) - NIST profile of the AI Risk Management Framework focused on generative AI, enumerating 12 risk categories (CBRN, Confabulation, Dangerous Content, Data Privacy, Environmental Impacts, Harmful Bias, Human-AI Configuration, Information Integrity, Information Security, Intellectual Property, Obscene Content, Value Chain). 200+ suggested actions across Govern/Map/Measure/Manage functions. Published July 2024.
- [NIST AI Risk Management Framework](https://www.nist.gov/artificial-intelligence/executive-order-safe-secure-and-trustworthy-artificial-intelligence) - NIST framework for managing AI risk including governance and accountability.
- [NIST IR 8596 (Cyber AI Profile)](https://csrc.nist.gov/pubs/ir/8596/iprd) - NIST profile crossing the Cybersecurity Framework 2.0 against AI in three focus areas (Secure AI System Components, Defend with AI, Thwart AI-Enabled Threats) across six CSF functions (Govern, Identify, Protect, Detect, Respond, Recover). Preliminary Draft (December 2025).
- [OpenTelemetry](https://opentelemetry.io/) - Vendor-neutral observability standard for traces, metrics, and logs. Foundation for agent observability pipelines.
- [Oracle Agent Spec](https://github.com/oracle/agent-spec) - Enterprise agent interoperability specification with governance and management capabilities.
- [OWASP Agentic Applications Top 10 (2026)](https://genai.owasp.org/resource/agentic-ai-threats-and-mitigations/) - OWASP classification of the top 10 security risks in agentic AI: excessive agency, trust boundary failures, identity spoofing, and more.
- [OWASP AI Security Verification Standard (AISVS)](https://github.com/OWASP/AISVS) - OWASP verification-controls standard with 14 chapters covering training data, input validation, model lifecycle, infrastructure, access control, supply chain, model behavior, memory/embeddings, autonomous orchestration (C9), MCP security (C10), adversarial robustness, privacy, monitoring, and human oversight. Releases v1.0 at OWASP Global AppSec EU Vienna on 24 June 2026.
- [OWASP Non-Human Identities (NHI) Top 10 (2025)](https://github.com/OWASP/www-project-non-human-identities-top-10) - OWASP awareness list of the top 10 risks for non-human identities (Improper Offboarding, Secret Leakage, Vulnerable Third-Party NHI, Insecure Authentication, Overprivileged NHI, Insecure Cloud Deployment Configurations, Long-Lived Secrets, Environment Isolation, NHI Reuse, Human Use of NHI). Risk-ranked using OWASP Risk Rating Methodology. Published December 2024.
- [PIC Standard (Provenance & Intent Contracts)](https://github.com/madeinplutofabio/pic-standard) - Open, local-first protocol for pre-execution action gating in AI agents: the agent declares intent, provenance, and evidence before a high-impact tool call; the verifier returns allow or block, failing closed on missing or invalid evidence, under a Trust Axiom that trust is verifier-derived, not producer-asserted. Apache-2.0. Pre-v1.0 draft.
- [Signed Decision Receipts (IETF)](https://datatracker.ietf.org/doc/draft-farley-acta-signed-receipts/) - Internet-Draft defining a portable, cryptographically signed receipt format for machine-to-machine access control decisions. Ed25519 + JCS canonicalization. Independently verifiable offline.
- [Singapore IMDA Model AI Governance Framework for Agentic AI](https://www.imda.gov.sg/-/media/imda/files/about/emerging-tech-and-research/artificial-intelligence/mgf-for-agentic-ai.pdf) - Singapore IMDA framework defining eight components of an agentic system (Model, Instructions, Memory, Planning & Reasoning, Tools, Protocols, Controls, Logging/Monitoring) and four governance dimensions (bounding risks, human accountability, technical controls, end-user responsibility). v1.5 published 20 May 2026
- [SPDX 3.0.1 AI Profile](https://github.com/spdx/spdx-3-model) - SPDX specification for AI Bill of Materials (AIBOM) with AIPackage and DatasetPackage classes covering automation level, autonomy type, hyperparameters, model explainability, safety risk assessment, anonymization method, dataset size, and sensitive personal information flags. Stable since December 2024 (3.0.1); 3.1-RC1 pre-release adds EU AI Act-aligned dataset size properties (token count, item count, content duration).

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

- [Anthropic's Responsible Scaling Policy](https://www.anthropic.com/responsible-scaling-policy) - Framework for responsible AI deployment with AI Safety Levels (ASL) and safety evaluation commitments.
- [Anthropic: Trustworthy Agents in Practice](https://www.anthropic.com/research/trustworthy-agents) - Anthropic's practical guidance on deploying trustworthy agents: balancing autonomy with human oversight, prompt-injection resistance, and operational safeguards.
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
- [Confidential Computing Summit](https://confidentialcomputingsummit.com/) - Annual conference on confidential computing, TEE hardware, and hardware-attested workloads. Primary venue for TRACE, cMCP, and Agent Manifest launch (June 2026, San Francisco).
- [ICML](https://icml.cc/) - International Conference on Machine Learning, with safe and reliable ML tracks.
- [NeurIPS](https://neurips.cc/) - Leading ML conference with AI safety, alignment, and trustworthy ML workshops.
- [OWASP GenAI](https://genai.owasp.org/) - OWASP community for security guidance on generative AI and agentic applications.
- [r/agentic](https://www.reddit.com/r/agentic/) - Reddit community for autonomous AI agents, tools, and governance.

## Contributing

Contributions welcome! Please read the [contribution guidelines](CONTRIBUTING.md) and submit a PR. Open-source governance tools, research papers, and community resources are especially welcome.

Join the community on [Discord](https://discord.gg/grgzFEHgkj).

---

*Maintained by [Imran Siddique](https://github.com/imran-siddique), CPO at [OPAQUE Systems](https://opaque.co), creator of the [Agent Governance Toolkit](https://github.com/microsoft/agent-governance-toolkit), and contributor to OWASP ASI, CoSAI WS4, and the Agentic AI Foundation. The curator also maintains AGT, the agentrust-io tools (TRACE, cMCP, Agent Manifest), and the four component repos (Agent OS, AgentMesh, Agent SRE, Agent Hypervisor).*
