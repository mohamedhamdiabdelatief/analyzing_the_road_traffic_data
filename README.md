# analyzing_the_road_traffic_data
## Building ETL Pipeline using Apache Kafka
    collect data available in different formats and consolidate it into a single file.
    
        Download Kafka:
        wget https://archive.apache.org/dist/kafka/2.8.0/kafka_2.12-2.8.0.tgz

        Extract Kafka:
        tar -xzf kafka_2.12-2.8.0.tgz

        Start MySQL server

        connect to MYSQL server:
        mysql --host=127.0.0.1 --port=3306 --user=root --password=Mjk0NDQtcnNhbm5h

        Create a database named tolldata:
        create database tolldata;

        Create a table named livetolldata with the schema to store the data generated by the traffic simulator:
        use tolldata;
        create table livetolldata(timestamp datetime,vehicle_id int,vehicle_type char(15),toll_plaza_id smallint);

        Disconnect from MySQL server:
        exit

        Install the python module kafka-python using the pip command:
        python3 -m pip install kafka-python

        Install the python module mysql-connector-python using the pip command:
        python3 -m pip install mysql-connector-python==8.0.31

        run zookeper server:
        cd kafka_2.12-2.8.0
        bin/zookeeper-server-start.sh config/zookeeper.properties

        run kafka server:
        cd kafka_2.12-2.8.0
        bin/kafka-server-start.sh config/server.properties

        Create a toll topic:
        cd kafka_2.12-2.8.0
        bin/kafka-topics.sh --create --topic toll --bootstrap-server localhost:9092

        run toll_traffic_generator.py 

        run streaming_data_reader.py
        
## Building ETL Pipeline using Apache Airflow

        Submit ETL_toll_data dag:
        cp ETL_toll_data.py  $AIRFLOW_HOME/dags 
        
        command that unpause dag:
        airflow dags unpause ETL_toll_data
        
        List dags to ensure that dag runs successfully:
        airflow dags list
