import sys

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

from networksecurity.entity.config_entity import TrainingPipelineConfig

from networksecurity.entity.config_entity import DataIngestionConfig
from networksecurity.components.data_ingestion import DataIngestion

STAGE_NAME = "data_ingestion_stage"

try:
    logging.info(f">>>>>> {STAGE_NAME} started <<<<<<")
    trainingpipelineconfig = TrainingPipelineConfig()
    dataingestionconfig = DataIngestionConfig(trainingpipelineconfig)
    dataingestion = DataIngestion(dataingestionconfig)
    dataingestion.initiate_data_ingestion()
    logging.info(f">>>>>> {STAGE_NAME} completed <<<<<<")
except Exception as e:
    raise NetworkSecurityException(e, sys)