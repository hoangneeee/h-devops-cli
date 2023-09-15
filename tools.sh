#!/bin/bash
set -e

show_usage() {
  echo "Usage: $0 <autopep8>"
}

if [ $# -ne 1 ]; then
  show_usage
  exit 1
fi

if [ "$1" == "autopep8" ]; then
  autopep8 --in-place --recursive h_devops
else
  show_usage
  exit 1
fi
