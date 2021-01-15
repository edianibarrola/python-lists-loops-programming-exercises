people = ['juan','ana','michelle','daniella','stefany','lucy','barak','emilio']

#Your code go here:

def deletePerson(person_name):
    #Your code go here:
    
    newlist= people  
    for person in people:
        
        if person_name == person:
            people.remove(person)
            return newlist
            
            
        
            
        
            
print(deletePerson("daniella"))
print(deletePerson("juan"))
print(deletePerson("emilio"))