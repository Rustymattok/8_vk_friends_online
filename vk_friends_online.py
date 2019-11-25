import argparse
import vk
from vk.exceptions import VkAuthError

APP_ID = 7221330


def get_online_friends(login, password):
    try:
        session = vk.AuthSession(
            app_id=APP_ID,
            user_login=login,
            user_password=password,
            scope='friends'
        )
        api_friends = vk.API(session, v='5.85')
        friends_online = api_friends.friends.getOnline()
        friends_online_info = api_friends.users.get(
            user_ids=friends_online,
            fields='nickname'
        )
    except VkAuthError:
        return None
    return friends_online_info


def output_friends_to_console(friends_online_info):
    if friends_online_info is not None:
        for friend_name in friends_online_info:
            print(friend_name['first_name'], friend_name['last_name'])


def create_parser():
    parser_arg = argparse.ArgumentParser()
    parser_arg.add_argument('-l',
                            '--login',
                            required=True,
                            help="command - input file"
                            )
    parser_arg.add_argument('-p',
                            '--password',
                            required=True,
                            help="command - input file"
                            )
    return parser_arg


if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args()
    login_user = args.login
    password_user = args.password
    user_friends_online = get_online_friends(login_user, password_user)
    output_friends_to_console(user_friends_online)
