"""
run_pipeline.py

Master execution script for the Mutual Fund Analytics Platform.

This script executes the project workflow in sequence:
1. Data Ingestion
2. Data Cleaning
3. Performance Analytics
4. Advanced Analytics

Author: Sayandip Sen
"""

import subprocess

scripts = [
    "scripts/data_ingestion.py",
    "scripts/data_cleaning.py",
    "scripts/performance_analytics.py",
    "scripts/advanced_analytics.py"
]

for script in scripts:
    print(f"Running: {script}")
    subprocess.run(["python", script])

print("\nPipeline execution completed successfully.")