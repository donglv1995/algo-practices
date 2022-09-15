def check_balanced_brackets(str):
    while True:  
       if '()' in str :  
           str = str.replace ( '()' , '' )  
       elif '{}' in str :  
           str = str.replace ( '{}' , '' )  
       elif '[]' in str :  
           str = str.replace ( '[]' , '' )  
       else :  
           return not str 

def check_balanced(str):
    count = 0

    for i in str:
        if i == '(' or i == '{' or i == '[':
            count += 1
        elif i == ')' or i == '}' or i == ']':
            count -1
        
        if count < 0: return False
    
    if count == 0: return True

    return False

# True
print(check_balanced_brackets("[()]{}{[()()]()}"))