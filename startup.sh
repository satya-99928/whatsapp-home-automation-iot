#!/bin/bash
sleep 25

# Start the Flask bot
python3 /home/pi/whatsapp_bot.py &

# Start ngrok in the background
/home/pi/ngrok http 5000 > /dev/null &
sleep 10

# Get ngrok public URL
NGROK_URL=$(curl -s http://localhost:4040/api/tunnels | grep -o 'https://[0-9a-zA-Z.-]*.ngrok-free.app')

# Twilio credentials
ACCOUNT_SID="YOUR_TWILIO_SID"
AUTH_TOKEN="YOUR_TWILIO_AUTH_TOKEN"

# Update Twilio webhook
curl -X POST https://api.twilio.com/2010-04-01/Accounts/$ACCOUNT_SID/IncomingPhoneNumbers.json \
--data-urlencode "SmsUrl=$NGROK_URL/bot" \
-u $ACCOUNT_SID:$AUTH_TOKEN
