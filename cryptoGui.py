#!/usr/bin/env python3
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from crypto import file_crypt, file_decrypt

class SignalHandler:
    def exit(self, *args, **kwargs):
        Gtk.main_quit()
    def get_data(self):
        global input_file
        global output_file
        global password
        o = output_file.get_uri()
        i = input_file.get_uri()
        p = password.get_text()
        if o and i:
            o = o[len('file://'):]
            i = i[len('file://'):]
            return i,o,p
        return None,None,None
    def do_crypt(self, *args, **kwargs):
        in_file,out_file,password = self.get_data()
        if in_file != None:
            file_crypt(in_file,out_file,password)

    def do_decrypt(self, *args, **kwargs):
        in_file,out_file,password = self.get_data()
        if in_file != None:
            file_decrypt(in_file,out_file,password)

if __name__ == '__main__':
    builder = Gtk.Builder()
    builder.add_from_file("cryptoGui.glade")
    builder.connect_signals(SignalHandler())

    window = builder.get_object("window1")
    input_file  = builder.get_object("filechooserbutton1")
    output_file = builder.get_object("filechooserbutton2")
    password = builder.get_object("entry1")

    window.show_all()
    Gtk.main()
