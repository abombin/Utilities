import boto3
import os

s3 = boto3.resource('s3')

obj = s3.Object('transfer-files-emory', 'download.me')
file=obj.get()['Body'].read().decode('utf-8')

file_split=file.split('/')


project_name=file_split[3]

run_nmae=file_split[4]

print(project_name, run_nmae)

run_path='C:\\Users\\Administrator\\OneDrive - Emory University\\virus\\output\\%s\\%s' % \
    (project_name, run_nmae)

print(run_path)

if not os.path.exists(run_path):
    os.makedirs(run_path)
else:
    print('path exists')