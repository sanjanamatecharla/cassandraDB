from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

# Connect to Cassandra
cluster = Cluster(['127.0.0.1'], 
                  port=9042,
                  auth_provider=PlainTextAuthProvider(username='your_username', password='your_password'))
session = cluster.connect('your_keyspace')

# Create a table if it doesn't exist
create_table_query = '''
    CREATE TABLE IF NOT EXISTS your_table (
        id UUID PRIMARY KEY,
        name TEXT,
        age INT
    )
'''
session.execute(create_table_query)

# Insert data
insert_data_query = '''
    INSERT INTO your_table (id, name, age) VALUES (uuid(), 'John Doe', 25)
'''
session.execute(insert_data_query)

# Query data
select_data_query = '''
    SELECT * FROM your_table
'''
result = session.execute(select_data_query)
for row in result:
    print(row.id, row.name, row.age)

# Close the connection
cluster.shutdown()
