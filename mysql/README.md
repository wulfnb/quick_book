#### Show slow query log
>show global variables like '%slow%';

#### Show full process list
>SHOW PROCESSLIST;

#### Kill the process
> KILL PID;

#### Move a table from a database to another
> ALTER TABLE my_old_db.mytable RENAME my_new_db.mytable


#### 
SHOW INDEX FROM <table_name>;


CREATE INDEX <to_table> ON <on_table>(<on_field>);

DROP INDEX <index_name> ON <table_name>;