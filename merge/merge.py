import configparser
from config import Config
from pyarrow import fs
import pyarrow.parquet as pq


def main():
    #Example of reading conf
    print("starting to read conf file")
    conf_path = "conf/merge.conf"
    config = Config(conf_path)
    parser = config.get_config_parser()
    config.print_config_section(parser,'Insights-Aggregator-Merge-Config')

    # Example of reading HDFS file
    host="novus-nameservice"
    port=8020
    user="hubble-dev"
    ticket_cache_path=None
    hdfs_path="/data/parser_parser_timezone/1/event_timestamp=202106241600/processing_id=202106241800/table_type=auction/part-00000-4cf1d7cb-249a-4596-8258-b44933b00c6f.c000.snappy.parquet"

    hdfs = fs.HadoopFileSystem(host, port, user=user, kerb_ticket=ticket_cache_path)
    # with fs.open(path, 'rb') as f:
    
    print("Starting to read hdfs file in arrow table")
    hdfs_table = pq.read_table(hdfs_path,filesystem=hdfs)
    print("Starting to write arrow table as hdfs file ")
    pq.write_table(hdfs_table, '/tmp/12072021a.parquet',flavor='spark',filesystem=hdfs)
        


if __name__ == "__main__":
    main()

