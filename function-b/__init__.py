# This is Function1/__init__.py
import logging
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    # Your code for Function1 goes here
    return func.HttpResponse("Function B completed")