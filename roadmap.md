# TributaryFS

## Goal
A production-grade distributed file transfer and storage system inspired by Dropbox and HDFS.

## TODO
- [ ] Phase 1: Basic CLI to upload/download
    - [ ] Design Schema for director and file namsespace
    - [ ] Metadata server routes /upload /download etc
    - [ ] Upload files
    - [ ] Download files
    - [ ] Folder upload
    - [ ] Folder download
    - [ ] Progress bar
    - [ ] Pause transfer
    - [ ] Resume transfer
    - [ ] Cancel transfer
- [ ] Phase 2:
    - [ ] chunking
    - [ ] implement Content-Defined Chunking (CDC) Common algorithms:
            Rabin Fingerprint
            Buzhash
            Gear Hash (FastCDC)
            AE Hash
    - [ ] implement encryption
    - [ ] grabage collection of chunks using ref_count 
- [ ] Phase 3:
    - [ ] retention policies ma versions and max time limit  
- [ ] Phase 4:
    - [ ] Implement key management service and dek for encrpytion
- [ ] Phase 5:

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
                (TCP initially, gRPC as stretch)
```
---

## Upload Workflow

1. Client requests an upload session from the Metadata Server.
2. Metadata Server determines:
   - Chunk size
   - Chunk IDs
   - Storage node assignment
3. Client splits the file into chunks.
4. Client opens TCP connections directly to storage nodes.
5. Storage nodes verify, compress (optional), encrypt (optional), and persist chunks.
6. Storage nodes acknowledge successful writes.
7. Metadata Server commits the completed upload.
---
## Storage Pipeline

For each uploaded file:

```
File
    ↓
Chunk
    ↓
SHA256 (logical hash)
    ↓
Deduplication
    ↓
Compress (optional)
    ↓
Encrypt (optional)
    ↓
Store
```
## Communication

### Client → Metadata Server

- HTTPS
- REST APIs
- JWT Authentication

### Client → Storage Node

- Custom Binary TCP Protocol
- High-throughput streaming
- Parallel chunk uploads
- Resume support

### Storage Node ↔ Storage Node

Initially:

- Custom TCP

Future:

- gRPC
- Streaming replication
- Heartbeats
- Replica synchronization

### Dashboard

- HTTPS
- WebSockets for live cluster updates

---

## Design Philosophy

The system separates metadata management from actual data transfer.

### Control Plane

Responsible for coordination and cluster management.

Implemented using **FastAPI (HTTPS)**.

Responsibilities:

- Authentication
- Upload/download session creation
- File & directory namespace
- Chunk metadata
- Chunk placement decisions
- Node discovery
- Replication metadata
- Cluster health
- User management

The metadata server **never stores file data**.

---

### Data Plane

Responsible for transferring and storing file chunks.

Implemented using a **custom TCP protocol**.

Responsibilities:

- Upload chunk
- Download chunk
- Chunk verification
- Replication
- Chunk migration
- Resume interrupted transfers
- Storage health

Clients communicate directly with storage nodes after obtaining upload instructions from the metadata server.




it does not support sparse files 

