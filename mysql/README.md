#### Show slow query log
>show global variables like '%slow%';

#### Show full process list
>SHOW PROCESSLIST;

#### Kill the process
> KILL PID;

#### Move a table from a database to another
> ALTER TABLE my_old_db.mytable RENAME my_new_db.mytable


#### 
CREATE INDEX emp_class ON employee(class_id);