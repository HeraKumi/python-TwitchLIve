import sys
from twitch import TwitchClient

try:
    if sys.version_info.major == 3:
        client = TwitchClient(client_id='24vvfy4ii87g3lb5s0ctn8oi5vrfwc')
        stream = client.streams.get_stream_by_user('230255743')

        if stream != None:
            channelName = stream.channel.name
            viewers = stream.viewers
            followers = stream.channel.followers
            print(f"Channel  :  {channelName}")
            print(f"Viewers  :  {viewers}")
            print(f"Followers:  {followers}")
            # print(f"Channel: {channelName} Viewers: {viewers} Followers: {followers}")
        
        elif stream == None:
            print('')
    elif sys.version_info.major != 3:
        print('You are not using python3 which this script should be ran with.')
except Exception as e:
    if isinstance(e):
        print(f"{e}")
    else:
        print('')