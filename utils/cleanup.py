import os
import shutil
from datetime import datetime, timedelta

def cleanup_reports(days_to_keep=7):
    """
    Remove reports and logs older than specified days
    :param days_to_keep: Number of days to keep reports (default: 7)
    """
    base_dir = os.path.dirname(os.path.dirname(__file__))
    reports_dir = os.path.join(base_dir, 'reports')
    logs_dir = os.path.join(base_dir, 'logs')
    
    cutoff_date = datetime.now() - timedelta(days=days_to_keep)
    
    # Cleanup reports directory
    if os.path.exists(reports_dir):
        for item in os.listdir(reports_dir):
            item_path = os.path.join(reports_dir, item)
            if os.path.isfile(item_path):
                # Check file modification time
                file_time = datetime.fromtimestamp(os.path.getmtime(item_path))
                if file_time < cutoff_date:
                    os.remove(item_path)
                    print(f"Removed old report: {item}")
            elif os.path.isdir(item_path) and item == 'screenshots':
                # Cleanup screenshots directory
                for screenshot in os.listdir(item_path):
                    screenshot_path = os.path.join(item_path, screenshot)
                    if os.path.isfile(screenshot_path):
                        file_time = datetime.fromtimestamp(os.path.getmtime(screenshot_path))
                        if file_time < cutoff_date:
                            os.remove(screenshot_path)
                            print(f"Removed old screenshot: {screenshot}")
    
    # Cleanup logs directory
    if os.path.exists(logs_dir):
        for log_file in os.listdir(logs_dir):
            log_path = os.path.join(logs_dir, log_file)
            if os.path.isfile(log_path):
                file_time = datetime.fromtimestamp(os.path.getmtime(log_path))
                if file_time < cutoff_date:
                    os.remove(log_path)
                    print(f"Removed old log: {log_file}")

def cleanup_all_reports():
    """
    Remove all reports and logs (use with caution)
    """
    base_dir = os.path.dirname(os.path.dirname(__file__))
    reports_dir = os.path.join(base_dir, 'reports')
    logs_dir = os.path.join(base_dir, 'logs')
    
    if os.path.exists(reports_dir):
        shutil.rmtree(reports_dir)
        os.makedirs(reports_dir)
        print("All reports removed")
    
    if os.path.exists(logs_dir):
        shutil.rmtree(logs_dir)
        os.makedirs(logs_dir)
        print("All logs removed") 