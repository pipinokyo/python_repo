# What is the expected output of the following code?

from datetime import datetime

datetime = datetime(2019, 11, 27, 11, 27, 22)
print(datetime.strftime('%y/%B/%d %H:%M:%S'))


# Code Explanation:
# from datetime import datetime  # Import datetime class from datetime module

# datetime = datetime(2019, 11, 27, 11, 27, 22)  # Create a datetime object
# print(datetime.strftime('%y/%B/%d %H:%M:%S'))  # Format and print the datetime
# Visualization:
# [datetime Object]
# ┌──────────────────────────────┐
# │ Year: 2019                   │
# │ Month: 11 (November)         │
# │ Day: 27                      │
# │ Hour: 11                     │
# │ Minute: 27                   │
# │ Second: 22                   │
# └───────────────┬──────────────┘
#                 │
#                 │ .strftime() formatting
#                 ▼
# "19/November/27 11:27:22"
# Format Specifiers Breakdown:
# %y → Last two digits of year (19)

# %B → Full month name (November)

# %d → Day of month (27)

# %H → Hour (11)

# %M → Minute (27)

# %S → Second (22)

# Expected Output:
# 19/November/27 11:27:22

# Important Notes:
# There's a naming conflict in the code (using datetime for both the class and variable name)

# The actual output format will show:

# 2-digit year (19)

# Full month name (November)

# 24-hour time format

# Corrected Version (recommended):
# from datetime import datetime
# dt = datetime(2019, 11, 27, 11, 27, 22)  # Better variable name
# print(dt.strftime('%y/%B/%d %H:%M:%S'))  # Same output but cleaner