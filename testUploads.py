import boto3

AWS_ACCESS_KEY_ID = 
AWS_SECRET_ACCESS_KEY = 
AWS_STORAGE_BUCKET_NAME = 'practice-demo-testing'
AWS_S3_SIGNATURE_VERSION = 's3v4'
AWS_S3_REGION_NAME = 'ap-south-1'




#initialize sc_client
s3 = boto3.client('s3',
                         aws_access_key_id=AWS_ACCESS_KEY_ID,
                         aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                         region_name=AWS_S3_REGION_NAME)


# # create Bucket
# bucket_location = s3.create_bucket(ACL='private', 
#                                           Bucket="my-first-bucket-07122023",
#                                           CreateBucketConfiguration={
#                                               "LocationConstraint": 'ap-south-1'
#                                           })
# print(bucket_location)

BUCKET_NAME = 'practice-demo-testing'
BUCKET_NAME_NEW = 'my-first-bucket-07122023'

#list all the objects in a bucket
#list of bukcets
empty_list = []
bucket_list = s3.list_buckets()
for bucket in bucket_list['Buckets']:
    empty_list.append(bucket)



# Create a JWT token with AWS credentials
expiration_time = datetime.now() + timedelta(days=1)
print(expiration_time)
expiration_timestamp = int(expiration_time.timestamp())
print(expiration_timestamp)

#payload, this contains user details generally but for this aws credentials
token_data = {
    'access_key': access_key,
    'secret_access_key': secret_access_key,
    'region_name': region_name,
    'exp': expiration_timestamp
}
jwt_token = jwt.encode(token_data,my_secret_key, algorithm='HS256')

return Response({'success': True , 'message': 'user succesfully login and credentials are correct','JWT_token': jwt_token,'buckets_list': empty_list})


 #list of bukcets
# empty_list = []
# # bucket_list = s3.list_buckets()
# # for bucket in bucket_list['Buckets']:
# #     empty_list.append(bucket)
    

# response= s3.list_objects_v2(Bucket=BUCKET_NAME_NEW)
# for obj in response['Contents']:
#     empty_list.append(obj['Key'])
    
# print(empty_list)




# list all the buckets in s3 for s3.client
# bucket_list = s3.list_buckets()
# for bucket in bucket_list['Buckets']:
#     print(bucket)


# Print out bucket names for s3.resource
# for bucket in s3.buckets.all():
#     print(bucket.name)

# bucket = s3.Bucket(BUCKET_NAME)

# for obj in bucket.objects.all():
#     print(obj)


#list all the objects in a bucket
# response= s3.list_objects_v2(Bucket=BUCKET_NAME_NEW)
# for obj in response['Contents']:
#     print(obj['Key'])

# print(len(response['Contents']))


# # upload file to a bucket
# with open ('./pexels-sean-valentine-3230136.jpg', 'rb') as file:
#     s3.upload_fileobj(
#         file,BUCKET_NAME,'newyork-flower-building.jpg'
#     )


# download a file
# s3.download_file(BUCKET_NAME_NEW,'presigned-uploads/test-presigned-url-1.mp4','test-presigned-downlaod.mp3')


# # download file with binary data
# with open('downloads/image4.jpg', 'wb') as file:   #with open means if there is file it will open other wise it will create new one
#     s3.download_fileobj(Bucket=BUCKET_NAME,Key='newyork-flower-building.jpg',Fileobj=file)



# # Open the source file in binary mode
# with open('downloads/image5.jpg', 'rb') as file:
#     # Read the content of the source file
#     file_content = file.read()

#     # Open the destination file in binary mode for writing
#     with open('downloads/image6.jpg', 'wb') as destination_file:
#         # Write the content to the destination file
#         destination_file.write(file_content)



# # copy objects from one bucket to another bucket

# object_key = 'newyork-flower-building.jpg'
# new_object_key = 'copied-object-newyork.jpg'
# s3.copy_object(
#     ACL= 'private',
#     Bucket = BUCKET_NAME_NEW,
#     CopySource= f'/{BUCKET_NAME}/{object_key}',
#     Key = new_object_key
# )




# #get object details
# response = s3.get_object(Bucket=BUCKET_NAME,Key='newyork-flower-building.jpg')

# print(response)




# def upload_to_s3(file_path, bucket_name, object_name):


#     # Upload the file
#     try:
#         s3.upload_file(file_path, bucket_name, object_name)
#         print(f"File uploaded successfully to {bucket_name}/{object_name}")
#     except Exception as e:
#         print(f"Error uploading file: {e}")

# # Example usage
# file_path = "pexels-sean-valentine-3230136.jpg"
# bucket_name = BUCKET_NAME_NEW
# object_name = 'function/newyork.jpg'

# upload_to_s3(file_path, bucket_name, object_name)




# def download_file( bucket_name, object_name,file_path):

#     # Upload the file
#     try:
#         s3.download_file(Bucket=bucket_name,Key=object_name, Filename=file_path)
#         print(f"File downlaoded successfully to {bucket_name}/{object_name}")
#     except Exception as e:
#         print(f"Error downloading file: {e}")

# # Example usage
# file_path = "down1-pexels-sean-valentine-3230136.jpg"
# bucket_name = BUCKET_NAME_NEW
# object_name = 'function/newyork.jpg'

# download_file( bucket_name, object_name,file_path)




# response = s3.generate_presigned_url(
#             ClientMethod = 'get_object',
#             Params = {
#                 'Bucket': BUCKET_NAME_NEW,
#                 'Key': 'pexels-piccinng-2977527.jpg'
#             },
#             ExpiresIn = 3600
#             )

# print(response) 



# users = {
#     'hans': 'active',
#     'tharun': 'inactive'
# }

# copy = users.copy()
# print(copy)

# for key,value in copy.items():
#     print(key,value)


# Create a sample collection
# users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# # Strategy:  Iterate over a copy
# for user, status in users.items(): #len 3
#     if status == 'inactive':
#         del users[user]

# Strategy:  Create a new collection
# active_users = {}
# for user, status in users.items():
#     if status == 'active':
#         active_users[user] = status

# print('name',users)

