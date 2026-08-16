from uuid import uuid4

from apps.storage.choices import ChunkStatus, Cluster, NodeStatus
from django.db import models


class Chunk(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    checksum = models.CharField(max_length=255, null=False)
    actual_size = models.BigIntegerField(null=False)
    stored_size = models.BigIntegerField(null=False)
    encryption_key_id = models.CharField(max_length=255, null=False)
    reference_count = models.IntegerField(null=False, default=1)
    replica_count = models.IntegerField(null=False, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "chunks"


class Node(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    hostname = models.CharField(max_length=255, null=False)
    ip_address = models.GenericIPAddressField(null=False)
    port = models.IntegerField(null=False)
    last_heartbeat = models.DateTimeField(null=True)
    status = models.CharField(choices=NodeStatus.choices, null=False)
    total_storage = models.BigIntegerField(null=False)
    used_storage = models.BigIntegerField(null=False)
    remaining_storage = models.BigIntegerField(null=False)
    rack_id = models.CharField(max_length=255, null=True)
    cluster = models.CharField(choices=Cluster.choices, max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "nodes"
        constraints = [  # noqa: RUF012
            models.UniqueConstraint(
                fields=["ip_address", "port"], name="uq_node_ip_port"
            ),
        ]


class ChunkReplica(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    chunk = models.ForeignKey(
        "storage.Chunk", on_delete=models.CASCADE, related_name="replicas"
    )
    node = models.ForeignKey(
        "storage.Node", on_delete=models.CASCADE, related_name="chunk_replicas"
    )
    replica_index = models.IntegerField(null=False, default=0)
    status = models.CharField(choices=ChunkStatus.choices, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "chunk_replicas"
        constraints = [  # noqa: RUF012
            models.UniqueConstraint(
                fields=["chunk", "node"], name="uq_chunk_replica_chunk_id_node_id"
            ),
        ]
