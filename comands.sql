
-- Cria slot de replicacao --
SELECT pg_create_physical_replication_slot('slot_replication_name');


pg_basebackup -h host -U user -D /var/lib/postgresql/data -v -P -X s -c fast

primary_conninfo = 'host=host port=5432 user=user password=password'