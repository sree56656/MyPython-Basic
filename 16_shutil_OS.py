import os  # to navigate through directories
import shutil  # to copy or move files
from collections import Counter
from collections import defaultdict
from collections import namedtuple
import datetime

# print(os.getcwd())
# print(os.listdir())


# dates_diff
today = datetime.datetime.today()
print(today)
print(today.ctime())
td = datetime.datetime(2021, 5, 25)
print(td)
update = td.replace(year=2022)
print(update)
diff = update - today
print(diff)