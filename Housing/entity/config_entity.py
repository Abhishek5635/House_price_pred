from collections import namedtuple

DataInjestionConfig = namedtuple('DataInjestionConfigure', ['dataset_download_url','tgz_download_dir','row_data_dir',
                                                               'injested_data_dir','injested_test_dir'])

DataValidationConfig = namedtuple('DataValidationConfig', ['schima_file_path'])

DataTransformationConfig = namedtuple('DataTransformationConfig', ['add_bedroom_per_room',
                                                                   'transformed_train_dir',
                                                                   'transformed_test_dir',
                                                                   'preprocessor_pkl_file_path'])
ModelTraninerConfig = namedtuple('ModelTraninerConfig', ['train_model_file_path', 'base_accuracy'])

ModelEvaluationConfig = namedtuple('ModelEvaluationConfig', ['model_evaluatin_file_path','time_stamp'])

ModelPusherConfig = namedtuple('ModelPusherConfig', ['Export_dir_path'])