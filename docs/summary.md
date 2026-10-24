---
title: JuryBee — Multi-Agent Contract Analyzer
tagline: My first hackathon project, a multi-agent assistant that reads a contract PDF and flags risky clauses using RAG.
area: ml
stack: [Google ADK, Gemini 2.0 Flash, Vertex AI RAG Engine, PyMuPDF]
note: My first hackathon
---

JuryBee was my first hackathon project, built for a generative AI hackathon. Honestly, it's a simple project and I'd build it very differently today. But it's the one that opened my eyes to how AI agents and retrieval-augmented generation (RAG) actually work.

The problem we picked: a lot of Filipinos and small businesses sign contracts without any legal help. JuryBee reads a contract and points out the clauses that matter and the risks to watch for. It's a first read, not legal advice.

My team and I started by mapping the system as a diagram. A root agent routes the user's message, a contract analyst agent pulls the text out of the PDF, and short- and long-contract agents do the analysis, with legal adviser and lawyer recommendation agents planned on top. Then we built it on Google's Agent Development Kit (ADK) with Gemini 2.0 Flash. You send a Google Drive link, the analyst extracts the text with PyMuPDF, and the short-contract agent checks each clause against a RAG corpus on Vertex AI built from the Contract Understanding Atticus Dataset (CUAD).

Only the short-contract path got finished. The rest stayed on the diagram. What I took away was bigger than the code: how to split a problem across agents, how chunking and embeddings feed retrieval, and why grounding a model in real documents matters. I plan to rebuild it with all of that.

[Watch our demo video](https://github.com/2nieGarcia/JuryBee/blob/main/docs/demo.mp4)
