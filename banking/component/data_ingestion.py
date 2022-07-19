from banking.entity.config_entity import DataIngestionConfig
import sys,os
from banking.exception import BankingException, HousingException
from banking.logger import logging


class DataIngestion:

    def __init__(self,data_ingestion_config:DataIngestionConfig ):
        try:
            logging.info(f"{'>>'*20}Data Ingestion log started.{'<<'*20} ")
            self.data_ingestion_config = data_ingestion_config

        except Exception as e:
            raise BankingException(e,sys)