import boto3
import os
import argparse

parser=argparse.ArgumentParser(description='Transfer latest run from S3 bucket')

# add arguments

parser.add_argument(
  "-p",
  "--project",
  type=str,
  nargs="?",
  default="virus",
  help="project name, virus or ICMC"
)

# parse arguments
args=parser.parse_args()

project=args.project

#S3
s3 = boto3.resource('s3')

# read from S3
obj = s3.Object('transfer-files-emory', 'download.me')
file=obj.get()['Body'].read().decode('utf-8')

# split S3 path to components
file_split=file.split('/')

def splitPath(project):
    if project=='virus':
        project_name=file_split[3]
        run_namae=file_split[4] 
    elif project=='ICMC':
        project_name=file_split[4]
        run_namae=file_split[5]
    return project_name, run_namae

project_name, run_namae = splitPath(project=project)

print(project_name)
print(run_namae)

# select output directory where to put files
def project_out_dir(project):
    if project=='virus':
        project_path='C:/Users/Administrator/OneDrive - Emory University/virus/output/'
    elif project == 'ICMC':
        project_path='C:/Users/Administrator/OneDrive - Emory University/'
    return(project_path)


run_path=project_out_dir(project=project)
print(run_path)

# create directory and download
def downloadDirectoryFroms3(bucketName, remoteDirectoryName):
    s3_resource = boto3.resource('s3')
    bucket = s3_resource.Bucket(bucketName) 
    for obj in bucket.objects.filter(Prefix = remoteDirectoryName):
        out_path=(run_path+obj.key)
        print(out_path)
        if not os.path.exists(os.path.dirname(out_path)):
            os.makedirs(os.path.dirname(out_path))
        bucket.download_file(obj.key, out_path)

def getRemoteDirName(project):
    if project=='ICMC':
        remDir='ICMC/%s/%s/custom_output' % (project_name, run_namae)
    elif project=='virus':
        remDir=project_name
    return remDir

remDir=getRemoteDirName(project=project)

# download files
downloadDirectoryFroms3(bucketName='transfer-files-emory', remoteDirectoryName=remDir)