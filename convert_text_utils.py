### All required functions for given specifications are implemented in this code and it is feasible to add/update any new specs in future ###




from word2number import w2n
import re


def readfile(filename):
  """
  reads the input text file and returns as a string to process further 
  """
  file = open(filename, 'r')
  data = file.read()
  data = data.replace("\n","")
  file.close()
  return data




def remove_whitespace(text):
    """ removes all white spaces """
    return  " ".join(text.split())




def get_special_symbol_dictionary():
  """
  returns the dictionary used for replacing the special symbols
  """
  special_symobl_txt = readfile('special_symbol.txt')
  special_symobl_list = special_symobl_txt.split(";")
  
  if('' in special_symobl_list):
    special_symobl_list.remove('')
  if(' ' in special_symobl_list):
    special_symobl_list.remove(' ')
  
  #print(special_symobl_list)
  #print(len(special_symobl_list))

  special_symbol_dict = {}
  for i in special_symobl_list:
      value_key = i.split(",")
      special_symbol_dict[value_key[1].lower()] = value_key[0]
  
  
  special_symbol_dict['comma'] = ","
  special_symbol_dict['semi colon'] = ";" # adding , and ; here because they are used as delimeters for string seperation in txt file

  return special_symbol_dict





def replace_special_symbols(text):
  """
  replaces the word with the appropriate special symbol
  """

  special_symbol_dictionary = get_special_symbol_dictionary() #uses special symbol dict to replace the word with symbol
  special_symbols = special_symbol_dictionary.keys()
  for i in special_symbols:
    text = text.replace(i,special_symbol_dictionary[i])
  return text;





def get_numerical_terms_list():
  """
  returns the list for identifying the words as numerals  
  """
  numerical_terms_txt = readfile('numerical_terms.txt')
  numerical_terms_txt = numerical_terms_txt.replace("\n","")
  numerical_terms_txt = numerical_terms_txt.lower();
  numerical_terms_list = numerical_terms_txt.split(",")
  if('' in numerical_terms_list):
    numerical_terms_list.remove('')
  if(' ' in numerical_terms_list):
    numerical_terms_list.remove(' ')
  return numerical_terms_list

#print(get_numerical_terms_list())






def get_numerical_type_dictionary():
  
  """
    returns the dict for diffenertiate the types of numericals. i.e., digits(e.g. nine), non digit but numerical(e.g. fifty)
  """
  file_data = readfile('digits_nondigits.txt')
  full_list = file_data.split(',')
  num_type_dictionary = {"D":full_list[0:10],"N_ND":full_list[10:32],'ALPHA':full_list[32:]}
  return num_type_dictionary





def get_type(term):
  """
  returns the type of the word
  returns 'D' if it is digit, returns 'N_ND' if it is non digit but numerical, returns 'others' if it is not digit and not numerical
  """
  type_dictionary = get_numerical_type_dictionary()
  types = type_dictionary.keys()
  for i in types:
    if(term in type_dictionary[i]):
      return i
  return 'others'




def replace_numerical_terms1(text):
    """
    replaces the numerical terms by its value
    """
    numerical_terms_list = get_numerical_terms_list()
    individual_terms_list = text.split(' ')
    digit_terms_replace = []
    ndigit_terms_replace = []
    
    if('' in individual_terms_list):
      individual_terms_list.remove('')  # for pre processing

    #print(individual_terms_list)

    numerical_text = ""
    length = 0
    index = 0
    present_term=individual_terms_list[index]
    list_length=len(individual_terms_list)
    present_type="others"
    
    while(index < list_length-1):

      present_term = individual_terms_list[index]
      present_type = get_type(individual_terms_list[index])  
      next_term = individual_terms_list[index+1]
      next_type = get_type(individual_terms_list[index+1])

      #print(present_term,next_term)
      #print(present_type,next_type)
      #print("length is ",length);
      
      if(present_type == 'D' and next_type == 'N_ND'):
        #print("case0")
        if(length == 0):
          numerical_text=present_term
          length = 1
        elif(length>0):
          numerical_text = numerical_text+" "+present_term
          length = length+1
      elif(present_type == 'N_ND' and next_type == 'D'):
        #print("case1")
        if(length == 0):
          numerical_text = present_term
          length = 1
        elif(length>0):
          numerical_text = numerical_text+" "+present_term
          length = length+1;
      elif(present_type == 'N_ND' and next_type == 'N_ND'):
        #print("case2")
        if(length == 0):
          numerical_text = present_term
          length = 1
        elif(length > 0):
          numerical_text = numerical_text+" "+present_term
          length = length+1

      elif(present_type == 'D' and next_type == 'D'):#this is end of the present number
        #print("case3")
        if(length == 0):
          numerical_text = present_term
          #print(numerical_text)  
          digit_terms_replace.append(numerical_text)
          numerical_text = ""
        elif(length > 0):
          numerical_text = numerical_text+" "+present_term
          #print(numerical_text)      
          ndigit_terms_replace.append(numerical_text)
          numerical_text = ""
          length = 0

      elif(present_type == 'D' and next_type == 'others'): #this is end of the present number 
        #print("case4")
        if(length == 0):
          numerical_text = present_term
          #print(numerical_text)     
          digit_terms_replace.append(numerical_text)
          numerical_text = ""
        elif(length>0):
          numerical_text = numerical_text+" "+present_term
          #print(numerical_text)      
          ndigit_terms_replace.append(numerical_text)
          numerical_text = ""
          length = 0


      elif(present_type == 'N_ND' and next_type == 'others'):#this is end of the present number
        #print("case5")
        if(length == 0):
          numerical_text=present_term
          #print(numerical_text)
          digit_terms_replace.append(numerical_text)
          numerical_text = ""
        elif(length>0):
          numerical_text = numerical_text+" "+present_term
          #print(numerical_text)      
          ndigit_terms_replace.append(numerical_text)
          numerical_text = ""
          length = 0


      index = index+1
      #print(index) 

    #print(digit_terms_replace)  #this list consisting of the strings which need to replace in numerical form.
    #print(ndigit_terms_replace)

    digits = {'zero':0,'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9}
    for i in ndigit_terms_replace:
        numerical_value = w2n.word_to_num(remove_whitespace(i))
        text = text.replace(i,str(numerical_value))
        
    for i in digit_terms_replace:
      if(get_type(i) == 'D'):
        text = text.replace(i,str(digits[i]))
      else:
        numerical_value = w2n.word_to_num(remove_whitespace(i))
        text = text.replace(i,str(numerical_value))

    #print(text) 
    return text



def defintion_preprocessing(text):
  """
  single letter processing
  """
  terms = text.split()
  #print(terms)
  process_text = terms[0]+" "
  i = 1
  while(i<len(terms)):
    #print(i)
    if(terms[i] != '.'):
        if(get_type(terms[i]) == 'ALPHA' and get_type(terms[i+1]) == 'ALPHA'):
          process_text = process_text + terms[i]
        else:
          process_text = process_text + terms[i] + " "
    else:
      process_text = process_text+terms[i] + " "
    i = i+1
  #print(process_text)
  return process_text






def get_tuple_dictionary():
  """
  this function holds the tuple name as a key and its value as value (e.g. double  = 2), returns the size of the tuple
  """
  tuple_terms_txt = readfile('tuple.txt').lower()
  #print(tuple_terms_txt)
  tuple_list = tuple_terms_txt.split(";")
  #print(tuple_list)
  #print(len(tuple_list))
  tuple_value_dict = {}
  for i in tuple_list:
    value_key = i.split(",")
    tuple_value_dict[value_key[1]] = int(value_key[0])
  #print(tuple_value_dict)
  return tuple_value_dict


def replace_the_tuples1(text):
  text = remove_whitespace(text)
  tuple_dictionary = get_tuple_dictionary() #accessing the tuple dictionary  
  tuple_list = tuple_dictionary.keys() # get all the list of tuple names
  #print(tuple_list)
  individual_terms = text.split(" ")
  #print(individual_terms)
  numerical_terms_list = get_numerical_terms_list()

  i = 0
  #print(numerical_terms_list)
  while(i < len(individual_terms)):
      if(individual_terms[i] in tuple_list):#it is checking given term is part of tuple or not
        #print(individual_terms[i])
        #print(get_type(individual_terms[i+1]))
        if(get_type(individual_terms[i+1]) == 'D'): #if it prev is tuple and next is digit, it need to replace with its multiplied  value.like double nine with 99.
          #print("yes",individual_terms[i],individual_terms[i+1])
          multiple_value = tuple_dictionary[individual_terms[i]]#it returns the numerical value .
          multliplied_value = (multiple_value-1)*(individual_terms[i+1]+" ")
          text = text.replace(individual_terms[i],multliplied_value,1);
          #print(multliplied_value)
        if(get_type(individual_terms[i+1]) == 'ALPHA'):#if it previous is tuple and next term is alphabet then it need to replace with its multiplied value.like triple A with AAA
          #print("yes",individual_terms[i],individual_terms[i+1])
          multiple_value = tuple_dictionary[individual_terms[i]]
          multliplied_value = (multiple_value-1)*(individual_terms[i+1]+" ")
          #print("this is appended",multliplied_value)
          text = text.replace(individual_terms[i],multliplied_value,1)
          #print(multliplied_value)  
      i = i+1
  text = remove_whitespace(text)
  #print("hello",text)
  return text





def complete_postprocessing(text):
  """
  removes the gap between numbers, and do other post processing.
  """
  terms_list = text.split()
  digits=['0','1','2','3','4','5','6','7','8','9']
  i = 1
  result = terms_list[0] + " "

  while(i < len(terms_list)-2):
    #print(i,terms_list[i])
    if(terms_list[i] in digits and terms_list[i+1] in digits):
      result = result + terms_list[i]
      i = i+1
    elif(terms_list[i] in digits and terms_list[i+1]=='point' and terms_list[i+2] in digits):
      result = result+" "+terms_list[i]+"."+terms_list[i+2]
      i = i+3
    else:
      result=result+terms_list[i]+" "
      i = i+1

  if(i == (len(terms_list)-1)):
    if(terms_list[i-1] in digits and terms_list[i] in digits):
      result = result + terms_list[i]
    else:
      result = result +" "+ terms_list[i]

  if(i == (len(terms_list)-2)):
    #print("second case")
    if(terms_list[i-1] in digits and terms_list[i] in digits):
      result = result+terms_list[i]
    else:
      result = result+" "+terms_list[i]
    i = i+1  
    if(terms_list[i-1] in digits and terms_list[i] in digits):
      result = result+terms_list[i]
    else:
      result = result + " " + terms_list[i]
       
  #print(result)
  return result





def dollar_processing(text):
  """
  puts the currency in front of the figure by swaping the symbol and amount.
  """
  text = text.replace('$',' $ ')
  text = text.replace('₹',' ₹ ')
  text = remove_whitespace(text)
  terms = text.split()
  #print(terms)

  i = 0
  while(i<len(terms)):
    if(terms[i] == '$'):
      if(terms[i-1].isnumeric()):
        terms[i-1] = "$"+ terms[i-1]
        terms.pop(i)
    if(terms[i] == '₹'):
      if(terms[i-1].isnumeric()):
        terms[i-1] = "₹" + terms[i-1]
        terms.pop(i)

    i=i+1
  #print(terms)  
  result = ""
  for i in terms:
    result = result + " " + i
  return result










