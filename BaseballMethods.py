class methods:
	def find_null_values(dataset):
		'''This function checks for null values and prints out the amount if there are any

		Args:
		 dataset: an oject representation of our dataset
		'''
		dataset.isnull().sum()
		num_null = dataset.isnull().sum().sum()
		print("No of Null Values: {}".format(num_null))

	def replace_values_for_consistency(dataset):
		'''This method replaces string values with "Philadelphia" with "Philly"

		Args:
		 dataset: an oject representation of our dataset
		 '''
		dataset.replace( 'Philadelphia', 'Philly',inplace = True)
		print(dataset.head(2))

	def replace_null_city_values(dataset):
		'''This method replaces null city values with a placeholder name

		Args:
		 dataset: an oject representation of our dataset
		 "'''
		dataset['city'].fillna( dataset['venue'].apply(lambda x: x[:5]),inplace = True)
		dataset[dataset['city']== 'Dubai']

	def display_post_profiling(dataset):
		'''This method displays the post profiling

		Args:
		 dataset: an oject representation of our dataset
		 '''
		print(dataset.columns)
		print(dataset['team1'].unique())

	def matches_won_total_matches(dataset, matches_won, total_matches):
		'''This method counts the total matches a certain team won and outputs them. It sorts them in
		descending order and then displays the data through a plot bar

		Args:
		 dataset: an oject representation of our dataset
		 matches_won: a placeholder variable for the raw count of matches 
		 total_matches:  a placeholder variable for the total amount of matches
		 '''
		matches_won = dataset.groupby('winner').count()
		matches_won
		
		total_matches = dataset['team1'].value_counts()+ dataset['team2'].value_counts()
		total_matches
		
		matches_won['Total matches']=total_matches
		matches_won[["Total matches","result"]].sort_values(by=["Total matches"],ascending=False).plot.bar(stacked=True,figsize=(7,3))

	def runs_scored_ascending(most_runs):
		'''Prints the runs scored in ascending order

		Args:
			most_runs: The maximum number of runs
		'''
		asc_most_runs = most_runs.sort_values(by="total_runs", ascending=True)
		print(asc_most_runs)
	def runs_scored_descending(most_runs):
		'''Prints the runs scored in descending order 
		
		Args:
			most_runs:The maximum number of runs
		'''
		desc_most_runs = most_runs.sort_values(by="total_runs", ascending=False)
		print(desc_most_runs)