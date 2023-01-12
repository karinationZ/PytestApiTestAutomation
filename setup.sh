#!/bin/bash
echo "Starting Test Environment Setup"
export PIPENV_VENV_IN_PROJECT=1
export PIPENV_VERBOSITY=-1
OS=$(uname -s)
case "$OS" in
Darwin* | Linux)
  echo "Running on $OS"
  python3 -m pip install pipenv
  ;;
CYGWIN* | MINGW32* | MSYS* | MINGW*)
  echo "Running on $OS"
  python -m pip install pipenv
  ;;
*)
  echo "Unsupported $OS OS"
  ;;
esac
pipenv install
pipenv shell
