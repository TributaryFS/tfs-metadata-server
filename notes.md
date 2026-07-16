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