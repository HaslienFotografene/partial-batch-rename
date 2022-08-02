# Partial Batch Rename
Rename a part of the filename, for many files at once, where name matches a pattern.  

Useful when you a serie of files with a specific name pattern, but you want to replace one constant of the name.

## Example
You have a customer folder with images. Images of the customer follows a specific naming pattern:  
[customer ID]_[sequential number]_[year and month].[cr2|xmp|jpg]
Then later you realize the customer ID or date is wrong, but you can't use any other batch rename, like the one built-in to Adobe Bridge.  
With this program you can replace one constant, while the rest remains untouched.  

`1234_001_2022.cr2` becomes `1235_001_2022.cr2`  
`1234_001_2022.xmp` becomes `1235_001_2022.xmp`  
`1234_002_2022.cr2` becomes `1235_002_2022.cr2`  
`1234_002_2022.xmp` becomes `1235_002_2022.xmp`  
`.thumbsdb` remains untouched.  
`1234_2022.jpg` remains untouched.  
... and so on.  

## Usage
The code reads a folder (not recursively) and starts renaming all files. If file does not match name, it skips the file.  
There are 3–4 variables you need to change in the file:
* `path` is the source folder where files resides
* `pattern` is a RegExp that should determine if you want to try to rename the file or not.
* `replace` is the old string you want to target for replacement
* `replace_with` is the new string you want to change it to

Once changed, you can run the program, and it will update you on the process.
