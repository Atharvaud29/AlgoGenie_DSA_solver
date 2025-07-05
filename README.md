# DSA Solving Multi Agent System using Microsoft AutoGen.

Creating an tool that uses a multi-agentv system with AutoGen to generate and run Python code for solving user-specified (DSA) problems, like binary search, fibonacci sequence, etc. 

# Why Use AutoGen?

   ![Screenshot 2025-07-05 113318](https://github.com/user-attachments/assets/5d7e5a4d-0842-445c-88a7-04d283b70a13)


**AutoGen Core :**

- AutoGen core offers an easy way to quickly build event-driven, distributed, scalable, resilient AI agent systems. Agents are developed by using the Actor model.

**AgentChat :**

- AgentChat is a high-level API for building multi-agent applications. It is built on top of the autogen-core package. For advanced users, autogen-core’s event-driven programming model provides more flexibility and control over the underlying components.
- AgentChat provides intuitive defaults, such as Agents with preset behaviors and Teams with predefined multi-agent design patterns.

**Teams :**

- A team is a group of agents that work together to achieve a common goal.
- AgentChat supports several team presets :
  - RoundRobinGroupChat : A team that runs a group chat with participants taking turns in a round-robin fashion (covered on this page).
  - SelectorGroupChat : A team that selects the next speaker using a ChatCompletion model after each message.
  - MagenticOneGroupChat : A generalist multi-agent system for solving open-ended web and file-based tasks across a variety of domains.
  - Swarm : A team that uses HandoffMessage to signal transitions between agents.

# Project Workflow :

![image](https://github.com/user-attachments/assets/7e7ae954-6994-4693-ab5e-1666be16398f)


**Key Features :**

- Asynchronous messaging
- Modular and extensible
- Observability and debugging
- Scalable and distributed
- Built-in and community extensions
- Cross-language support
- Full type support

