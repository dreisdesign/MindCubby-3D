#!/bin/bash
# Quick commit helper for MINDCUBBY-3D repo
# Usage: gcode-commit "your commit message"
#
# Example:
#   gcode-commit "add: new model"
#
# What it does:
#   1. Stages all changes (git add .)
#   2. Runs the pre-commit hook manually to generate specs
#   3. Commits everything with your message
#   4. Pushes to remote

set -e

if [ -z "$1" ]; then
    echo "Usage: gcode-commit \"your commit message\""
    echo ""
    echo "Examples:"
    echo "  gcode-commit \"add: chip clip v2\""
    echo "  gcode-commit \"update: apple pencil specs\""
    exit 1
fi

COMMIT_MSG="$1"
REPO_ROOT=$(git rev-parse --show-toplevel 2>/dev/null)

if [ -z "$REPO_ROOT" ]; then
    echo "Error: Not in a git repository"
    exit 1
fi

echo "📦 Staging changes..."
git add .

echo "🔍 Running spec generation..."
bash "$REPO_ROOT/.githooks/pre-commit"

echo ""
echo "💾 Committing: $COMMIT_MSG"
git commit -m "$COMMIT_MSG"

echo ""
echo "🚀 Pushing to remote..."
git push

echo ""
echo "✅ Done!"
