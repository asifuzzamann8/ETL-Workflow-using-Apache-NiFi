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


  


