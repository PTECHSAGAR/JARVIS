# JARVIS Architecture Document

## Overview
JARVIS (Just A Rather Very Intelligent System) is structured as a modular assistant containing modules for AI planning/conversation, voice processing, browser automation, third-party integrations, database operations, and a vector-based knowledge base.

## Block Diagram / Modules
1. **Core**: Handles initialization, configuration, logging, and startup procedures.
2. **AI**: Manages communication with local LLMs (Ollama), plans agent actions, builds prompts, and manages dialogue state.
3. **Voice**: Accesses physical inputs/outputs for wake-word activation, microphone captures, STT (Speech-to-Text), and TTS (Text-to-Speech).
4. **Browser**: Executes web automation tasks like crawler management, screenshotting, page retrieval, and session storage.
5. **Integrations**: Bridges JARVIS with services like VTOP, BookMyShow, and MakeMyTrip.
6. **Knowledge**: Processes incoming information, computes embeddings, and stores document metadata.
7. **Database**: Stores relational logs, configuration data, and transaction histories.
