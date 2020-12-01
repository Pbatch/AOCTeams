# Advent of Code Teams

This is a repository for tracking the scores of teams in Advent of Code.

# Setup

Clone the repository and install the requirements
```
>>> git clone https://github.com/Pbatch/AOCTeams.git
>>> cd AOCTeams
>>> pip install -r requirements.txt
```

# Usage
To run `leaderboard.py` you will need to set a few variables in `main()`

1.) `leaderboard_url` - This is the URL of the JSON of your leaderboard,
you should be able to find it on the leaderboard page.

Example: `https://adventofcode.com/2020/leaderboard/private/view/1021522.json`

2.) `cookie` - This is the cookie that you need to provide when requesting the data,
you should be able to find it using your browser's developer tools on the leaderboard page.

Example: `53616c7465645f5f8d0bc9a25eb833b45a33898430b29371a155ff4758e12207b0ca0529077bd4be62df2edaa2f784e7`

3.) `teams` - This is a list of the teams in your leaderboard.
Each team is a dictionary with two keys, `team` and `members`.
Each member is a dictionary with key `name` and value `id`.
Participants can find their ID by going to their settings page.

Example: 
```
[
{
'team': 'Team Rocket', 
'members': {'player1': '1021522', 'player2': '1021522'}
}, 
{
'team': 'Team Plasma', 
'members': {'player3': '1021522'}
}
]
```

(Unlike the example, in your JSON each player should have a unique ID)

If you have done all of the above correctly, you should be ready to go!
Print a markdown leaderboard to the terminal with
```
>>> python leaderboard.py
```

Example: 

| Team        |   1.1 |   1.2 |   Total |
|:------------|------:|------:|--------:|
| Team Rocket |     2 |     2 |       4 |
| Team Plasma |     1 |     1 |       2 |

# Advanced Usage

In `main()` in `leaderboard.py` you can change the metric under which teams are scored.

To force collaboration within teams try
```
>>> metric = min
```
Now for a team to get a point, every member must answer the question successfully.

To encourage collaboration within teams try
```
>>> metric = lambda x: x*x
```
Now a team is rewarded for getting more members to answer the same question.

Warning - The square metric is not fair when teams are uneven.


