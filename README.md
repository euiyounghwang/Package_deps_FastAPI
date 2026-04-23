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

- uv help
```bash
사용법: uv [옵션] <명령어>

명령어:
  run      명령어나 스크립트 실행
  init     새 프로젝트 생성
  add      프로젝트에 의존성 추가
  remove   프로젝트에서 의존성 제거
  sync     프로젝트의 환경 업데이트
  lock     프로젝트의 락파일 업데이트
  export   프로젝트의 락파일을 다른 형식으로 내보내기
  tree     프로젝트의 의존성 트리 표시
  tool     Python 패키지가 제공하는 명령어 실행 및 설치
  python   Python 버전 및 설치 관리
  pip      pip 호환 인터페이스로 Python 패키지 관리
  venv     가상 환경 생성
  build    Python 패키지를 소스 배포판 및 휠로 빌드
  publish  배포판을 인덱스에 업로드
  cache    uv의 캐시 관리
  self     uv 실행 파일 관리
  version  uv 버전 표시
  help     명령어에 대한 문서 표시
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

# -- sample --
$ uv add fastapi
$ uv add uvicorn --extra standard
$ uv add ruff --dev
$ uv add pytest --group test

[dependency-groups]
dev = [
    "ruff>=0.11.4",
]
test = [
    "pytest>=8.3.5",
]
# -- --

```

- Installation libraries
```bash

uv export -o ./dev_uv_requirements.txt

uv pip install -r ./dev_requirements.txt

#export UV_NATIVE_TLS=true
#uv python install 3.11

# uv is significantly faster than standard venv, often over 6x faster.
# Create a .venv virtual environment with default Python
uv venv

# Create a virtual environment with a specific Python version
uv venv --python 3.11

# Create a virtual environment with a custom name
uv venv <env_name> --python 3.11

#uv venv test --python 3.11
#cpython-3.11.15-windows-x86_64-none (download) ------------------------------ 12.67 MiB/24.41 MiB   

pip freeze > ./dev_requirements.txt

python -m venv test
source test/Script/activate
pip install uv
time uv add -r dev_uv_requirements.txt --system-certs --active   # 의존성 설치

uv sync # pyproject.toml 과 uv.lock 파일을 기준으로 가상환경 재생성 및 동기화
uv tree

```

### Run via uv
- uv run --python 3.10 --with fastapi,pytest main.py (uv run 명령어를 사용하여 설치되지 않은 파이썬 버전을 자동으로 설치하고, 필요한 패키지를 포함시켜 스크립트를 실행할 수 있습니다.)
