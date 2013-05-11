import sys
import operator
import pickle
import random

points_table = { 'CSK': 20,
                 'MI' : 18,
                 'RR' : 18,
                 'RCB': 16,
                 'SRH': 16,
                 'KXP': 10,
                 'KKR': 10,
                 'DD' :  6,
                 'PWI':  4
                }

match_schedule = [
                   (60, ('KKR',  'RCB')),
                   (61, ('RR' ,  'CSK')),
                   (62, ('MI' ,  'SRH')),
                   (63, ('RCB',  'KXP')),
                   (64, ('CSK',  'DD' )),
                   (65, ('KKR',  'PWI')),
                   (66, ('MI' ,  'RR' )),
                   (67, ('KXP',  'DD' )),
                   (68, ('SRH',  'RR' )),
                   (69, ('KXP',  'MI' )),
                   (70, ('RCB',  'CSK')),
                   (71, ('PWI',  'DD' )),
                   (72, ('SRH',  'KKR'))
                 ]

total_matches = len(match_schedule)
total_pts_comb = (1 << total_matches) - 1 
print "total matches = ", total_matches
print "Total combination = ", total_pts_comb

qual_chance = {}
for key in points_table.keys():
    qual_chance[key] = 0

for i in range(total_pts_comb): # enumerating all possible results
    new_pts_table = points_table.copy()
    for m in range(total_matches): #iterating through the matches
        if (i & (1 << m)):
            new_pts_table[match_schedule[m][1][0]] += 2
        else:
            new_pts_table[match_schedule[m][1][1]] += 2

    new_pts_table = sorted(new_pts_table.iteritems(), key=operator.itemgetter(1), reverse=True)
#    print type(new_pts_table)
#    print new_pts_table

    fourth_pts = new_pts_table[3][1]
    selected = []
    random_pool = []
    for term in new_pts_table:
        if term[1] > fourth_pts:
            selected.append(term)
            qual_chance[term[0]] += 1
        elif term[1] == fourth_pts:
            random_pool.append(term)

    random.shuffle(random_pool)
    for term in random_pool:
        selected.append(term)
        qual_chance[term[0]] += 1
        if(len(selected) == 4):
            break

#    break

#print qual_chance
def myprint(a):
    print a[0], a[1]*100.0 / total_pts_comb
    return a[0], a[1]*100.0 / total_pts_comb
    

norm_qual = map(lambda x : (x[0], 100.0*x[1]/total_pts_comb), 
        qual_chance.iteritems())
norm_qual_sorted = sorted(norm_qual, key=operator.itemgetter(1),
        reverse=True)
map((lambda x : sys.stdout.write("%s, %0.3f\n"%(x[0], x[1]))), norm_qual_sorted)
