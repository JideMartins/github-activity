# 🐙 GitHub Activity CLI (`gitact`)

**Simple Python Command-Line Interface (CLI) tool to fetch and display a user's 10 most recent public GitHub activities.**

This project demonstrates professional API interaction using Python's `requests` library, secure authentication via environment variables, and robust data parsing.

[![Roadmap.sh Project](https://img.shields.io/badge/Project-Roadmap.sh-blue.svg)](https://roadmap.sh/projects/github-user-activity)

<!-- ## Table of Contents

1.  [Prerequisites](https://www.google.com/search?q=%231-prerequisites)
2.  [Setup & Installation](https://www.google.com/search?q=%232-setup--installation)
3.  [Authentication (Setting Your GitHub PAT)](https://www.google.com/search?q=%233-authentication-setting-your-github-pat)
4.  [Usage](https://www.google.com/search?q=%234-usage)
5.  [Project Structure](https://www.google.com/search?q=%235-project-structure) -->

-----

## 1\. Prerequisites

You need **Python 3.7+** installed on your system.

### `requirements.txt`

The project relies on the popular `requests` library for handling HTTP API calls.

```text
# requirements.txt
requests>=2.25.1
```

-----

## 2\. Setup & Installation

Follow these steps to set up the project and install the CLI tool in an isolated virtual environment.

### Step 1: Clone the Repository

Open your terminal or command prompt and clone the project:

```bash
git clone https://github.com/YourUsername/github-activity-cli.git
cd github-activity-cli
```

### Step 2: Create and Activate a Virtual Environment

It is highly recommended to use a virtual environment to manage dependencies:

| Operating System | Command |
| :--- | :--- |
| **Linux/macOS** | `python3 -m venv venv && source venv/bin/activate` |
| **Windows (CMD)** | `py -m venv venv` and then `venv\Scripts\activate` |

### Step 3: Install Dependencies and the CLI Tool

Install the required library (`requests`) and install the project itself in editable mode (`-e`) using `pip`:

```bash
pip install -r requirements.txt
pip install -e .
```

The CLI tool, named **`gitact`**, is now available in your terminal.

-----

## 3\. Authentication (Setting Your GitHub PAT)

Accessing public activity feeds often requires authentication to achieve a higher **Rate Limit** (5,000 requests/hour instead of 60/hour). This project uses a **GitHub Personal Access Token (PAT)** for secure authentication.

**Security is paramount:** We use **Environment Variables** to keep your secret token separate from the code.

### Step 1: Generate Your Token

1.  Go to **GitHub Settings** $\rightarrow$ **Developer Settings** $\rightarrow$ **Personal Access Tokens**.
2.  Click **"Generate new token (classic)"**.
3.  Give it a name (e.g., `gitact_cli`).
4.  No scopes/permissions are needed for public activities, but selecting the **`public_repo`** scope is harmless.
5.  Copy the generated token\!

### Step 2: Set the Environment Variable

You need to set the environment variable **`GITHUB_PAT`** in your current terminal session. Replace `YOUR_ACTUAL_TOKEN` with the token you copied in Step 1.

| Operating System | Command to Set `GITHUB_PAT` |
| :--- | :--- |
| **Linux/macOS (Bash/Zsh)** | `export GITHUB_PAT="YOUR_ACTUAL_TOKEN"` |
| **Windows (CMD)** | `set GITHUB_PAT=YOUR_ACTUAL_TOKEN` |
| **Windows (PowerShell)** | `$env:GITHUB_PAT="YOUR_ACTUAL_TOKEN"` |

**Note:** This variable is only active in the terminal session where you run this command. You must run this **before** using the `gitact` command.

-----

## 4\. Usage

The CLI tool is simple to use. Just provide a valid GitHub username as a positional argument.

### Syntax

```bash
gitact [username]
```

### Example

To view the recent activity for the iconic GitHub user `octocat`:

```bash
gitact octocat
```

### Example Output

```
Recent Activity Feed for octocat: 
--------------------------------------------------
- Starred repository octocat/Spoon-Knife
- Created new repository: octocat/test-repo-actions
- Pushed 3 commits to octocat/git-consortium
- Created branch test-branch in octocat/git-consortium
- Created new repository: octocat/test-repo
... (5 more activities)
```

-----

## 5\. Project Structure

The project is structured into three main files:

| File | Purpose |
| :--- | :--- |
| `github_events.py` | Contains the core logic: the `get_events` function that handles API communication, error handling, and formatting of raw JSON into human-readable messages. |
| `cli.py` | Defines the command-line interface using `argparse` and acts as the entry point for the `gitact` command. It takes the `username` argument and passes it to `github_events.get_events`. |
| `setup.py` | Configuration file that tells `pip` how to install the project and create the `gitact` console script. |
| `requirements.txt` | Lists external Python dependencies (`requests`). |