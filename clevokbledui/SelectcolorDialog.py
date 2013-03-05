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

from gi.repository import Gtk # pylint: disable=E0611

from clevokbledui_lib.helpers import get_builder

import gettext
from gettext import gettext as _
gettext.textdomain('clevokbledui')

class SelectcolorDialog(Gtk.Dialog):
    __gtype_name__ = "SelectcolorDialog"

    def __new__(cls):
        """Special static method that's automatically called by Python when 
        constructing a new instance of this class.
        
        Returns a fully instantiated SelectcolorDialog object.
        """
        builder = get_builder('SelectcolorDialog')
        new_object = builder.get_object('selectcolor_dialog')
        new_object.finish_initializing(builder)
        return new_object

    def finish_initializing(self, builder):
        """Called when we're finished initializing.

        finish_initalizing should be called after parsing the ui definition
        and creating a SelectcolorDialog object with it in order to
        finish initializing the start of the new SelectcolorDialog
        instance.
        """
        # Get a reference to the builder and set up the signals.
        self.builder = builder
        self.ui = builder.get_ui(self)

        self.colors = {
            'white'     : 111,
            'yellow'    : 110,
            'light_blue': 101,
            'green'     : 100,
            'purple'    : 11,
            'red'       : 10,
            'blue'      : 1,
            'nocolor'   : 0 
        }

    def on_white_clicked(self, widget, data=None):
        self.response(self.colors['white'])
        
    def on_yellow_clicked(self, widget, data=None):
        self.response(self.colors['yellow'])

    def on_light_blue_clicked(self, widget, data=None):
        self.response(self.colors['light_blue'])
        
    def on_green_clicked(self, widget, data=None):
        self.response(self.colors['green'])
        
    def on_purple_clicked(self, widget, data=None):
        self.response(self.colors['purple'])
        
    def on_red_clicked(self, widget, data=None):
        self.response(self.colors['red'])
        
    def on_blue_clicked(self, widget, data=None):
        self.response(self.colors['blue'])
        
    def on_nocolor_clicked(self, widget, data=None):
        self.response(self.colors['nocolor'])


    def on_btn_cancel_clicked(self, widget, data=None):
        """The user has elected cancel changes.

        Called before the dialog returns Gtk.ResponseType.CANCEL for run()
        """
        pass


if __name__ == "__main__":
    dialog = SelectcolorDialog()
    dialog.show()
    Gtk.main()
