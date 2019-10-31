# Text Conversion
Converts spoken english (usually text transcript of a speech recognition system) into written english. 

### Built with
*  [Python 3.6](https://www.python.org/downloads/release/python-360/) - Programming Language
* [Jupyter notebook](https://jupyter.org/) - Open source web-app for creating and sharing the code


### Features implemented

This is the initial phase of developement, the following features are implemented and many other features will be added in future.

1. Converts the words by replacing with the corresponding special symbols. e.g. 'exclamation mark' as '!', 'question mark' as '?' and many more.

2. Converts all the words that represents digits and numbers into corresponding values excluding space between them. e.g. 'five hundred thirty' as '530'.

3. Converts all the tuple terms followed by numbers/digits by repeating the number/digit that many times. e.g. 'double three'  as '33' and 'triple a' as 'aaa'.  

4. All the currency symbols are added as prefix to the figure. e.g. 'five dollars' can be written as '$5','six rupees' as '₹6'.


### Features yet to be implemented

1. We can include the feature maps(dicts or text files) for all the mathematical operations and formulas.

2. Abbreviations can be replaced with thier meaning.

### Test cases 
Example text : 
```
Hello exclamation mark I am saikumar, I wont study twenty four by seven. my income is thirty five thousand rupees it is equal to five hundred dollars. my email is sai at the rate gmail dot com. My contact number is double nine eight nine two triple three zero four. I was interested in double i t s and triple i t s.

```
Output :
```
Hello ! I am saikumar, I wont study 24 / 7. my income is ₹35000 it is equal to $500. my email is sai @ gmail. com. My contact number is 9989233304. I was interested in iits and iiits.
```

### Usage
#### Files
##### convert_text_utils.py
The functions impelemnted in this file are perfoming all utility functions ranging from pre processing of the text and convert the text into desired format.
##### convert_text.ipynb
The driver function for taking the input text and gives the converted text.
##### other files 
Remaining files contain the features that are used to map with the text. 





