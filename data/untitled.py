import warnings
warnings.filterwarnings('ignore')
import pandas as pd
from pandasql import sqldf
pysqldf = lambda q: sqldf(q, globals())
oly_evts = pd.read_csv("../data/120-years-of-olympic-history-athletes-and-results/athlete_events.csv", header = 'infer')
oly_rgn = pd.read_csv("../data/120-years-of-olympic-history-athletes-and-results/noc_regions.csv", header='infer')
print(oly_evts.shape)
print(oly_rgn.shape)
oly_evts.head()

male_df = df[df.Sex=='M']
sport_weight_height_metrics = male_df.groupby(['Sport'])['Weight','Height'].agg(
  ['min','max','mean'])

sport_weight_height_metrics.Weight.dropna().sort_values('mean', ascending=False)[:5]
sns.distplot(sport_weight_height_metrics.Weight.dropna()['mean'])

means = list(sport_weight_height_metrics.Weight.dropna()['mean'])
sports = list(sport_weight_height_metrics.Weight.dropna().index)
plot_data = sorted(zip(sports, means), key = lambda x:x[1])
plot_data_dict = {
    'x' : [i for i, _ in enumerate(plot_data)],
    'y' : [v[1] for i, v in enumerate(plot_data)],
    'group' :  [v[0] for i, v in enumerate(plot_data)]
}
sns.scatterplot(data = plot_data_dict, x = 'x' , y = 'y')

print('lightest:')
for sport,weight in plot_data[:5]:
    print(sport + ': ' + str(weight))

print('\nheaviest:')    
for sport,weight in plot_data[-5:]:
    print(sport + ': ' + str(weight))

mean_heights = sport_weight_height_metrics.Height.dropna()['mean']
mean_weights = sport_weight_height_metrics.Weight.dropna()['mean']
avg_build = mean_weights/mean_heights
avg_build.sort_values(ascending = True)
builds = list(avg_build.sort_values(ascending = True))

plot_dict = {'x':[i for i,_ in enumerate(builds)],'y':builds}
sns.lineplot(data=plot_dict, x='x', y='y')


from collections import Counter

sport_min_year = male_df.groupby('Sport').Year.agg(['min','max'])['min'].sort_values('index')
year_count = Counter(sport_min_year)
year = list(year_count.keys())
new_sports = list(year_count.values())

data = {'x':year, 'y':new_sports}
sns.scatterplot(data=data, x = 'x', y='y')
