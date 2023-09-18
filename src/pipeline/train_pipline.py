from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer
from src.logger import logger

def create_step_text(pipline_name, border_len=20):
    border = "# " * border_len
    text = f"Step {pipline_name}".center(border_len*2, ' ')
    return f"\n{border}\n{text}\n{border}"

if __name__=="__main__":


    logger.info(create_step_text('Data Ingestion', border_len=20))
    obj=DataIngestion()
    train_data,test_data=obj.initiate_data_ingestion()

    logger.info(create_step_text('Data Transformation', border_len=20))
    data_transformation=DataTransformation()
    train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data,test_data)

    logger.info(create_step_text('Model Trainer', border_len=20))
    modeltrainer=ModelTrainer()
    print(modeltrainer.initiate_model_trainer(train_arr,test_arr))