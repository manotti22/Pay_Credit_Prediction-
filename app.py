from flask import Flask 
import sys
from banking.logger import logging
from banking.exception import BankingException

app=Flask(__name__)

@app.route("/",methods=['GET','post'])
def index():

    try:
        raise Exception('WE ARE TESTING CUSTUM EXCEPTION')
    except Exception as e:
        banking= BankingException(e,sys)
        logging.info(banking.error_message)
    logging.info('we are testing logging modul')
    return 'CD CI PIPLINE has been established'

if __name__=='__main__':
    app.run(debug=True)

