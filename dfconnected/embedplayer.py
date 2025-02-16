import requests
import json
import re
import datetime

def get_current_unix_timestamp():
    return datetime.datetime.now().strftime("%I:%M %p")

# Example usage
current_unix_timestamp = get_current_unix_timestamp()

def fetch_player_count():
    try:
        response = requests.get('https://gms-status-tcr6.shuttle.app/')
        response.raise_for_status()
        data = response.text
        
        # Parse the JSON data
        json_data = json.loads(data)
        game_data = next((node for node in json_data['status'] if any(game['title'] == 'DF CONNECTED (Undertale MMORPG)' for game in node['games'])), None)
        
        if game_data:
            game = next(game for game in game_data['games'] if game['title'] == 'DF CONNECTED (Undertale MMORPG)')
            player_count = game['loggedIn']
            
            # Read the index.html file
            with open('dfconnected/index.html', 'r') as file:
                html_content = file.read()
            
            # Update the content attribute of the <meta property="og:description"/> tag
            og_description_pattern = r'<meta property="og:description" content="(.*?)"'
            new_og_description = f'<meta property="og:description" content="(Last Updated: {get_current_unix_timestamp()} UTC )"'
            updated_html_content1 = re.sub(og_description_pattern, new_og_description, html_content)
            
            og_title_pattern = r'<meta property="og:title" content="(.*?)"'
            new_og_title = f'<meta property="og:title" content="DFC Connected players:{player_count}"'
            updated_html_content2 = re.sub(og_title_pattern, new_og_title, updated_html_content1)
            
            # Write the updated content back to the index.html file
            with open('dfconnected/index.html', 'w') as file:
                file.write(updated_html_content2)
            with open('dfconnected/stats/temp.txt', 'r') as file:
                tempnum = file.read()
            if int(tempnum) < player_count:
                with open('dfconnected/stats/temp.txt', 'w') as file:
                    file.write(f"{player_count}")
            return player_count
        else:
            raise Exception('DFC game data not found')
    
    except (requests.exceptions.RequestException, Exception) as e:
        print(f'Error fetching player count: {e}')
        with open('dfconnected/index.html', 'r') as file:
            html_content = file.read()
        
        # Update the content attribute of the <meta property="og:description"/> tag
        og_description_pattern = r'<meta property="og:description" content="(.*?)"'
        new_og_description = f'<meta property="og:description" content="(Last Updated: {get_current_unix_timestamp()} UTC )"'
        updated_html_content1 = re.sub(og_description_pattern, new_og_description, html_content)
        
        og_title_pattern = r'<meta property="og:title" content="(.*?)"'
        new_og_title = f'<meta property="og:title" content="DFC Connected players:0"'
        updated_html_content2 = re.sub(og_title_pattern, new_og_title, updated_html_content1)
        
        # Write the updated content back to the index.html file
        with open('dfconnected/index.html', 'w') as file:
                file.write(updated_html_content2)
        return 'Error'
fetch_player_count()
