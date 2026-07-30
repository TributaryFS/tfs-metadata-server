# TributaryFS

Distributed File System + Parallel File Transfer (Python)

Eg: Dropbox, HDFS, rsync

[https://github.com/mochivi/distributed-file-system](https://github.com/mochivi/distributed-file-system)

**One suggestion:** Since you're targeting companies like Mastercard, Rubrik, Stripe, and Databricks, I'd make this even more "production-like" by splitting it into **microservices** (Metadata Service, Storage Service, Transfer Service, Auth Service, Monitoring Service) instead of a single application. That architectural decision alone will make the project much stronger in interviews and system design discussions.

## Goal

Build a production-grade distributed file transfer and storage system inspired by Dropbox, HDFS, and rsync.

The project should demonstrate:

- Distributed Systems
- Network Programming
- Concurrent Programming
- Storage Systems
- Fault Tolerance
- System Design
- Production-grade Backend Engineering

---
pluggable node selection algorithms.
frames
upload sessions
encryption iv will be first  12 bytes and tag will be last 16 bytes.
# Tech Stack bytes and tag will be last 

## Backend

- Python
- FastAPI
- AsyncIO
- ThreadPoolExecutor
- Multiprocessing

## Networking

- TCP Sockets
- HTTP/REST
- WebSockets (optional)
- gRPC (stretch)

## Databases

- PostgreSQL
- Redis

## Storage

- Local File Storage
- S3 Compatible Storage (stretch)

## Infrastructure

- Docker
- Docker Compose
- Kubernetes (stretch)

## Monitoring

- Prometheus
- Grafana

Project:
TributaryFS

Coordinator:
Headwaters

Storage Nodes:
Tributaries

Replication Groups:
Basins

Entire Cluster:
Watershed

Garbage Collector:
Sediment Cleaner

Chunk Migration:
Current

---

# Phase 1 — Basic File Transfer

### Features

- Upload files
- Download files
- Folder upload
- Folder download
- Progress bar
- Pause transfer
- Resume transfer
- Cancel transfer

### Learning

- TCP sockets
- File streams
- Binary data transfer

---

# Phase 2 — Chunked Transfers

Split files into chunks.

### Features

- Configurable chunk size
- Chunk metadata
- Chunk IDs
- Chunk ordering

Example

```
movie.mp4

↓

chunk0
chunk1
chunk2
...
chunkN
```

### Learning

- Chunking strategies
- Metadata management

---

# Phase 3 — Parallel Uploads

Upload multiple chunks simultaneously.

### Features

- Thread pool
- Configurable workers
- Parallel uploads
- Parallel downloads

Example

```
Worker 1 -> Chunk 0
Worker 2 -> Chunk 1
Worker 3 -> Chunk 2
Worker 4 -> Chunk 3
```

### Learning

- Thread pools
- Concurrency
- Synchronization

---

# Phase 4 — Resume Support

Resume interrupted uploads.

### Features

- Chunk acknowledgements
- Resume from failed chunk
- Partial upload tracking

Example

```
Chunk 0 ✔
Chunk 1 ✔
Chunk 2 ✖

↓

Resume from Chunk 2
```

### Learning

- Fault recovery
- State management

---

# Phase 5 — Integrity Verification

### Features

- SHA256 checksum
- Per-chunk verification
- Whole file verification

Example

```
Chunk

↓

SHA256

↓

Receiver verifies

↓

ACK
```

### Learning

- Hashing
- Data integrity

---

# Phase 6 — Compression

### Features

- Zstandard
- LZ4
- Configurable compression

Benchmark

- Compression ratio
- Throughput
- CPU usage

---

# Phase 7 — Encryption

### Features

- AES-256 Encryption
- Secure key management
- Initialization Vector (IV)

Pipeline

```
Chunk

↓

Encrypt

↓

Transfer

↓

Decrypt
```

### Learning

- Cryptography
- Secure transfers

---

# Phase 8 — Metadata Server

Create a centralized metadata service.

### Stores

- File name
- Owner
- Chunk locations
- File size
- Checksums
- Permissions

### APIs

```
POST /upload

GET /download

GET /metadata

DELETE /file
```

### Learning

- FastAPI
- Database schema design

---

# Phase 9 — Storage Nodes

Store chunks across multiple nodes.

Architecture

```
Client

↓

Metadata Server

↓

Storage Node A
Storage Node B
Storage Node C
```

### Learning

- Distributed storage
- Node communication

---

# Phase 10 — Replication

Replicate chunks.

Example

```
Chunk 15

↓

Node A

↓

Node B

↓

Node C
```

Configurable

```
Replication Factor = 3
```

### Learning

- High availability
- Replication strategies

---

# Phase 11 — Failure Recovery

### Features

- Node heartbeat
- Health checks
- Replica recovery
- Automatic failover

Scenario

```
Node B fails

↓

Serve from Replica

↓

Create new replica
```

### Learning

- Fault tolerance
- Recovery algorithms

---

# Phase 12 — Load Balancing

Store chunks intelligently.

Selection based on

- Free space
- CPU usage
- Disk usage
- Network latency

### Learning

- Scheduling
- Load balancing

---

# Phase 13 — Deduplication

Reuse identical chunks.

Pipeline

```
Chunk

↓

SHA256

↓

Already exists?

↓

Reuse existing chunk
```

### Learning

- Content-addressable storage

---

# Phase 14 — Versioning

### Features

```
resume.pdf

↓

v1

↓

v2

↓

v3
```

Support

- Rollback
- History
- Restore

---

# Phase 15 — Authentication

### Features

- JWT
- User login
- Roles

Permissions

- Read
- Write
- Delete
- Admin

---

# Phase 16 — Monitoring

Collect metrics.

### Prometheus Metrics

- Upload speed
- Download speed
- Chunk latency
- Active uploads
- Failed uploads
- Storage usage
- Replication lag

Visualize using Grafana.

---

# Phase 17 — Retry Logic

### Features

- Retry failed chunks
- Exponential backoff
- Timeout handling
- Dead connection detection

---

# Phase 18 — Web Dashboard

React Dashboard

Features

- Upload manager
- Download manager
- Storage nodes
- Cluster health
- Active transfers
- File browser
- User management
- Metrics dashboard

---

# Phase 19 — Docker

Docker Compose setup

Services

- Metadata Server
- PostgreSQL
- Redis
- Storage Node A
- Storage Node B
- Storage Node C

---

# Phase 20 — Kubernetes

Deploy

- Metadata API
- Storage Nodes
- PostgreSQL
- Redis

Features

- Persistent Volumes
- Autoscaling
- Rolling Updates
- Ingress

---

# Testing

## Unit Tests

- Chunking
- Hashing
- Compression
- Encryption

## Integration Tests

- Upload
- Download
- Resume
- Replication

## Chaos Tests

- Kill storage node during upload
- Network interruption
- Disk full
- Metadata server restart

---

# Benchmarking

Benchmark

- 1 GB
- 5 GB
- 10 GB
- 100 GB

Measure

- Throughput
- CPU usage
- Memory usage
- Network bandwidth
- Chunk latency
- Replication overhead

---

# Stretch Goals

- gRPC between services
- Erasure Coding
- S3-compatible API
- WebDAV support
- Delta Synchronization (rsync-like)
- File Search
- Audit Logs
- Rate Limiting
- Multi-region replication
- Content Addressable Storage
- Pluggable Storage Backends (Local, S3, MinIO)

---

# Skills Demonstrated

- Python
- FastAPI
- AsyncIO
- Threading
- Multiprocessing
- TCP Networking
- Distributed Systems
- REST APIs
- PostgreSQL
- Redis
- Docker
- Kubernetes
- Cryptography
- Compression
- System Design
- Fault Tolerance
- Scalability
- Monitoring & Observability
- Production Engineering

> 
> 
> 
> # Not every file benefits
> 
> Suppose the user uploads
> 
> ```
> movie.mp4
> ```
> 
> It's already compressed.
> 
> Trying to compress it again:
> 
> ```
> 100 MB
> 
> ↓
> 
> 99 MB
> ```
> 
> You wasted CPU.
> 
> Same for
> 
> - JPG
> - PNG
> - MP4
> - ZIP
> - RAR
> - 7z
> - PDF (many PDFs)
> - Parquet
> 
> These formats are already compressed.
> 
> ---
> 
> # Real systems detect this
> 
> Many storage systems either:
> 
> - don't compress certain MIME types
> - sample the first few KB
> - attempt compression and reject it if the ratio is poor
> 
> For example
> 
> ```
> Compression Ratio
> 
> compressed_size / original_size
> ```
> 
> If
> 
> ```
> 98%
> ```
> 
> they simply store the original.
>

Project:
TributaryFS

Coordinator:
Headwaters

Storage Nodes:
Tributaries

Replication Groups:
Basins

Entire Cluster:
Watershed

Garbage Collector:
Sediment Cleaner

Chunk Migration:
Current


UploadSession
--------------
id
user_id
file_id (nullable until committed)
status
total_chunks
uploaded_chunks
started_at
completed_at
expires_at

UploadChunk
-----------
session_id
chunk_index
chunk_checksum
status
assigned_node_id
retry_count

INITIATED

↓

PLANNING

↓

UPLOADING

↓

VERIFYING

↓

REPLICATING

↓

COMMITTING

↓

COMPLETED
FAILED
CANCELLED
EXPIRED         




FileUpload Workflow:
0. check client access to parent directory
1. client checks if file present with same local path
2. if yes -> check if  file ulpload session status is not complete
        if yes -> ask for resume or new upload
   if no -> if path is same and checksum is different , ask overwrite permission
         -> create a new file obj in db 
         -> change permission of older file obj version to orphan
         -> check chunk cheksums and send which chunks to upload on which node based on node availibilty
         -> if new file upload unsuccesful
            -> if due to unforseen error : revert permission status old file obj and ask client to re-upload
            -> if due to client cancellation: revert permission status old file obj  and delete new file obj
3. if file version above max-version-config then grabage collector remove oldest file obj ver and remove permission access for the same 


listdir Workflow:
0. check current dir perssioms
1. list all child files and sub-dirs for which user has atleat read access


```
logical_offset is the position (in bytes) where a chunk begins within the logical file.

It isn't required for your first version of TributaryFS, but it's a concept used in many storage systems.

Let's build it from first principles.

Suppose your chunk size is 4 MB

You have a 12 MB file.

movie.mp4

12 MB

After chunking:

Chunk 0   4 MB
Chunk 1   4 MB
Chunk 2   4 MB

Their positions in the file are:

Chunk	Starts at byte
Chunk 0	0
Chunk 1	4,194,304
Chunk 2	8,388,608

These starting positions are the logical offsets.

So your FileChunk table could look like
file_id	chunk_id	chunk_index	logical_offset
A	C1	0	0
A	C2	1	4,194,304
A	C3	2	8,388,608
Why not just use chunk_index?

For your project, you probably can.

If every chunk except the last is always exactly 4 MB:

logical_offset =
chunk_index × chunk_size

So

Chunk 5

↓

Offset = 5 × 4 MB = 20 MB

No need to store it.

When is logical_offset useful?

Imagine later you implement:

Variable-sized chunking (Content Defined Chunking)

Instead of fixed 4 MB chunks:

Chunk 0 -> 3.2 MB

Chunk 1 -> 4.7 MB

Chunk 2 -> 2.9 MB

Now

Chunk	Offset
0	0
1	3.2 MB
2	7.9 MB

You can't compute the offset from the index anymore.

Sparse files

Suppose a VM disk image has a 1 GB hole:

Chunk 0

↓

1 GB gap

↓

Chunk 1

Now

Chunk 1

offset = 1 GB

Even though it's only the second chunk.

Partial reads

Suppose a client asks:

Give me bytes

8 MB → 12 MB

The storage system can quickly determine which chunks overlap that byte range using their offsets.

Should TributaryFS have it?

For Version 1, I would not store logical_offset.

Instead, keep:

FileChunk

file_id

chunk_id

chunk_index

Since you're using fixed-size chunks, the offset is simply:

logical_offset = chunk_index * CHUNK_SIZE

Easy.

If you later add rsync-like synchronization or content-defined chunking

Then I'd extend the schema to:

FileChunk

file_id

chunk_id

chunk_index

logical_offset

At that point, logical_offset becomes valuable because chunk sizes are no longer fixed.

My recommendation

For the roadmap you're following:

✅ Keep chunk_index
❌ Skip logical_offset for now

It's one of those fields that becomes useful only when you move beyond fixed-size chunking into more advanced storage techniques. Starting without it keeps your schema simpler while leaving room to add it later if your design evolves.
```



Common CDC Algos:
    Rabin Fingerprint
    Buzhash
    Gear Hash (FastCDC)
    AE Hash

## High-Level Architecture

```
                    +----------------------+
                    |   React Dashboard    |
                    +----------+-----------+
                               |
                      HTTPS + WebSockets`
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

