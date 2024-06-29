from pytrends.request import TrendReq

# def get_google_trends(keyword):
#     pytrends = TrendReq(hl='en-US', tz=360)
#     pytrends.build_payload([keyword], cat=0, timeframe='2016-12-14 2017-01-25', geo=[keyword], gprop='')

#     # Get interest over time data
#     interest_over_time_df = pytrends.interest_over_time()

#     return interest_over_time_df

# # Example usage
# keyword = 'Valentines Day'
# results = get_google_trends(keyword)
# print(results)


# kw_list =["Scandlines",]

# pytrends = TrendReq( hl='DK', tz=360)

# pytrends.build_payload(kw_list, cat=0, timeframe='2016-12-14 2017-01-25', geo='DK', gprop='')
# print(pytrends.build_payload)

# iot_df = pytrends.interest_over_time()

# iot_df = iot_df.reset_index()

# iot_df = iot_df.drop(['isPartial'], axis=1)

# print(iot_df)



# pytrends = TrendReq(hl='en-US', tz=360)
# kw_list = ["machine learning"] # list of keywords to get data 
# pytrends.build_payload(kw_list, cat=0, timeframe='today 12-m')
# data = pytrends.interest_over_time() 
# data = data.reset_index()
# import plotly.express as px

# fig = px.line(data, x="date", y=['machine learning'], title='Keyword Web Search Interest Over Time')
# fig.show()
# # print(fig)



pytrend = TrendReq()
pytrend.build_payload(kw_list=['Messi'])
df = pytrend.interest_by_region()
df.head(10)


pytrend = TrendReq(hl='eng-US')

all_keywords = ['Fidget spinner',
                'Food','Cycling',
                'Home Alone']

timeframes = ['today 5-y', 'today 12-m',
              'today 3-m', 'today 1-m']

cat = '0'
geo = ''
gprop = ''

pytrend.build_payload(all_keywords,
                      cat,
                      timeframes[0],
                      geo,
                      gprop)

data = pytrend.interest_over_time()
print(data)