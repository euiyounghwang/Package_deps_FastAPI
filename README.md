# Package_deps_FastAPI
<i> Package_deps_FastAPI

FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.8+ based on standard Python.
This is a repository that provides to deliver the records to the Prometheus-Export application.



### Using Uv: Create the virtual environment in the same directory as the project and install the dependencies:
- uv installation : https://www.0x00.kr/development/python/python-uv-simple-usage-and-example
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

