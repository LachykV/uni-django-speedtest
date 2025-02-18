from django.shortcuts import render
from django.http import JsonResponse
import speedtest
from .models import SpeedTestResult

def index(request):
    latest_results = SpeedTestResult.objects.all()[:5]
    return render(request, 'speedtest_app/index.html', {'latest_results': latest_results})

def check_speed(request):
    try:
        st = speedtest.Speedtest()
        download_speed = st.download() / 1000000  # Convert to Mbps
        upload_speed = st.upload() / 1000000  # Convert to Mbps
        ping = st.results.ping

        # Save results
        SpeedTestResult.objects.create(
            download_speed=download_speed,
            upload_speed=upload_speed,
            ping=ping
        )

        return JsonResponse({
            'success': True,
            'download_speed': round(download_speed, 2),
            'upload_speed': round(upload_speed, 2),
            'ping': round(ping, 2)
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        })