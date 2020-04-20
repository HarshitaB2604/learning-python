class ContactBook:
    """
    This class represents a book of contacts.
    It can store names and phone numbers.
    """
    
    def __init__(self):
        # Create an empty dictionary
        self.contacts = {}
	
    def __repr__(self):
        # Just print a string version of the dictionary
	    return str(self.contacts)
	
    #combine two contact books, if there is a name in both books, both
    #number will be saved seperated by or
    def __add__(self, other):
        cb = ContactBook()
		
        for key1 in self.contacts:
            #print(key1 + " -> " + self.contacts[key1])
            cb.add_contact(key1, self.contacts[key1])
		    
        
        for key2 in other.contacts:
            if(key2 in cb.contacts):
                cb.contacts[key2] = cb.contacts[key2] + " or " + other.contacts[key2]
            else:
                cb.add_contact(key2, other.contacts[key2])
                    
        return cb
		
	
    def add_contact(self, name, number):
        # Adds a name --> phone number pair to
        # the dictionary.
        self.contacts[name] = number

#############################
# Program starts here

cb1 = ContactBook()
cb2 = ContactBook()

cb1.add_contact("Jonathan", "444-555-6666")
cb1.add_contact("Puneet", "333-555-7777")
cb2.add_contact("Jonathan", "222-555-8888")
cb2.add_contact("Lisa", "111-555-9999")

print (cb1)
print (cb2)

cb3 = cb1 + cb2
print(cb3)
