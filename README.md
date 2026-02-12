# AI-Powered-DDR
Project Overview

This project is an AI-powered DDR (Detailed Diagnostic Report) Generator designed to convert unstructured property inspection data into a clear, structured, and client-ready diagnostic report.

The system processes:

Inspection Reports (visual observations)

Thermal Reports (temperature and moisture indicators)

and produces a reliable DDR including issue summary, root cause analysis, severity assessment, and recommended actions.

The focus of this project is accuracy, reliability, and real-world system design, not just raw AI output.

Problem Statement

Property inspection data is often:

Unstructured

Inconsistent

Hard to interpret for clients

Manual report generation is:

Time-consuming

Error-prone

Difficult to scale

This project automates the DDR creation process while avoiding hallucination and clearly flagging missing data.

 Solution Approach

The solution is implemented in two layers:

1️ Rule-Based DDR Generator (Reliable Baseline)

Parses inspection and thermal text reports

Extracts area-wise observations

Merges findings logically

Flags missing or unclear information explicitly

Generates a structured DDR output

This ensures deterministic and trustworthy results.

2️ AI-Powered DDR Generator (LangChain)

Uses LangChain + OpenAI

Applies a strict prompt to:

Prevent hallucination

Maintain structured output

Produce client-friendly language

Designed for scalable, production-grade usage

 System Workflow

Read inspection and thermal report text files

Extract area-wise observations

Merge findings by location

Identify probable root causes

Assess severity

Generate recommendations

Output a structured DDR report
