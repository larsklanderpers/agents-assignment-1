# Main Approaches to Building AI Agents That Can Reason and Act

## Executive Summary

AI agents can connect reasoning to action in several ways. Traditional designs include **reactive agents**, which respond to current conditions, and **deliberative agents**, which represent goals or intentions and plan before acting. Other designs combine perception, memory, planning, and action in repeated cycles. Contemporary LLM-based agents add methods that interleave language-based reasoning with actions, call external tools, generate plans for later checking, and use feedback to guide future attempts.

Across the sources, a consistent design principle is to connect reasoning to observations and executable actions. External tools can address some limits of language-only prediction, while planners or people can check plans that an LLM proposes. Memory and feedback can help shape later decisions, but they do not guarantee coherent behavior over long periods. The evidence does not establish one best architecture. Direct comparisons remain limited, and several of the supplied source excerpts are incomplete.

## Introduction

An AI agent is commonly distinguished from a system that only generates a response by its relation to an environment. A traditional account describes agents as perceiving environments that may include the physical world, a user interface, other agents, or the internet (Wooldridge, 1995). A survey of LLM-based agents uses terms such as beliefs and desires, although the supplied excerpt does not show how the survey defines or measures these concepts (Xi et al., 2023).

This review addresses the question: **What are the main approaches to building AI agents that can reason and act?** It compares reactive and deliberative architectures with newer LLM-based methods for reasoning-action cycles, tool use, planning, memory, and feedback. It also considers what the supplied evidence can and cannot show about their relative strengths.

## Methodology

The review draws on the supplied search strategy, evidence excerpts, and synthesis. Searches covered agent definitions; reactive, deliberative, and hybrid architectures; LLM reasoning and action; tool use; planning and plan checking; memory and feedback; and reported limitations. The strategy also called for critical and comparative evidence, including searches for failures as well as benefits.

The evidence set includes foundational agent theory, an LLM-agent survey, and papers on ReAct, Toolformer, LLM planning, Reflexion, and generative agents. This is a thematic review of the supplied material, not a systematic review of all relevant research. The retrieved passages are often short; several are explicitly truncated or contain extraction artifacts. Therefore, this review does not reconstruct missing text or infer unreported methods, results, or bibliographic details.

## Findings

### 1. Agency centers on interaction with an environment

The traditional agent account foregrounds perception of an environment (Wooldridge, 1995). This suggests that agency involves more than producing text: the system must relate its behavior to observations or conditions outside its response. The supplied excerpt is incomplete, however, and does not provide a full definition.

The LLM-agent survey excerpt uses intentional terms such as beliefs and desires (Xi et al., 2023). This differs in emphasis from the traditional account: one centers the agent’s relation to an environment, while the other invokes internal attitudes. The available evidence does not show how these concepts are operationalized or whether they are necessary conditions for agency.

Taken together, the sources support a practical distinction between response generation and environment-linked action. They do not settle whether a tool call alone is enough to qualify a system as an agent. A more demanding account would ask whether the system selects actions in relation to observations and can use action outcomes to guide later behavior.

### 2. Reactive and deliberative architectures offer different ways to select actions

Reactive agents use local patterns in their current surroundings to produce relatively hardwired responses to stimuli (Wooldridge, 1995). This approach links a present condition to an action without necessarily constructing an explicit long-range plan. It provides a direct route from observation to response.

Deliberative architectures instead represent internal states such as beliefs, desires, or intentions. Wooldridge’s discussion gives the Intelligent Resource-bounded Machine Architecture (IRMA) as an example of an architecture based on such attitudes (Wooldridge, 1995). These representations can inform decisions about what actions to take, rather than relying only on an immediate stimulus-response mapping.

The sources also point to designs that combine memory and planning with ongoing perception. A discussion of earlier symbolic systems describes short- and long-term memory, symbolic structures, and perceive–plan–act cycles (Park et al., 2023). This suggests that reactive and deliberative elements can be part of a broader agent architecture rather than mutually exclusive choices.

The supplied material supports a conceptual contrast between immediate responsiveness and explicit deliberation. It does not provide a direct experimental comparison of their speed, cost, or performance in uncertain and changing environments. Any claim that one approach is generally superior would therefore go beyond the evidence.

### 3. LLM agents connect reasoning to action through interaction and tools

A central LLM-agent approach is to connect language-based reasoning with actions and observations. ReAct describes a limitation of static chain-of-thought reasoning: reasoning that remains internal to the model is not grounded in external interaction (Yao et al., 2023). ReAct instead combines reasoning and acting. The paper reports consistent advantages over controlled action-only baselines and identifies interpretability as a potential benefit. The supplied excerpt does not specify the tasks or quantify the reported gains.

Tool use provides another way to extend a language model’s capabilities. Toolformer describes a model that can decide when to call external APIs (Schick et al., 2023). The paper motivates tool use by noting that language models can struggle with tasks such as arithmetic and factual lookup, despite their broader language abilities. External systems can therefore provide functions or information that the language model may not handle reliably on its own.

These approaches share a basic idea: connect model outputs to actions or external resources instead of relying only on text generation. They differ in emphasis. ReAct focuses on an interleaved reasoning-and-action pattern, while Toolformer focuses on selecting API calls. The supplied excerpts do not provide enough detail for a full comparison of their execution loops, reliability, or performance across tasks. They also do not establish that tool use by itself creates robust, sustained agency.

### 4. Planning benefits from external checking and oversight

LLMs can generate candidate plans, but the supplied planning evidence cautions against treating these plans as automatically reliable. *On the Planning Abilities of Large Language Models – A Critical Investigation* reports that plans generated by LLMs can be corrected by sound planners such as LPG to guarantee soundness (Valmeekam et al., 2023). The excerpt also refers to human-in-the-loop planning, but ends before the comparison is complete.

This evidence supports a hybrid design: use an LLM to propose a plan, then use a planner or a human to check or correct it. The approach separates the LLM’s role in generating candidates from the validator’s role in checking plan properties. It does not show that a sound plan will always succeed in a real environment, or how often correction is needed.

The evidence also leaves open how agents should monitor execution and respond when conditions change. The supplied passages provide limited detail on replanning, progress monitoring, or recovery from failed actions. These are important steps between producing a plan and completing a task.

### 5. Memory and feedback can guide later behavior, but do not ensure long-term coherence

Memory can support decisions beyond the current observation. The account of earlier symbolic systems describes short- and long-term memory within repeated perceive–plan–act cycles (Park et al., 2023). In LLM-based agents, Reflexion uses environmental feedback in a different way: it converts binary or scalar feedback into a verbal summary and adds that summary as context for a later episode (Shinn et al., 2023). In the supplied description, feedback guides future attempts through text rather than through an explicit change to model parameters.

The generative-agents discussion also identifies a limit. It notes that agents may fail to use past experience or make important inferences, and that long-term planning and coherence remain difficult (Park et al., 2023). Memory mechanisms may help preserve relevant information, but their presence does not by itself establish that an agent will remain coherent over long periods.

The sources therefore support memory and feedback as design components, not as guaranteed solutions. The supplied material does not directly compare different memory types, textual reflection, policy learning, or parameter updates. It also offers little evidence about when stored feedback is accurate, useful, or likely to mislead later decisions.

### 6. The evidence supports complementary designs, not a general winner

Across the sources, agent designs connect observations, internal reasoning, plans, actions, memory, and feedback in different combinations. Reactive policies map current conditions to actions; deliberative systems represent goals or intentions; perceive–plan–act cycles can incorporate memory; and LLM-based systems can interleave reasoning and action, call tools, generate plans for checking, or use feedback in later attempts.

The strongest shared finding is that reasoning is more clearly connected to action when the system can interact with an environment, use an execution mechanism, or receive feedback. ReAct links reasoning to actions; Toolformer uses external APIs; the planning study describes checking LLM-generated plans; and Reflexion carries feedback into later attempts (Yao et al., 2023; Schick et al., 2023; Valmeekam et al., 2023; Shinn et al., 2023).

The sources do not provide a direct contradiction in which one architecture clearly outperforms another across shared tasks. Instead, they identify trade-offs and limits: immediate response versus deliberation, flexible plan generation versus the need for checking, and the potential value of memory alongside persistent problems of long-term coherence. The available evidence does not establish a universally best approach.

## Discussion

The reviewed approaches differ in how they balance internal reasoning with interaction. Reactive systems prioritize a direct response to current conditions. Deliberative systems add explicit representations and planning. Hybrid cycles can combine observation, memory, planning, and action. LLM-based systems extend these patterns with natural-language reasoning and the capacity to call external tools or generate candidate plans.

Across the evidence, interaction plays an important role in grounding agent behavior. A language model can produce reasoning or a plan, but those outputs are not the same as successful action. Tool execution, environmental observations, external validation, and feedback can help connect a proposed decision to what happens next. At the same time, the supplied excerpts do not show that these mechanisms eliminate tool errors, planning failures, or inconsistent behavior.

Several limits constrain the conclusions. First, the excerpts are often truncated, so some papers’ task settings, methods, and results are unavailable. Second, the sources do not offer a common evaluation that compares traditional reactive and deliberative agents with LLM-based systems. Third, evidence is limited on reinforcement-learning policy adaptation, safe exploration, efficiency, generalization, and safety. The synthesis can identify design patterns, but it cannot rank them reliably.

### Research gaps

1. **Operational definitions of agency:** Research should distinguish response generation, tool invocation, and sustained action guided by observation and feedback.
2. **Comparable architecture evaluations:** Reactive, deliberative, hybrid, and LLM-based agents should be tested on shared tasks with clear measures of success, efficiency, robustness, and cost.
3. **Plan execution and recovery:** Studies should examine whether plan checking improves task completion and how agents monitor progress, revise plans, and recover from failure.
4. **Memory and learning comparisons:** Research should compare memory and feedback mechanisms, including textual reflection and learned policies, against memoryless or fixed-policy baselines.
5. **Reliability and safety:** Evaluations should assess tool-call errors, misleading feedback, unsafe exploration, and when human or planner oversight is needed.
6. **Long-term behavior:** Studies should test whether memory and feedback improve coherence over extended interactions, rather than only on a later attempt.

## Conclusion

The main approaches to building AI agents that can reason and act are **reactive action selection**, **deliberative planning with explicit goals or intentions**, and **hybrid cycles that combine perception, memory, planning, and action**. LLM-based designs add **interleaved reasoning and acting**, **external tool use**, **plan generation with planner or human checking**, and **feedback stored as guidance for future attempts**.

The supplied sources support a broad design principle: connect reasoning to observations and executable actions, and use feedback or external checking where possible. They do not show that any one design is best across tasks. Stronger comparative evidence is needed, especially on reliability, long-term coherence, plan execution, safety, and the benefits of memory and learning.

## References

- Park, J. S., et al. (2023). *Generative Agents: Interactive Simulacra of Human Behavior*.
- Schick, T., et al. (2023). *Toolformer: Language Models Can Teach Themselves to Use Tools*.
- Shinn, N., et al. (2023). *Reflexion: Language Agents with Verbal Reinforcement Learning*.
- Valmeekam, K., et al. (2023). *On the Planning Abilities of Large Language Models – A Critical Investigation*.
- Wang, et al. (2023). *A Survey on Large Language Model based Autonomous Agents*.
- Wooldridge, M. (1995). *Intelligent Agents: Theory and Practice*.
- Xi, et al. (2023). *The Rise and Potential of Large Language Model Based Agents: A Survey*.
- Yao, S., et al. (2023). *ReAct: Synergizing Reasoning and Acting in Language Models*.