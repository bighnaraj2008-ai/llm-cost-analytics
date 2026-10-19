# LLM Cost Optimization Strategy Guide

Strategies for reducing token consumption and cloud inference expenditures:

## 1. Prompt Caching
Take advantage of provider prompt caching for static instructions, system prompts, and multi-turn chat history. Cached tokens typically receive an 80-90% discount.

## 2. Model Routing & Tier Classification
- **Tier 1 (Economy)**: Use `gemini-1.5-flash` or `gpt-3.5-turbo` for classification, entity extraction, and routing.
- **Tier 2 (Standard)**: Use `claude-3-sonnet` or `gemini-1.5-pro` for summarization and standard generation.
- **Tier 3 (Premium)**: Reserve `gpt-4` or `claude-3-opus` strictly for complex reasoning, code generation, and mathematical validation.

## 3. Automated Cost Spike Alerting
Configure `cost_spike_detector.sql` with a threshold trigger to catch runaway evaluation loops or leaked API keys early.
