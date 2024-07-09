'''
exceptional.py is a file where you typically define custom exceptions or handle exceptions in a centralized manner.
Exceptions are errors that occur during the execution of a program, and 
handling them allows your program to recover gracefully or provide meaningful feedback to the user.
'''
#It allows interaction with the interpreter directly, access to command-line arguments, and various system-related functionalities. Here’s a breakdown of what the sys library offers:
import sys # provides access to system-specific parameters and functions.


def error_message_detail(error,error_detail:sys):
    _,_,exc_tb = error_detail.exc_info() ##first two not imp iam taking last two errors     '''This exc_tb file will say about and shows the In which file the and which line will exception occurs'''

    file_name =exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(_,_,exc_tb)
    file_name,exc_tb.tb_lineno,str(error)
    
    return error_message


class CustomeException(Exception):
    def __init__(self,error_message,error_detail: sys):
        super().__init__(error_message)  ## It calls the super calls constructor
        self.error_message = error_message_detail(error_message,error_detail=error_detail)
    
    def __str__(self):
        return self.error_message
