# Using the Data Migration Tool

The Data Migration Tool, introduced in Frappe Framework version 9, abstracts the syncing of data between a remote source and a DocType. It acts as a middleware layer between your Frappe-based website and a remote data source.

## Key Components

### Data Migration Plan
A Data Migration Plan encapsulates a set of mappings. For example, you can create a plan named 'Atlas Sync' and add mappings in the child table.

### Data Migration Mapping
A Data Migration Mapping specifies field-to-field mapping. For example, you can create a mapping called 'Item to Atlas Item' and define the structure of local and remote data.

### Data Migration Connector
To connect to the remote source, create a Data Migration Connector. Specify the connector type, hostname, username, and password for authentication.

## Running a Data Migration

1. Create a Data Migration Plan and add mappings.
2. Create a Data Migration Connector.
3. Execute a Data Migration Run to sync data. The tool handles queueing, batching, and delta updates.