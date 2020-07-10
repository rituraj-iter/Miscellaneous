from discord_webhooks import DiscordWebhooks

# discord webhook url here.
discord_webhook_url = ''


def message_send(username, change_follower, followers, unfollowers, count_followers, count_unfollowers, time,
                 webhook_url):
    webhook = webhook_url

    if followers == [] and unfollowers == []:
        print("No change in followers, message not send to discord")
        return

    if not followers:
        followers = 'None'

    if not unfollowers:
        unfollowers = 'None'

    webhook = DiscordWebhooks(webhook)

    webhook.set_content(title='Report  %s' % time, description="Here's the report with ")

    webhook.set_footer(text='-- Account')

    webhook.add_field(name='Username', value=username)
    webhook.add_field(name='Total follower change', value=change_follower)

    if unfollowers != 'None':
        webhook.add_field(name='People who unfollow (%d)' % count_unfollowers, value=', '.join(unfollowers))
    else:
        webhook.add_field(name='People who unfollow (%d)' % count_unfollowers, value=unfollowers)

    if followers != 'None':
        webhook.add_field(name='People who follow (%d)' % count_followers, value=', '.join(followers))
    else:
        webhook.add_field(name='People who follow (%d)' % count_followers, value=followers)

    webhook.send()

    print("Message sent to discord")