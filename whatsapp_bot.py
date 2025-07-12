from flask import Flask, request
from gpiozero import LED, OutputDevice
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

# GPIO Pin Assignments
led = LED(17)          # LED (Light)
in1 = OutputDevice(22) # Motor IN1
in2 = OutputDevice(23) # Motor IN2
ena = OutputDevice(18) # ENA (Enable A - motor power)

@app.route("/bot", methods=["POST"])
def bot():
    msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()

    if 'light on' in msg:
        led.on()
        resp.message("✅ Light is ON")
    elif 'light off' in msg:
        led.off()
        resp.message("✅ Light is OFF")
    elif 'fan on' in msg:
        ena.on()
        in1.on()
        in2.off()
        resp.message("✅ Fan is ON")
    elif 'fan off' in msg:
        ena.off()
        in1.off()
        in2.off()
        resp.message("✅ Fan is OFF")
    else:
        resp.message("Send:\nlight on / light off\nfan on / fan off")

    print(f"Received message: {msg}")
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
