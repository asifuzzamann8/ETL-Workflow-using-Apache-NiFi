# ETL Workflow using Apache NiFi
The project is developed with open source big data tools from Apache. All the required tools are installed and configured from scratch in a Linux environment to explore the mechanism of the Apache Big Data ecosystem.

All the supporting tutorials are provided so that this document can be used as a development manual. Also, the technical challenges during the development process and their solution are described or highlighted in the sections. In addition, all the required configuration and coding files are attached to the project folder. Also, important code and configuration steps are mentioned in the glossary.  

## Scope
As part of the ETL process, the data needs to be fetched from UCI Machine Learning Repository from HTTPS link. The compressed file will be extracted. The dataset contains 2,916,697 records and ten attributes. The target column contains the name of families, including the Ransomware ones (e.g., Cryptxxx, cryptolocker etc). A new column needs to be added to flag the probable Ransomware transaction. Also, column names will be changed to avoid system keywords (e.g. year, day, and count). After the required transformation, data will be inserted into the data warehouse (HIVE) for future use.

## Platform & Tools
<table>
    <tr>
        <td>Purpose</td>
        <td>Name</td>
        <td>Version</td>
        <td>Download Link</td>
    </tr>
    <tr>
        <td>Virtualization</td>
        <td>VMWare Workstation Player</td>
        <td>16</td>
        <td><a href="https://www.vmware.com/ca/products/workstation-player/workstation-player-evaluation.html" target="_blank">Download Link</a></td>
    </tr>
    <tr>
        <td>OS </td>
        <td>Ubuntu </td>
        <td>20.04</td>
        <td><a href="https://ubuntu.com/download/desktop">Download Link</a></td>
    </tr>
    <tr>
        <td>Bigdata framework </td>
        <td>Apache Hadoop</td>
        <td>3.1.2</td>
        <td><a href="https://archive.apache.org/dist/hadoop/common/">Download Link</a></td>
    </tr>
    <tr>
        <td>Database </td>
        <td>Apache Hive</td>
        <td>3.1.2</td>
        <td><a href="https://archive.apache.org/dist/hive/">Download Link</a></td>
    </tr>
    <tr>
        <td>ETL Tool</td>
        <td>Apache NiFi</td>
        <td>1.16.0</td>
        <td><a href="https://archive.apache.org/dist/nifi/">Download Link</a></td>
    </tr>
</table>

## Set up Big Data 
The following section briefly describes the required steps to configure Hadoop and Hive. For set up, different .xml and .env files need to be configured. The details installion tutorial links are pasted with each section. On top of that cross check with the <a href="https://github.com/asifuzzamann8/ETL-Workflow-using-Apache-NiFi-/blob/442b7bf06d3db09aa6e2362aca026fbed06ea0a0/Project%20Glossary.docx">Glossary File</a> for any additional configuration and essential parts included for this project. Copy of my configuration files are also shared in the <a href="https://github.com/asifuzzamann8/ETL-Workflow-using-Apache-NiFi-/tree/main/Configs">Configs</a> folder. 




### Install VMware and Os:
VMware is installed on a Windows machine (Laptop with six cores and 24GB memory). Although the procedure is simple, the memory and process allocation should be done accordingly. 8GB of memory, three cores, and 30GB of space are allocated for this project.

VM and Ubuntu installation guide: <a href="https://unixcop.com/how-to-install-ubuntu-21-04-on-vmware-workstation-pro/">Click Here</a>

### Hadoop:
As a prerequisite for Hadoop, JDK 8 and OpenSHH needs to be installed. A separate os user is created for better management and security. Hadoop is downloaded from the mentioned link. The linux bash profile and configuration files should be updated with caution. The required commands are given in the glossary.     

Hadoop installation guide: <a href="https://phoenixnap.com/kb/install-hadoop-ubuntu">Click Here</a>

### Hive:
Apache Hive is a data warehouse software project built on Apache Hadoop to provide SQL query and analysis features. In the backend, it runs a map-reduce process to extract data from HDFS. Hive is installed to store and manage the data for further analysis.  

Hive requires a conventional relational DB to store the necessary metadata for its management. The default installation comes with a derby database. However, accessing Hive from external tools or servers requires concurrent sessions. HiveServer2 facilitates the necessary services. It requires MySQL database as the metadatabase. Special care should be given to download the correct version of MySQL JDBC connector. The detailed steps are given in the glossary. 

Hive installation guide: <a href="https://phoenixnap.com/kb/install-hive-on-ubuntu">Click Here</a>
HiveServer2 config details: <a href="https://cwiki.apache.org/confluence/display/Hive/Setting+Up+HiveServer2#SettingUpHiveServer2-HiveServer2">Click Here</a>
HiveServer2 config: <a href="https://youtu.be/BZAfoQMrkmk">Youtube Tutorial</a> 

### NiFi:
Apache NiFi was built to automate the flow of data between systems. It supports almost all the databases and sources with a GUI-based data flow design facility that is easy to understand and manage. Also, the data flow can be saved and imported as a template to build redundant flows. It scales up the development time. NiFi is backed by ZooKeeper and can be worked in the distributed cluster.  

NiFi is developed to manage huge data volumes with high throughput and low latency. It is advised to install NiFi on a separate server with dedicated raid space for logs and contents for the production environment. However, the same server is used for this project. The archive configuration and Java heap size need to be changed to run it smoothly. The log files need to be checked regularly for warnings.  

NiFi installation Guide: <a href="https://nifi.apache.org/docs/nifi-docs/html/getting-started.html">Youtube Tutorial</a> 

### Manage Services:
#### Start:
Once installed and configured, the services can be started with below commands in terminal.
```
cd /home/hadoop/hadoop-3.1.2/sbin
./start-dfs.sh
./start-yarn.sh
hive --service metastore
hiveserver2
sudo service nifi start
```

#### Stop:
```
stop-dfs.sh 
stop-yarn.sh
sudo service nifi stop
```

#### Service Portals: 
From the same VM below URLs can be access through browser.<br>
namenode: http://localhost:9870<br>
datanode: http://localhost:9864<br>
yarn manager: http://localhost:8088<br>
hive: http://localhost:10002/<br>
nifi: https://localhost:8443/nifi/login

## Hive Database Setup
The destination tables are created before workflow design. Both regular table and external table is created with same table structure. The purpose will be discussed in the following sections.

### Access through Terminal
```
beeline -u jdbc:hive2://localhost:10000
```
### Create Database:
```
CREATE DATABASE ETL;
SHOW DATABASES;
USE ETL;
```

### Create Normal Hive Table:
```
CREATE TABLE IF NOT EXISTS etl.uci_ransomware (address string, year_at int, day_at int, length int, weight string, count_of int, looped int, neighbors int, income string, label string, ransomware int)
ROW FORMAT DELIMITED 
FIELDS TERMINATED BY ',';

CREATE TABLE IF NOT EXISTS etl.uci_ransomware_v2 (address string, year_at int, day_at int, length int, weight string, count_of int, looped int, neighbors int, income string, label string, ransomware int)
ROW FORMAT DELIMITED 
FIELDS TERMINATED BY ',';
```

### External Table Set Up:
From terminal create HDFS Location and Structure.
```
hdfs dfs -mkdir -p /user/hive/uci_ransomware_ext
hdfs dfs -chmod g+w /user/hive/uci_ransomware_ext
hdfs dfs -ls /user/hive
```

### External Table Creation in Hive:
```
CREATE EXTERNAL TABLE IF NOT EXISTS etl.uci_ransomware_ext (address string, year_at int, day_at int, length int, weight string, count_of int, looped int, neighbors int, income string, label string, ransomware int)
ROW FORMAT DELIMITED 
FIELDS TERMINATED BY ','
STORED AS TEXTFILE
LOCATION '/user/hive/uci_ransomware_ext'
tblproperties ("skip.header.line.count"="1");
```

## ETL Workflow Development in NiFi
NiFi's fundamental design concepts closely relate to the main ideas of Flow-Based Programming. Data or "FlowFile" is moved from one step to another for required processing and transformation. Each task is completed by the "FlowFile Processor". Connection defines the relationship among processors. 

Details Overview of NiFi: <a href="https://nifi.apache.org/docs/nifi-docs/html/overview.html#the-core-concepts-of-nifi">Click Here</a>

<p>
    <img src="https://user-images.githubusercontent.com/99446979/214911261-02edd756-98ab-4a23-938a-9b1652157eee.png" alt><br>
    <em>Nifi Processors Design - Final Workflow<br>
        Blue: Common processors for Data Pulling<br> 
        Orange: Insert directly into Hive Table Using JDBC Connection<br>
        Green: Insert Using External Hive Table
    </em>
</p>

As shown above, total 10 FlowFile Processors are configured to complete all the steps discussed in the ETL Workflow Description. The marked blue processors are for data fetching. Data transform and loading in Hive table is performed in two different methods (Marked green and orange). The processes are described in the following sections.

### Common Processors for Data Pulling:

#### InvokeHTTP:
It is an HTTP client processor which can interact with a configurable HTTP endpoint. It is capable of processing API requests. SSL certificate needs to be downloaded from the site and configured in the processor to fetch data from Rest API/HTTPs. The figure below shows the required configuration, including URL, HTTP Method (Get/post), SSL Context Service, and others. <a href="https://www.youtube.com/watch?v=Jk7H8w3evN0">Youtube Tutorial</a> for the required process to configure the processor and SSL certificate.

![InvokeHTTP](https://user-images.githubusercontent.com/99446979/214915398-944489f0-8760-4c06-820a-87cf74e9c96d.png)

#### UnpackContent:
This processor takes a compressed file as an input and delivery uncompressed files as output. The compression type and file name can be filtered from this processor. 

![UnpackContent](https://user-images.githubusercontent.com/99446979/214915742-88632cc7-286b-44cd-bc17-3554ce45dcca.png)

#### PutFile:
The uncompressed file is forwarded to the PutFile processor to store it in the local file system. 

![PutFile](https://user-images.githubusercontent.com/99446979/214915969-b139a317-2686-426e-ad60-cfcab2565950.png)

### Insert directly into Hive Table Using JDBC Connection: 
This method ingests data in the Hive table straight from the NiFi application using the Hive JDBC connection.

Twitter Data Example: <a href="https://www.velotio.com/engineering-blog/building-an-etl-workflow-using-apache-nifi-and-hive">Click Here</a>

#### ExecuteStreamCommand (ExecutePythonScript): 
This processor can execute external commands on the content of the FlowFile and creates a new FlowFile with the results. The FlowFile content in the input can be accessed as STDIN, and the processor can forward STOUT from the command as an output to the next processor. 

The below figure shows the configuration of the processor. It takes a python script as the command. The python script takes the STDIN and updates the dataset with an additional "Ransomware" flag column based on the label value. In addition, it supports code blocks (Groovy, Jython, Javascript, JRuby) instead of the script from the local machine.

![ExecuteStreamCommand](https://user-images.githubusercontent.com/99446979/214926076-908b9a45-5d9c-46c5-ab13-858ef2b298a6.png)

#### ReplaceText (RenameHeader):
The ReplaceText processor is used to rename the header names with system keywords like year, day, and count.

![ReplaceText](https://user-images.githubusercontent.com/99446979/214926335-587dd914-d88f-4acd-9fb3-c2403ed8b1ea.png)

#### QueryRecords (FilterRecords):
QueryRecords processor can perform SQL-like queries directly on the FlowFile content. Also, the data format can be changed with this processor. In this case, the CSV format is converted into JSON for further processing compatibility. Record Reader/Writer value needs to be configured with the arrow sign on the right. In this figure, a new property "data" is included with the "+" sign in the top right corner, and an SQL query is provided as an input. The SQL query should not have any ";" at the end as the processor.

![QueryRecords](https://user-images.githubusercontent.com/99446979/214926646-54e48248-7ee9-4729-bb33-239118e7910d.png)

#### ConvertJSONToSQL:
This processor transforms each entry of the JSON file into an SQL INSERT statement. The database JDBC connection pool needs to be created for this processor. The detail of the configuration is given below. Database connection URL, Database user, and Password are provided. The path of hive-site.xml should be provided in the Hive configuration resources box. Although it is not a mandatory parameter, without the Validation query "Select 1 as Test_column" the connection cannot be established.   
Moreover, table and schema names need to be provided as input. Also, SQL parameter attributes have to be defined. In this case, "hiveql" is the correct input. The output FlowFile is a queue of insert statements. The hive table creation DDL is given in the glossary. 

![HiveConnectionPool](https://user-images.githubusercontent.com/99446979/214927100-186ef1b4-4706-4940-a1ca-6c89980e0b92.png)

![ConvertJsonToSQL](https://user-images.githubusercontent.com/99446979/214927222-5389d846-0f27-4b13-8505-c1031d970d72.png)

#### PutHiveQL:
It receives insert statements as input in the FlowFile and executes it in the Hive database through a JDBC connection.

![PutHiveQL](https://user-images.githubusercontent.com/99446979/214927354-0ad6c002-9043-4fdd-a9a2-e12e0ca25ad0.png)

Once completed, all records will be inserted in Hive. 

### Insert Using External Hive Table:
The aforementioned process executes single insert statements in a queue. It requires a lot of time due to JDBC connection overhead. In addition, Hive works differently than transactional databases and is not suitable for single insert statements. Hence, to improve the data insertion time below method is proposed using Hive external table functionality. 

In this method, CSV data is transferred into a file location of HDFS. A Hive external table is defined in the database, which points to the same directory, and the table properties should match the columns and delimiter of the CSV file. Basically, the external table is an abstraction that presents the data in the CSV file as a table. However, it doesn't hold any information. The data will stay in the CSV file even if the external table architecture is dropped. Then an insert statement from the external table to the normal Hive table transfers all the data into the database. Since the operation happens within the HDFS, the execution time is much faster than the JDBC connection request.   

#### ExecuteStreamCommand (ExecuteShellScript):
A shell script is called using this processor to add the Ransomware flag column in the dataset and transfer the updated CSV file to the HDFS location. 

![ExecuteShellScript](https://user-images.githubusercontent.com/99446979/214928795-722ac385-b453-42bc-aaa2-056ce3880875.png)

#### SelectHiveQL (InsertFromExtrenalTable):
The SelectHiveQL has an additional property, "HiveQL Post-Query". This property is used in this step to execute the insert statement from the external table to Hive table. For the primary "HiveQl Select Query", a dummy statement has been provided.

![SelectHiveQL](https://user-images.githubusercontent.com/99446979/214929080-f86f41c6-007c-49f6-8942-15e820c6ceec.png)

### Additional Configuration:
Please check the <a href="https://nifi.apache.org/developer-guide.html">NiFi Developer Manual</a> for proper configuration of the connections, loop back, and error handling. Also buffer, wait time, recurrence parameters need to be configured for each processor based on the requirements. 

## Execution and Results
The workflow can be scheduled based on event or time(cron). Once the starting point is executed, the workflow will be completed accordingly and data will be loaded in final table. The data can be accessed from Hive beeline editor. 

![Result](https://user-images.githubusercontent.com/99446979/214944963-f22b0d2c-fd66-4e92-8ed5-9cf30e54a2f1.png)

In this case, the external table method takes less than a minute to insert 2.9Mn records in the Hive database. In contrast, the JDBC connection takes 5 minutes to execute a batch of 1000 insert statements. Hence external table method should be used for bulk data insertion in the data warehouse environment.

## Conclusion:
Overall, NiFi is a reasonably simple ETL design tool. The GUI makes it easy to understand. The 200+ built-in processors serve all the purposes of modern data ingestion needs. The connections can hold the FlowFile in case of failure. It provides an efficient way to execute the workflow from the point of failure. Using Kafka, NiFi can serve the purpose of message queueing as well. Also, the custom script execution makes NiFi versatile to make any custom operations. However, it losses cache information if the primary node gets disconnected. NiFi cluster can solve this problem. The configuration and resource allocation is the most important thing while working with Big Data platforms.



