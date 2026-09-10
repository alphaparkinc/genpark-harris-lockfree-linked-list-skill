# genpark-harris-lockfree-linked-list-skill

[![CI](https://github.com/alphaparkinc/genpark-harris-lockfree-linked-list-skill/actions/workflows/ci.yml/badge.svg)](https://github.com/alphaparkinc/genpark-harris-lockfree-linked-list-skill/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)

> Harris lock-free ordered linked list using logical deletion marking and single-word compare-and-swap (CAS) physical unlinking.

## Architecture

```mermaid
flowchart TD
    Client[AI Agent / Producer Threads] -->|Atomic Op / CAS| Engine[genpark-harris-lockfree-linked-list-skill]
    Engine --> LockFreeCore[Non-Blocking Pointer & Ring Buffer Core]
    LockFreeCore --> Consumer[Consumer / Thief Threads]
```

## Features
- Pure standard library Python implementation with strictly zero pip dependencies.
- True non-blocking algorithms preventing priority inversion, deadlocks, and lock contention.
- Native Model Context Protocol (MCP) server support for high-throughput AI agent pipelines.

## Installation

```bash
git clone https://github.com/alphaparkinc/genpark-harris-lockfree-linked-list-skill.git
cd genpark-harris-lockfree-linked-list-skill
```

## Quickstart

```bash
python example_usage.py
```
