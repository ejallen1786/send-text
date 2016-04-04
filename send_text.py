# Lesson 3.3: Use Classes
# Mini-Project: Send Text

# It can be important for businesses to automate sending
# text messages. In this mini-project we'll uses classes
# to send a text message using Twilio, a library we'll
# download from the Internet and add to Python.

from twilio import rest

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC3c7d4c513285816362f284b802d29fcf"
auth_token  = "560202377d0c15c44c5cc89ed05fb00b"
client = rest.TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="HI FWEND",
    to="+16163402809",    # Replace with your phone number
    from_="+16162025878") # Replace with your Twilio number
print message.sid