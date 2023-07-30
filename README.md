# python_bulk_string_replace
Given a starting location and two strings -- the substring to find, and the replacement substring -- recursively replaces all substrings with the new substring

## How To Use This Script

The following command will run this program:

```bash
python3 rename.py [-r optional] [substring you want to find] [substring you want to replace it with] [starting location]

# rename all .py file extensions to .sh file extensions
python3 rename.py -r ".py" ".sh" ./
```

Some talking points worth noting:
* This is strictly a name changing script. The rename.py script will not do intense file conversions such as transcoding. (e.g., will not convert a .png to .jpeg)
* Hidden files will have their name changed. I may implement a means of ignoring hidden files in the future, but that's not the case now so do keep this functionality in mind.
* Searching for "." will affect hidden files as well as filenames with multiple "." characters. The current directory `./` will not be affected. 
  For example, if the file `.output.log.old` exists, then running `python3 rename.py . ~ ./` will rename the file to `~output~log~old`.

## Running The Tests

To run the tests, simply use the following command:
```bash
python3 test.py
```

You may notice that `test_directory/` exists in the project root directory. The mask for it is 0700 (`drwx------` if you use `ls -l`). The test file will create two copies of the `test_directory/` directory and use the copies
to test the recursive and non-recursive options.

Note:
* At this time, the tests must be manually verified by running through the directories to see if all instances of CHANGE-ME are renamed to CHANGED. I am debating whether to add a "walk the tree" testing function to test.py or rename.py.
* The easiest way to manually verify is to run `ls -R | grep "CHANGE-ME"`. If grep outputs text, then the output will give the path to the files that were not changed. 
* Due to the requirement to manually verify the results, there is no cleanup functionality to remove the newly created directories that are used for testing.
* Each time the `test.py` script is run, it deletes any existing versions of the test directories and re-create them by copying the `test_directory/` directory.

## What Was The Inspiration For Writing This Script?

Admittedly, I have a large anime collection thanks to yt-dlp and Crunchyroll integration. I noticed all of the colons in the filenames were "full-width colon unicode characters" (：, or U+FF1A). 
I started to manually convert them to colons (:, U+003A) by hand until I realized far too many filenames had the full-width colon character -- and some of the names had multiple full-width colons.
I decided it would be in my best interest to simply write a bulk renaming script -- one with some degree of customizability -- that I can also use for future use.
