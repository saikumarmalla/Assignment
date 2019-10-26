# Text Conversion
Converts spoken english (usually text transcript of a speech recognition system) into written english. 

### Motivation
Developed as part of the recruitment procedure held by Aganitha cognitive solutions.

### Built with
*  [Python 3.6](https://www.python.org/downloads/release/python-360/) - Programming Language
* [Jupyter notebook](https://jupyter.org/) - OPen source web-app for creating and sharing the code


### Features implemented

This is the initial phase of developement, the following features are implemented and many other features will be added in future.

1. Converts the words by replacing with the corresponding special symbols. e.g. 'exclamation mark' as '!', 'question mark' as '?' and many more.

2. Converts all the words that represents digits and numbers into corresponding values excluding space between them. e.g. 'five hundred thirty' as '530'.

3. Converts all the tuple terms followed by numbers/digits by repeating the number/digit that many times. e.g. 'double three'  as '33' and 'triple a' as 'aaa'.  

4. All the currency symbols are added as prefix to the figure. e.g. 'five dollars' can be written as '$5','six rupees' as '₹6'.


### Features yet to be implemented

1. We can include the feature maps(dicts or text files) for all the mathematical operations and formulas.

2. All abbreviations can be replaced with thier meaning.

### Test cases 
Example text : 
```
My email id is sai triple nine double a at the rate gmail dot com comma my income is fifteen hundred dollars.

```
Output :
```
My email id is sai 999 aa @ gmail.com, my income is $1500.
```

### Usage
#### Files
##### convert_text_utils.py
The functions impelemnted in this file are perfoming all utility functions ranging from pre processing of the text and convert the text into desired format.
##### convert_text.ipynb
The driver function for taking the input text and gives the converted text.
##### other files 
Remaining files contain the features that used to map with the text. 





