def find_null_values(imdb):
	imdb.isnull().sum().sum()
	num_null = imdb.isnull().sum()
	print("No of Null Values: {}".format(num_null))

def average_bat(imdb):
  total_bat = imdb['batsman_run'].sum()
  total_bat= len(imdb.index) - 1
  avg_runs = total_bat / total_bat
  print('Average of Batsman run for Ball_to_ball is: {}'.format(avg_runs))

def duration_rating(imdb, Runtime, IMDB_Rating):
  im = imdb.groupby('Released_Year').count()
  imdb
  
  duration_rating = imdb['Series_Title'].value_counts()+ imdb['Team2'].value_counts()
  duration_rating
  
  imdb['Total Movies']=total_movies
  imdb[["Total Duration","IMDB Rated"]].sort_values(by=["Total Movies"],ascending=False).plot.bar(stacked=True,figsize=(7,3))

def runs_scored_ascending(most_runs):
  asc_most_runs = most_runs.sort_values(by="total_run", ascending=True)
  print(asc_most_runs)




