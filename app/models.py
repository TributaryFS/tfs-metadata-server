from uuid import uuid4

from sqlalchemy import (
    BigInteger,
    Column,
    DateTime,
    Enum,
    Float,
    ForeignKey,
    Integer,
    String,
    UniqueConstraint,
    func,
)
from sqlalchemy.dialects.postgresql import INET, UUID

from app.db import Base
from app.enums import ChunkStatus, Cluster, NodeStatus, PermissionLevel
from config_reader import CONFIG


class User(Base):
    __tablename__ = "users"
    __table_args__ = (UniqueConstraint("username", name="uq_user_username"),)

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    username = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(
        DateTime(timezone=True), onupdate=func.now(), server_default=func.now()
    )


class Directory(Base):
    __tablename__ = "directories"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = Column(String, nullable=False)


class DirectoryPermission(Base):
    __tablename__ = "directory_permissions"
    __table_args__ = (
        UniqueConstraint("directory_id", "user_id", name="uq_directory_permission"),
    )

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    directory_id = Column(UUID(as_uuid=True), ForeignKey("directories.id"), nullable=False)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    permission_level = Column(Enum(PermissionLevel), nullable=False)


class DirectorySubdirectoryAssociation(Base):
    __tablename__ = "directory_subdirectory_associations"
    __table_args__ = (
        UniqueConstraint(
            "parent_directory_id",
            "child_directory_id",
            name="uq_directory_hierarchy_parent_child",
        ),
    )

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    parent_directory_id = Column(
        UUID(as_uuid=True), ForeignKey("directories.id"), nullable=False
    )
    child_directory_id = Column(
        UUID(as_uuid=True), ForeignKey("directories.id"), nullable=False
    )


class File(Base):
    __tablename__ = "files"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = Column(String, nullable=False)
    checksum = Column(String, nullable=False)
    size = Column(BigInteger, nullable=False)
    version = Column(Integer, nullable=False, default=1)
    last_modified = Column(DateTime(timezone=True), nullable=False)
    last_modified_by = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(
        DateTime(timezone=True), onupdate=func.now(), server_default=func.now()
    )


class DirectoryFileAssociation(Base):
    __tablename__ = "file_directory_associations"
    __table_args__ = (
        UniqueConstraint("file_id", "directory_id", name="uq_file_directory"),
    )

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    file_id = Column(UUID(as_uuid=True), ForeignKey("files.id"), nullable=False)
    directory_id = Column(UUID(as_uuid=True), ForeignKey("directories.id"), nullable=False)


class FilePermission(Base):
    __tablename__ = "file_permissions"
    __table_args__ = (UniqueConstraint("file_id", "user_id", name="uq_file_permission"),)

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    file_id = Column(UUID(as_uuid=True), ForeignKey("files.id"), nullable=False)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    permission_level = Column(Enum(PermissionLevel), nullable=False)


class Chunk(Base):
    __tablename__ = "chunks"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    checksum = Column(String, nullable=False)
    actual_size = Column(BigInteger, nullable=False)
    stored_size = Column(BigInteger, nullable=False)
    encryption_key_id = Column(String, nullable=False)
    logical_offset = Column(BigInteger, nullable=False)
    reference_count = Column(Integer, nullable=False, default=1)
    current_replica_count = Column(
        Integer, nullable=False, default=0, max=CONFIG.MAX_CHUNK_REPLICA
    )
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(
        DateTime(timezone=True), onupdate=func.now(), server_default=func.now()
    )


class FileChunkAssociation(Base):
    __tablename__ = "file_chunk_associations"
    __table_args__ = (UniqueConstraint("file_id", "chunk_id", name="uq_file_chunk"),)

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    file_id = Column(UUID(as_uuid=True), ForeignKey("files.id"), nullable=False)
    chunk_id = Column(UUID(as_uuid=True), ForeignKey("chunks.id"), nullable=False)
    chunk_index = Column(Integer, nullable=False)


class Node(Base):
    __tablename__ = "nodes"
    __table_args__ = (UniqueConstraint("ip", "port", name="uq_node_ip_port"),)

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    hostname = Column(String, nullable=False)
    ip = Column(INET, nullable=False)
    port = Column(Integer, nullable=False)
    last_heartbeat = Column(DateTime(timezone=True), nullable=True)
    status = Column(Enum(NodeStatus), nullable=False)
    total_storage = Column(Float, nullable=False)
    used_storage = Column(Float, nullable=False)
    remaining_storage = Column(Float, nullable=False)
    rack_id = Column(String, nullable=True)
    cluster = Column(Enum(Cluster), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(
        DateTime(timezone=True), onupdate=func.now(), server_default=func.now()
    )


class ChunkReplica(Base):
    __tablename__ = "chunk_replicas"
    __table_args__ = (
        UniqueConstraint("chunk_id", "node_id", name="uq_chunk_replica_chunk_id_node_id"),
    )

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    chunk_id = Column(UUID(as_uuid=True), ForeignKey("chunks.id"), nullable=False)
    node_id = Column(UUID(as_uuid=True), ForeignKey("nodes.id"), nullable=False)
    replica_index = Column(
        Integer, nullable=False, default=0, max=CONFIG.MAX_CHUNK_REPLICA - 1
    )
    status = Column(Enum(ChunkStatus), nullable=False, default=ChunkStatus.PENDING)
    path = Column(String, nullable=False)
    last_verified = Column(DateTime(timezone=True), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(
        DateTime(timezone=True), onupdate=func.now(), server_default=func.now()
    )
