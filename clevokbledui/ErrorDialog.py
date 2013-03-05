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

class ErrorDialog(Gtk.MessageDialog):
    __gtype_name__ = "ErrorDialog"

    def __new__(cls):
        """Special static method that's automatically called by Python when 
        constructing a new instance of this class.
        
        Returns a fully instantiated ErrorDialog object.
        """
        return Gtk.MessageDialog(None,0,Gtk.MessageType.ERROR,
                Gtk.ButtonsType.OK, 'Error')
if __name__ == "__main__":
    dialog = ErrorDialog()
    dialog.show()
    Gtk.main()
