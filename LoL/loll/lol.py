from flask import Flask, jsonify, request, render_template_string
import requests

app = Flask(__name__)

html_form = """
<!DOCTYPE html>
<html>
<head>
    <title>Summoner Account Info</title>
</head>
<body>
    <h2>Enter Summoner Name, Tag Line, and Region</h2>
    <form action="/process_form" method="post">  <!-- Note the action attribute -->
        Summoner Name: <input type="text" name="form_summoner_name"><br>
        Tag Line: <input type="text" name="tag_line"><br>
        Region: 
        <select name="region">
            <option value="europe">Europe</option>
            <option value="americas">Americas</option>
            <option value="asia">Asia</option>
        </select><br>
        <input type="submit" value="Submit">
    </form>
</body>
</html>
"""


@app.route('/')
def home():
    # Serve the HTML form when visiting the home page
    return render_template_string(html_form)

@app.route('/process_form', methods=['POST'])
def process_form():
        summoner_name = request.form['form_summoner_name']
        tag_line = request.form['tag_line']
        region = request.form['region']
        api_key = "RGAPI-bf84cce7-2730-4c67-9bcc-1480e498ac4f"


        account_url = f"https://{region}.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{summoner_name}/{tag_line}?api_key={api_key}"
        account_response = requests.get(account_url)
        account_data = account_response.json()
        puuid = account_data['puuid']
        
        

        matches_url = f"https://{region}.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?start=0&count=1&api_key={api_key}"
        matches_response = requests.get(matches_url)
        match_id = matches_response.json()
        match_id = match_id[0]



        last_match = f"https://{region}.api.riotgames.com/lol/match/v5/matches/{match_id}?api_key={api_key}"
        last_match_response = requests.get(last_match)
        last_match_data = last_match_response.json()
        participant_list = []
        for participant in last_match_data['info']['participants']:
            # Assuming you want to collect both 'summonerName' and 'championName'
            participant_list.append({
            'summonerName': participant.get('summonerName', ''),
            'championName': participant.get('championName', '')
            })
        
        return jsonify(participant_list)

        
            


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)