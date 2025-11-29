#!/bin/bash
# Start OctoPrint with macOS sleep prevention
# Usage: ./start-octoprint.sh

# Activate the virtual environment
source ~/octoprint-env/bin/activate

echo "🚀 Starting OctoPrint..."
echo "☕️ Caffeinate is active: System sleep is disabled while OctoPrint runs."
echo "🌐 Open http://localhost:5001 in your browser."
echo "❌ Press Ctrl+C to stop."

# Run OctoPrint wrapped in caffeinate
# -i: Prevent idle sleep
# --port 5001: Avoid conflict with macOS AirPlay Receiver (port 5000)
caffeinate -i octoprint serve --port 5001
