import boto3
AWS_ACCESS_KEY_ID = 'AKIATCP4XX4BJ4QFVVML'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'practice-demo-testing'
AWS_S3_SIGNATURE_VERSION = 's3v4'
AWS_S3_REGION_NAME = 'ap-south-1'




#initialize sc_client
s3 = boto3.client('s3',
                         aws_access_key_id=AWS_ACCESS_KEY_ID,
                         aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                         region_name=AWS_S3_REGION_NAME)

BUCKET_NAME_NEW = 'my-first-bucket-07122023'


def process_objects(objects):
    # Process the list of objects
    count = 1

    for obj in objects:
        print(count,obj['Key'])
        count += 1


def list_all_objects(bucket_name):
    
    response = s3.list_objects_v2(Bucket=bucket_name)

    process_objects(response['Contents'])

    # Check if there are more pages
    while response.get('NextContinuationToken'):
        # Make subsequent requests to get the next page
        response = s3.list_objects_v2(
            Bucket=bucket_name,
            ContinuationToken=response['NextContinuationToken']
        )
        # Process each page of objects
        process_objects(response['Contents'])


list_all_objects(BUCKET_NAME_NEW)






