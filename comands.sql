! pg_hba.conf
host    replication     all             0.0.0.0/0               scram-sha-256

! Conecte ao psql
# psql -U admin -d enem

! Rode
create role repuser with replication password 'repuser';
grant select on all tables in schema public to repuser;
GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA public TO repuser; 
alter default privileges in schema public grant select on tables to repuser;
select pg_create_physical_replication_slot('master_replication_slot');
alter role repuser login;

! postgresql.conf
primary_conninfo = 'host=db-master port=5432 user=repuser password=repuser'	
primary_slot_name = 'master_replication_slot'	
 
! rode no container replica
pg_basebackup -h db-master -U repuser -D /var/lib/postgresql/data -v -P -X s -c fast


  db-replication-1:
    image: postgres:15
    ports:
      - target: 5432
        published: 5434
        protocol: tcp
        mode: host
    environment:
      POSTGRES_DB: enem
      POSTGRES_USER: repuser
      POSTGRES_PASSWORD: repuser
      POSTGRES_HOST: db-replication-1
      PGDATA: /tmp
    volumes:
      - ./replication:/var/lib/postgresql/ata
      - type: tmpfs
        target: /dev/shm

    container_name: postgres_db_replication_1
