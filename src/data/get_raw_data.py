import os
import logging

def extract_data(file_name, file_path):
    !kaggle competitions download titanic -f $file_name -p $file_path --force

def main(project_dir):
    logger = logging.getLogger(__name__)
    logger.info('Getting raw data')
    
    train_file = 'train.csv'
    test_file = 'test.csv'

    raw_data_path = os.path.join(os.path.pardir, 'data', 'raw')
    extract_data(train_file, raw_data_path)
    extract_data(test_file, raw_data_path)
    logger.info('Test data and training data fetched')
    
if __name__=='__main__':
    project_dir = os.path.join(os.path.dirname(__file__), os.pardir, os.pardir)
    
    log_fmt = '%(asctime) - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level = logging.info, format = log_fmt)
    
    main(project_dir)