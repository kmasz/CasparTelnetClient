#!/usr/bin/python3
# -*- coding: utf-8 -*-

###
#nie ma implementacji komend SWAP,ADD,REMOVE,PRINT,LOG LEVEL,LOG CATEGORY,SET,LOCK,
# TemplateInvoke nie przetestowany
###
import sys
#from _ast import Str

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
        return 'loadbg ' + self.set_all_commands()#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    
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
        self._value = ('duration','min_input','max_input','max_output','min_output','gamma','x','y','x_scale','y_scale','width','height','left_edge','right_edge','top_edge','bottom_edge','angle','top_left_x','top_left_y','top_right_x','top_right_y','bottom_right_x','bottom_right_y','bottom_left_x','bottom_left_y')
    
    def get_variable(self,k):    
        if k == 'layer':
            return self._variables.get(k, None)
        elif self._value.__contains__(k):
            return ' ' + str(self._variables.get(k,''))
        else:# self._variables.__contains__(k):
            return ' ' + k + ' ' + str(self._variables.get(k,''))
    
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
        return "mixer " + str(self.channel_layer()) + str(self.get_variable('keyer')) #brak DEFER!!
    
    def mixerChroma(self):
        return "mixer " + str(self.channel_layer()) + str(self.get_variable('chroma')) + str(self.get_string("color")) #brak tweena! #brak DEFER!!

    def mixerBlend(self):
        return "mixer " + str(self.channel_layer()) + str(self.get_variable('blend')) #brak DEFER!!
    
    def mixerOpacity(self):
        return "mixer " + str(self.channel_layer()) + str(self.get_variable('opacity')) + str(self.get_variable('duration'))#brak tweena! #brak DEFER!!
    
    def mixerBrightness(self):
        return "mixer " + str(self.channel_layer()) + str(self.get_variable('brightness')) + str(self.get_variable('duration'))#brak tweena! #brak DEFER!!
    
    def mixerSaturation(self):
        return "mixer " + str(self.channel_layer()) + str(self.get_variable('saturation')) + str(self.get_variable('duration'))#brak tweena! #brak DEFER!!
    
    def mixerContrast(self):
        return "mixer " + str(self.channel_layer()) + str(self.get_variable('contrast')) + str(self.get_variable('duration'))#brak tweena! #brak DEFER!!
    
    def mixerLevels(self):
        return "mixer " + str(self.channel_layer()) + str(self.get_variable('levels')) + str(self.get_variable('min_input')) + str(self.get_variable('max_input')) + str(self.get_variable('gamma')) + str(self.get_variable('min_output')) + str(self.get_variable('max_output')) + str(self.get_variable('duration'))#brak tweena! #brak DEFER!!
    
    def mixerFill(self):
        return "mixer " +str(self.channel_layer()) + str(self.get_variable('fill')) + str(self.get_variable('x')) + str(self.get_variable('y')) + str(self.get_variable('x_scale')) + str(self.get_variable('y_scale')) + str(self.get_variable('duration'))#brak tweena! #brak DEFER!!
    
    def mixerClip(self):
        return "mixer " + str(self.channel_layer()) + str(self.get_variable('clip')) + str(self.get_variable('x')) + str(self.get_variable('y')) + str(self.get_variable('width')) + str(self.get_variable('height')) + str(self.get_variable('duration'))#brak tweena! #brak DEFER!!
    
    def mixerAnchor(self):
        return "mixer " + str(self.channel_layer()) + str(self.get_variable('anchor')) + str(self.get_variable('x')) + str(self.get_variable('y')) + str(self.get_variable('duration')) #brak tweena! #brak DEFER!!
    
    def mixerCrop(self):
        return "mixer " + str(self.channel_layer()) + str(self.get_variable('crop')) + str(self.get_variable('left_edge')) + str(self.get_variable('top_edge')) + str(self.get_variable('right_edge')) + str(self.get_variable('bottom_edge')) + str(self.get_variable('duration')) #brak tweena! #brak DEFER!!
    
    def mixerRotation(self):
        return "mixer " + str(self.channel_layer()) + str(self.get_variable('rotation')) + str(self.get_variable('angle')) + str(self.get_variable('duration')) #brak tweena! #brak DEFER!!
    
    def mixerPerspective(self):
        return "mixer " + str(self.channel_layer()) + str(self.get_variable('perspective'))  + str(self.get_variable('top_left_x')) + str(self.get_variable('top_left_y')) + str(self.get_variable('top_right_x')) + str(self.get_variable('top_right_y')) + str(self.get_variable('bottom_right_x')) + str(self.get_variable('bottom_right_y')) + str(self.get_variable('bottom_left_x')) + str(self.get_variable('bottom_left_y')) + str(self.get_variable('duration')) #brak tweena! #brak DEFER!!
    
    def mixerMipmap(self):
        return "mixer " +str(self.channel_layer()) + str(self.get_variable('mipmap'))#brak DEFER!!
    
    def mixerVolume(self):
        return "mixer "+ str(self.channel_layer()) + str(self.get_variable('volume'))  + str(self.get_variable('duration'))#brak tweena! #brak DEFER!!
    
    def mixerMastervolume(self):
        return "mixer " + str(self.channel_layer()) + str(self.get_variable('mastervolume'))#brak DEFER!!
    
    def mixerStraight_alpha_output(self):
        return "mixer " + str(self.channel_layer()) + str(self.get_variable('straight_alpha_output'))#brak DEFER!!
    
    def mixerGrid(self):
        return "mixer " + str(self.channel_layer()) + str(self.get_variable('grid')) + str(self.get_variable('duration')) #brak tweena! #brak DEFER!!
    
    def mixerCommit(self):
        return "mixer " + str(self.channel_layer()) + ' commit'
    
    def mixerClear(self):
        return "mixer " + str(self.channel_layer()) + ' clear'
    
    def mixerChannelgrid(self):
        return "channel_grid"
    
class CasparThumbnailsCommands:
    def __init__(self,string_name = None):
        self._string_name = string_name
        
    def optional_arg(self):
        if self._string_name == None:
            return ""
        else:
            return self._string_name
        
    def thumbnail_list(self):
        return "thumbnail list " + str(self.optional_arg())
    
    def thumbnail_retrieve(self):
        return "thumbnail retrieve " + str(self.optional_arg())
    
    def thumbnail_generate(self):
        return "thumbnail generate " + str(self.optional_arg())
    
    def thumbnail_generate_all(self):
        return "thumbnail generate_all"
    
class CasparQueryCommands:
    def __init__(self,string_name = None):
        self._string_name = string_name
        
    def optional_arg(self):
        if self._string_name == None:
            return ""
        else:
            return self._string_name
    
    def cinf(self):
        return "cinf " + str(self.optional_arg())
    
    def cls(self):
        return "cls " + str(self.optional_arg())
    
    def fls(self):
        return "fls"
    
    def tls(self):
        return "tls " + str(self.optional_arg())
    
    def version(self):
        return "version " + str(self.optional_arg())
    
    def info(self):
        return "info " + str(self.optional_arg())
    
    def diag(self):
        return "diag"
    
    def gl_info(self):
        return "gl info"
    
    def gl_gc(self):
        return "gl gc"
    
    def bye(self):
        return "bye"
    
    def kill(self):
        return "kill"
    
    def restart(self):
        return "restart"
    
    def help(self):
        return "help " + str(self.optional_arg())
        
