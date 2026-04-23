# Package_deps_FastAPI
<i> Package_deps_FastAPI

FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.8+ based on standard Python.
This is a repository that provides to deliver the records to the Prometheus-Export application.

UV is an extremely fast Python package and project manager, written in Rust. UV manages project dependencies and environments, with support for lockfiles, workspaces, and more.
- A single tool to replace pip, pip-tools, pipx, poetry, pyenv, twine, virtualenv, and more
- 10-100x faster than pip.
- Installs and manages Python versions.


### Using Uv: Create the virtual environment in the same directory as the project and install the dependencies:
- uv installation : https://www.0x00.kr/development/python/python-uv-simple-usage-and-example
```bash
# On macOS and Linux.
curl -LsSf https://astral.sh/uv/install.sh | sh

# On Windows.
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# With pip.
pip install uv

# With pipx.
pipx install uv

# With Homebrew.
brew install uv

# With Pacman.
pacman -S uv
```

- uv venv
```bash
uv venv --python 3.12.0

uv python list
```

- Create virtualenv and install the library via uv
```bash
python -m venv .venv
source .venv/bin/activate

pip install uv

# --
Collecting uv
  Downloading uv-0.11.7-py3-none-win_amd64.whl.metadata (12 kB)
Downloading uv-0.11.7-py3-none-win_amd64.whl (25.4 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 25.4/25.4 MB 6.8 MB/s eta 0:00:00
Installing collected packages: uv
Successfully installed uv-0.11.7
# --
uv init
# --
error: Failed to discover parent workspace; use `uv init --no-workspace` to ignore
  Caused by: No `project` table found in: C:\Users\euiyoung.hwang\pyproject.toml
(.venv)
# --

uv init --no-workspace
# --
Initialized project `package-deps-fastapi`
README.md  main.py  pyproject.toml
# --

uv add fastapi --extra standard --system-certs
# --
Resolved 44 packages in 1.97s
Prepared 42 packages in 4.25s
Installed 42 packages in 1.47s
 + annotated-doc==0.0.4
 + annotated-types==0.7.0
 + anyio==4.13.0
 + certifi==2026.4.22
 + click==8.3.3
 + colorama==0.4.6
 + dnspython==2.8.0
 + email-validator==2.3.0
 + fastapi==0.136.0
 + fastapi-cli==0.0.24
 + fastapi-cloud-cli==0.17.0
 + fastar==0.11.0
 + h11==0.16.0
 + httpcore==1.0.9
# --

# The issue is that 'fcntl' is not available on windows
uv add gunicorn --system-certs

# 그리고 lint를 해주기 위해 ruff 를 추가해주도록 합시다. 개발할 때만 사용하고 배포 시에는 활용하지 않을 것이므로 --dev에 추가해주도록 합시다.
uv add --dev ruff

uv run fastapi dev main.py
# --
  FastAPI   Starting development server 🚀

             Searching for package file structure from directories with __init__.py files

    module   🐍 main.py

      code   Importing the FastAPI app object from the module with the following code:

             from main import app

       app   Using import string: main:app

    server   Server started at http://127.0.0.1:8000
    server   Documentation at http://127.0.0.1:8000/docs

       tip   Running in development mode, for production use: fastapi run
# --
```

