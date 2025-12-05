# 🐙 GitHub Activity CLI (`gitact`)

**Simple Python Command-Line Interface (CLI) tool to fetch and display a user's 10 most recent public GitHub activities.**

![GitHub Activity Demo](img/gitact-demo.gif)

This project demonstrates professional API interaction using Python's `requests` library, secure authentication via environment variables, and robust data parsing.

[![Roadmap.sh Project](https://img.shields.io/badge/Project-Roadmap.sh-blue.svg)](https://roadmap.sh/projects/github-user-activity)

## Table of Contents

1.  [Prerequisites](#1-prerequisites)
2.  [Setup & Installation](#2-setup--installation)
3.  [Authentication (Setting Your GitHub PAT)](#3-authentication-setting-your-github-pat)
4.  [Usage](#4-usage)
5.  [Project Structure](#5-project-structure)

-----

## 1\. Prerequisites

You need **Python 3.7+** installed on your system.

### `requirements.txt`

The project relies on the popular `requests` library for handling HTTP API calls.

```text
# requirements.txt
requests>=2.32.5
```

-----

## 2\. Setup & Installation

That's an important detail\! Since you're using Windows, knowing the **PowerShell** command for virtual environment activation is essential for a complete set of instructions.

Here is the revised setup table, including the instructions for **Windows PowerShell**.

## 🛠️ Revised Setup Instructions (Including PowerShell)

| Operating System | Command to Create `venv` | Command to **Activate** `venv` |
| :--- | :--- | :--- |
| **Linux/macOS** | `python3 -m venv venv` | `source venv/bin/activate` |
| **Windows (CMD)** | `py -m venv venv` | `venv\Scripts\activate` |
| **Windows (PowerShell)** | `py -m venv venv` | `.\venv\Scripts\Activate.ps1`|

### Combined Activation Commands

To make the process easier for users, you can combine the create and activate steps in the `README.md`:

| Operating System | Combined Command |
| :--- | :--- |
| **Linux/macOS** | `python3 -m venv venv && source venv/bin/activate` |
| **Windows (CMD)** | `py -m venv venv` & `venv\Scripts\activate` |
| **Windows (PowerShell)** | `py -m venv venv` ;`.\venv\Scripts\Activate.ps1` |

-----

## 2\. Setup & Installation (Updated README Section)

Follow these steps to set up the project and install the CLI tool in an isolated virtual environment.

#### Step 1: Clone the Repository

Open your terminal or command prompt and clone the project:

```bash
git clone https://github.com/YourUsername/github-activity-cli.git
cd github-activity-cli
```

#### Step 2: Create and Activate a Virtual Environment

It is highly recommended to use a virtual environment to manage dependencies. Run the appropriate command for your system:

| Operating System | Command |
| :--- | :--- |
| **Linux/macOS** | `python3 -m venv venv && source venv/bin/activate` |
| **Windows (CMD)** | `py -m venv venv` & `venv\Scripts\activate` |
| **Windows (PowerShell)** | `py -m venv venv` ;`.\venv\Scripts\Activate.ps1` |


#### Step 3: Install Dependencies and the CLI Tool

Install the required library (`requests`) and install the project itself in editable mode (`-e`) using `pip`:

```bash
pip install -r requirements.txt
pip install -e .
```

The CLI tool, named **`gitact`**, is now available in your terminal.

#### Step 4: Verify the Installation ✅

Test that the `gitact` command is correctly installed and accessible by asking it for its help message. This confirms your Python environment is linking to the new command successfully.

```bash
gitact --help
```

##### Expected Output

The output will show the description you defined in `cli.py` and confirm the required `username` argument:

```text
usage: gitact [-h] username

Simple CLI tool to display recent github activities

positional arguments:
  username    Valid GitHub Username

options:
  -h, --help  show this help message and exit
```

If you see this help message, your tool is ready\! You can now proceed to Authentication

-----

## 3\. Authentication (Setting Your GitHub PAT)

Accessing public activity feeds often requires authentication to achieve a higher **Rate Limit** (5,000 requests/hour instead of 60/hour). This project uses a **GitHub Personal Access Token (PAT)** for secure authentication.

**Security is paramount:** We use **Environment Variables** to keep your secret token separate from the code.

#### Step 1: Generate Your Token

1.  Go to **GitHub Settings** $\rightarrow$ **Developer Settings** $\rightarrow$ **Personal Access Tokens**.
2.  Click **"Generate new token (classic) or Fine Grained"**.
3.  Give it a name (e.g., `gitact_cli`).
4.  No scopes/permissions are needed for public activities, but selecting the **`public_repo`** scope is harmless.
5.  Copy the generated token\!

#### Step 2: Set the Environment Variable

You need to set the environment variable **`GITHUB_PAT`** in your current terminal session. Replace `YOUR_ACTUAL_TOKEN` with the token you copied in Step 1.

| Operating System | Command to Set `GITHUB_PAT` |
| :--- | :--- |
| **Linux/macOS (Bash/Zsh)** | `export GITHUB_PAT="YOUR_ACTUAL_TOKEN"` |
| **Windows (CMD)** | `set GITHUB_PAT=YOUR_ACTUAL_TOKEN` |
| **Windows (PowerShell)** | `$env:GITHUB_PAT="YOUR_ACTUAL_TOKEN"` |

That's a crucial point! Confirming the environment variable is set correctly is the essential final step before running the Python code.


#### Step 3: 🔑 Verifying/Testing the Environment Variable

After running the command to set the variable, use the corresponding command below to ensure your operating system has successfully stored the `GITHUB_PAT` value. If successful, the command should print your actual token to the terminal.

| Operating System | Command to **Set** `GITHUB_PAT` | Command to **Verify** (Test) |
| :--- | :--- | :--- |
| **Linux/macOS (Bash/Zsh)** | `export GITHUB_PAT="YOUR_ACTUAL_TOKEN"` | `echo $GITHUB_PAT` |
| **Windows (CMD)** | `set GITHUB_PAT=YOUR_ACTUAL_TOKEN` | `echo %GITHUB_PAT%` |
| **Windows (PowerShell)** | `$env:GITHUB_PAT="YOUR_ACTUAL_TOKEN"` | `echo $env:GITHUB_PAT` |

If the verification command returns your token, your Python script will be able to access it securely using `os.environ.get("GITHUB_PAT")`.

**Note:** This variable is only active in the terminal session where you run this command. You must run this **before** using the `gitact` command.

-----

## 4\. Usage

The CLI tool is simple to use. Just provide a valid GitHub username as a positional argument.

#### Syntax

```bash
gitact [username]
```

#### Example

To view the recent activity for the iconic GitHub user `octocat`:

```bash
gitact octocat
```

#### Example Output

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