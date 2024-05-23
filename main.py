from tumorClassifier import logger
from tumorClassifier.pipe.stage_01_data_ingestion import DataIngestionPipeline
from tumorClassifier.pipe.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from tumorClassifier.pipe.stage_03_model_training import ModelTrainingPipeline

STAGE_NAME = 'Data Ingestion'
if __name__ == '__main__':
    try:
        logger.info(f'>>>>> Stage {STAGE_NAME} Started <<<<<')
        obj = DataIngestionPipeline()
        obj.main()
        logger.info(f'>>>>> Stage {STAGE_NAME} Completed <<<<<')
    except Exception as e:
        logger.exception(e)
        raise e
    

STAGE_NAME = 'Prepare Base Model'
if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = PrepareBaseModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e
    

STAGE_NAME = "Model Training"
if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e