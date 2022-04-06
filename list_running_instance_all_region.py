import boto3

ec2 = boto3.client('ec2')
response = ec2.describe_regions()
result=""
for regions in response['Regions']:
    client=boto3.client('ec2',region_name=regions['RegionName'])
    #get all instance details for a region
    instance_details = client.describe_instances()
    for reservation_details in instance_details['Reservations']:
        for instance in reservation_details['Instances']:
            if instance['State']['Name']=="running":
                result=result+"-------{}---------".format(regions['RegionName'])+"\n"
                result=result+"{},{}".format(instance['InstanceId'],instance['State']['Name'])+"\n"
print(result)
