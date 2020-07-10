from os import path
import sys
import getpass

if path.exists('config_file.txt'):
    overwrite_input = input('The configured file found, do you want to overwrite it? (Y/N)')
    overwrite_input = overwrite_input.upper()
    if overwrite_input == 'N':
        sys.exit(0)

ig_bot_username = input("Enter username of bot account  ")
ig_bot_password = getpass.getpass()

ig_main_monitor_username = input("Enter username of main account to monitor the followers ")

discord_webhook_url = input("Enter your discord webhook URL")

if not "discordapp.com" in discord_webhook_url:
    discord_webhook_url = discord_webhook_url.replace("discord.com", "discordapp.com")

f = open("config_file.txt", "w")

f.write(str({'instagram_username': ig_bot_username, 'instagram_password': ig_bot_password,
             'monitor_username': ig_main_monitor_username, 'discord_webhook_url': discord_webhook_url}))

f.close()

print("Configured successfully!")