import pickle
points_table = { 'CSK': 18,
                 'MI' : 16,
                 'RR' : 16,
                 'RCB': 14,
                 'SRH': 14,
                 'KXP': 10,
                 'KKR':  8,
                 'DD' :  6,
                 'PWI':  4
                }

match_schedule = [
                   (54, ('SRH',  'CSK')),
                   (55, ('KXP',  'RR' )),
                   (56, ('PWI',  'KKR')),
                   (57, ('DD' ,  'RCB')),
                   (58, ('PWI',  'MI' )),
                   (59, ('KXP',  'SRH')),
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
f = open("data.pkl","w")
pickle.dump([points_table, match_schedule], f)
f.close()
