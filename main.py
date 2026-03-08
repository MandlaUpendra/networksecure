import sys

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

from networksecurity.entity.config_entity import TrainingPipelineConfig

from networksecurity.entity.config_entity import DataIngestionConfig, DataValidationConfig,DataTransformationConfig,ModelTrainerConfig
from networksecurity.entity.artifact_entity import DataIngestionArtifact,DataValidationArtifact
from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.components.data_transformatioon import DataTransformation
from networksecurity.components.model_trainer import ModelTrainer

STAGE_NAME = "data_ingestion_stage"

try:
    logging.info(f">>>>>> {STAGE_NAME} started <<<<<<")
    trainingpipelineconfig = TrainingPipelineConfig()
    dataingestionconfig = DataIngestionConfig(trainingpipelineconfig)
    dataingestion = DataIngestion(dataingestionconfig)
    dataingestionartifact = dataingestion.initiate_data_ingestion()
    logging.info(f">>>>>> {STAGE_NAME} completed <<<<<<")
except Exception as e:
    raise NetworkSecurityException(e, sys)


STAGE_NAME = "data_validation_stage"

try:
    logging.info(f">>>>>> {STAGE_NAME} started <<<<<<")
    trainingpipelineconfig = TrainingPipelineConfig()
    datavalidationconfig = DataValidationConfig(trainingpipelineconfig)
    datavalidation = DataValidation(dataingestionartifact,datavalidationconfig)
    data_validation_artifact = datavalidation.initiate_data_validation()
    logging.info(f">>>>>> {STAGE_NAME} completed <<<<<<")
except Exception as e:
    raise NetworkSecurityException(e, sys)

STAGE_NAME = "data_transformation_stage"

try:
    logging.info(f">>>>>> {STAGE_NAME} started <<<<<<")
    trainingpipelineconfig = TrainingPipelineConfig()
    datatransformationconfig = DataTransformationConfig(trainingpipelineconfig)
    datatransformation = DataTransformation(data_validation_artifact, datatransformationconfig)
    data_transformation_artifact = datatransformation.initiate_data_transformation()
    logging.info(f">>>>>> {STAGE_NAME} completed <<<<<<")
except Exception as e:
    raise NetworkSecurityException(e, sys)

STAGE_NAME = "model_training_stage"

try:
    logging.info(f">>>>>> {STAGE_NAME} started <<<<<<")
    trainingpipelineconfig = TrainingPipelineConfig()
    modeltrainerconfig = ModelTrainerConfig(trainingpipelineconfig)
    model_trainer = ModelTrainer(modeltrainerconfig,data_transformation_artifact)
    model_trainer_artifact = model_trainer.initiate_model_trainer() 
    logging.info(f">>>>>> {STAGE_NAME} completed <<<<<<")
except Exception as e:
    raise NetworkSecurityException(e,sys)
