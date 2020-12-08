#!/usr/bin/env python

import sys
import boto3

session = boto3.Session(
    aws_access_key_id=MY_AWS_ACCESS_KEY_ID,
    aws_secret_access_key=MY_AWS_SECRET_ACCESS_KEY
)

services = session.get_available_services()

def main():

    if len(sys.argv) < 2:
        print("Please supply a VPC id as an argument!")
    else:
        vpc_id = sys.argv[1]
        print("VPC ID:", vpc_id)

        # Display RDS instances in VPC
        client = boto3.client('rds')
        response = client.describe_db_instances()
        print('Regions:', response['Regions'])
        # Disply ec2 instances
        ec2 = boto3.resource('ec2')
        response = ec2.describe_regions()
        print('Regions:', response['Regions'])
        # Display subnets  in VPC
        subnets = list(vpc.subnets.all())
    if len(subnets) > 0:
        print("\nSubnets:")
        for subnet in subnets:
            print(subnet.id, "-", subnet.cidr_block)
    else:
        print("There is no subnet in this VPC!")




if __name__ == "__main__":
    main()






