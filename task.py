"""


"""

import uuid


# --- Task class ---
class Task:
    """

    """

    # --- Constructor ----------------------------------------------------------
    def __init__(self, task_name):
        self._d_uuid = {task_name: uuid.uuid4()}
        self._d_parm = {}
        self._d_rrhh = {}
        self._d_equi = {}
        self._d_area = {}
        self._d_resu = {}
        self._d_func = {}

        self._d_input = {}
        self._d_output = {}

    # --- Properties -----------------------------------------------------------
    """
    
    """
    # --- _d_uuid                                             ---  READ-ONLY ---
    @property
    def d_uuid(self):
        return self._d_uuid

    # --- _d_parm                                             --- READ-WRITE ---
    @property
    def d_parm(self):
        return self._d_parm

    @d_parm.setter
    def d_parm(self, value):
        self._d_parm = value

    # --- _d_rrhh                                             --- READ-WRITE ---
    @property
    def d_rrhh(self):
        return self._d_rrhh

    @d_rrhh.setter
    def d_rrhh(self, value):
        self._d_rrhh = value

    # --- _d_equi                                             --- READ-WRITE ---
    @property
    def d_equi(self):
        return self._d_equi

    @d_equi.setter
    def d_equi(self, value):
        self._d_equi = value

    # --- _d_area                                             --- READ-WRITE ---
    @property
    def d_area(self):
        return self._d_area

    @d_area.setter
    def d_area(self, value):
        self._d_area = value

    # --- _d_resu                                             --- READ-WRITE ---
    @property
    def d_resu(self):
        return self._d_resu

    @d_resu.setter
    def d_resu(self, value):
        self._d_resu = value

    # --- _d_func                                             --- READ-WRITE ---
    @property
    def d_func(self):
        return self._d_func

    @d_func.setter
    def d_func(self, value):
        self._d_func = value

    # --- _d_input                                            ---  READ-ONLY ---
    @property
    def d_input(self):
        return self._d_input

    # --- _d_output                                            ---  READ-ONLY ---
    @property
    def d_output(self):
        return self._d_output

    # --- Methods --------------------------------------------------------------
    # --- Public ---
    def input(self, d_input):
        """

        """
        pass

    # --- Private ---
    def output(self):
        """

        """
        pass

    pass  # END of CLASS
