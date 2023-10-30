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

! postgresql.conf
primary_conninfo = 'host=db-master port=5432 user=repuser password=repuser'	
primary_slot_name = 'master_replication_slot'	
