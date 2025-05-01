import pandas as pd
from soda.scan import Scan

# Load the Parquet file
df = pd.read_parquet("yellow_tripdata_2025-02.parquet")

# Create the scan
scan = Scan()
scan.set_data_source_name("pandas")
scan.add_configuration_yaml_file("soda.yaml")
scan.set_data_frame("yellow_tripdata_2025-02", df)
scan.add_checks_yaml_file("yellow_taxi_checks.yml")
scan.execute()