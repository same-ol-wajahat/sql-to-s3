import boto3
import sys

# AWS credentials and settings
aws_access_key = sys.argv[1]
aws_secret_key = sys.argv[2]
bucket_name = sys.argv[3]
s3_file_path = sys.argv[4]
csv_file_path = 'output.csv'  # Path to the generated CSV file

# Create an S3 client
s3_client = boto3.client('s3', aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key)

# Upload the CSV file to S3
s3_client.upload_file(csv_file_path, bucket_name, s3_file_path)
