import os
from sqlalchemy import create_engine
from typing import List, Optional, Dict
from sqlalchemy.sql import text


class Engine:
    def __init__(self):
        # self.engine = create_engine(os.getenv('DATABASE_URL'))
        self.engine = create_engine('postgresql://postgres:postgres@data:5432/postgres')

    def get_engine(self):
        return self.engine

    def dispose(self):
        self.engine.dispose()


class Connection:
    def __init__(self, engine):
        self.conn = engine.get_engine().connect()

    def execute(self, sql) -> List[Optional[Dict]]:
        result = self.conn.execute(text(sql))
        rows = result.fetchall()
        return [dict(zip(result.keys(), row)) for row in rows]

    def execute_no_result(self, sql):
        self.conn.execute(text(sql))

    def close(self):
        self.conn.close()


eng = Engine()
conn = Connection(eng)
