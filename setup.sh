#!/usr/bin/env bash
set -euo pipefail
USER=${1:-}
HOST=${2:-}

echo "Deploying to ${USER}@${HOST}"

ansible-playbook \
  --inventory "$HOST", \
  --user "$USER" \
  --become \
  --become-method sudo \
  setup-playbook.yaml