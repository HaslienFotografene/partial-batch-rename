# Rename a part of a bunch of files all at once.
# 
# Used for when part of their name is wrong and 
# needs to be changed, but we need to retain the 
# other parts of it.

import os, re

# File path to files. Can be local or a server path.
# Examples:
# '\\\\myserver\\customers\\1234\\images'
# 'C:/Users/Me/Images/vacation'
path = '\\\\myserver\\customers\\1234\\images'

# A regex pattern to match with file name.
# If the file matches this pattern, it is eligible for renaming.
pattern = '^\d+_\d+_\d+.*$' # In this case, it matches. '1234_001_2022.jpg' and '1234_002_2022.cr2' and any other extensions.

# This is the part we will replace:
replace = r"1234"
# This is what we will change it to:
replace_with = "1235"

# ???
comp = re.compile(pattern)
for f in os.listdir(path):
    # Store full path
    full_path = os.path.join(path, f)

    # If file
    if os.path.isfile(full_path):
        match = comp.search(f)

        # Matches initial regex
        if not match:
            continue

        # Execute regex replace to create file name, and its full path
        try:
            new_name = re.sub(replace, replace_with, f)
            new_name = os.path.join(path, new_name)
        except re.error:
            continue

        # If filename already exist, skip it
        if os.path.isfile(new_name):
            print('%s -> %s skipped' % (f, new_name))
        else:
            # Rename the file
            os.rename(full_path, new_name)
