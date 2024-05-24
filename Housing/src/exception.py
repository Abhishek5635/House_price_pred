import sys
from logger import logging

def erro__message_details(error,error_details:sys):
    """
    Args: error --> Type of error
          error_details --> Error details
    
    returns: error message with filename, error occured line number
             and error message
    """

    _,_,exc_tb = error_details.exc_info()
    filename = exc_tb.tb_frame.f_code.co_filename
    
    error_message ="Error occured in python script name [{0}] line number [{1}] error message [{2}].".format(filename, error,exc_tb.tb_lineno,str(error))
     
    return error_message


class CustomException(Excetption):
    def __init__(self,error_message,erro_details:sys):
        super().__init__(error_message)
        self.error_message = erro__message_details(error_message,erro_details=erro_details)

        def __str__(self):
            return self.error_message
        

if __name__ == "__main__":
    logging.info("Logging has started")

    try :
        a = 1/0

    except Exception as e :
        logging.info("Division by zero")
        raise(CustomException(e,sys))