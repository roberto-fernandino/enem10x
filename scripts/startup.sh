#!/bin/bash
echo "🟡 starting NGROK"
ngrok http app:8000 &
sleep 10

public_url=$(curl -s http://localhost:4040/api/tunnels | jq -r '.tunnels[0].public_url')
echo "✅ Public NGROK url initialized: $public_url"
echo "🟡 Copy and paste in your browser. 🟡"

wait %1