# ETL flow with Spark, Postgres, Docker and dbt

## Overview

This DBT project is designed to transform raw data into a clean and structured format for analysis. It leverages DBT's capabilities to create data models, run tests, and generate documentation.

## Requirements

- **DBT version**: 1.8 or higher
- **Python version**: 3.11 or higher
- Supported databases: PostgreSQL

## Setup

### DBT

1. **Install DBT**  
   Follow the [dbt core installation guide](https://docs.getdbt.com/docs/core/installation-overview)

2. **Clone the Repository**  
   ```bash
   git clone https://github.com/xpcosmos/jaffle-shop.git
   cd jaffle-shop
   ```

3. **Configure DBT Profile**  
   Edit `profiles.yml` with your database connection details. Use environment variables for sensitive information.

4. **Install Dependencies**
   
   ```bash
   dbt deps
   ```

## Usage

- **Run all models**  
  ```bash
  dbt run
  ```

- **Run specific models**  
  ```bash
  dbt run --models <model_name>
  ```

- **Test models**  
  ```bash
  dbt test
  ```

- **Create snapshots**  
  ```bash
  dbt snapshot
  ```

- **Load seed data**  
  ```bash
  dbt seed
  ```
### PostgresSQL via Docker

...

### PySpark via Docker

...

## Documentation

Generate and view documentation:

```bash
dbt docs generate
dbt docs serve
```

## Contributing

Contributions are welcome! Please fork the repository and open a pull request with your changes.
