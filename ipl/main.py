import ipldata
from collections import defaultdict
#matches = ipldata.ipldata.get_matches()
deliveries = ipldata.get_deliveries()
print len(deliveries)

rsharma_deliveries = {
    k:v for k,v in deliveries.iteritems()
    if v.batsman == 'RG Sharma'
#    and v.bowling_team == 'Chennai Super Kings'
}

print "RG Sharma faced", len(rsharma_deliveries), "deliveries."
runs_per_match = defaultdict(lambda: 0)

for k,v in rsharma_deliveries.iteritems():
    runs_per_match[v.match_id] += v.batsman_runs

zero_runs = [x for x in runs_per_match.values() if x == 0]
less_than_ten = [x for x in runs_per_match.values() if x > 0 and x <= 10]

print len(zero_runs), len(less_than_ten), len(runs_per_match.keys())
