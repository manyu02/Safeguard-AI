from twilio.rest import Client

# Twilio Credentials (replace with your actual credentials)
TWILIO_ACCOUNT_SID = "AC8992a905528cb9e37a8c838ec1fed400"
TWILIO_AUTH_TOKEN = "55cee5b369023cd5808bb13cfb700048"
TWILIO_PHONE_NUMBER = "+12629753385"

def make_emergency_call():
    emergency_contact = "+919667192218"
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    call = client.calls.create(
        to=emergency_contact,  # test phone number
        from_=TWILIO_PHONE_NUMBER,
        twiml="<Response><Say>This is an emergency call from SafeGuard AI. Please respond immediately.</Say></Response>"
    )

    return "call mikey"

# if __name__ == "__main__":
#     make_emergency_call("+12629753385")  # Replace with a test number
