#!/usr/bin/env python
# coding: utf-8

# In[1]:


from convert_text_utils import *


# In[2]:


text = "  hello exclamation mark I am saikumar, I cant study twenty four by seven. my income is thirty five thousand rupees it is equal to five hundred dollars. my email is sai at the rate gmail dot com. My contact number is double nine eight nine two triple three zero four. I was so interested in double i t s and triple i t s.";
#text = readfile('sample')
text = text.replace('.'," . ");
text = replace_special_symbols(text);
text = replace_the_tuples1(text);
text = replace_numerical_terms1(text);
text = complete_postprocessing(text);
text = dollar_processing(text)
text = defintion_preprocessing(text)
text = text.replace(' .',".");
print(remove_whitespace(text))


# In[ ]:




