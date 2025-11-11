import psutil
import sys, os



def get_cpu_load():
    """
    Returns CPU usage percentage over the given interval.
    :param interval: Time in seconds to sample CPU usage.
    """
    try:
        interval=1.0
        cpu_percent = psutil.cpu_percent(interval=interval)
        return cpu_percent
    except Exception as e:
        print(f"Error retrieving CPU load: {e}", file=sys.stderr)
        return None