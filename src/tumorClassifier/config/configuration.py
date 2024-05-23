# Import Dependencies
import os 
from tumorClassifier.constants import *
from tumorClassifier.utils.common import read_yaml, create_directories, save_json
from tumorClassifier.entity.config_entity import (DataIngestionConfig,
                                                 PrepareBaseModelConfig,
                                                 TrainingConfig)

class ConfigurationManager:
    def __init__(self, config_filepath=CONFIG_FILE_PATH, params_filepath=PARAMS_FILE_PATH):
        """
        Initialize the ConfigurationManager with the provided configuration and parameter files.

        Args:
            config_filepath (str): The path to the configuration file. Defaults to CONFIG_FILE_PATH.
            params_filepath (str): The path to the parameter file. Defaults to PARAMS_FILE_PATH.

        Attributes:
            config (dict): The dictionary containing the configuration details.
            params (dict): The dictionary containing the parameter details.
        """
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        """
        Get the configuration details for data ingestion.

        Args:
            self (ConfigurationManager): An instance of ConfigurationManager.

        Returns:
            DataIngestionConfig: A dictionary containing the configuration details for data ingestion.

        Attributes:
            root_dir (str): The root directory for data ingestion.
            source_URL (str): The source URL for the data.
            local_data_file (str): The local file path for the data.
            unzip_dir (str): The directory where the data will be unzipped.

        Raises:
            ValueError: If the configuration file is not found or is incomplete.
        """
        config = self.config.data_ingestion
        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )

        return data_ingestion_config
    
    def get_prepare_base_model_config(self) -> PrepareBaseModelConfig:
        """
        Get the configuration details for preparing the base model.

        Args:
            self (ConfigurationManager): An instance of ConfigurationManager.

        Returns:
            PrepareBaseModelConfig: A dictionary containing the configuration details for preparing the base model.

        Attributes:
            root_dir (Path): The root directory for the base model.
            base_model_path (Path): The path to the base model.
            updated_base_model_path (Path): The path to the updated base model.
            params_image_size (int): The size of the input images.
            params_learning_rate (float): The learning rate for the model.
            params_include_top (bool): Whether to include the top layers of the base model.
            params_weight (str): The weight to be used for the model.
            params_classes (int): The number of classes for the model.

        Raises:
            ValueError: If the configuration file is not found or is incomplete.
        """
        config = self.config.prepare_base_model
        create_directories([config.root_dir])

        prepare_base_model_config = PrepareBaseModelConfig(
            root_dir=Path(config.root_dir),
            base_model_path=Path(config.base_model_path),
            updated_base_model_path=Path(config.update_base_model_path),
            params_image_size=self.params.IMAGE_SIZE,
            params_learning_rate=self.params.LEARNING_RATE,
            params_include_top=self.params.INCLUDE_TOP,
            params_weight=self.params.WEIGHTS,
            params_classes=self.params.CLASSES
        )

        return prepare_base_model_config
    
    def get_training_config(self) -> TrainingConfig:
        """
        Get the configuration details for training the model.

        Args:
            self (ConfigurationManager): An instance of ConfigurationManager.

        Returns:
            TrainingConfig: A dictionary containing the configuration details for training the model.

        Attributes:
            root_dir (Path): The root directory for the training process.
            trained_model_path (Path): The path to save the trained model.
            updated_base_model_path (Path): The path to the updated base model.
            training_data (Path): The path to the training data.
            params_epochs (int): The number of epochs for the training process.
            params_batch_size (int): The batch size for the training process.
            params_is_augmentation (bool): Whether to apply data augmentation during training.
            params_image_size (int): The size of the input images.

        Raises:
            ValueError: If the configuration file is not found or is incomplete.
        """
        training = self.config.training
        prepare_base_model = self.config.prepare_base_model
        params = self.params
        training_data = os.path.join(self.config.data_ingestion.unzip_dir, 'BrainTumor')
        create_directories([Path(training.root_dir)])

        training_config = TrainingConfig(
            root_dir=Path(training.root_dir),
            trained_model_path=Path(training.trained_model_path),
            updated_base_model_path=Path(prepare_base_model.update_base_model_path),
            training_data=Path(training_data),
            params_epochs=params.EPOCHS,
            params_batch_size=params.BATCH_SIZE,
            params_is_augmentation=params.AUGMENTATION,
            params_image_size=params.IMAGE_SIZE
        )

        return training_config
    