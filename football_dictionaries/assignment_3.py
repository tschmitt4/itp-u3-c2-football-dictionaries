def players_by_country_and_position(squads_list):
    data = {}
    for player in squads_list:
        data.setdefault(player[6],{})
        data[player[6]].setdefault(player[1],[])
        
        players_dict = {
            'number': player[0],
            'position': player[1],
            'name': player[2],
            'date_of_birth': player[3],
            'caps': player[4],
            'club': player[5],
            'country': player[6],
            'club_country': player[7],
            'year': player[8],
            
        }
        
       # country = players_dict['country']
        #data.setdefault(country,{})
        #position = players_dict['position']
        #data.setdefault(position,[])
        
        
        data[player[6]][player[1]].append(players_dict)
    
    return data