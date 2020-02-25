from crawler import Crawler
from args import get_args


if __name__ == '__main__':
	args = get_args()
	crawler = Crawler()
	contents = crawler.crawl(args.start_date, args.end_date)
    # TODO: write content to file according to spec
	with open(output,'w') as csv_out:
		for obj in contents:
			outstr = f'{str(obj[0])},"{obj[1]}","{obj[2]}"\n'
			f.write(outstr)
