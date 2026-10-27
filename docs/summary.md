---
title: JuryBee — Multi-Agent Contract Analyzer
tagline: A multi-agent legal assistant that reads a contract PDF and flags risky clauses, grounded in real contracts with RAG.
area: ml
stack: [Google ADK, Gemini 2.0 Flash, Vertex AI RAG Engine, PyMuPDF]
note: Gen AI Hackathon semi-finalist; 3 agents read a contract PDF and check its clauses against the CUAD legal dataset
---

A lot of Filipinos and small businesses sign contracts without any legal help. JuryBee gives them a first read, not legal advice: send it a contract and it pulls out the clauses that matter and points out the risks. It made the semi-finals of the Gen AI Hackathon.

I led our team, Joybread Studios, and wrote the agent code on Google's Agent Development Kit (ADK) with Gemini 2.0 Flash. A root agent looks for a Google Drive link in the message and hands it to a contract analyst agent, which downloads the PDF and extracts the text with PyMuPDF. The analyst passes it to a short-contract agent that summarizes the terms, walks through the critical clauses (parties, term, payment, termination, liability, governing law) and flags the risks.

The part I'm proudest of is the retrieval-augmented generation (RAG). A setup script loads the 510 contracts of the Contract Understanding Atticus Dataset (CUAD) into a Vertex AI RAG corpus, and the short-contract agent queries it clause by clause, so its advice comes from real contract language instead of only the model's memory. In the demo it caught that a sample contract had no governing law clause and recommended adding one.

Honestly, only the short-contract path got finished. Long-contract chunking and the legal adviser and lawyer recommendation agents stayed on the diagram. It was my first hackathon, and it's where I learned how to split a problem across agents and why grounding a model in real documents matters.

[Watch our demo video](https://github.com/2nieGarcia/JuryBee/blob/main/docs/demo.mp4)
