calls = 0

def count_calls():
    global calls
    calls += 1 

def string_info(string):
    count_calls()
    return (len(string), string.upper(), string.lower())   
    
def is_contains(string, list_to_search):
    count_calls()
    string = string.lower()
    list_to_search = [words.lower() for words in list_to_search]
    return string in list_to_search        

print(string_info('Dudhsagar'))
print(string_info('Tiwanaku'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) 
print(is_contains('parade', ['paradigma', 'separating', 'prepare'])) 
print(calls)