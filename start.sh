#!/bin/bash

# Port to check
PORT=5173

echo "Stopping any existing processes on port $PORT..."

# Find the PID of the process using the port and kill it
PID=$(lsof -t -i:$PORT)

if [ -z "$PID" ]; then
    echo "No process found on port $PORT."
else
    echo "Killing process $PID..."
    kill -9 $PID
    if [ $? -eq 0 ]; then
        echo "Successfully killed process $PID."
    else
        echo "Failed to kill process $PID."
    fi
fi

# Also kill any other vite processes just in case
pkill -f vite

echo "Starting the application..."
npm run dev
