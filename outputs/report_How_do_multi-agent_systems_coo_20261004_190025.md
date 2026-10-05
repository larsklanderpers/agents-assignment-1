# How Do Multi-Agent Systems Coordinate and Communicate?

## Executive Summary

Multi-agent systems coordinate by aligning agents’ actions, plans, and roles. Communication is one way to achieve this, but it is not the only possible mechanism. The supplied evidence is strongest for large language model (LLM)-based systems that use explicit conversation. These systems organize work through role assignments, instruction messages, speaker selection, message broadcasts, and social discussion. Examples include AutoGen’s conversational workflows and manager–specialist arrangement, CAMEL’s role-based message exchanges, and Generative Agents’ simulated social planning (AutoGen, 2023; CAMEL, 2023; Park et al., 2023).

The examples show that agents can exchange information and coordinate particular activities. They do not establish that multi-agent designs consistently improve performance. AutoGen’s reported evaluation found that both systems answered eight of ten questions correctly, but the supplied excerpt does not give enough detail to interpret the full comparison (AutoGen, 2023). Generative Agents reports simulated social coordination, alongside a tendency toward over-cooperation and a small rate of hallucinated awareness responses (Park et al., 2023).

The evidence does not adequately cover classical multi-agent protocols, coordination through markets or shared environments, formal conflict resolution, or performance under unreliable communication and large-scale conditions. Thus, the most supported answer is that the LLM-based systems in the supplied sources coordinate mainly through role-structured, explicit messages and planning. Whether those methods are more effective, robust, or efficient than other approaches remains uncertain.

## Introduction

Multi-agent systems consist of multiple agents whose actions affect one another or contribute to a shared task. Coordination concerns how agents align their actions, goals, plans, or use of resources. Communication can support this alignment by sharing information, instructions, or proposals. It is not the same as coordination: agents may coordinate through rules, shared plans, or features of a shared environment, even when they do not exchange direct messages.

This review addresses the question: **How do multi-agent systems coordinate and communicate?** It considers evidence from both classical multi-agent systems and LLM-based systems. However, the supplied evidence is weighted toward LLM-based systems. It includes descriptions of AutoGen, CAMEL, and Generative Agents, but offers little usable detail about classical communication protocols or non-message coordination mechanisms.

The central pattern in the available evidence is that LLM-based systems use roles and explicit conversation to organize joint work. The sources also show why claims about the benefits of this approach need care: the reported evaluations are limited, and coordinated behavior in a simulation does not by itself demonstrate reliable performance in operational settings.

## Methodology

This review uses the supplied search strategy and evidence collection. Searches covered coordination and communication in classical and LLM-based multi-agent systems. The search terms included agent roles, orchestration, message passing, dialogue, shared memory, task allocation, negotiation, coordination mechanisms, evaluation, and system limitations.

The evidence includes retrieved excerpts from three sources:

- *AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation* (AutoGen, 2023).
- *CAMEL: Communicative Agents for Mind Exploration of Large Language Model Society* (CAMEL, 2023).
- *Generative Agents: Interactive Simulacra of Human Behavior* (Park et al., 2023).

Several excerpts are incomplete or truncated. This review does not fill in missing text or infer unreported methods and results. The supplied material also does not include full bibliographic details such as publication venues, page ranges, or complete author lists for AutoGen and CAMEL. These details are therefore not added to the references.

## Findings

### 1. Roles and delegated work organize coordination

A recurring design in the LLM-based sources is to assign agents distinct roles or capabilities, then use their interactions to organize a workflow. AutoGen describes complex workflows as a combination of agent actions and messages between agents. It calls this approach “conversation programming” and describes defining agents with specific capabilities as part of the design (AutoGen, 2023).

One AutoGen example uses a Commander agent that coordinates with Writer and Safeguard assistants. This illustrates a manager–specialist structure: one agent directs or coordinates work, while other agents contribute specialized functions (AutoGen, 2023). The supplied excerpt does not show the full interaction or establish how the system handles disagreements among these agents.

AutoGen also describes agents that can use LLMs, people, or tools. This suggests that coordination may involve participants with different capabilities, not only multiple LLM instances (AutoGen, 2023). The excerpt is incomplete, so it does not establish how these participants’ responsibilities are assigned in general.

CAMEL provides a related example of role-based interaction. Its retrieved passages describe iterative instruction messages between agents and a prescribed message format intended to support consistency and accuracy (CAMEL, 2023). The excerpts do not show the full message format or establish whether it improves coordination in practice.

**Synthesis.** AutoGen and CAMEL both treat roles and communication structure as ways to organize joint work. These descriptions establish design patterns, not a general performance advantage. The supplied evidence does not compare role-based systems with simpler approaches or test how well roles adapt when tasks or agent capabilities change.

### 2. Explicit messages support information exchange and workflow control

The clearest communication mechanisms in the supplied evidence are explicit messages. AutoGen frames workflows as inter-agent conversation and message passing (AutoGen, 2023). Its group-chat example describes selecting a speaker, asking that agent to respond, and broadcasting the response to the other agents. This gives a concrete process for circulating contributions across a group. The retrieved passage notes that the source discusses validation of dynamic group chat and role-based speaker selection, but it does not include the validation results.

CAMEL’s fragments describe agents exchanging iterative instruction messages under a specified format (CAMEL, 2023). Generative Agents instead illustrates natural-language social exchanges. In one example, agents discuss information about a local election; however, the excerpt states that two agents heard the news from another source. It therefore illustrates discussion, but not a direct chain of information sharing between every agent (Park et al., 2023).

Across these examples, messages can convey information, issue instructions, invite responses, or support planning. The sources do not establish a common formal protocol for message meaning, timing, or compliance. Nor do they show how agents decide when to communicate and when to act without another message.

**Synthesis.** Explicit communication appears in all three systems, but it takes different forms: programmed conversations and broadcasts in AutoGen, formatted instruction messages in CAMEL, and social dialogue in Generative Agents. The supplied evidence does not compare these methods directly. It therefore supports a description of different communication patterns, not a conclusion that one pattern is generally superior.

### 3. Conversation and planning can support synchronization

Generative Agents offers an example of coordination across time. In the simulation, agents form acquaintances, invite one another to a party, and coordinate to arrive together at the right time through social interaction and planning (Park et al., 2023). This example links communication with synchronization: agents discuss a shared activity and align when they take part.

The source also reports a rise in the simulated community’s social-network density from 0.167 to 0.74. It reports that six of 453 responses about agents’ awareness of other agents were judged to be hallucinated, or 1.3%, and describes evidence of coordination for Isabella’s party (Park et al., 2023). These measures provide evidence about one simulated community. They do not, by themselves, establish general task success, reliable synchronization, or performance outside that setting.

The same source notes that instruction tuning appeared to make agents overly cooperative. For example, agents offered Isabella many suggestions for a Valentine’s Day party (Park et al., 2023). This observation qualifies the coordination example. Agents may align readily because of a cooperative response tendency, not because the system can resolve serious disagreement or balance competing preferences.

**Synthesis.** The simulation demonstrates that conversational agents can coordinate a shared activity in a particular setting. It does not show how they would perform with scarce resources, conflicting goals, or high costs for coordination. Over-cooperation is a relevant limitation because agreement between agents is not always evidence of sound conflict resolution.

### 4. Performance evidence is limited and does not establish a general advantage

The supplied AutoGen excerpt reports a small evaluation with an expert Python programmer and ten randomly selected questions. Both systems answered eight questions correctly. The excerpt is truncated before it fully identifies the systems and reports the timing comparison (AutoGen, 2023). The equal answer counts do not demonstrate an accuracy advantage for the multi-agent system. But the small sample and missing details also do not show that multi-agent systems lack such an advantage.

Generative Agents reports different measures: changes in social-network density, judged hallucinations in agent-awareness responses, and an observed instance of party coordination (Park et al., 2023). These measures describe a simulated society and cannot be directly compared with AutoGen’s answer accuracy. The sources therefore provide evidence about different outcomes rather than a shared measure of coordination quality.

**Synthesis.** The evidence shows that agents can display coordinated behavior, but it does not establish that multi-agent coordination reliably improves task performance. The AutoGen result is limited and does not show a difference in accuracy in the reported test. The Generative Agents findings show coordination in a simulation, but also identify possible over-cooperation and hallucinated awareness. These findings are not direct contradictions: the systems, tasks, and outcome measures differ.

### 5. The evidence is thin on classical and non-message mechanisms

Although the search strategy included classical multi-agent coordination, the supplied excerpts do not provide enough evidence to describe specific classical communication languages, formal negotiation protocols, contract nets, auctions, voting, or consensus procedures. They also do not give substantiated examples of coordination through stigmergy, shared plans, conventions, or other environment-mediated mechanisms.

This is a limit of the supplied evidence, not evidence that these mechanisms are absent or ineffective. The review can therefore describe conversational LLM-agent designs in more detail than it can compare those designs with classical coordination approaches.

### 6. Robustness, scale, and conflict resolution remain open questions

The supplied excerpts do not quantify message volume, communication overhead, latency, bandwidth, or the effects of unreliable messages. They also do not show how the systems perform when agents fail, information is incomplete, or the number of agents grows.

Likewise, the sources provide little direct evidence about formal conflict resolution. Role-based collaboration and social discussion are present, but the excerpts do not establish how agents negotiate when they have incompatible goals, how they reach agreement, or whether they can maintain coordination under persistent disagreement. The evidence is also insufficient to assess learned communication or emergent conventions in multi-agent learning.

## Discussion

The supplied sources support a clear but bounded account of how the featured LLM-based systems coordinate. They use roles or capabilities to divide work and explicit messages to exchange instructions, information, and proposals. Communication may be structured as a group conversation, a formatted sequence of instructions, or social dialogue. Planning can then help agents align actions, including when to take part in a shared activity (AutoGen, 2023; CAMEL, 2023; Park et al., 2023).

The sources agree on the importance of communication as part of the coordination design. They do not show that communication alone produces successful coordination, or that more messages produce better outcomes. Nor do they provide a direct comparison of conversational approaches with coordination through shared rules, markets, or environments.

The evidence on effectiveness is mixed in a limited sense. AutoGen’s excerpt does not show an accuracy advantage in a ten-question comparison, while Generative Agents describes coordinated behavior in a simulation. These findings do not conflict because they concern different tasks and measures. Instead, they reveal a broader evaluation problem: the sources use different indicators of success, and the supplied evidence does not establish a common basis for comparison.

Several limitations constrain the conclusions:

- **Incomplete excerpts:** Some passages end before describing full protocols, outcomes, or comparisons.
- **Narrow evidence base:** The usable evidence focuses on three LLM-based systems and does not provide a balanced account of classical MAS.
- **Limited evaluation:** The AutoGen excerpt reports a small sample, while the Generative Agents evidence comes from a particular simulation.
- **Limited operational evidence:** The supplied material does not establish performance in real-world deployments.
- **Limited evidence on costs and failures:** It does not quantify communication overhead, scale, reliability, or agent-failure effects.

These limits point to research needs. Future studies should compare coordination architectures on common tasks; measure task outcomes alongside message costs; test explicit communication against reduced-message, silent, and environment-mediated approaches; and examine genuine conflict, changing goals, and resource constraints. Evaluations should also test reliability and scale, use clear baselines, and report enough detail to support replication and comparison. Finally, work on LLM-agent systems would benefit from a clearer comparison with established multi-agent theory and classical coordination mechanisms.

## Conclusion

In the supplied evidence, multi-agent systems—especially the LLM-based systems examined here—coordinate mainly by assigning agents roles or capabilities and using explicit communication to organize their actions. Messages carry instructions, information, and proposals. Conversation may be directed through a manager–specialist structure, a selected-speaker group chat, formatted role-based exchanges, or social dialogue. Planning can help agents synchronize their behavior around a shared activity.

However, these examples do not establish that conversation-based coordination is generally more effective than other mechanisms. The evaluation evidence is limited, and the reported outcomes come from different tasks and measures. The sources also leave major gaps in evidence about classical coordination mechanisms, conflict resolution, communication cost, scalability, and robustness.

The direct answer is therefore: **multi-agent systems can coordinate through explicit messages and structured roles, and some can coordinate through social interaction and planning. But the available evidence does not show when these methods are best, how they compare with non-message mechanisms, or whether their benefits hold under conflict, failure, and scale.**

## References

- AutoGen. (2023). *AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation*. Full-text source supplied; complete bibliographic details were not provided.
- CAMEL. (2023). *CAMEL: Communicative Agents for Mind Exploration of Large Language Model Society*. Full-text source supplied; complete bibliographic details were not provided.
- Park, J. S., O’Brien, J. C., Cai, C. J., Morris, M. R., Liang, P., & Bernstein, M. S. (2023). *Generative Agents: Interactive Simulacra of Human Behavior*. Full-text source supplied.