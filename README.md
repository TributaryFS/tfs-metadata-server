# TributaryFS
A production-grade distributed file transfer and storage system inspired by Dropbox and HDFS.

## TODO
- [ ] Phase 1:
    - [x] Design Schema for director and file namsespace
    - [x] User create and update routes
    - [ ] User Login Session flow
    - [ ] Directory/Files create routes with permission handling
    - [ ] Node/Chunk create and update routes
    - [ ] Design File version schema and flow
    - [ ] Upload Session create and resume and cancel route
    - [ ] Upload Same File new/same version handling
    - [ ] Add/Remove permissions handling
    - [ ] Design Delete flow for all apps 
    - [ ] Implement Delete flow
    - [ ] Phase 1 Test Integration
- [ ] Phase 2:
    - [ ] Design client cli
    - [ ] Register user commands in cli
    - [ ] List and traverse directory structure commands in cli
    - [ ] Create light FastAPI server for chunk upload to node machine
        - [ ] Create endpoints on metadata server for node<->metadata_server communication
    - [ ] File Upload flow in cli
        - [ ] Get file metadata/upload session from metadata server
        - [ ] Write simple chunking algo
        - [ ] Upload chunks to node code in cli
    - [ ] Implement Directory upload in cli
    - [ ] Implement File/Directory sharing in cli
    - [ ] Implement File/Directory Download routes in Metadata server and node server
    - [ ] Implement File/Directory Download in cli
    - [ ] Implement File/Directory delete in cli
    - [ ] Phase 2 Test Integration
- [ ] Phase 3:
    - [ ] Background workers using celery for upload and download
    - [ ] Implement Benchmarking Suite  
        - [ ] Bench mark File Upload/Download
    - [ ] Create Node setup service/script
        - [ ] Design and creata light weight dockerfile for node docker image
        - [ ] Create route to setup Node (copy importanct scripts, create cron jobs etc). Call this on Node creation route also
        - [ ] Metadata server web page to manage nodes
        - [ ] Simple bash script to create spin up containers as nodes
    - [ ] Implement Replication Manager Service
    - [ ] Bench node<=>node replication of chunks
    - [ ] Create a Grabage Collector Service
        - [ ] Implements Check for orphaned/deleted Directories, File and Chunks.
        - [ ] excuted delete over ssh in node-machines of found chunks , update db
        - [ ] Remove Directory/File/Chunk from db
        - [ ] Remove oldest File if file version count above max version
    - [ ] Implement Scheduler Service(node selection , free space, load balancing)
     - [ ] Phase 3 Test Integration
- [ ] Phase 4:
    - [ ] Implement HeartBeat and Status Manager/Service for nodes(Control Plane)
    - [ ] Implement Intergrity check service for chunks
    - [ ] Explore Encryption algos and implement encryption in chunking
    - [ ] Explore Compression algos and implement compression in chunking
    - [ ] Benchmarking File Upload/Download
    - [ ] Implement Content-Defined Chunking (CDC)
        - [ ] Explore CDC algos
        - [ ] Implement logical offset chunking
    - [ ] Phase 4 Test Integration
- [ ] TBD: 
    - [ ] Implement key management service and dek for encrpytion
    - [ ] pre commit
    - [ ] CI/CD


## High-Level Architecture

```
                    +----------------------+
                    |   React Dashboard    |
                    +----------+-----------+
                               |
                      HTTPS + WebSockets
                               |
+-----------+         +--------v--------+
| CLI Client| ------> | Metadata Server |
+-----------+  HTTPS  +--------+--------+
                               |
                    PostgreSQL / Redis
                               |
          Upload Session & Chunk Assignment
                               |
         +---------------------+----------------------+
         |                     |                      |
         |   Custom TCP        |   Custom TCP         |
         |                     |                      |
+--------v------+    +---------v------+    +----------v------+
| Storage Node A|    | Storage Node B |    | Storage Node C  |
+---------------+    +----------------+    +-----------------+
         ^                    ^                      ^
         |<------ Replication / Heartbeats --------->|
               
```
---