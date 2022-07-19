
from banking.config.configuration import Configuration
from banking.constant import DATA_INGESTION_ARTIFACT_DIR
from banking.logger import logging
from banking.exception import BankingException
from banking.entity.artifact_entity import ModelPusherArtifact, DataIngestionArtifact, ModelEvaluationArtifact
from banking.entity.config_entity import DataIngestionConfig
from banking.component.data_ingestion import DataIngestion

import os, sys




class Pipeline:
   
    def __init__(self, config: Configuration ) -> None:
        try:
            self.config = config
        except Exception as e:
            raise BankingException(e, sys) from e

    
    
    
    
    def start_data_ingestion(self) -> DataIngestionArtifact:
        try:
            data_ingestion = DataIngestion(data_ingestion_config=self.config.get_data_ingestion_config())
            return data_ingestion.initiate_data_ingestion()
        except Exception as e:
            raise BankingException(e, sys) from e

    
    def run_pipeline(self):
        try:
         data_ingestion_artifact = self.start_data_ingestion()

        except Exception as e:
            raise BankingException(e, sys) from e
