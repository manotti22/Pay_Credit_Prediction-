import logging
from sklearn import pipeline
from banking.pipeline.pipeline import Pipeline
from banking.logger import logging
from banking.exception import BankingException

def main(self):

   try:

    pipeline = Pipeline
    pipeline.run_pipeline(self)

   except Exception as e:
        logging.error(f"{e}")
        print (e)

if __name__=="__main__":
    main(self=any)