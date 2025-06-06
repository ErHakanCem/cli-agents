# My CLI Agents Project

This project contains two custom command-line agents:
- `researcher`: A tool to perform web searches from the terminal.
- `shelly`: An AI-powered assistant to generate and execute shell commands using a local LLM.

---

## How to Set Up and Run This Project

Follow these steps to get the agents working on any machine.

### 1. Initial Setup

- **Clone or copy this folder** to your computer.
- **Open a terminal** in the project directory (`cli-agents`).

### 2. Create and Activate Virtual Environment

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate

# For Windows
python -m venv venv
.\venv\Scripts\activate

### 3. Install All Dependencies

This single command reads the `pyproject.toml` file and installs everything needed, including making the `researcher` and `shelly` commands available system-wide (within the virtual environment).

pip install -e .

### 4. One-Time Setup for `shelly` (Local LLM)

The `shelly` agent requires a local LLM managed by Ollama.

- **Install Ollama** from [ollama.com](https://ollama.com).
- **Download the model:** Run this command in your terminal to download and install the AI model `shelly` will use.
  ```bash
  ollama run codellama:7b-instruct
