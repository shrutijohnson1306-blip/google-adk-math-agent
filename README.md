#  Math Agent (Google ADK + Gemini + Function Tools)

##  Project Overview

This project implements a tool-based AI agent using Google's Agent Development Kit (ADK).

The agent functions as a calculator by:

- Using Gemini as the LLM
- Registering arithmetic operations as callable tools
- Executing tool calls when required
- Returning structured mathematical results

This demonstrates LLM tool-calling architecture.

---

##  Architecture

User Input  
   ↓  
Gemini Model (via ADK Agent)  
   ↓  
Tool Selection (FunctionTool)  
   ↓  
Execution of Arithmetic Function  
   ↓  
Final Response  

---

##  Tech Stack

- Python
- Google ADK (Agent Development Kit)
- Gemini 2.5 Flash
- FunctionTool (Tool Calling)
- Environment-based API key configuration

---

