from twilio.rest import Client
import keys

client = Client(keys.account_sid, keys.auth_token)

print("FROM:", keys.twilio_number)
print("TO  :", keys.my_phone_number)

message = client.messages.create(
    body="Test SMS from Python",
    from_=keys.twilio_number,
    to=keys.my_phone_number
)

print("Sent ✅")
print("SID:", message.sid)
