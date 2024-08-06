import sys

def error_message_details(error,error_detail:sys):
    #exc_tb stands for excetion traceback
    _,_,exc_tb = error_detail.exc_info()
    #exc_info() retrieves most recent exception from sys and returns tuple of three values (exc_type, exc_value, traceback_object)
    file_name = exc_tb.tb_frame.f_code.co_filename

    error_message = "Error occrued in File [{0}] at line number [{1}] \n Error Message : [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )

    return error_message

#Custom Exception class
class CustomException(Exception):
    def __init__(self,error_message,error_details:sys):

        #Inheriting the super class output
        super().__init__(error_message)
        self.error_message= error_message_details(error_message, error_detail=error_details)

    def __str__(self):
        return self.error_message