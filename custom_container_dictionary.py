class Tags_exem:

    def __init__(self):
        self.tags = {}
    
    def __str__(self):
        return f"({self.tags})"
    
    def add(self,key):
        self.tags[key.lower()] = self.tags.get(key.lower(),0) + 1
    
    def __getitem__(self,key):
        return self.tags.get(key.lower(),'Invalid key !')

    def __setitem__(self,key,count):
        self.tags[key.lower()] = count

    def __len__(self):
        return len(self.tags)

    def __delitem__(self, key):
        tags_del = self.tags.get(key.lower(),0)
        if tags_del != 0:
            del self.tags[key]
        else:
            pass
    
    def __iter__(self):
        return iter(self.tags)
    
    
# instance initializing (empty dictionary)
var = Tags_exem()

# adding new kye - values into the dictionary
var.add("Python")
var.add("Java")
var.add("Python")
var.add("Python")

# access to keys 
var["php5"] = 5

# keys removing 
del var["java"]

# checking the shape instance using __str__ method
print(var)

# checking the length of the instance 
print(len(var))

# iterating over keys
for key in iter(var):
    print(key,var[key])





