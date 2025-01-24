parties=["Party A","Party B","Party C"]
candidates=["candidate X","candidate Y","candidate Z"]
votes=[
    [15000, 12000, 18000],
    [13000, 10000, 11000],
    [27000, 14000, 16000],
]
total_votes_per_party=[0]*len(parties)
constituency_winners=[]
for constituency in votes:
    for i,vote_count in enumerate(constituency):
        total_votes_per_party[i] +=vote_count
        winning_party_index=constituency.index(max(constituency))
        constituency_winners.append(parties[winning_party_index])
        overall_winner=parties[total_votes_per_party.index(max(total_votes_per_party))]
        close_contests=[]
        vote_shares=[]
        for constituency in votes:
            total_votes=sum(constituency)
            shares=[(vote/total_votes)*100 for vote in constituency]
            vote_shares.append(shares)
            sorted_votes=sorted(constituency,reverse=True)
            margin=((sorted_votes[0]-sorted_votes[1])/total_votes)*100
            if margin<12:
                close_contests.append(True)
            else:
                close_contests.append(False)
        print("total votes for each party:",total_votes_per_party)
        print("winning party in each constituency:",constituency_winners)
        print("overall election winner:",overall_winner)
        print("vote shares(percentages)in each constituency:",vote_shares)
        print("close contests(true if close):",close_contests)