from django.urls import path
from .views import *



urlpatterns = [
    path('api/daily-trend/', DailyTrendView.as_view(), name='daily_trend'),
    path('api/trending-searches/', TrendingSearchesView.as_view(), name='trending_searches'),
    path('api/trend_over_time/', TrendOverTimeView.as_view(), name='trend_over_time'),
    path('trends/', get_trends, name='trends'),
    # path('api/google-trends/<str:keyword>/', get_google_trends, name='get_google_trends'),
    # path('api/google-trends/<str:keyword>/', GoogleTrendsView.as_view(), name='google_trends_view'),
]
