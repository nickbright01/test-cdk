import uuid
from aws_cdk import (
    Stack,
    aws_s3 as s3,
    RemovalPolicy,  # <-- import from top-level
)
from constructs import Construct

class TestCdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Generate a unique bucket name
        unique_id = str(uuid.uuid4())[:8]
        bucket_name = f"test-cdk-bucket-{unique_id}"

        s3.Bucket(
            self,
            "TestBucket",
            bucket_name=bucket_name,
            versioned=True,
            removal_policy=RemovalPolicy.DESTROY,  # <-- use top-level RemovalPolicy
            auto_delete_objects=True
        )
