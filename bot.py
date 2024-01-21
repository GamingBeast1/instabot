import instabot
import time

# Initialize the Instabot
bot = instabot.Bot()
bot.login(username="xinac55472@wuzak.com", password="#ekampreet1")

# Define a function to listen for messages and reply
def auto_reply_messages():
    while True:
        new_message = bot.get_last_direct_message()
        if new_message and new_message.lower() == "hello":
            bot.send_message("hi bro")
        time.sleep(2)  # Polling interval to avoid excessive API requests

# Call the auto_reply_messages function to start listening for messages
auto_reply_messages()
