# Setup Read Operations from Slave/Secondary MySQL System

In a normal setup, the system performs both read and write operations on the same database. However, as the data size or the number of concurrent activities increases, you may start experiencing delays in operations.

One immediate solution to mitigate such delays is to separate read and write activities. This means:
- **Read operations** are performed on a replica/secondary database.
- **Write operations** are performed on the master/primary database.

Frappe allows you to split read and write activities between the master and replica databases.

---

## Steps to Set Up a Read-Only Environment

### 1. Pre-requisites
You should have a setup for:
- **MariaDB Master-Slave** or
- **Cluster** environment.

---

### 2. Configurations for Read-Only Replica
In your `site_config.json`, add the following keys to enable reading from the replica/secondary system:

```json
{
  "read_from_replica": 1, // Set to 1 to enable reading from the replica
  "different_credentials_for_replica": 1, // Set to 1 if the database credentials are different on the replica
  "replica_host": "IP address for replica",
  "replica_db_port": "Replica DB port",
  "replica_db_name": "Replica DB name",
  "replica_db_password": "Replica DB password"
}
```

#### Note:
- If you have enabled a MariaDB master-replica environment, the database name and password are typically the same on both the master and replica.

---

### 3. Grant Access Permissions
Grant the necessary access permissions for the master host on the slave/secondary system.

---

By following these steps, you can optimize your database operations by offloading read activities to a replica database, improving overall system performance.

---

Was this article helpful? Let us know your feedback!