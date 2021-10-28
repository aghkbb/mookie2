import psycopg2
import ast
import os
from dotenv import load_dotenv

load_dotenv()
DB_CONNECTION_STRING = os.getenv("DB_CONNECTION_STRING")

def list_player_by_name():
    conn = psycopg2.connect(DB_CONNECTION_STRING)
    cur = conn.cursor()

    cur.execute("SELECT * FROM player")
    records = cur.fetchall()

    result_list = []
    for record in records:
        result_list.append(record[0])
    result = "\n".join(result_list)

    cur.close()
    conn.close()

    return result

def insert_player(name):
    conn = psycopg2.connect(DB_CONNECTION_STRING)
    cur = conn.cursor()

    print("Inserting player: " + name)
    cur.execute(
        """
        INSERT INTO player (name, level)
        VALUES (%s, %s);
        """,
        (name, 1)
    )

    conn.commit()
    cur.close()
    conn.close()

    print("Inserted successfully")

def remove_player(name):
    conn = psycopg2.connect(DB_CONNECTION_STRING)
    cur = conn.cursor()

    print("Removing player: " + name)
    cur.execute(
        """
        DELETE FROM player
        WHERE name = '{0}';
        """.format(name)
    )

    conn.commit()
    cur.close()
    conn.close()

    print("Removed successfully")

if __name__ == "__main__":
    remove_player("pumpkin")