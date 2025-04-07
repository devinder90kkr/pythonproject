from utils.cleanup import cleanup_reports, cleanup_all_reports
import argparse

def main():
    parser = argparse.ArgumentParser(description='Cleanup old test reports and logs')
    parser.add_argument('--all', action='store_true', help='Remove all reports and logs')
    parser.add_argument('--days', type=int, default=7, help='Number of days to keep reports (default: 7)')
    
    args = parser.parse_args()
    
    if args.all:
        cleanup_all_reports()
    else:
        cleanup_reports(args.days)

if __name__ == '__main__':
    main() 