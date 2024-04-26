import pytest
import requests
import json
from project import get_season, get_league, print_top_scorers


def test_get_season():
    assert get_season('2020')==2020
    assert get_season('2019')==2019
    assert get_season('2018')==2018

def test_get_league():
    assert int(get_league('Premier League')) == 39

def test_print_top_scorers(capsys):
    url2 = "https://v3.football.api-sports.io/players/topscorers"

    headers = {
        "X-RapidAPI-Key": "2fa208034dec3075b93d340a632f9b8b",
        "X-RapidAPI-Host": "v3.football.api-sports.io"
    }
    params = {
        'league': 39,
        'season': 2020
    }

    response2 = requests.get(url2, headers=headers, params=params)
    data2 = response2.json()
    data2['response']


    print_top_scorers(data2['response'])


    captured = capsys.readouterr()


    expected_output = """Top Scorers:

Name: H. Kane
Team: Tottenham
Goals: 23
----------------------------------
Name: Mohamed Salah
Team: Liverpool
Goals: 22
----------------------------------
Name: Bruno Fernandes
Team: Manchester United
Goals: 18
----------------------------------
Name: Son Heung-Min
Team: Tottenham
Goals: 17
----------------------------------
Name: P. Bamford
Team: Leeds
Goals: 17
----------------------------------
Name: D. Calvert-Lewin
Team: Everton
Goals: 16
----------------------------------
Name: J. Vardy
Team: Leicester
Goals: 15
----------------------------------
Name: O. Watkins
Team: Aston Villa
Goals: 14
----------------------------------
Name: İ. Gündoğan
Team: Manchester City
Goals: 13
----------------------------------
Name: A. Lacazette
Team: Arsenal
Goals: 13
----------------------------------
Name: K. Ịheanachọ
Team: Leicester
Goals: 12
----------------------------------
Name: D. Ings
Team: Southampton
Goals: 12
----------------------------------
Name: C. Wood
Team: Burnley
Goals: 12
----------------------------------
Name: C. Wilson
Team: Newcastle
Goals: 12
----------------------------------
Name: M. Rashford
Team: Manchester United
Goals: 11
----------------------------------
Name: S. Mané
Team: Liverpool
Goals: 11
----------------------------------
Name: G. Bale
Team: Tottenham
Goals: 11
----------------------------------
Name: W. Zaha
Team: Crystal Palace
Goals: 11
----------------------------------
Name: Matheus Pereira
Team: West Brom
Goals: 11
----------------------------------
Name: R. Sterling
Team: Manchester City
Goals: 10
----------------------------------"""

    assert captured.out.strip() == expected_output.strip()

    

