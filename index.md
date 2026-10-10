# Awesome AI Agent Governance

Community updates and contributor highlights: [AgenTrust on LinkedIn](https://www.linkedin.com/company/agentrust-io/).

> A curated list of tools, frameworks, standards and resources for governing AI agents: keeping them safe, knowing who they are, seeing what they do, and showing that they followed the rules.

An AI agent is an AI system that takes actions on its own, such as sending email or updating a database, instead of only answering questions. Agents now reach email, CRMs, databases and financial systems. Content filters catch a lot of bad output, yet a company that lets agents act also needs a record it can check of what each agent did. This list collects the tools and practices that help make agents safe, checkable and trustworthy in real use. New to the terms? The [AgenTrust plain-terms list](https://agentrust-io.com/#plain-terms) explains the common ones in a line each.

Sponsors are listed in [SPONSORS.md](https://governance.agentrust-io.com/SPONSORS/index.md). Sponsorship has no effect on which entries are included, their order, editorial decisions, who maintains the list, or how the project is run. Sponsors and their competitors are judged by the same published contribution rules.

## Contents

- [Governance Frameworks](#governance-frameworks)
- [End-to-End Governance: Software and Hardware](#end-to-end-governance-software-and-hardware)
- [Policy as Code](#policy-as-code)
- [LLM Safety & Guardrails](#llm-safety--guardrails)
- [Agent Frameworks with Governance Features](#agent-frameworks-with-governance-features)
- [Agent Identity & Attestation](#agent-identity--attestation)
- [Agent Action Records](#agent-action-records)
- [Observability & Monitoring](#observability--monitoring)
- [Security Testing](#security-testing)
- [Fairness & Bias Auditing](#fairness--bias-auditing)
- [Standards & Specifications](#standards--specifications)
- [Research Papers](#research-papers)
- [Industry Reports & Guidance](#industry-reports--guidance)
- [Talks & Videos](#talks--videos)
- [Conferences & Communities](#conferences--communities)

## Governance Frameworks

*Platforms that sit between an agent and the systems it uses, check each action against your rules while the agent runs, and keep a record of what was allowed or refused.*

- [AAES](https://aaes.dev) - Governance layer for enterprise AI agents applying identity, human approvals, budgets, and sealed, offline-verifiable action records to routed agent actions; public documentation and OpenAPI specification, core repository private.
- [Agent Governance Toolkit (AGT)](https://github.com/microsoft/agent-governance-toolkit) - Production governance layer for autonomous agents with a policy enforcement kernel (\<0.1ms p99), execution rings (Ring 0-3), cryptographic Merkle audit logs, and integrations across LangChain, CrewAI, AutoGen, Google ADK, and more. Python + .NET + Rust. Provides the software governance layer that integrates with hardware-attested enforcement via cMCP. ★4000+
- [AI Gateway HQ](https://aigatewayhq.com/platform/governance/) - Hosted AI gateway that applies identity, model, tool, data-handling, and budget rules before provider requests; supports Observe, Shadow, and Enforce rollout modes with reason-coded audit metadata and a free evaluation workspace.
- [Allowly](https://allowly.ai/) - Hosted policy decisions and signed receipts for AI-agent actions; the caller enforces, and receipts verify offline with workspace Ed25519 keys using open-source Python (`allowly-receipt-format`) and TypeScript (`@allowly/verifier`) verifiers, with a [CC BY 4.0 specification and interoperability map](https://github.com/Allowly-AI/allowly-receipt-format/blob/main/INTEROP.md).
- [Bifrost](https://github.com/maximhq/bifrost) - Go-native, OpenAI-compatible gateway for runtime AI governance at the model and tool boundary, enforcing guardrails, rate limits, fine-grained access controls, and usage tracking while supporting MCP gateway flows with logs, metrics, and tracing.
- [Coral Server](https://github.com/Coral-Protocol/coral-server) - Agent coordination and trust server enabling safe multi-agent collaboration with structured communication protocols.
- [CIRVIX AgentControl](https://github.com/CIRVIX/agent-control) - Apache-2.0 local runtime authorization for tool calls explicitly routed through its MCP gateway or returned SDK wrappers.
- [Cordum](https://github.com/cordum-io/cordum) - Agent control plane providing governance, lifecycle management, and policy enforcement for autonomous agents.
- [CCS (Correctover Conformance Shape)](https://github.com/DSHCorrectover/ccs-conformance-vectors) - Cryptographic runtime-verification receipts for agent tool calls: Ed25519 (RFC 8032) over RFC 8785 JCS canonical JSON, with prev-receipt hash chaining. MIT-licensed, language-neutral conformance vectors (10 vectors covering valid, tampered, algorithm-substitution, key-substitution, and chain-linked cases) let any implementation verify receipt signing and verification without a dependency on the reference implementation.
- [Dome Systems](https://www.domesystems.ai) - Hosted control plane for AI agents: per-agent identity and revocable credentials, Cedar authorization rules evaluated on every tool and model call (including rules on tool arguments), and an exportable audit trail of each decision. Free tier.
- [Enterprise Agentic AI](https://github.com/Poochaman/enterprise-agentic-ai) - Runnable Python reference for bounded agent actions: separates requester and approver roles, binds approval to an action digest, enforces expiry, revocation, tenant and batch limits, and reconciles a committed CRM write after response loss.
- [ExecLayer](https://www.execlayer.io) - Deterministic execution governance kernel that evaluates AI-proposed actions against policy before execution, refuses out-of-bounds actions, and emits an Ed25519-signed receipt for every decision. Closed-source kernel; public live kernel at [kernel.execlayer.io](https://kernel.execlayer.io) and DOI-registered architecture papers including the Governed Execution Artifact Standard ([10.5281/zenodo.18749299](https://doi.org/10.5281/zenodo.18749299)).
- [Gate22](https://github.com/aipotheosis-labs/gate22) - MCP gateway with role-based access control, audit logging, and fine-grained permission management for tool access.
- [HOL Guard](https://hol.org/guard) - Apache-2.0 local-first runtime control for AI coding agents that evaluates supported shell, file, MCP, plugin/skill, and package actions before side effects, applies allow/block/approval policy, and records local security receipts; optional cloud adds shared policy and evidence sync.
- [IBM mcp-context-forge](https://github.com/IBM/mcp-context-forge) - Enterprise MCP gateway with context-aware guardrails, request routing, and compliance controls.
- [Impri](https://github.com/sekera-radim/impri) - Approval inbox for AI agents: agents propose actions via MCP or REST, a human approves/edits/rejects from web, Slack, Telegram or phone, then the agent executes. MIT-licensed open-core, self-hostable, free tier.
- [Invariant Guardrails](https://github.com/invariantlabs-ai/invariant) - Rule-based guardrails engine with policy-as-code, trace analysis, and real-time intervention for agentic applications.
- [LedgerGuard](https://github.com/Val1-IT/Arvanta-Ledgerguard) - Apache-2.0 TypeScript runtime that sits between an AI agent and a PostgreSQL system of record: deterministic allow/deny/require-approval policy, approvals bound to a plan id and version that agents cannot grant themselves, typed allowlisted corrections instead of free SQL, and execute, verify and commit in one transaction with a persisted idempotency key. Pre-1.0, Postgres only, synthetic demo scenarios.
- [LiteLLM](https://github.com/BerriAI/litellm) - Unified LLM gateway with spend tracking, rate limiting, guardrails, and access controls across 100+ LLM providers.
- [MARGINAL](https://github.com/SignalLayerLabs/Marginal) - Local-first runtime governor for AI coding agents that starts in Shadow Mode, records evidence for proven no-progress repetition, and enables narrow Codex tool enforcement only after repository-local evidence; Claude Code and OpenCode integrations are observe-only.
- [MREA](https://github.com/JairValle/mrea-framework) - Multi-role enterprise agent governance framework with separate Architect, Auditor, and Implementer roles, enforcing human approval gates and independent audits to prevent self-validation bias in AI-assisted development.
- [Okto Nexus](https://github.com/OktoLabsAI/okto-nexus) - Local-first MCP coordination hub for teams of AI coding agents, with single-winner task claims, human-in-the-loop approval on risky actions, and durable handoff history for crash recovery.
- [Okto Pulse](https://github.com/OktoLabsAI/okto-pulse) - Local-first, spec-driven SDLC workbench enforcing independent validation and blocking evidence gates at the permission level, with a knowledge graph that catches drift from recorded decisions.
- [Operational Memory Gates](https://github.com/NiraNexus-Ltd/operational-memory-gates) - MIT specification and reference implementation of 21 mechanical pre-code gates for AI-assisted development, each documented as either a production incident made mechanical or a discipline made mechanical. Twenty refuse with a non-zero exit; one advises. The reference script is deliberately hardcoded to the author's stack, so the artifact is a checkable specification rather than a turnkey tool.
- [Proofpane](https://proofpane.com) - Runtime governance gateway for AI coding agents and MCP clients, enforcing policy gates and DLP redaction in the execution path with a hash-chained, offline-verifiable audit. Closed-source (proprietary daemon); [public reference architecture](https://github.com/Proofpane/architecture) under CC BY 4.0.
- [Provenza](https://github.com/kironovlaziz-del/provenza#readme) - Self-hosted AI governance platform with policy approvals, request auditing, prompt masking with optional named-entity recognition, and a registry of reported shadow-AI sightings. Apache-2.0.
- [Regulus](https://github.com/neul-labs/regulus) - EU & UK compliance plane for Google ADK encoding 10 regulations (EU AI Act, GDPR, DORA, NIS2, EHDS, UK GDPR, FCA SYSC, PRA SS1/23, PRA SS2/21, NHS DSPT) and 6 governance frameworks as runtime ADK `BasePlugin` profiles; emits hash-chained audit envelopes with GRC adapters (ServiceNow IRM, OneTrust, MetricStream).
- [SEMAPRAX](https://wavect.io/semaprax/) - Apache-2.0 experimental systems programming language ([source](https://github.com/wavect/semaprax)) whose compiler gives declarations stable semantic identities, independently replays patch evidence before supported mutations, and models explicit capability and authority boundaries for agent-driven code changes. v0.2 pre-alpha; no built-in model, autonomous agent, transport, keys, or production authority.
- [ScopeBlind protect-mcp](https://github.com/ScopeBlind/scopeblind-gateway) - Security gateway for MCP servers with Cedar policy enforcement (AWS Cedar via WASM), Ed25519-signed decision receipts, issuer-blind spending authority (VOPRF), and multi-agent swarm tracking. [Merged into AGT](https://github.com/microsoft/agent-governance-toolkit/pull/667).
- [Squelette](https://github.com/JyMinet/squelette) - Repository-level governance for AI coding agents: work items declare the file paths they may touch and a pre-commit gate refuses anything outside them, human decisions are recorded in the repo, and a task cannot close without evidence verified against its artifacts.
- [sofagent](https://github.com/KongFangXun/sofagent) - Open-source harness for governing AI coding agents: ontology-driven workflows plus 24 commit-time audit rules over git diffs (secrets, out-of-scope edits, blind modifications, prompt injection), HMAC-signed tamper-evident audit history, and MCP tools for governance aggregation. MIT.
- [Speakeasy](https://www.speakeasy.com/product/ai-control-plane) - Enterprise AI control plane for governing access, policy, and auditability across agents, MCP servers, and Skills.
- [TrinityGuard](https://github.com/AI45Lab/TrinityGuard) - Multi-agent safety framework with three-layer defense for detecting and preventing unsafe agent behaviors.
- [WitnessOS](https://github.com/narko4u/witnessos) - Runtime governance layer producing evidence-grade receipts for every agent action, with policy evaluation before execution and a tamper-evident audit chain.
- [YYLO](https://github.com/yylo-dev/yylo) - Command-line orchestrator that governs coding-agent repository changes: each task freezes the protected target SHA and runs in a dedicated branch/worktree behind typed task, validation, merge, and release-readiness boundaries; the merge queue owns risk-based review (low risk has no semantic reviewer, high risk two sequential reviewers on one frozen candidate) and stops as REVIEW_FINDINGS_EXHAUSTED instead of starting an unbounded review loop; runs retain declared receipt hashes and terminal manifests as receipt-backed repository changes. MIT, on npm as @yylo/cli; orchestrates Pi and Codex subagents.

## End-to-End Governance: Software and Hardware

*Tools that pair software rules with evidence from the hardware. The rules, the logs and the agent's identity run inside a trusted execution environment (TEE), a protected area of the chip whose memory stays encrypted while it runs, and the chip signs a report of exactly what was loaded (an attestation). A privileged operator, a tampered runtime or a supply chain attack cannot forge that report. The result is a compliance record that anyone can check offline, without having to trust the company running the agent.*

*The stack, in the order of the AgenTrust chain from model weights to evidence: Weight Custody Manifest hands out the key that decrypts a model's weights only to a machine whose attestation checks out. Agent Manifest signs all ten parts of an agent deployment into one identity document. AGT checks actions against Cedar policies in software, cMCP runs those checks inside a TEE for MCP tool calls (MCP is a common way agents connect to tools), and cA2A is a profile for checkable handoffs of work between agents over A2A. TRACE records the result as a signed receipt. OPAQUE Systems offers the commercial OPAQUE Confidential AI Platform™.*

- [Agent Manifest](https://github.com/agentrust-io/agent-manifest) - Signs all 10 parts of an agent deployment (system prompt, policy bundle, model identity, tool schemas, RAG corpus, memory baseline, decision trace, A2A delegation chain, build provenance, HITL approvals) into one record, so any later change to any part shows up. Can include a signed hardware report (attestation) from a TPM, AMD SEV-SNP or Intel TDX chip. Four conformance levels, with compliance mappings for the EU AI Act, DORA, GDPR, and HIPAA. 197 conformance tests. Python. Developer preview.
- [cMCP (Confidential MCP Gateway)](https://github.com/agentrust-io/cmcp) - A gateway that sits between an agent and its MCP tools and checks each tool call against Cedar policy inside a TEE. On real hardware, the policy bundle is recorded in the chip's signed report before any code runs, and the signing key never leaves the protected area; software mode gives no hardware protection. Every tool call produces a signed receipt (a GatewayClaim) tied to that hardware record. Supports TPM, AMD SEV-SNP, and Intel TDX attestation. Developer preview.
- [cA2A (Confidential A2A)](https://github.com/agentrust-io/ca2a) - A profile for the Agent2Agent (A2A) protocol, which agents use to hand work to each other. A2A's Signed Agent Card proves only who owns a domain. cA2A adds delegation where each agent can pass on the same or less authority than it received, provably; a hardware check of the other agent's runtime; a sealed channel between the two (tying the seal to a verified hardware measurement on a live call is on the roadmap); and a record of each handoff that can be checked offline. Reuses the delegation rules from Agent Manifest and the TEE and policy building blocks from cMCP. Python, developer preview; installable with `pip install ca2a-runtime`.
- [OPAQUE Systems](https://opaque.co) - The OPAQUE Confidential AI Platform™, with OPAQUE Agent Control™ for governing agent actions and OPAQUE Confidential Core™ for running them in TEEs with hardware attestation. Sponsor of this list and of the AgenTrust specifications (see [SPONSORS.md](https://governance.agentrust-io.com/SPONSORS/index.md)). The open cMCP and Agent Manifest repositories mark their OPAQUE attestation provider as not implemented. Commercial.
- [TRACE (Trust Runtime Attestation and Compliance Evidence)](https://github.com/agentrust-io/trace-spec) - Open specification (a Series of LF Projects, with an AAIF Sandbox proposal open) and Python SDK for signed receipts of what an agent run did. Each run produces a signed record of the model, the runtime, the policy version and the tool calls, which anyone can check offline without contacting the operator; proving which hardware it ran on needs a separately verified attestation. Built on IETF RATS (RFC 9334), EAT (RFC 9711), SCITT, SLSA, and SPIFFE. Spec v0.2.
- [Weight Custody Manifest (WCM)](https://github.com/agentrust-io/weight-custody-manifest) - Open, pre-1.0 specification and Python SDK that hands out the key to decrypt a model's weights only to a workload whose CPU (and, when required, GPU) attestation matches a signed manifest, with short-lived approval and a record of each release. The reference SDK verifies AMD SEV-SNP, Intel TDX, and NVIDIA H100 CC evidence captured on real hardware. Against an operator who physically owns the machine it offers accountability rather than cryptographic custody. Apache-2.0; `pip install weight-custody-manifest`; docs at [wcm.agentrust-io.com](https://wcm.agentrust-io.com).
- [SourceryKit](https://github.com/ProvablyAI/sourcerykit) - Verifies an agent's outbound requests and MCP handoffs against a source of truth using zero-knowledge proofs, so a call only goes out if the agent's claims check out. Hooks into the HTTP libraries, logs every outbound call, and blocks endpoints not on the trusted allow-list. Python, BSL 1.1 (source-available), with a hosted backend that runs the proof and source-of-truth check.

## Policy as Code

*Languages and engines for writing access rules as code and checking them. Useful for limiting what an agent may do, which tools it may call and which data it may touch.*

- [agent-evidence-admission](https://github.com/probityai/agent-evidence-admission) - Apache-2.0 Kubernetes admission policies for OPA, Kyverno, and Sigstore policy-controller that evaluate agent-execution evidence, with documented enforcement limits and conformance checks.
- [Casbin](https://github.com/casbin/casbin) - Cross-language authorization library supporting ACL, RBAC, and ABAC models. Available in Go, Python, Java, and more.
- [Cedar](https://github.com/cedar-policy/cedar) - Amazon's policy language for fine-grained, type-safe access control. Used as the policy engine in the Agent Governance Toolkit. Fast, formally verified, and human-readable.
- [GOPAL](https://github.com/Principled-Evolution/gopal) - Apache-2.0 library of 85 Rego policies encoding AI-governance regulations (EU AI Act, NIST AI RMF, ICAO/FAA/EASA aviation, FERPA/COPPA, fair lending) as executable allow/deny checks for the OPA engine, versioned per framework with allow/deny tests in CI.
- [Open Policy Agent (OPA)](https://github.com/open-policy-agent/opa) - CNCF general-purpose policy engine. Decouples policy decisions from application logic using the Rego language. Widely deployed for Kubernetes and API authorization.
- [SpiceDB](https://github.com/authzed/spicedb) - Google Zanzibar-inspired database for fine-grained, relationship-based authorization. Useful for cross-agent and multi-tenant permission modeling.

## LLM Safety & Guardrails

*Filters that check what goes into and comes out of a language model (LLM): unsafe content, leaked personal data, and prompt injection, which is text written to hijack the model's instructions.*

- [ai-evaluation](https://github.com/future-agi/ai-evaluation) - Open-source LLM evaluation framework with 50+ metrics, LLM-as-Judge, and guardrail scanners (jailbreak, PII, injection).
- [Arthur Shield](https://www.arthur.ai/product/shield) - Firewall for LLMs that detects hallucinations, toxicity, PII leakage, and prompt injection in real time.
- [Guardrails AI](https://github.com/guardrails-ai/guardrails) - Framework for structural, type, and quality guarantees on LLM outputs. Guardrails Hub provides community validators.
- [Hyperion](https://github.com/Salesforce/hyperion) - Framework for evaluating and improving robustness of LLM-based agents against adversarial attacks.
- [Lakera Guard](https://www.lakera.ai/) - Real-time API for detecting prompt injections, data leakage, toxic content, and other LLM security threats.
- [LLM Guard](https://github.com/protectai/llm-guard) - Input and output scanners covering toxicity, PII, prompt injection, invisible text, and code detection.
- [Meta Llama Guard](https://github.com/meta-llama/PurpleLlama) - Safety classifier models for filtering unsafe LLM inputs and outputs. Part of Meta's Purple Llama safety suite.
- [NVIDIA NeMo Guardrails](https://github.com/NVIDIA/NeMo-Guardrails) - Open-source toolkit for adding programmable guardrails to LLM-based conversational systems using Colang.
- [Rebuff](https://github.com/protectai/rebuff) - Prompt injection detection using multi-layer defense: heuristics, LLM analysis, and canary tokens.
- [shim-cli](https://github.com/GetSHIM/shim-cli) - Local hooks for Claude Code, Codex, Copilot CLI and VS Code that detect secrets and personal data in agent traffic, mask them in Claude Code tool results before the model reads them, and keep a count-only session record.
- [Vigil](https://github.com/deadbits/vigil-llm) - LLM security scanner for detecting prompt injections using embedding similarity, heuristics, and canary tokens.

## Agent Frameworks with Governance Features

*Toolkits for building agents that include places to plug in safety checks, human approval or policy rules.*

- [AgentScope](https://github.com/modelscope/agentscope) - Multi-agent platform with fault tolerance, agent-level monitoring, and configurable message validation.
- [AutoGen](https://github.com/microsoft/autogen) - Multi-agent conversation framework with human oversight, code execution sandboxing, and conversation policies.
- [CorvinOS](https://github.com/CorvinLabs/CorvinOS) - Self-hosted agentic OS connecting local and cloud models to Discord, Telegram, WhatsApp, Slack, and Email, with a fail-closed GDPR consent gate, hash-chained audit log, and bot-disclosure controls. Python, Apache-2.0.
- [CrewAI](https://github.com/crewAIInc/crewAI) - Multi-agent orchestration with role-based agents, task delegation, and configurable guardrails.
- [Dify](https://github.com/langgenius/dify) - LLM app development platform with content moderation, rate limiting, and annotation logging.
- [Google Agent Development Kit (ADK)](https://github.com/google/adk-python) - Google's agent framework with safety callbacks, evaluation tools, and multi-agent session management.
- [Google Sovereign Agent Mesh (SAM)](https://github.com/google/sam) - Apache-2.0 agent-mesh project with cryptographic node identities, authenticated peer connections and packets, discovery, authorization policies, and MCP sidecar routing. The repository states that it is not an officially supported Google product.
- [Haystack](https://github.com/deepset-ai/haystack) - End-to-end NLP framework with pipeline-based architecture supporting content filtering and validation.
- [LangChain](https://github.com/langchain-ai/langchain) - Composable framework with callbacks, tracing, and moderation chains for LLM applications.
- [LangGraph](https://github.com/langchain-ai/langgraph) - Stateful, multi-actor agent framework with human-in-the-loop and persistence built in.
- [LightAgent](https://github.com/wanxingai/LightAgent) - Python agent framework with narrowing-only security contexts, scoped capability gates, durable human approvals, and application-owned verification before publishing immutable DAG artifacts.
- [LlamaIndex](https://github.com/run-llama/llama_index) - Data framework with observability callbacks, evaluation modules, and structured output guarantees.
- [Microsoft Agent Framework (MAF)](https://github.com/microsoft/agent-framework) - Microsoft's multi-agent orchestration framework for Python and .NET, with migration paths from Semantic Kernel and AutoGen. Governance-relevant pieces are human-in-the-loop workflow steps, checkpointing, and built-in OpenTelemetry tracing.
- [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) - Official OpenAI SDK with built-in guardrails, input/output validation, and handoff controls.
- [PydanticAI](https://github.com/pydantic/pydantic-ai) - Agent framework with type-safe tool definitions, structured outputs, and dependency injection.
- [Semantic Kernel](https://github.com/microsoft/semantic-kernel) - Microsoft's AI orchestration SDK with plugin permission models, function filtering, and responsible AI hooks.
- [smolagents](https://github.com/huggingface/smolagents) - Hugging Face's lightweight agent library with sandboxed code execution and security controls.

## Agent Identity & Attestation

*Ways to give an AI agent an identity that others can check with cryptography, and to trace where it came from. For agent identity backed by a signed hardware report, see [End-to-End Governance: Software and Hardware](#end-to-end-governance-software-and-hardware).*

- [Agent Card / AI Card](https://a2a-protocol.org/latest/specification/#8-agent-discovery-the-agent-card) - Specification for machine-readable agent capability and policy metadata, enabling discovery and trust decisions.
- [Agent Passport System](https://github.com/aeoess/agent-passport-system) - Apache-2.0 protocol for agent identity, scoped delegation with monotonic narrowing, runtime enforcement, and signed action receipts. TypeScript and Python SDKs; active IETF Internet-Draft (draft-pidlisnyi-aps).
- [Etch](https://etch.systems) - Signed, offline-verifiable audit chain for AI agent decisions with portable per-agent identity across MCP client tools. Open-source reference verifier (`world-model-mcp` on PyPI, MIT): hybrid Ed25519 + FIPS 205 SLH-DSA-SHA2-128f signing over Merkle-chained epochs, chain-integrity + signature verification offline. Hosted service (etch.systems, BSL 1.1) extends with Sigstore Rekor + Bitcoin OpenTimestamps anchoring, key rotation, delegation grants and revocations, and memory-per-identity across MCP client tools. Portable identity envelope + JSON Schema + conformance vectors on Zenodo ([DOI 10.5281/zenodo.22154537](https://doi.org/10.5281/zenodo.22154537)).
- [Kepil](https://github.com/oleg-vdv/kepil) - AGPL-3.0 Python toolkit for agent-version passports, per-job mandates, and a gateway that checks submitted actions against permissions, spending limits, and expiry. Passport construction rejects the highest autonomy class. Uses the Python standard library.
- [scitt-cose](https://github.com/action-state-group/scitt-cose) - Payload-agnostic IETF SCITT + COSE verification substrate (Python): verifies Signed Statements and RFC 9162 SHA-256 Receipts with inclusion/consistency proofs, offline. Open source to run yourself, or hit the free community verify service at verify.agentactioncapsule.org to check a receipt without trusting the issuer. Apache-2.0.
- [SPIFFE/SVID](https://spiffe.io/) - Secure Production Identity Framework for Everyone. Cryptographic workload identity applicable to agent-to-agent authentication.
- [W3C Decentralized Identifiers (DIDs)](https://www.w3.org/TR/did-core/) - W3C standard for decentralized, self-sovereign identifiers applicable to durable agent identity without centralized registries.

## Agent Action Records

*Formats and services that record what an agent actually did as signed receipts and public logs, which anyone can check later, offline if needed. The Agent Identity & Attestation section covers who the agent is; this one covers what it did.*

- [Agent Action Capsule (AAC)](https://github.com/action-state-group/agent-action-capsule) - Open SCITT statement profile (IETF draft-mih-scitt-agent-action-capsule) for recording and verifying what an AI agent did: each action is sealed into a content-addressed, offline-verifiable capsule (JCS/RFC 8785) a third party can check without calling the operator. Apache-2.0; reference library, test vectors, and standard site at agentactioncapsule.org.
- [agent-evidence-vectors](https://github.com/probityai/agent-evidence-vectors) - Apache-2.0 conformance corpora and reference verifiers for proposed agent-execution evidence predicates, SCITT/COSE carriage, and related evidence-binding profiles.
- [agent-trace](https://github.com/oleg-vdv/agent-trace) - MIT TypeScript verifier for Python-generated, hash-chained agent journals. Checks sequence, chain linkage, and record hashes, reporting the first failing record's sequence number. Developed in the ProofByte monorepo.
- [capsule-anchor](https://github.com/action-state-group/capsule-anchor) - Software for anyone to run their own vendor-neutral SCITT Transparency Service (RFC 9162): submit a digest, get a COSE receipt anchoring it into an append-only, independently auditable log that anyone can verify offline. Run your own, or use the free community instance at witness.agentactioncapsule.org. Apache-2.0.
- [capsule-emit](https://github.com/action-state-group/capsule-emit) - The reference implementation of Agent Action Capsule: a one-call `emit()` producer that seals an action into a capsule, anchors it by default, and ships a ledger-view CLI with thin framework adapters. Apache-2.0.
- [Nobulex](https://github.com/arian-gogani/nobulex) - Bilateral receipt primitive for tamper-evident agent audit trails: two Ed25519 signatures per action (pre- and post-execution), hash-chained via JCS canonicalization (RFC 8785). The receipt-signing approach is [merged into AGT](https://github.com/microsoft/agent-governance-toolkit/pull/1333). MIT licensed.
- [PIC Standard (Provenance & Intent Contracts)](https://github.com/madeinplutofabio/pic-standard) - Open, local-first protocol for pre-execution action gating in AI agents: the agent declares intent, provenance, and evidence before a high-impact tool call; the verifier returns allow or block, failing closed on missing or invalid evidence, under a Trust Axiom that trust is verifier-derived, not producer-asserted. Apache-2.0. Pre-v1.0 draft.
- [proofbundle](https://github.com/b7n0de/proofbundle) - Signed, portable receipts for AI evaluation and review results, verifiable offline with the public key alone: Ed25519 over canonical JSON (RFC 8785), RFC 6962 Merkle inclusion for samples, optional SD-JWT selective disclosure and in-toto statement export, a verifier with a fixed exit-code contract and a 130-case conformance corpus. Establishes evidence integrity, not whether the result is correct. MIT.
- [Signed Decision Receipts (IETF)](https://datatracker.ietf.org/doc/draft-farley-acta-signed-receipts/) - Internet-Draft defining a portable, cryptographically signed receipt format for machine-to-machine access control decisions. Ed25519 + JCS canonicalization. Independently verifiable offline.
- [YYLO Benchmark](https://github.com/yylo-dev/yylo-benchmark) - Evaluation layer for task prompts that records each attempt for verification: every candidate runs in a private fresh-repository workspace behind an initial workspace receipt plus a deterministic post-execution manifest covering Git HEAD/tree/refs/index/status and every worktree file; recovery reuses hash-verified terminals, and retained state is rejected unless the complete chain from state, plan, and attempt through receipt, manifest, terminal, and evidence forms one exact linkage. Deterministic and LLM-judge evaluations append immutable records with evidence and evaluator provenance hashes; running a plan grants no production or external authority. MIT; CLI `yylo-benchmark` (also delegated unchanged by `yy benchmark`) and library on npm as @yylo/benchmark; part of the YYLO suite alongside the YYLO CLI orchestrator.

## Observability & Monitoring

*Tools for tracing, monitoring, testing and debugging what AI agents do.*

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
- [OrcaPromptVault](https://github.com/Continuum-AI-Corp/OrcaPromptVault) - Versioned archive of agent prompts, developer instructions, and tool schemas. Distinguishes locally captured material with reproduction commands from model-reported material whose accuracy is unverified. AGPL-3.0.
- [Prometheus](https://prometheus.io/) + [Grafana](https://grafana.com/) - Industry-standard metrics and visualization. Foundation for custom agent SLO dashboards.
- [Provena](https://github.com/rajfirke/provena) - Open-source Python library for tamper-evident audit trails of AI agent context inputs: hash-chained logging, provenance validation, and freshness checking, with EU AI Act and OWASP ASI06 compliance reporting.
- [traceAI](https://github.com/future-agi/traceAI) - Open-source OpenTelemetry-native tracing for LLM and agent apps with 50+ framework integrations.
- [Weights & Biases](https://wandb.ai/) - ML experiment tracking with LLM tracing, evaluation pipelines, and model monitoring.

## Security Testing

*Scanners, red-teaming tools (which run simulated attacks) and frameworks for testing how AI agents and LLMs hold up against attackers.*

- [Commit](https://getcommit.dev) - Supply chain trust scoring for npm, PyPI, Cargo, and Go packages. Scores maintainer concentration, OIDC publisher gaps, and release consistency to surface high-risk dependency patterns that vulnerability databases miss. CLI, GitHub Action, IDE hooks, REST API, and MCP server.
- [Counterfit](https://github.com/Azure/counterfit) - Azure's tool for assessing ML model security through adversarial attacks.
- [CyberSecEval](https://github.com/meta-llama/PurpleLlama/tree/main/CybersecurityBenchmarks) - Meta's benchmark suite for LLM cybersecurity risks including insecure code generation and prompt extraction.
- [Garak](https://github.com/NVIDIA/garak) - LLM vulnerability scanner from NVIDIA. Probes for hallucination, data leakage, prompt injection, toxicity, and more.
- [Hermes Jailbench](https://github.com/hermes-labs-ai/hermes-jailbench) - Deterministic jailbreak regression battery that runs repeatable attacks against an LLM endpoint and scores refusal, partial, and compliance outcomes across runs.
- [HouYi](https://github.com/LLMSecurity/HouYi) - Prompt injection attack framework for testing LLM-integrated application security boundaries.
- [mcp-evidence-validator](https://github.com/narko4u/mcp-evidence-validator) - Reference implementation of SHA-256 evidence chains for MCP agents: verifies declared tool contracts against observed runtime behavior (declared vs observed). Apache-2.0, OpenSSF Best Practices badge.
- [PyRIT](https://github.com/Azure/PyRIT) - Microsoft's Python Risk Identification Toolkit for red-teaming generative AI systems with automated attack strategies.
- [sentinel-scan-cli](https://github.com/Ventrova/sentinel-scan-cli) - Free, open-source CLI (and MCP server) that scans MCP manifests and LLM apps for tool poisoning, prompt injection, and rug-pulls, with OWASP LLM Top 10-mapped findings.
- [Snyk Agent Scan](https://github.com/snyk/agent-scan) - Security scanner for AI agents and MCP servers. Detects vulnerabilities in tool configurations, permissions, and data flows.

## Fairness & Bias Auditing

*Toolkits for checking AI decision systems for unfair bias and measuring whether a fix worked.*

- [Fair Code](https://github.com/yakew7/Fair-Code) - Audits real-world-style AI decision systems (criminal justice, hiring, lending, insurance, welfare, hospital readmission, tenant screening) for algorithmic bias, pairing a biased baseline with a mitigated version and measured before/after fairness metrics.

## Standards & Specifications

*Protocols, specifications and regulations that matter for governing agents and for making agents from different vendors work together.*

- [AIREP (AI Runtime Evidence Protocol)](https://github.com/halvrenofviryel/ai-runtime-evidence-protocol) - Experimental, vendor-neutral runtime-evidence format for AI decisions, control delivery, execution, and observed effects, with signed/hash-linked artifacts and explicit missing or unevaluated states. Open specification; not a ratified standard.

- [AI Agent Trace Schema](https://github.com/Isaacruwa/ai-agent-trace-schema) - Open JSON Schema normalizing AI-agent runtime events (tool calls, human interventions, errors, deployment changes) into a common format for compliance evidence, with converters for OpenTelemetry and LangSmith exports.

- [agent-evidence-vocabulary](https://github.com/probityai/agent-evidence-vocabulary) - Versioned CC0 vocabulary for adversarial-execution evidence claims, with crosswalk templates, governance rules, and validation tooling. Repository code and documentation are Apache-2.0.

- [Agent-to-Agent Protocol (A2A)](https://github.com/google/A2A) - Google-led open protocol for inter-agent communication, task delegation, and capability discovery.

- [Universal Commerce Protocol (UCP)](https://github.com/Universal-Commerce-Protocol/ucp) - Open protocol for interoperable agentic commerce, including checkout operations and response-carried request constraints that can narrow what a client is permitted to submit.

- [ACI/AIP/AJSON](https://github.com/narko4u/aci-spec) - Open standards for agent interoperability and governance: Agent Communication Interface (ACI), Agent Interaction Protocol (AIP), and Agent JSON (AJSON) machine-readable agent manifests for discovery, delegation, and governance.

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

- [Singapore IMDA Model AI Governance Framework for Agentic AI](https://www.imda.gov.sg/-/media/imda/files/about/emerging-tech-and-research/artificial-intelligence/mgf-for-agentic-ai.pdf) - Singapore IMDA framework defining eight components of an agentic system (Model, Instructions, Memory, Planning & Reasoning, Tools, Protocols, Controls, Logging/Monitoring) and four governance dimensions (bounding risks, human accountability, technical controls, end-user responsibility). v1.5 published 20 May 2026

- [SPDX 3.0.1 AI Profile](https://github.com/spdx/spdx-3-model) - SPDX specification for AI Bill of Materials (AIBOM) with AIPackage and DatasetPackage classes covering automation level, autonomy type, hyperparameters, model explainability, safety risk assessment, anonymization method, dataset size, and sensitive personal information flags. Stable since December 2024 (3.0.1); 3.1-RC1 pre-release adds EU AI Act-aligned dataset size properties (token count, item count, content duration).

## Research Papers

*Key academic papers on agent safety, governing groups of agents that work together, and trust in AI systems.*

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

*Practical guides, threat models (lists of how a system can be attacked) and industry analysis on governing agents.*

- [AI Agent Incident Register](https://companyscope.io/register) - A numbered public corpus of AI agent incidents, each analysed for the legal duty engaged, who bears liability across the chain (deployer / shared / vendor), and the governance that would have prevented it. Includes a Liability Crosswalk mapping OWASP's agentic Top 10, the NIST AI RMF, Singapore's IMDA framework, and the EU AI Act to each other and to who carries liability. Free to read and cite; CC BY 4.0 machine-readable feed.
- [Singapore AI Governance Readiness Checklist](https://vyrwork.com/tools/singapore-ai-governance-readiness-checklist) - Free evidence-oriented planning checklist translating IMDA's 2026 agentic AI governance dimensions into 24 prompts for risk bounds, accountable ownership, lifecycle technical controls, and end-user responsibility. It is a planning aid, not a certification or compliance score.
- [Preventive vs. Reactive AI Agent Governance](https://penholder.ai/preventive-vs-reactive-ai-agent-governance.html) - Comparison of preventive control (gating an agent's write to a system of record behind human approval before it commits) versus reactive governance (detecting and remediating harmful actions after they have executed), and the trade-offs of each model.
- [Anthropic's Responsible Scaling Policy](https://www.anthropic.com/responsible-scaling-policy) - Framework for responsible AI deployment with AI Safety Levels (ASL) and safety evaluation commitments.
- [Anthropic: Trustworthy Agents in Practice](https://www.anthropic.com/research/trustworthy-agents) - Anthropic's practical guidance on deploying trustworthy agents: balancing autonomy with human oversight, prompt-injection resistance, and operational safeguards.
- [CSA AI Safety Initiative](https://cloudsecurityalliance.org/research/working-groups/artificial-intelligence) - Cloud Security Alliance publications on AI safety and security best practices.
- [Google Secure AI Framework (SAIF)](https://safety.google/cybersecurity-advancements/saif/) - Conceptual framework for securing AI systems across the development and deployment lifecycle.
- [Microsoft Responsible AI](https://www.microsoft.com/en-us/ai/responsible-ai) - Hub for Microsoft's responsible AI practice: the six principles, the governance structure behind them, and transparency notes for shipped systems. Links out to the Responsible AI Standard itself, which is a separate document.
- [MITRE ATLAS](https://atlas.mitre.org/) - Adversarial Threat Landscape for AI Systems. Adversary tactics and techniques against AI/ML systems, structured like ATT&CK.
- [OWASP Agentic AI Threats and Mitigations](https://genai.owasp.org/resource/agentic-ai-threats-and-mitigations/) - OWASP's threat catalog and mitigation strategies for agentic applications.
- [OWASP Top 10 for LLM Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/) - Top 10 security risks for LLM applications including prompt injection, insecure output handling, and supply chain vulnerabilities.
- [EU AI Regulation Decoded](https://euaird.vercel.app/) - Practitioner reference mapping EU AI Act obligations to the specific evidence an auditor expects (by role, risk tier, and deadline), with common audit red flags. Includes a free interactive audit-readiness checklist and a CC BY 4.0 machine-readable [obligation-to-evidence dataset](https://github.com/Kroniquedubaboo/eu-ai-act-obligation-evidence-dataset).
- [Model Trust Gate](https://github.com/josephManzambi/model-trust-gate) - Adopter-side method for deciding whether to trust one AI model for one use, ending in a signed, expiring record with a JSON schema a policy engine can check.

## Talks & Videos

*Recorded talks and sessions on governing agents, enforcing rules while agents run, and running agents on hardware that can prove what it ran. Speaker and venue are listed so you can see who said what.*

- [Agentic AI Is Running Your Infrastructure](https://www.youtube.com/watch?v=1Z_7hvy_-YE) - Mike Bursell, Confidential Computing Consortium. Keynote on what changes when agents operate infrastructure rather than assist people, and where confidential computing sits in that trust model. Confidential Computing Summit 2026.
- [Agentic Zero Trust: at Rest, in Transit, and at Runtime](https://www.youtube.com/watch?v=x7j0D5VYUhw) - N. Polshakova (Solo.io) and J. Halley (Cisco) on extending zero-trust principles to the agent runtime, not just the network. Confidential Computing Summit 2026.
- [Building Governed AI Agents with the Agent Governance Toolkit](https://www.youtube.com/watch?v=uDQBqp9Om5s) - Imran Siddique (OPAQUE Systems) walking through AGT's policy enforcement and audit model for enterprise deployments. GenAI Gurus, May 2026.
- [From Trust to Proof: The Next Generation of AI Agent Governance](https://www.youtube.com/watch?v=uz4absejhHc) - Imran Siddique and Jason Lazarski (OPAQUE Systems) on the gap between controlling an agent and proving you controlled it, and how Agent Manifest, cMCP, and TRACE close it. July 2026.
- [Governing AI Agents at Runtime: Open Source Zero-Trust with AGT](https://www.youtube.com/watch?v=YtjjoPTN0U8) - Imran Siddique on runtime governance for agents moving from demo to production. Ubuntu Summit 26.04, Canonical.
- [Governing AI Agents at the Hardware Boundary](https://www.youtube.com/watch?v=z8hOZ77iiJo) - Imran Siddique (OPAQUE Systems) on why software-only enforcement has a structural ceiling and what moving the control point into a TEE buys. Confidential Computing Summit 2026.
- [NVIDIA Confidential Computing Attestation for Next-Generation AI](https://www.youtube.com/watch?v=vzQVZA7veO0) - R. Nertney and S. Gilson (NVIDIA) on GPU attestation and the evidence it produces for AI workloads. Confidential Computing Summit 2026.
- [Open Source Friday: Governance for AI Agents](https://www.youtube.com/watch?v=bIioEmT2KEM) - Imran Siddique with GitHub on why prompts are not a control surface, plus the practical side of running a fast-growing governance project in the open. June 2026.
- [Reliability in AI (Agentic) Systems](https://www.youtube.com/watch?v=jvHZAQdx-LU) - Panel on failure modes, evaluation, and what reliability means for systems that act. Confidential Computing Summit 2026.

## Conferences & Communities

*Where research, practice and discussion on agent governance happen.*

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

Contributions are welcome. Read the [contribution guidelines](https://governance.agentrust-io.com/CONTRIBUTING/index.md) and open a pull request. Open-source governance tools, research papers and community resources are especially welcome.

Join the community on [Discord](https://discord.gg/grgzFEHgkj).

______________________________________________________________________

*Maintained by [Imran Siddique](https://github.com/imran-siddique), CPO at [OPAQUE Systems](https://opaque.co), creator of the [Agent Governance Toolkit](https://github.com/microsoft/agent-governance-toolkit), and contributor to OWASP ASI, CoSAI WS4, and the Agentic AI Foundation. The curator also maintains the [agentrust-io](https://github.com/agentrust-io) repositories: Weight Custody Manifest, Agent Manifest, cMCP, cA2A, TRACE and its conformance suite and registry, and AgenTrust Telemetry.*
