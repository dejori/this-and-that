# copy http://www2.census.gov/econ2007/CBP_CSV/zbp07detail.zip 
# unpack data
# copy file onto hdfs: hadoop dfs -copyFromLocal /local-data-folder /data-folder/

hadoop jar $HADOOP_HOME/contrib/streaming/hadoop-streaming-xxx.jar \
-input /data-folder/zbp07detail.txt \
-output /out \
-mapper ./map.py \
-reducer ./reduce.py \
-file ./map.py \
-file ./reduce.py
