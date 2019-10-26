# Text Conversion
Converts spoken english (usually text transcript of a speech recognition system) into written english. 

### Motivation
Developed as part of the recruitment procedure held by Aganitha cognitive solutions.

### Built with
All the implentations were carried out in [Python 3.6](https://www.python.org/downloads/release/python-360/) with the  [Jupyter notebook](https://jupyter.org/) on my local computer.

### Features implemented

This is the initial phase of developement, the following features are implemented and many other features will be added in future.

1. Converts the words by replacing with the corresponding special symbols. e.g. 'exclamation mark' as '!', 'question mark' as '?' and many more.

2. Converts all the words that represents digits and numbers into corresponding values excluding space between them. e.g. 'five hundred thirty' as '530'.

3. Converts all the tuple terms followed by numbers/digits by repeating the number/digit that many times. e.g. 'double three'  as '33' and 'triple a' as 'aaa'.  

4. All the currency symbols are added as prefix to the figure. e.g. 'five dollars' can be written as '$5','six rupees' as '₹6'.


### Features yet to be implemented

1. We can include the feature maps(dicts or text files) for all the mathematical operations and formulas.

2. All abbreviations can be replaced with thier meaning.

#### Test cases 
Example text : 
```
My email id is sai triple nine double a at the rate gmail dot com comma my income is fifteen hundred dollars.

```
Output :
```
My email id is sai 999 aa @ gmail.com, my income is $1500.

```


## Authors

[Saikumar Malla](https://github.com/saikumarmalla)

