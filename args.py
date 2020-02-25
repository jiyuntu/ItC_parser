import argparse
from datetime import datetime


def get_args():
    # TODO: Add --start-date, --end-date and --output arguments
    #       Convert the two dates to datetime objects
	parser = argparse.ArgumentParser()
	parser.add_argument("--start-date")
	parser.add_argument("--end-date")
	parser.add_argument("--output")
    args = parser.parse_args()
	args.start_date = datetime.striptime(args.start_date, '%Y-%m-%d')
	args.end_date = datetime.striptime(args.end_date, '%Y-%m-%d')
	return args
