# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
### BEGIN LICENSE
# Copyright (C) 2013 Fabrizio Fortunato fortune@cortesconta.net
# This program is free software: you can redistribute it and/or modify it 
# under the terms of the GNU General Public License version 3, as published 
# by the Free Software Foundation.
# 
# This program is distributed in the hope that it will be useful, but 
# WITHOUT ANY WARRANTY; without even the implied warranties of 
# MERCHANTABILITY, SATISFACTORY QUALITY, or FITNESS FOR A PARTICULAR 
# PURPOSE.  See the GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License along 
# with this program.  If not, see <http://www.gnu.org/licenses/>.
### END LICENSE

from locale import gettext as _

import os, sys
import subprocess

from gi.repository import Gtk # pylint: disable=E0611
import logging
logger = logging.getLogger('clevokbledui')

from clevokbledui_lib import Window
from clevokbledui.AboutClevokbleduiDialog import AboutClevokbleduiDialog
from clevokbledui.PreferencesClevokbleduiDialog import PreferencesClevokbleduiDialog
from clevokbledui.SelectcolorDialog import SelectcolorDialog
from clevokbledui.ErrorDialog import ErrorDialog

# See clevokbledui_lib.Window.py for more details about how this class works
class ClevokbleduiWindow(Window):
    __gtype_name__ = "ClevokbleduiWindow"
    
    def finish_initializing(self, builder): # pylint: disable=E1002
        """Set up the main window"""
        super(ClevokbleduiWindow, self).finish_initializing(builder)

        self.AboutDialog = AboutClevokbleduiDialog
        self.PreferencesDialog = PreferencesClevokbleduiDialog
        self.SelectcolorDialog = SelectcolorDialog
        self.ErrorDialog = ErrorDialog

        

        self.cmd = "echo %s > /sys/devices/platform/clevo_wmi/kbled/%s"
        self.path = '/sys/devices/platform/clevo_wmi/kbled/'


        # Code for other initialization actions should be added here.

        #Clevopp needs to be root
        if not os.geteuid() == 0:
            errorDialog = self.ErrorDialog()
            errorDialog.format_secondary_text('Need to be root')
            res = errorDialog.run()
            errorDialog.destroy()
            sys.exit("\nOnly root can run\n")
       
        #Check module loaded
        if not os.path.exists(self.path):
            errorDialog = self.ErrorDialog()
            errorDialog.format_secondary_text('Cannot find devices \n Check if module loaded')
            res = errorDialog.run()
            errorDialog.destroy()
            sys.exit("\nPath not exists\n")
        

    #For color regions
    def on_left_clicked(self, widget, data=None):
        if self.SelectcolorDialog is not None:
            scd = self.SelectcolorDialog()
            res = scd.run()
            if res != Gtk.ResponseType.CANCEL:
                subprocess.call(self.cmd %(str(res).zfill(3),'left'),shell=True)
            scd.destroy()
            
    def on_middle_clicked(self, widget, data=None):
        if self.SelectcolorDialog is not None:
            scd = self.SelectcolorDialog()
            res = scd.run()
            if res != Gtk.ResponseType.CANCEL:
                subprocess.call(self.cmd %(str(res).zfill(3),'middle'),shell=True)
            scd.destroy()
            
    def on_right_clicked(self, widget, data=None):
        if self.SelectcolorDialog is not None:
            scd = self.SelectcolorDialog()
            res = scd.run()
            if res != Gtk.ResponseType.CANCEL:
                subprocess.call(self.cmd %(str(res).zfill(3),'right'),shell=True)
            scd.destroy()
           
    #bightness
    def on_brightnessPlus_clicked(self,widget,data=None):
        brFile = open(self.path+'brightness','r')
        current = brFile.readline().strip()
        if (current == '10'):
            return
        else:
            current = int(current) + 1
            subprocess.call(self.cmd%(str(current),'brightness'),shell=True)
        brFile.close()       

    def on_brightnessMinus_clicked(self,widget,data=None):
        brFile = open(self.path+'brightness','rw')
        current = brFile.readline().strip()
        if (current == '0'):
            return
        else:
            current = int(current) - 1
            
            subprocess.call(self.cmd%(str(current),'brightness'),shell=True)
        brFile.close()      

    def on_brightnessOff_clicked(self, widget, data=None):
        subprocess.call(self.cmd%(1,'all_off'),shell=True)


    #For effects & co 
    def on_random_clicked(self, widget, data=None):
        subprocess.call(self.cmd%(1,'random'),shell=True)

    def on_patternOff_clicked(self, widget, data=None):
        subprocess.call(self.cmd%(1,'pattern_off'),shell=True)

    def on_leftRight_clicked(self, widget, data=None):
        subprocess.call(self.cmd%(1,'left_right'),shell=True)

    def on_randomFlicker_clicked(self, widget, data=None):
        subprocess.call(self.cmd%(1,'random_flicker'),shell=True)

    def on_singleFade_clicked(self, widget, data=None):
        subprocess.call(self.cmd%(1,'single_fade'),shell=True)

    def on_outMid_clicked(self, widget, data=None):
        subprocess.call(self.cmd%(1,'out_mid'),shell=True)
        
        
