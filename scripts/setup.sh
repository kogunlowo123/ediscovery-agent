#!/bin/bash
set -euo pipefail
echo "Setting up eDiscovery Agent..."
pip install -e ".[dev]"
echo "Setup complete!"
