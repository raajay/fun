from datetime import datetime
import csv
import os
import pkg_resources

def _formatdate(s):
    return datetime.strptime(s, '%Y-%m-%d')


_match_schema = {
    1: ('id', int),
    2: ('season', str),
    3: ('city', str),
    4: ('date', _formatdate),
    5: ('team1', str),
    6: ('team2', str),
    7: ('toss_winner', str),
    8: ('toss_decision', str),
    9: ('result', str),
    10: ('dl_applied', int),
    11: ('winner', str),
    12: ('win_by_runs', int),
    13: ('win_by_wickets', int),
    14: ('player_of_match', str),
    15: ('venue', str),
    16: ('umpire1', str),
    17: ('umpire2', str),
    18: ('umpire3', str),
}


_deliveries_schema = {
    1: ('match_id', int),
    2: ('inning', int),
    3: ('batting_team', str),
    4: ('bowling_team', str),
    5: ('over', int),
    6: ('ball', int),
    7: ('batsman', str),
    8: ('non_striker', str),
    9: ('bowler', str),
    10: ('is_super_over', bool),
    11: ('wide_runs', int),
    12: ('bye_runs', int),
    13: ('legbye_runs', int),
    14: ('noball_runs', int),
    15: ('penalty_runs', int),
    16: ('batsman_runs', int),
    17: ('extra_runs', int),
    18: ('total_runs', int),
    19: ('player_dismissed', str),
    20: ('dismissal_kind', str),
    21: ('fielder', str),
}


class Delivery:
    def __init__(self, parts):
        [
            setattr(self, _deliveries_schema[i+1][0], _deliveries_schema[i+1][1](parts[i]))
            for i in range(len(parts))
        ]


class Match:
    def __init__(self, parts):
        [
            setattr(self, _match_schema[i+1][0], _match_schema[i+1][1](parts[i]))
            for i in range(len(parts))
        ]


def get_matches():
    with open(pkg_resources.resource_filename(__name__, os.path.join('data', 'matches.csv'))) as fp:
        reader = csv.reader(fp)
        rows = [row for row in csv.reader(fp)]
        matches = { int(row[0]) : Match(row) for row in rows[1: ] }
    return matches


def get_deliveries(enhance=True):
    with open(pkg_resources.resource_filename(__name__, os.path.join('data', 'deliveries.csv'))) as fp:
        reader = csv.reader(fp)
        rows = [row for row in csv.reader(fp)]
        delivery_counter = 1
        deliveries = dict()
        for row in rows[1: ]:
            deliveries[delivery_counter] = Delivery(row)
            delivery_counter += 1

    if not enhance:
        return deliveries
    else:
        # TODO(raajay) add a function to add required run rate at each delivery
        return deliveries
