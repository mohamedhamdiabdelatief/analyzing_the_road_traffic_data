# import the libraries
from datetime import timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago

#defining DAG arguments

default_args = {
    'owner': 'Mohamed Hamdi',
    'start_date': days_ago(0),
    'email': ['mohamed.hamdi@nies-eg.com'],
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# define the DAG
dag = DAG(
    'ETL_toll_data',
    default_args=default_args,
    description='Apache Airflow Final Assignment',
    schedule_interval=timedelta(days=1)
)

# define the task 'unzip_data'

unzip_data = BashOperator(
    task_id='unzip_data',
    bash_command='unzip /home/project/airflow/dags/finalassignment/tolldata.tgz',
    dag=dag,
)

# define the task 'extract_data_from_csv'

extract_data_from_csv = BashOperator(
    task_id='extract_data_from_csv',
    bash_command='cut -f1,2,3,4,6 -d "," vehicle-data.csv > csv_data.csv',
    dag=dag,
)

# define the task 'extract_data_from_tsv'

extract_data_from_tsv = BashOperator(
    task_id='extract_data_from_tsv',
    bash_command="cut -f5,6,7 -d $'\t' tollplaza-data.tsv | sed 's/\t/,/g' | > csv_data.csv",
    dag=dag,
)

# define the task 'extract_data_from_fixed_width'

extract_data_from_fixed_width = BashOperator(
    task_id='extract_data_from_fixed_width',
    bash_command="cut -c 59-67 payment-data.txt | sed 's/ /,/g' | > fixed_width_data.csv",
    dag=dag,
)


# define the task 'consolidate_data'

consolidate_data = BashOperator(
    task_id='consolidate_data',
    bash_command="paste -d ',' csv_data.csv tsv_data.csv fixed_width_data.csv > extracted_data.csv",
    dag=dag,
)


# define the task 'transform_data'

transform_data = BashOperator(
    task_id='transform_data',
    bash_command="tr '[:upper:]' '[:lower:]' < extracted_data.csv > transformed_data.csv",
    dag=dag,
)

unzip_data >> extract_data_from_csv >> extract_data_from_tsv >> extract_data_from_fixed_width >> consolidate_data >> transform_data



