#!/usr/bin/python3
# -*- coding: utf-8 -*-

###
#nie ma implementacji komend SWAP,ADD,REMOVE,PRINT,LOG LEVEL,LOG CATEGORY,SET,LOCK,
# TemplateInvoke nie przetestowany
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

class CasparTemplateCommands:
    def __init__(self, template_name, channel, cg_layer, play_on_load, **kwargs):  #layer, data
        self._channel = channel
        self._cg_layer = cg_layer
        self._template_name = template_name
        self._play_on_load = play_on_load
        self._variables = kwargs
        
    def get_variable(self, k):
        if k == 'layer':
            return self._variables.get(k, None)
        else:
            return self._variables.get(k,'')
    
    def channel_layer(self):    
        if self.get_variable("layer") == None:
            return str(self._channel)
        else:
            return str(self._channel)+'-'+str(self.get_variable('layer'))
                
    def templateAdd(self, *argsf):
        #f0 = ("tekst_gora", "Tomasz Nowak")
        #f1 = ("tekst_dol", "dyr. IT i techniki TV")
        _listf = []
        for _n in argsf:
            _listf.append(_n)
        return "cg " + str(self.channel_layer()) + " add " + str(self._cg_layer) + " " + self._template_name + " " + str(self._play_on_load) + " " + str(self.templateData(*_listf))
    
    def templateData(self, *args):
        #_f0 = ("tekst_gora", "Tomasz Nowak")
        #_f1 = ("tekst_dol", "dyr. IT i techniki TV")
        #_tempdata = r' "<templateData><componentData id=\"' + _f0[0] + r'\"><data id=\"text\" value=\"' + _f0[1] + r'\"></data> </componentData>' + r'<componentData id=\"' + _f1[0] + r'\"><data id=\"text\" value=\"' + _f1[1] + r'\"></data></componentData>' + r'</templateData>"'
        _tempdata = r' "<templateData>'
        for _n in args:
            _tempdata += r'<componentData id=\"' + _n[0] + r'\"><data id=\"text\" value=\"' + _n[1] + r'\"></data> </componentData>'
        _tempdata += r'</templateData>"'
        return _tempdata
    
    def templatePlay(self):
        return "cg " + str(self.channel_layer()) + " play " + str(self._cg_layer)
        
    def templateStop(self):
        return "cg " + str(self.channel_layer()) + " stop " + str(self._cg_layer)

    def templateNext(self):
        return "cg " + str(self.channel_layer()) + " next " + str(self._cg_layer)

    def templateRemove(self):
        return "cg " + str(self.channel_layer()) + " remove " + str(self._cg_layer)

    def templateClear(self):
        return "cg " + str(self.channel_layer()) + " clear "
    
    def templateUpdate(self, *argsf):
        #f0 = ("tekst_gora", "Tomasz Nowak")
        #f1 = ("tekst_dol", "dyr. IT i techniki TV")
        _listf = []
        for _n in argsf:
            _listf.append(_n)
        return "cg " + str(self.channel_layer()) + " update " + str(self._cg_layer) + " " + str(self.templateData(*_listf))
    
    def templateInvoke(self, _method):
        #f0 = ("tekst_gora", "Tomasz Nowak")
        #f1 = ("tekst_dol", "dyr. IT i techniki TV")
        self.method = _method
        return "cg " + str(self.channel_layer()) + " update " + str(self._cg_layer) + " " + str(self.method)

    def templateInfo(self):
        return "cg " + str(self.channel_layer()) + " info " + str(self._cg_layer)


class CasparMixerCommands:
    def __init__(self, channel, **kwargs):
        self._channel = channel
        self._variables = kwargs
        self._color = ('none', 'green', 'blue')
        
    def get_variable(self, k):
        if k == 'layer':
            return self._variables.get(k, None)
        elif k == 'keyer':
            return ' keyer ' + str(self._variables.get(k, ''))
        elif k == 'chroma':
            return ' chroma ' + str(self._variables.get(k, ''))
        elif k== 'blend':
            return ' blend ' + str(self._variables.get(k,''))
        elif k== 'opacity':
            return ' opacity ' + str(self._variables.get(k,''))
        elif k == 'duration':
            return ' ' + str(self._variables.get(k,''))
        elif k == 'brightness':
            return ' brightness ' + str(self._variables.get(k,''))
        elif k == 'saturation':
            return ' saturation ' + str(self._variables.get(k,''))
        elif k == 'contrast':
            return ' contrast ' + str(self._variables.get(k,''))
        elif k == 'levels':
            return ' levels ' + str(self._variables.get(k,''))
        else:
            return self._variables.get(k,'')
        
    def get_string(self, s):
        if s == 'color' and (self._variables.get(s) in self._color):
            if self._variables.get("spill") == None:
                return self._variables.get(s) + ' ' + str(self._variables.get("threshold")) + ' ' + str(self._variables.get("softness"))
            else:
                return self._variables.get(s) + ' ' + str(self._variables.get("threshold")) + ' ' + str(self._variables.get("softness")) + ' ' + str(self._variables.get("spill"))
        #elif s == 'tween':
        #    return self.get_variable(s) + ' '
        else:
            pass
            
            
    def channel_layer(self):    
        if self.get_variable("layer") == None:
            return str(self._channel)
        else:
            return str(self._channel)+'-'+str(self.get_variable('layer'))
        
    def mixerKeyer(self):
        return "mixer " + str(self.channel_layer()) + str(self.get_variable('keyer'))
    
    def mixerChroma(self):
        return "mixer " + str(self.channel_layer()) + str(self.get_variable('chroma')) + str(self.get_string("color")) #brak tweena!

    def mixerBlend(self):
        return "mixer " + str(self.channel_layer()) + str(self.get_variable('blend'))
    
    def mixerOpacity(self):
        return "mixer " + str(self.channel_layer()) + str(self.get_variable('opacity')) + str(self.get_variable('duration'))#brak tweena!
    
    def mixerBrightness(self):
        return "mixer " + str(self.channel_layer()) + str(self.get_variable('brightness')) + str(self.get_variable('duration'))#brak tweena!
    
    def mixerSaturation(self):
        return "mixer " + str(self.channel_layer()) + str(self.get_variable('saturation')) + str(self.get_variable('duration'))#brak tweena!
    
    def mixerContrast(self):
        return "mixer " + str(self.channel_layer()) + str(self.get_variable('contrast')) + str(self.get_variable('duration'))#brak tweena!
    
    def mixerLevels(self):
        return "mixer " + str(self.channel_layer()) + str(self.get_variable('levels'))##brak parametrów #brak tweena!
#######################################################        
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