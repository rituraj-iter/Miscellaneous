from igramscraper.instagram import Instagram
from time import sleep
import os
from os import path
import datetime
import Discord_Webhook
import ast
import sys
from pytz import timezone

follower_limit = # by yourself

# bot account username
ig_bot_username = ''

# bot account password
ig_bot_password = ''

# Username of the main account to be monitor
username = ''

MINS_TO_SLEEP = 60

# discord webhook url here.
discord_webhook_url = ''


def unfollowers_check(current, old):
    return list(set(old) - set(current))


def followers_check(current, old):
    return list(set(current) - set(old))


def start():
    while True:
        try:
            print("Test")
            instagram = Instagram()
            instagram.with_credentials(ig_bot_username, ig_bot_password)
            instagram.login(force=False, two_step_verificator=True)
            sleep(2)

            account = instagram.get_account(username)
            sleep(1)
            curr_time = datetime.datetime.now(timezone('Asia/Kolkata'))
            curr_time = curr_time.strftime("%b %d, %Y - %H:%M:%S")
            followers = instagram.get_followers(account.identifier, follower_limit, 100, delayed=True)

            current_followers = []

            for follower in followers['accounts']:
                current_followers.append(follower.username)

            del followers

            if not path.exists("follower_list.txt"):
                i = open("follower_list.txt", "w")
                i.write(str(current_followers))
                i.close()
            else:
                i = open("follower_list.txt", "r+")
                old_followers = i.read()
                i.close()
                old_followers = ast.literal_eval(old_followers)

                unfollowers = unfollowers_check(current_followers, old_followers)
                followers = followers_check(current_followers, old_followers)

                follower_change = len(current_followers) - len(old_followers)

                follow_count = len(followers)
                unfollow_count = len(unfollowers)

                Discord_Webhook.message_send(username, follower_change, followers, unfollowers, follow_count,
                                             unfollow_count, curr_time, discord_webhook_url)

                i = open("follower_list.txt", "w")
                i.write(str(current_followers))
                i.close()

        except KeyboardInterrupt:
            print("Exiting")
            sys.exit(0)
        except Exception as e:
            print(e)

        sleep(MINS_TO_SLEEP * 60)


if __name__ == '__main__':
    if not os.path.exists('config_file.txt'):
        print("Not configured your Run Configuration.py")
        sys.exit(0)

    f = open('config_file.txt', 'r')
    configuration = f.read()
    f.close()
    configuration = ast.literal_eval(configuration)
    ig_bot_username = configuration['instagram_username']
    ig_bot_password = configuration['instagram_password']
    username = configuration['monitor_username']
    discord_webhook_url = configuration['discord_webhook_url']

    start()