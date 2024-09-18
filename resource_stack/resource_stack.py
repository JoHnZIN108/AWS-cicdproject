from constructs import Construct
from aws_cdk.pipelines import CodePipeline, CodePipelineSource, ShellStep
import aws_cdk as cdk
from aws_cdk import (
    Stack,
    Stage,
    Duration,
    aws_sqs as sqs,
    aws_lambda as lambda_,
    aws_s3 as s3,
    aws_codepipeline as codepipeline,
)



class ResourceStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        queue = sqs.Queue(self, "MyQueue",
                          visibility_timeout=Duration.seconds(300),
                          queue_name="MyQueue")
        
        function = lambda_.Function(self, "MyFunction",
                                    function_name="codepipeline_lambda",
                                    runtime=lambda_.Runtime.PYTHON_3_9,
                                    handler="demo_lambda.handler",
                                    code=lambda_.Code.from_asset("./lambda_code"))
        
        bucket = s3.Bucket(self, "MyBucket",
                           versioned=True,
                           bucket_name="my-demo-bucket-s3",
                           removal_policy=cdk.RemovalPolicy.DESTROY,
                           block_public_access=s3.BlockPublicAccess.BLOCK_ALL)