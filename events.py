"""
Event class to handle the comunication between classes

When a class wants to send a message/data to other class it fires and event
wich is handle by the event class and redirected to the specified class/classes.

The events need to be registered in the class manually or load from a .csv file
the structure of the event is the following:

dict{event_type: [surce_class, destination_class, callback_class]}

The event may have data (arguments) to pass between classes.
                                                                      2023-03-09
"""

import os
import csv


class Events(object):
    """
    Class to handle the comunication betwen classes (events).

    """

    # --- Constructor ----------------------------------------------------------
    """
    Set the private attibute to store the events handlers and the name of the
    instance of the class (every instanciate class object MUST have a NAME).
    
    """
    def __init__(self, name):
        self.__eHandlers = {}

        self._name = name

    # --- Properties -----------------------------------------------------------
    """
    Properties to acces (READ ONLY; READ/WRITE) the attributes of the class.
    
    Attributes
                * _name:         read-only
                *__eHandlers:    not accesible by properties
                
    """
    # --- _name                                               ---  READ-ONLY ---
    @property
    def name(self):
        return self._name

    # --- __Methods ------------------------------------------------------------
    """
    Methos to add and remove events handlers manually.
    
    """
    def __iadd__(self, event, handlers):
        self.__eHandlers[event] = handlers

        return self

    def __isub__(self, event):
        del self.__eHandlers[event]

        return self

    # --- Methods --------------------------------------------------------------
    """
    Public methods of the class:
            * list()
            * del_all_ehandlers()
            * load_ehandlers()
                
    """
    def list(self):
        """
        Return a list of all the event handlers register within the class.

        :return: a list of handlers

        """
        return self.__eHandlers

    def del_all_ehandlers(self):
        """
        Deletes all event handlers registered within the class.

        :return: None
        """
        self.__eHandlers.clear()

    def load_ehandlers(self, path_file_handlers):
        """
        Load the events handlers containes in a .csv file.
        If the file do not exist raise and exception,
        :param path_file_handlers
        :return: True:None / Fails:Exception

        """
        file_exists = os.path.exists(path_file_handlers)

        if file_exists:
            with open(path_file_handlers, newline='') as f:
                reader = csv.reader(f)

                for row in reader:
                    self.__eHandlers[row[0]] = [row[1], row[2], row[3]]
        else:
            raise Exception('File do not Exist')

    pass  # END of CLASS
