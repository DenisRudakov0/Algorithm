def all_continents(lst): 
    continent = ['Africa', 'Americas', 'Asia', 'Europe', 'Oceania']
    if len(lst) >= 5:    
        for i in continent:
            answer = False
            for j in lst:
                if i == j['continent']:
                    answer = True
                    print(i, j['continent'])
                    break
            if answer == False:
                return False
        if answer == True:
            return answer
        else:
            return answer
    return False
