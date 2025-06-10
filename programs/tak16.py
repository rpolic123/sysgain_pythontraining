

teams = {
    "TeamA": [
        {"name": "Alice", "role": "Batsman"},
        {"name": "Bob", "role": "Bowler"}
    ],
    "TeamB": [
        {"name": "Charlie", "role": "Allrounder"},
        {"name": "Dave", "role": "Wicketkeeper"}
    ]
}



for team,values in teams.items():
    print(team)
    print("--------")
    for i in values:
        print(i['name'])
    print()
