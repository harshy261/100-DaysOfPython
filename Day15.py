# EXERCISE - 2

import time
timestamp_limit = '12:00:00'

timestamp = time.strftime('%H:%M:%S')
print(timestamp)

if(timestamp < timestamp_limit ):
    print("Good Morning")
else:
    print("Good Afternoon")