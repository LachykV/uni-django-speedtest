from django.shortcuts import render
from django.http import JsonResponse
import speedtest
from django.views.decorators.csrf import csrf_exempt
from .models import SpeedTestResult
import logging

logger = logging.getLogger(__name__)

# Add this index view function
def index(request):
    latest_results = SpeedTestResult.objects.all()[:5]  # Get last 5 results
    return render(request, 'speedtest_app/index.html', {'latest_results': latest_results})

@csrf_exempt
def check_speed(request):
    try:
        st = speedtest.Speedtest()
        st.get_best_server()  # Get best server
        
        # Get server details
        server = st.get_best_server()
        server_location = f"{server['name']}, {server['country']}"
        
        # Perform speed test
        download_speed = st.download() / 1000000
        upload_speed = st.upload() / 1000000
        ping = st.results.ping

        # Save results with server info
        result = SpeedTestResult.objects.create(
            download_speed=download_speed,
            upload_speed=upload_speed,
            ping=ping,
            server_name=server['name'],
            server_location=server['sponsor'],
            server_country=server['country']
        )

        return JsonResponse({
            'success': True,
            'download_speed': round(download_speed, 2),
            'upload_speed': round(upload_speed, 2),
            'ping': round(ping, 2),
            'server_location': server_location
        })
    except Exception as e:
        logger.error(f"Speed test error: {str(e)}")
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=500)