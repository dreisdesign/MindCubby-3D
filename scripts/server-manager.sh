#!/bin/bash

# MindCubby OctoPrint Server Manager
# Checks if OctoPrint is running, starts it if not, detaches it
# Usage: ./scripts/server-manager.sh

SCREEN_SESSION="octoprint"
OCTOPRINT_SCRIPT="$HOME/scripts/start-octoprint.sh"

echo "🔍 Checking if OctoPrint is running..."

# Check if screen session exists
if screen -list | grep -q "$SCREEN_SESSION"; then
    echo "✅ OctoPrint is already running in screen session '$SCREEN_SESSION'"
    echo "📋 To view: screen -r $SCREEN_SESSION"
    echo "📋 To detach: Press Ctrl+A then D"
    exit 0
fi

# If not running, start it in a detached screen session
echo "🚀 Starting OctoPrint in detached screen session..."
screen -d -m -S "$SCREEN_SESSION" "$OCTOPRINT_SCRIPT"

# Give it a moment to start
sleep 2

# Check if it started successfully
if screen -list | grep -q "$SCREEN_SESSION"; then
    echo "✅ OctoPrint started successfully!"
    echo "🌐 Access at: http://192.168.86.33:5001"
    echo "📋 To view logs: screen -r $SCREEN_SESSION"
    echo "📋 To detach: Press Ctrl+A then D"
else
    echo "❌ Failed to start OctoPrint"
    exit 1
fi
