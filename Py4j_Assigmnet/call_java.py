from py4j.java_gateway import JavaGateway

# Connect to the JVM
gateway = JavaGateway()

# Get the entry point (the instance of DBConnection)
db_connection = gateway.entry_point

# Call the getData method
result = db_connection.getData()
print(f"The result is: {result}")
