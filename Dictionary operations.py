pythonmarks = {"karan":72, "Ruman":89, "Aman":65}
print(pythonmarks)           #print whole dict
print( pythonmarks.keys() )  #print all keys if dict 
print( pythonmarks.values() ) #print all values of dict
print( pythonmarks['karan'] )  #print value where index is 'karan'
print( pythonmarks.get('karan') ) #print value where index is 'karan' using .get()

pythonmarks['karan'] = 20      # change the value to 30 where key = 'karan'
print(pythonmarks)           #print whole dict

for i in pythonmarks.keys():     #print all data of dictinary using for loop
    print(i, pythonmarks[i])    

pythonmarks["Mayur"] = 77 # adding new pair of key:value
print(pythonmarks)           #print whole dict

pythonmarks_new ={'pooja':23, 'Rahul':100}
print(pythonmarks_new)

pythonmarks.update(pythonmarks_new)  # this is extesion of first dict. with new dict.
print(pythonmarks)
