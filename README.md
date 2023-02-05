## Quick start guide

1. Clon repo to your machine

2. To start airflow run following command:
```bash
docker compose up
```

Airflow credentials: ``airflow/airflow``.


To stop and remove airflow containers run following command in extra terminal:
```shell
docker compose down
```

To connect to postgres instance with data use following credentials:
```yaml
host: localhost
port: 5438  # set it to 5432 for Airflow Connection
user: postgres
password: postgres
```

3. Start API
4. Check workability of dt filter without table order_status_stats
5. Check CRUDs (try craziest variants - need to crack validators)
6. Trigger DAG with creation and fullfilling order_status_stats
7. Check workability of dt filter


