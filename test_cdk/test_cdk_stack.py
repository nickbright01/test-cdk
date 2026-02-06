from aws_cdk import (
    Stack,
    aws_s3 as s3,
)
from constructs import Construct

class TestCdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create a simple S3 bucket
        s3.Bucket(
            self,
            "TestBucket-cdk",
            bucket_name="test-cdk-bucket-unique-12345",  # must be globally unique
            versioned=True,
            removal_policy=s3.RemovalPolicy.DESTROY,  # delete bucket when stack is destroyed
            auto_delete_objects=True                  # deletes objects automatically when removing stack
        )
