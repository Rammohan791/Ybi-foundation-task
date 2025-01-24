import pandas as pd

# Sample cricket match data (replace with actual data)
data={
    'Player':['Rohit Sharma','KL rahul','Virat Kohli','Suryakumar Yadav','Hardik Pandya','MS Dhoni','Ravindra Jadeja','Bhuvneshwar Kumar','Jasprit bumrah','Yuzvendra Chahal','Mohammed Shami'],
    'Runs':[45,68,35,75,25,50,15,10,0,5,0],
    'Wickets':[0,0,0,0,1,0,2,0,1,2,3],
    'Balls Faced':[30,60,42,55,20,45,12,8,4,1,1],
    'Balls Bowled':[0,0,0,0,10,0,10,10,10,10,10]
}

match_data=pd.DataFrame(data)

# Calculate team total runs
total_runs=match_data['Runs'].sum()
print("Total Runs:",total_runs)

# Calculate batting average for each player
match_data['Batting Average']=match_data['Runs']/(match_data['Balls Faced']-match_data['Runs']) #Adjust formula as needed
print("\nBatting Averages:\n",match_data[['Player','Batting Average']])

# Calculate bowling strike rate for bowlers
bowlers=match_data[match_data['Balls Bowled']>0]
bowlers['Bowling Strike Rate']=bowlers['Balls Bowled']/bowlers['Wickets']
print("\nBowling Strike Rates:\n",bowlers[['Player','Bowling Strike Rate']])

#Identify top run-scorer
top_scorer=match_data.loc[match_data['Runs'].idxmax(),'Player']
print("\nTop Run-scorer:",top_scorer)

#Identify top wicket-taker
top_wicket_taker=bowlers.loc[bowlers['Wickets'].idxmax(),'Player']
print("Top Wicket-taker:",top_wicket_taker)

# Simple points system (example)
match_data['Points']=(match_data['Runs']/10)+(match_data['Wickets']*20)
print("\nPlayer Points:\n",match_data[['Player','Points']])

