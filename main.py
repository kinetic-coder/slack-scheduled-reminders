import slack_sdk
import Utilities.File
import os
import Utilities.ConfluenceUtility as Confluence
import Utilities.Settings as Settings

def post_message_to_slack(token, channel, message):
    client = slack_sdk.WebClient(token=token)
    response = client.chat_postMessage(channel=channel, text=message)
    return response

def main():

    current_folder = os.path.dirname(os.path.abspath(__file__))

    slack_secrets_file = current_folder + "\\secret\\slack_token.txt"
    confluence_secrets_file = current_folder + "\\secret\\confluence_token.txt"
    confluence_link_file = current_folder + "\\secret\\confluence_link.txt"
    confluence_page = current_folder + "\\secret\\confluence_page.txt"

    slack_token = Utilities.File.read_single_line(slack_secrets_file, 1)
    confluence_token = Utilities.File.read_single_line(confluence_secrets_file, 1)
    confluence_link = Utilities.File.read_single_line(confluence_link_file, 1)
    confluence_page = Utilities.File.read_single_line(confluence_page, 1)

    Settings.initialise(current_folder + "\\secret\\configuration.json")

    duty_staff_message = Confluence.get_this_weeks_duty_staff(confluence_link, confluence_token, confluence_page)

    channel = "#test_cm_app"
    # channel = "#sbc_clientmanagement_app"
    response = post_message_to_slack(slack_token, channel, duty_staff_message)
    
    print(duty_staff_message)

if __name__ == "__main__":
    main()