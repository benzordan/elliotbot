import telebot

# Create a bot object
bot = telebot.TeleBot("6259661929:AAG28vS_-NGCkWydsKuDdKG7J1NrNzc4Drg")

# Define a function to handle commands
def handle_command(message):
    # Check if the command is "start"
    if message.text == "/start":
        # Send a welcome message
        bot.send_message(message.chat.id, "Welcome to my bot! I can do many things, such as provide information, automate tasks, or simply have fun. What would you like me to do?")

    # Check if the command is "help"
    elif message.text == "/help":
        # Send a help message
        bot.send_message(message.chat.id, """Here are some of the things I can do:
        - Provide information
        - Automate tasks
        - Simply have fun

        To get started, just type a command and I will do my best to fulfill your request.""")

    # Check if the command is "info"
    elif message.text == "/info":
        # Send an information message
        bot.send_message(message.chat.id, "I am a Telegram bot that can be used to automate tasks, provide information, or simply have fun. I am still under development, but I am learning new things every day.")

    # Otherwise, send a message saying that the command is not recognized
    else:
        bot.send_message(message.chat.id, "I am sorry, I do not recognize that command. Please try again.")

# Start listening for messages
bot.polling()
