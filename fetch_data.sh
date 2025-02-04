#!/bin/bash

echo "Starting the GitHub data fetch process"

pip install requests

python3 fetch_github_data.py

if [ -f "repo_data.csv" ]; then
    echo "CSV file created successfully."
else
    echo "Error in fetching data."
fi
