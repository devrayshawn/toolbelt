""" 
    Enable the developer/programmer/coder to do multiple things using one class.
    They are basic methods but, can be very useful when trying to maintain clean code.
    Easy to understand and simple to use.
"""

from unique import __unique__

class helper(metaclass=__unique__):
    """ contains methods for getting, holding, changing or even executing data. """
    
    
    def __init__(self, object):
        self.object = object

    
    def info(self):
        ''' shows basic information about the object.
            returns a dictionary holding the information.
        '''
        
        print("\nitem: {},\nid/mem_addr: {},\ntype: {},\ncallable: {}\n".format(str(self.object), id(self.object), type(self.object).__name__, callable(self.object)))
            
        print("<< more info >>:\n\n{}".format(self.object.__doc__))
            
        return {'item': self.object, 'id': id(self.object), 'type': type(self.object).__name__,
                'callable': callable(self.object), 'more_info': (self.object.__doc__)}
    
    
    def copy(self):
        ''' returns a copy of the given object. '''
        
        return self.object
    
    
    def grab(self):
        ''' returns a dictionary with the objects type name as key
            and the object itself as the value.
        '''
        
        return {str(type(self.object).__name__): self.object}
    
    
    def execute(self, *args, **kwargs):
        ''' executes a function/method/class with or without parameters.
            *** TO EXECUTE WITH PARAMETERS, SUCH PARAMETERS MUST BE PROVIDED ***
            returns the executed object.
        '''
        
        if callable(self.object):
                
            try:
                return self.object(args, kwargs)
                
            except TypeError:
                return self.object()
            
            else:
                
                try:
                    return self.object(args)
                
                except TypeError:
                    return self.object(kwargs)
                
    
    
    def replace(self, old=None, new=None):
        ''' replaces an old value with a new one.
            returns a new object.
        '''
        
        if type(self.object).__name__ == 'dict':
            
            if old is not None and new is not None:
              
                for k, v in self.object.items():
                    if k == old:
                        k = new
                        self.object[k] = v
                    
                    elif v == old:
                        v = new
                        self.object[k] = v
                
                return self.object
            
            elif old is not None and new is None:
                
                for k, v in self.object.items():
                    if k == old:
                        self.object[k] = v
                    
                    elif v == old:
                        self.object[k] = v
                
                return self.object
            
            elif old is None and new is not None:
                new = {str(new): new}
                
                self.object.update(new)
                
                return self.object
            
            elif old is None and new is None:
                ReplacementError = Exception("Nothing to replace.")
                
                raise ReplacementError
        
        
        elif type(self.object).__name__ == 'list':
            
            if old is not None and new is not None:
                pos = 0
                
                for item in self.object:
                    pos += 1
                    
                    if item == old:
                        self.object[pos-1] = new
                
                return self.object
                    
            elif old is None and new is not None:
                
                self.object.insert(0, new)
                
                return self.object
            
            elif old is not None and new is None:
                
                pos = 0
                
                for item in self.object:
                    pos += 1
                    
                    if item == old:
                        self.object[pos-1] = old
                
                return self.object
            
            elif old is None and new is None:
                ReplacementError = Exception("Nothing to replace.")
                
                raise ReplacementError
        
        elif type(self.object).__name__ == 'tuple':
            
            data = []
            
            if old is not None and new is not None:
                
                pos = 0
                
                if old in self.object:
                    for item in self.object:
                        
                        data.append(item)
                    
                    for item in data:
                        pos += 1
                        
                        if item == old:
                            data[pos-1] = new
                    
                    data = tuple(data)
                    self.object = data
                
                return self.object
            
            elif old is None and new is not None:
                
                data = []
                
                for item in self.object:
                    
                    data.append(item)
                
                data.append(new)
                data = tuple(data)
                
                self.object = data
                
                return self.object
            
            elif old is not None and new is None:
                
                data = []
                
                for item in self.object:
                    
                    if old == item:
                        data.append(item)
                    
                    data.append(item)
                    data = tuple(data)
                    
                    self.object = data
                    
                return self.object
            
            elif old is None and new is None:
                ReplacementError = Exception("Nothing to replace.")
                
                raise ReplacementError
        
        if type(self.object).__name__ == 'set':
            
            if old is not None and new is not None:
                
                for item in self.object:
                    
                    if item == old:
                        self.object.remove(item)
                        break

                    self.object.add(item)
                self.object.add(new)
            
                return self.object
            
            elif old is None and new is not None:
                
                self.object.add(new)
                
                return self.object
            
            elif old is not None and new is None:
                
                for item in self.object:
                    
                    if old == item:
                        self.object = self.object
                
                return self.object
            
            elif old is None and new is None:
                ReplacementError = Exception("Nothing to replace.")
                
                raise ReplacementError
        
        while type(self.object).__name__ not in ['list', 'tuple', 'dict', 'set']:
            
            if old is not None and new is not None:
                
                copy = self.object
                
                if copy == old:
                    self.object = new
                
                else:
                    raise NameError("{} not found.".format(old))
                
                return self.object
            
            elif old is None and new is not None:
                
                self.object = new
                
                return self.object
            
            elif old is not None and new is None:
                
                copy = self.object
                
                if copy == old:
                    self.object = old
                
                else:
                    raise AttributeError("'old' parameter is set and attempting to create a new object. Set the 'new' parameter.")
                
                return self.object


if __name__ == '__main__':
    _helper = helper('name')
    print(_helper.info())
    print(_helper.copy())
    print(_helper.grab())
    print(_helper.replace('name', int))
    #_helper.execute()
    print(_helper.__dict__)
