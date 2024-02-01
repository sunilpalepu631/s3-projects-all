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



# object_key = 'rename-test1.jpg'

# s3.upload_file(
#     'downloads/image1.jpg',
#     BUCKET_NAME_NEW,
#     object_key,
# )



# def rename_file(old_file_name, new_file_name):
#     #Copy
#     response = s3.copy_object(
#     Bucket=BUCKET_NAME_NEW,
#     Key=new_file_name,  #new key
#     CopySource={
#         'Bucket':BUCKET_NAME_NEW,
#         'Key': old_file_name  #old key
#         }
#     )

#     #deleting the old
#     response = s3.delete_object(
#         Bucket = BUCKET_NAME_NEW,
#         Key = old_file_name
#     )
#     return response

# rename_file(old_file,new_file)







import boto3
from botocore.exceptions import ClientError

def paginate_through_all_objects_s3_bucket(bucket_name, max_items=None,page_size=None, starting_token=None):

    try:
        paginator = s3.get_paginator('list_objects')
        response = paginator.paginate(Bucket=bucket_name, PaginationConfig={
            'MaxItems':max_items,
            'PageSize':page_size,
            'StartingToken':starting_token}
        )
        return response
    except ClientError as e:
        raise Exception("boto3 client error in paginate_through_all_objects_s3_bucket: " + e.__str__())
    except Exception as e:
        raise Exception("Unexpected error in paginate_through_all_objects_s3_bucket: " + e.__str__())



#1st Run
a = paginate_through_all_objects_s3_bucket(BUCKET_NAME_NEW,50,5)
for i in a:
    for item in i['Contents']:
        print(item['Key'])

#2nd Run
# for items in a:
#     for i in items['Contents']:
#         print(i['Key'])
# [max_items-1]['Key']

# b = paginate_through_all_objects_s3_bucket('s3-test-bucket',2,5,next_token)
# print(*b)
        
# response = s3.list_objects(Bucket=BUCKET_NAME_NEW, Prefix='multipart-test') #prefix means folder name
# objects = response.get('Contents', [])

# for object in objects:
#     print(object['Key'])







#working pagination piece of code


# import boto3

# def paginate_s3_objects(bucket_name, prefix=''):
    
#     paginator = s3.get_paginator('list_objects_v2')

#     list_objects_params = {
#         'Bucket': bucket_name,
#         'Prefix': prefix
#     }
#     pagination_config = {'MaxItems': 100, 'PageSize': 10}

#     # Paginate through results
#     for page in paginator.paginate(**list_objects_params,PaginationConfig=pagination_config):
#         # Process each page of results
#         objects = page.get('Contents', [])
#         print('hiii')
#         for obj in objects:
#             # Process each object in the page
#             print(f"Object Key: {obj['Key']}")

# # Example usage
# bucket_name = 'practice-demo-testing'
# prefix = ''

# paginate_s3_objects(bucket_name, prefix)





# import boto3
# from rest_framework import viewsets, status
# from rest_framework.response import Response

# class S3ObjectViewSet(viewsets.ViewSet):
#     def list(self, request):
#         s3 = boto3.client('s3')  # Replace with your preferred S3 client
#         bucket_name = 'your-bucket-name'  # Replace with your bucket name

#         try:
#             response = s3.list_objects_v2(Bucket=bucket_name, MaxKeys=1000)
#             objects = response['Contents']
#             next_token = response.get('NextContinuationToken')

#             return Response({
#                 'objects': [obj['Key'] for obj in objects],
#                 'next_token': next_token
#             })

#         except Exception as e:
#             return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
