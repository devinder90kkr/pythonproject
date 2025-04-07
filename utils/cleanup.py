import os
import shutil
import time
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
            try:
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
            except PermissionError:
                print(f"Permission denied for {item_path}. Skipping...")
            except Exception as e:
                print(f"Error processing {item_path}: {str(e)}")
    
    # Cleanup logs directory
    if os.path.exists(logs_dir):
        for log_file in os.listdir(logs_dir):
            log_path = os.path.join(logs_dir, log_file)
            try:
                if os.path.isfile(log_path):
                    file_time = datetime.fromtimestamp(os.path.getmtime(log_path))
                    if file_time < cutoff_date:
                        os.remove(log_path)
                        print(f"Removed old log: {log_file}")
            except PermissionError:
                print(f"Permission denied for {log_path}. Skipping...")
            except Exception as e:
                print(f"Error processing {log_path}: {str(e)}")

def cleanup_all_reports():
    """
    Remove all reports and logs (use with caution)
    """
    base_dir = os.path.dirname(os.path.dirname(__file__))
    reports_dir = os.path.join(base_dir, 'reports')
    logs_dir = os.path.join(base_dir, 'logs')
    
    try:
        # Cleanup reports directory
        if os.path.exists(reports_dir):
            # First, try to remove individual files
            for root, dirs, files in os.walk(reports_dir):
                for file in files:
                    try:
                        file_path = os.path.join(root, file)
                        os.remove(file_path)
                        print(f"Removed file: {file_path}")
                    except PermissionError:
                        print(f"Permission denied for {file_path}. Skipping...")
                    except Exception as e:
                        print(f"Error removing {file_path}: {str(e)}")
            
            # Then try to remove empty directories
            for root, dirs, files in os.walk(reports_dir, topdown=False):
                for dir in dirs:
                    try:
                        dir_path = os.path.join(root, dir)
                        os.rmdir(dir_path)
                        print(f"Removed directory: {dir_path}")
                    except PermissionError:
                        print(f"Permission denied for {dir_path}. Skipping...")
                    except Exception as e:
                        print(f"Error removing {dir_path}: {str(e)}")
            
            # Finally, try to remove the reports directory itself
            try:
                os.rmdir(reports_dir)
                print("Reports directory removed")
            except PermissionError:
                print("Permission denied for reports directory. Skipping...")
            except Exception as e:
                print(f"Error removing reports directory: {str(e)}")
        
        # Cleanup logs directory
        if os.path.exists(logs_dir):
            for root, dirs, files in os.walk(logs_dir):
                for file in files:
                    try:
                        file_path = os.path.join(root, file)
                        os.remove(file_path)
                        print(f"Removed log file: {file_path}")
                    except PermissionError:
                        print(f"Permission denied for {file_path}. Skipping...")
                    except Exception as e:
                        print(f"Error removing {file_path}: {str(e)}")
            
            try:
                os.rmdir(logs_dir)
                print("Logs directory removed")
            except PermissionError:
                print("Permission denied for logs directory. Skipping...")
            except Exception as e:
                print(f"Error removing logs directory: {str(e)}")
        
        # Create fresh directories
        os.makedirs(reports_dir, exist_ok=True)
        os.makedirs(os.path.join(reports_dir, 'screenshots'), exist_ok=True)
        os.makedirs(logs_dir, exist_ok=True)
        print("Fresh directories created")
        
    except Exception as e:
        print(f"Error during cleanup: {str(e)}") 