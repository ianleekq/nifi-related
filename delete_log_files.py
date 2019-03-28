import os
import re
from datetime import datetime, timedelta

log_dir = os.path.join('h:', os.sep, 'python_scripts', 'logs')
category = 'nifi-app'
category_regex = re.compile("{}.*".format(category))
category_prefix = category + '_'
filetype_suffix = 'txt'
days_to_retain = 5

files = os.listdir(log_dir)

cat_files = [file for file in files if category_regex.search(file)]

delete_files = cat_files[:]

regex = re.compile("{}\.{}".format(category, filetype_suffix))
delete_files = [file for file in delete_files if not regex.search(file)]

for day in range(days_to_retain + 1):
	date = datetime.today() - timedelta(days=day)
	formatted_date = "{:%Y-%m-%d}".format(date)
	file_to_retain_regex = re.compile("{}{}\.\d+\.{}".format(category_prefix, formatted_date, filetype_suffix))
	delete_files = [file for file in delete_files if not file_to_retain_regex.search(file)]

for file in delete_files:
	try:
		os.remove(os.path.join(log_dir, file))
	except OSError:
		pass