import requests
import pandas as pd


def parse_completion(completion_json):
    return set([f'{key}.{key2}' for key, value in completion_json.items() for key2 in value.keys()])


def retrieve_leaderboard(leaderboard_url, cookie):
    r = requests.get(leaderboard_url, cookies={"session": cookie})

    if r.status_code != requests.codes.ok:
        raise ConnectionError('The leaderboard could not be retrieved successfully')

    data = r.json()['members'].values()
    leaderboard = {d['id']: parse_completion(d['completion_day_level']) for d in data}

    return leaderboard


def make_teams_leaderboard_df(leaderboard, teams, metric):
    all_question_ids = [f'{i}.{j}' for i in range(1, 26) for j in range(1, 3)]
    for team in teams:
        for question_id in all_question_ids:
            team[question_id] = []
            for member_id in team['members'].values():
                if question_id in leaderboard[member_id]:
                    team[question_id].append(1)
                else:
                    team[question_id].append(0)
            team[question_id] = metric(team[question_id])
        team['total'] = sum([team[question_id] for question_id in all_question_ids])

    df = pd.DataFrame.from_dict(teams)
    columns_to_drop = ['members']
    for question_id in all_question_ids:
        if sum(df[question_id]) == 0:
            columns_to_drop.append(question_id)
    df.drop(columns=columns_to_drop, inplace=True)
    df.columns = [s.capitalize() for s in df.columns]
    df.set_index('Team', inplace=True)

    return df


def main():
    leaderboard_url = 'https://adventofcode.com/2020/leaderboard/private/view/1021522.json'
    cookie = '53616c7465645f5f8d0bc9a25eb833b45a33898430b29371a155ff4758e12207b0ca0529077bd4be62df2edaa2f784e7'
    teams = [{'team': 'Team Rocket', 'members': {'Pbatch': '1021522', 'Pbatch2': '1021522'}},
             {'team': 'Team Plasma', 'members': {'Pbatch': '1021522'}}]
    metric = sum

    if None in [leaderboard_url, cookie, teams]:
        raise ValueError('One of the required arguments has not been set')

    leaderboard = retrieve_leaderboard(leaderboard_url, cookie)
    df = make_teams_leaderboard_df(leaderboard, teams, metric)
    print(df.to_markdown())


if __name__ == '__main__':
    main()

