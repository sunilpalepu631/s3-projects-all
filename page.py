import time
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

bucket_name = 'peepul-agri-dev'






#this pieace of shit will bring more than 1000 limit objects from s3
def paginate_objects(bucket_name,prefix,max_items,page_size):

    paginator = s3.get_paginator('list_objects_v2')

    PaginationConfig = {
        'MaxItems' : max_items, #100
        'PageSize': page_size,  #10
        }
    page_sizes = 100
    response = paginator.paginate(Bucket=bucket_name,Prefix=prefix)

    count = 1
    for item in response:
        print('hii')
        # print(item['CommonPrefixes'])
        
        objects = item['Contents'][:page_sizes] 
        for object in objects:
            print(count, object['Key'])
            count += 1
        
        # for prefixs in item['CommonPrefixes']:
        #     print(prefixs['Prefix'])

start_time = time.time()
paginate_objects(bucket_name,'',10000,100)
end_time = time.time()

total_time = end_time-start_time
print('total_time = ',total_time)

# response = s3.list_objects_v2(Bucket=BUCKET_NAME_NEW, Delimiter='stepwise/')

# # for obj in response['Contents']:
# #     print(obj['Key'])

# for prefix in response['CommonPrefixes']:
#     print(prefix['Prefix'])  # Prints prefixes for grouped objects

