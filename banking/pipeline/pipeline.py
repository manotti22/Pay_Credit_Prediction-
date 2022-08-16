from collections import namedtuple
from datetime import datetime
import uuid
from banking.config.configuration import Configuration
from banking.logger import logging
from banking.exception import BankingException
from threading import Thread
from typing import List

from multiprocessing import Process
from banking.entity.artifact_entity import ModelPusherArtifact, DataIngestionArtifact, ModelEvaluationArtifact
from banking.entity.artifact_entity import DataValidationArtifact, DataTransformationArtifact, ModelTrainerArtifact
from banking.entity.config_entity import DataIngestionConfig, ModelEvaluationConfig
from banking.component.data_ingestion import DataIngestion
from banking.component.data_validation import DataValidation


import os, sys
from collections import namedtuple
from datetime import datetime
import pandas as pd






class Pipeline():
   
    def __init__(self, config: Configuration ) -> None:
        try:
            os.makedirs(config.training_pipeline_config.artifact_dir, exist_ok=True)
           
            self.config = config
        except Exception as e:
            raise BankingException(e, sys) from e

    def start_data_ingestion(self) -> DataIngestionArtifact:
        try:
            data_ingestion = DataIngestion(data_ingestion_config=self.config.get_data_ingestion_config())
            return data_ingestion.initiate_data_ingestion()
        except Exception as e:
            raise BankingException(e, sys) from e

    def start_data_validation(self, data_ingestion_artifact: DataIngestionArtifact) \
            -> DataValidationArtifact:

        try:
            data_validation = DataValidation(data_validation_config=self.config.get_data_validation_config(),
                                             data_ingestion_artifact=data_ingestion_artifact
                                             )
            return data_validation.initiate_data_validation()
        except Exception as e:
            raise BankingException(e, sys) from e 
      

    def start_data_transformation(self,
                                  data_ingestion_artifact: DataIngestionArtifact,
                                  data_validation_artifact: DataValidationArtifact
                                  ) -> DataTransformationArtifact:
            pass
       

    def start_model_trainer(self, data_transformation_artifact: DataTransformationArtifact) -> ModelTrainerArtifact:
        pass

    def start_model_evaluation(self, data_ingestion_artifact: DataIngestionArtifact,
                               data_validation_artifact: DataValidationArtifact,
                               model_trainer_artifact: ModelTrainerArtifact) -> ModelEvaluationArtifact:
        pass

    def start_model_pusher(self, model_eval_artifact: ModelEvaluationArtifact) -> ModelPusherArtifact:
        pass

    def run_pipeline(self):
        try:
         
            # data ingestion
            logging.info("Pipeline starting.")
            data_ingestion_artifact = self.start_data_ingestion()
            data_validation_artifact = self.start_data_validation(data_ingestion_artifact=data_ingestion_artifact)
            
        except Exception as e:
            raise BankingException(e, sys) from e

    def run(self):
        try:
            self.run_pipeline()
        

        except Exception as e:
            raise BankingException(e, sys) from e

   