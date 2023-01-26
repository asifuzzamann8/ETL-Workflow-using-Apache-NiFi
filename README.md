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
The following section briefly describes the required steps to configure Hadoop and Hive. Configuration files are shared in folders. Essential commands are added to the glossary file.

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

## ETL Workflow Development in NiFi:
NiFi's fundamental design concepts closely relate to the main ideas of Flow-Based Programming. Data or "FlowFile" is moved from one step to another for required processing and transformation. Each task is completed by the "FlowFile Processor". Connection defines the relationship among processors. 

Details Overview of NiFi: <a href="https://nifi.apache.org/docs/nifi-docs/html/overview.html#the-core-concepts-of-nifi">Click Here</a>

![Picture1](https://user-images.githubusercontent.com/99446979/214911261-02edd756-98ab-4a23-938a-9b1652157eee.png)






  


