# -*- coding: utf-8 -*-

###
#nie ma implementacji komend SWAP,ADD,REMOVE,PRINT,LOG LEVEL,LOG CATEGORY,SET,LOCK,
###
import sys

class CasparBasicCommands_old:
    def __init__(self):
        pass
    
    def loadbg(self):
        pass
    
    def laod(self):
        pass
    
    def play(self, _filename,  _channel, _layer = None):
        if _layer == None:
            return 'play ' + str(_channel) + ' ' + _filename
            #return self.get_function_name() +' ' + str(_channel) + ' ' + _filename
        else:
            #return self.get_function_name() +' ' + str(_channel) + '-' + str(_layer) + ' ' + _filename
            return 'play ' + str(_channel) + '-' + str(_layer) + ' ' + _filename
        
class CasparBasicCommands:
    def __init__(self, filename,  channel, **kwargs):  
        self.variables = kwargs
        self._filename =filename
        self._channel = channel
        
        
    def set_variable(self, k, v):
        self.variables[k] = v
        
    def get_variable(self, k):
        if k == 'layer':
            return self.variables.get(k, None)
        else:
            return self.variables.get(k,'')
        
    def simple_set_commands(self):
        if self.get_variable('layer') ==None:
            _command_build = str(self._channel)
        else:
            _command_build = str(self._channel)+'-'+str(self.get_variable('layer'))
        return _command_build

    def set_commands(self):
        if self.get_variable('layer') ==None:
            _command_build = str(self._channel)
            for k in self.variables:
                _command_build += ' ' + str(self.get_variable(k))
        else:
            _command_build = str(self._channel)+'-'+str(self.get_variable('layer'))
            for k in self.variables:
                if k == 'layer':
                    _command_build += ''
                else:
                    _command_build += ' '+ str(self.get_variable(k))
        return _command_build                    
    
    def set_all_commands(self):
        if self.get_variable('layer') ==None:
            _command_build = str(self._channel) + ' ' + self._filename
            for k in self.variables:
                _command_build += ' ' + str(self.get_variable(k))
        else:
            _command_build = str(self._channel)+'-'+str(self.get_variable('layer'))+' '+self._filename
            for k in self.variables:
                if k == 'layer':
                    _command_build += ''
                else:
                    _command_build += ' ' + str(self.get_variable(k))
        return _command_build
        #print(_command_build)
    
    def play(self):
        return 'play ' + self.set_all_commands()
    
    def load(self):
        return 'load ' + self.set_all_commands()
    
    def loadbg(self):
        return 'loadbg ' + self.set_all_commands()
    
    def pause(self):
        return 'pause ' + self.simple_set_commands()
  
    def resume(self):
        return 'resume ' + self.simple_set_commands()

    def stop(self):
        return 'stop ' + self.simple_set_commands()
        
    def clear(self):
        return 'clear ' + self.simple_set_commands() 

    def call(self):
        return 'call ' + self.set_commands()
    
class CasparDataCommands:
    def __init__(self, data_name = None, data_string = None):
        if data_name != None:
            self._data_name = data_name.replace(" ", "_")
        else:
            self._data_name = None
        self._data_string = data_string
        
    def data_store(self):
        if self._data_name == None or self._data_string == None:
            pass
            #return "No data to store"
        else:
            return "data store " + self._data_name + " " + self._data_string
 
    def data_retrieve(self):
        if self._data_name == None:
            pass
        else:
            return "data retrieve " + self._data_name

    def data_list(self):
        return "data list"
    
    def data_remove(self):
        if self._data_name == None:
            pass
        else:
            return "data remove " + self._data_name


        
class Caspar2:
    def __init__(self):
        pass
    
    def command(self, _filename,  _channel, _layer = None):
        if _layer == None:
            #return 'play ' + str(_channel) + ' ' + _filename
            return self.get_function_name() +' ' + str(_channel) + ' ' + _filename
        else:
            return self.get_function_name() +' ' + str(_channel) + '-' + str(_layer) + ' ' + _filename
        
    def get_function_name(self):
        # for current func name, specify 0 or no argument.
        # for name of caller of current func, specify 1.
        # for name of caller of caller of current func, specify 2. etc.
        return sys._getframe(1).f_code.co_name