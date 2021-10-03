  
# TODO: create the User class
# it must support rank, progress, and the inc_progress(rank) method

class User():
    rank = -8
    progress = 0

    def inc_progress(lv):
        rank_list = [i for i in range(-8, 9) if i != 0]
        if user.rank == lv:
            user.progress += 3
        elif user.rank - 1 == lv:
            user.progress += 1
        elif user.rank < lv:
            user.progress = 10 * (rank_list.index(lv) - rank_list.index(user.rank)) * (rank_list.index(lv) - rank_list.index(user.rank)) 
        else:
            user.progress += 0
        
        if user.progress >= 100:
            if user.rank != 8:
                if rank_list.index(user.rank) + (user.progress // 100) > len(rank_list) - 1:
                    user.rank = 8
                else:
                    user.rank = rank_list[rank_list.index(user.rank) + (user.progress // 100)]
                    user.progress = user.progress % 100
        return user.progress, user.rank 
    
user = User()
user.rank = -8
user.progress = 0
print(User.inc_progress(6))
