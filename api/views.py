from rest_framework.response import Response
from pytrends.request import TrendReq
import urllib.parse
from rest_framework.views import APIView
from pytrends.exceptions import ResponseError
from django.http import JsonResponse






class DailyTrendView(APIView):
    def get(self, request):
        pytrend = TrendReq()
        trending_today_urls = pytrend.today_searches(pn='US')
        trending_today = [urllib.parse.parse_qs(urllib.parse.urlparse(url).query)['q'][0] for url in trending_today_urls]
        response_data = {
            'trending_today': trending_today[:50],
        }
        return Response(response_data)



class TrendingSearchesView(APIView):
    def get(self, request):
        country_code = request.GET.get('pn', 'united_states')
        pytrend = TrendReq()
        trending_searches = pytrend.trending_searches(pn=country_code)
        response_data = {
            'trending_searches': trending_searches[0].values.tolist(),
        }
        return Response(response_data)



# class TrendOverTimeView(APIView):
#     def get(self, request):
#         try:
#             keyword = request.GET.get('keyword', 'python')
#             country_code = request.GET.get('pn', 'united_states')
            
#             pytrend = TrendReq()
#             # pytrend.build_payload(kw_list=[keyword], timeframe='today 5-y', geo=country_code)
#             pytrend.build_payload()
#             interest_over_time_data = pytrend.interest_over_time()
#             interest_over_time_values = interest_over_time_data[keyword].tolist()
            
#             response_data = {
#                 'keyword': keyword,
#                 'country_code': country_code,
#                 'interest_over_time': interest_over_time_values,
#             }
            
#             return Response(response_data)
        
#         except ResponseError as e:
#             error_message = f"Google Trends API error: {e}"
#             print(error_message)
#             print(f"Error response: {e.response.text}")
#             return Response({'error': error_message}, status=400)



class TrendOverTimeView(APIView):
    def get(self, request):
        try:
            keyword = request.GET.get('keyword', 'python')
            country_code = request.GET.get('pn', 'united_states')
            
            pytrend = TrendReq()
            pytrend.build_payload(kw_list=[], geo=country_code)  # Provide an empty list for kw_list
            interest_over_time_data = pytrend.interest_over_time()
            
            # If a specific keyword is provided, extract its data
            if keyword in interest_over_time_data.columns:
                interest_over_time_values = interest_over_time_data[keyword].tolist()
            else:
                interest_over_time_values = []

            response_data = {
                'keyword': keyword,
                'country_code': country_code,
                'interest_over_time': interest_over_time_values,
            }
            
            return Response(response_data)
        
        except ResponseError as e:
            error_message = f"Google Trends API error: {e}"
            print(error_message)
            print(f"Error response: {e.response.text}")
            return Response({'error': error_message}, status=400)





# from ratelimit.decorators import ratelimit




# @ratelimit(key='ip', rate='10/m', block=True)
# def get_google_trends(request, keyword):
#     pytrends = TrendReq(hl='en-US', tz=360)
#     pytrends.build_payload([keyword], timeframe='today 5-y')
#     interest_over_time = pytrends.interest_over_time()

#     return JsonResponse({'interest_over_time': interest_over_time.to_dict(orient='records')})




def get_trends(request):
    # Retrieve keyword and time period from request parameters
    keyword = request.GET.get('keyword')
    timeframe = request.GET.get('timeframe')

    # Initialize PyTrends object
    pytrends = TrendReq()

    # Build payload with keyword and timeframe
    pytrends.build_payload(
        kw_list=[keyword],
        timeframe=timeframe
    )

    # Get interest over time data
    data = pytrends.interest_over_time()

    # Serialize data as JSON
    response_data = data.to_json(orient='records')

    return JsonResponse({'data': response_data})
