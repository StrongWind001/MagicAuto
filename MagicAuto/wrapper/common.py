#! -*- coding:utf-8 -*-
# Define the functions about parsing and param check here
import re,os
import traceback

def parser():
    """

    :return:
    """
    #TODO
    pass

def paramCheck(param1,param2):
    """
    Check whether the parameters meet the requirements
    :param:
        -param1 the stand param
        -param2 the param compare with standard

    :return:Boolean value
        -true   satisfy
        -false  Dissatisfaction
    """
    for key in param2:
        if key not in param1:
            raise Exception("the param value is not right!")
        elif param1[key] == "required":
            if param2[key] == "":
                raise Exception("the param value is not right!")
            else:
                pass
        return True


