import requests
import json

def main():
    league = get_league()
    season = get_season()

    url = "https://v3.football.api-sports.io/standings"
    url2 = "https://v3.football.api-sports.io/players/topscorers"

    params = {
        'league': league,
        'season': season
    }

    headers = {
        "X-RapidAPI-Key": "2fa208034dec3075b93d340a632f9b8b",
        "X-RapidAPI-Host": "v3.football.api-sports.io"
    }

    response = requests.get(url, headers=headers, params=params)
    response2 = requests.get(url2, headers=headers, params=params)

    if response.status_code == 200 and response2.status_code == 200:
        data = response.json()
        data2 = response2.json()

        if data['response'] and data2['response']:
            standings = data['response'][0]['league']['standings'][0]


            print("League Standings:")
            print("")
            for team in standings:
                if team['rank']==1:
                    print('🏆 THE CHAMPION 🏆')

                print(team['team']['name'])
                print("Position:", team['rank'])
                print("Points:", team['points'])
                print("Goals on favor:", team['all']['goals']['for'])
                print("Goals against:", team['all']['goals']['against'])
                print("Goals difference:", team['goalsDiff'])
                print("Matches played:", team['all']['played'])
                print("Wins:", team['all']['win'])
                print("Draws:", team['all']['draw'])
                print("Defeats:", team['all']['lose'])
                print("--------------------------------------------------")

            choice = input("Do you want to see the top scorers? (y/n): ")
            if choice.lower() == 'y':
                print_top_scorers(data2['response'])
                return data2['response']

        else:
            print("No league data found.")
    else:
        print("Error retrieving data:", response.status_code)

def get_season(year=None):
    if year is None:
        year = input("What year's info do you want to see?: ")
    try:
        year = int(year)
        return year
    except ValueError:
        print('Please enter a valid year')



def print_top_scorers(players):
    print('Top Scorers:')
    print('')
    for player in players:
        print("Name:", player['player']['name'])
        print("Team:", player['statistics'][0]['team']['name'])
        print("Goals:", player['statistics'][0]['goals']['total'])
        print("----------------------------------")

def get_league(league=None):
    table = {
            'Premier League': '39',
            'La Liga': '140',
            'Bundesliga': '78',
            'Serie A': '135',
            'League 1': '61',
            'Eredivisie': '100',
            'Primeira Liga': '94',
            'MLS': '253',
            'Brasileirao': '71'
        }
    if league is None:
        league = input("What league do you want to see?: ")
    try:
        return table[league]
    except KeyError:
        print('Please enter a valid league.')


if __name__=='__main__':
    main()
