The Terraform build on aws: 
- vpc, 2 networks and routes.
- security groups for port80 & 443.
- elb for port 80 & 443
- publish the elb records in route53
- ec2 machine with nginx and static index.html that saved on s3 bucket- for tests

Python Script:

The Python script "aws_get.svc.py" uses boto3 to get the all active services.
Check if rds is active, ec2, subnets.