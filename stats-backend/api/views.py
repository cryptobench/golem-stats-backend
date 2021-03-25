from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .utils import get_stats_data
import os
import time


@api_view(['GET'])
def network_utilization(request, start, end):
    """
    Queries the networks utilization from a start date to the end date specified, and returns
    timestamps in ms along with providers computing.
    """
    if request.method == 'GET':
        time_difference = end - start
        if not time_difference > 300000:
            domain = os.environ.get(
                'STATS_URL') + f"api/datasources/proxy/40/api/v1/query_range?query=sum(activity_provider_created%7Bjob%3D~%22community.1%22%7D%20-%20activity_provider_destroyed%7Bjob%3D~%22community.1%22%7D)&start={start}&end={end}&step=30"
            data = get_stats_data(domain)
            return Response(data)
        else:
            content = {
                'reason': 'The queried time range cannot surpass 300000 seconds'}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def providers_computing_currently(request):
    """
    Returns how many providers are currently computing a task.
    """
    if request.method == 'GET':
        end = round(time.time())
        start = round(time.time()) - int(10)
        domain = os.environ.get(
            'STATS_URL') + f"api/datasources/proxy/40/api/v1/query_range?query=sum(activity_provider_created%7Bjob%3D~%22community.1%22%7D%20-%20activity_provider_destroyed%7Bjob%3D~%22community.1%22%7D)&start={start}&end={end}&step=1"
        data = get_stats_data(domain)
        content = {'computing_now': data['data']['result'][0]['values'][-1][1]}
        return Response(content, status=status.HTTP_200_OK)


@api_view(['GET'])
def network_earnings(request, hours):
    """
    Returns the earnings for the whole network the last n hours.
    """
    if request.method == 'GET':
        end = round(time.time())
        start = round(time.time()) - int(10)
        domain = os.environ.get(
            'STATS_URL') + f"api/datasources/proxy/40/api/v1/query_range?query=sum(increase(payment_amount_received%7Bjob%3D~%22community.1%22%7D%5B{hours}h%5D)%2F10%5E9)&start={start}&end={end}&step=1"
        data = get_stats_data(domain)
        content = {'total_earnings': data['data']
                   ['result'][0]['values'][-1][1][0:4]}
        return Response(content, status=status.HTTP_200_OK)
