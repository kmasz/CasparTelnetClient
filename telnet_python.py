#!/usr/bin/python3
# -*- coding: utf-8 -*-

import telnetlib
from Caspar_Basic_Commands import CasparBasicCommands
from Caspar_Basic_Commands import CasparDataCommands
from Caspar_Basic_Commands import CasparTemplateCommands
from Caspar_Basic_Commands import CasparMixerCommands

HOST = "localhost"
PORT = "5250"

def tn_connect():
    print("Starting connection to {}:{} ...".format(HOST, PORT))
    try:
        _tn = telnetlib.Telnet(HOST, PORT)
        print("Connected.")
        return _tn
    except ConnectionRefusedError as _ce:
        print('Connection Error ', _ce)
    except TimeoutError as _te:
        print("Timeout Error ", _te)
    except:
        print("Error")
  
def tn_read(_tn):
    _tn_incoming = ""
    try:        
        while _tn_incoming != b'\r\n':
            _tn_incoming = _tn.read_until(b"\r\n",0.1)
            if _tn_incoming == b'':
                break
            print(_tn_incoming.strip().decode())
    except:
        print("Reading from server Error.")
                

def tn_write(_tn,_command):
    try:      
        _command += '\r\n'
        _tn.write(_command.encode('ascii'))
    except:
        print("Sending to server Error.")
        
def tn_close(_tn):
    try:
        _tn.close()
        print("Connection with {}:{} close.".format(HOST,PORT))
    except:
        print("Closing connection Error.")
   
def main():
    #BasicCommands = CasparBasicCommands()
    #aaa = play1()
    #print(dupa.play('amb', 1,1))
    #print(tttt.play('amb', 1,1))
    tn=tn_connect()
    if tn != None:
        #tn_write(tn, BasicCommands.play('amb', 1,0))
        #tn_write(tn, aaa.getArgs('amb', 1,0))
        #print(play1('amb', 1, loop = 'loop').play2())
        #tn_write(tn, CasparBasicCommands('amb', 1, layer=0, loop = 'loop').play())
        #tn_write(tn, CasparBasicCommands('amb', 1, layer=0, framerate = 'seek 25').call())
        #tn_write(tn, CasparDataCommands("test_data1").data_remove())
        #Trzeba zbudowa� t� list� dynamicznie!!
        #f0 = ("tekst_gora", "Tomasz Nowak")
        #f1 = ("tekst_dol", "dyr. IT i techniki TV")
        #f2 = ("tekst_gora", "33")
        #f3 = ("tekst_dol", "44")
        #ist_of_f= [f0, f1]
        #list_of_f2= [f2, f3]
        #tn_write(tn, CasparTemplateCommands("wizytowka_wtk2", 1, 1,0, layer=2).templateAdd(*list_of_f))
        #tn_read(tn)
        #tn_write(tn, CasparTemplateCommands("wizytowka_wtk2", 1, 1,0, layer=2).templatePlay())
        #tn_read(tn)
        #tn_write(tn, CasparTemplateCommands("wizytowka_wtk2", 1, 1,0, layer=2).templateInfo())
        #tn_read(tn)
        #n_close(tn)
        #print(CasparTemplateCommands("wizytowka_wtk1_cs6", 1, 1,1).templateData())
        #tn_write(tn, CasparMixerCommands(1,layer=1,keyer=1).mixerKeyer())
        #tn_write(tn, CasparMixerCommands(1, layer=0, color='green', threshold = 0.1, softness = 0.1, spill = 0.1).mixerChroma())
        #tn_write(tn, CasparMixerCommands(1, layer=1,blend='screen').mixerBlend())
        #tn_write(tn, CasparMixerCommands(1,layer=0, opacity = 1, duration =50).mixerOpacity())
        #tn_write(tn, CasparMixerCommands(1,layer=0, brightness = 1, duration = 50).mixerBrightness())
        #tn_write(tn, CasparMixerCommands(1,layer=0, saturation = 1, duration = 24).mixerSaturation())
        #tn_write(tn, CasparMixerCommands(1,layer=0, contrast = 1, duration = 24).mixerContrast())
        #tn_write(tn, CasparMixerCommands(1,layer=0,min_input=0,max_input=1,min_output=0,max_output=1,gamma=1).mixerLevels())
        #tn_write(tn, CasparMixerCommands(1,layer=0,x=0,y=0,x_scale=1,y_scale=1,duration = 50).mixerFill())
        #tn_write(tn, CasparMixerCommands(1,layer=0,x=0,y=0,width=1,height=1,duration=50).mixerClip())
        #tn_write(tn, CasparMixerCommands(1,layer=0,x=0,y=0,duration=50).mixerAnchor())
        #tn_write(tn, CasparMixerCommands(1,layer=0,left_edge=0,right_edge=1,top_edge=0,bottom_edge=1,duration=50).mixerCrop())
        #tn_write(tn, CasparMixerCommands(1,layer=0,angle=0,duration=50).mixerRotation())
        #tn_write(tn, CasparMixerCommands(1,layer=0,top_left_x=0.4,top_left_y=0.4,top_right_x=0.6,top_right_y=0.4,bottom_right_x=1,bottom_right_y=1,bottom_left_x=0,bottom_left_y=1,duration=50).mixerPerspective())
        #tn_write(tn, CasparMixerCommands(1,layer=0, mipmap=0).mixerMipmap())
        #tn_write(tn, CasparMixerCommands(1,layer=0, volume=1).mixerVolume())
        #print(CasparMixerCommands(1,layer=0).mixerFill())
        #tn_write(tn, CasparMixerCommands(1,layer=0,mastervolume=1).mixerMastervolume())
        #tn_write(tn, CasparMixerCommands(1,layer=0,straightalphaoutput=0).mixerStraightalphaoutput())
        #tn_write(tn, CasparMixerCommands(1,layer=0,grid=2).mixerGrid())
        #tn_write(tn, CasparMixerCommands(1,layer=0).mixerCommit())
        #tn_write(tn, CasparMixerCommands(1,layer=4).mixerClear())
        tn_write(tn, CasparMixerCommands(1).mixerChannelgrid())
        tn_read(tn)
        tn_close(tn)
    else:
        print("blad polacznia")
    #tn = tn_connect()
    #tn.write('version\r\n'.encode('ascii'))
    #print("wyslane")

#    while tn_incoming != b'\r\n':
#        tn_incoming = tn.read_until(b"\r\n",0.1)
#       if tn_incoming == b'':
#            break
#        print(tn_incoming)
    
    #print(tn.read_until(b'aa',1))
    #decode('utf8').strip()
    #tn.close()
    


if __name__ == "__main__": main()

#tn.read_until(b"login: ", 1)
#tn.read_until("login: ", 1)
#tn.write(user.encode('ascii') + b"\n")
#if password:
#    tn.read_until(b"Password: ")
#    tn.write(password.encode('ascii') + b"\n")

#tn.write(b"ls\n")
#tn.write(b"exit\n")

#print(tn.read_all().decode('ascii'))