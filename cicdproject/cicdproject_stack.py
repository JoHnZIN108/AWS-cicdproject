from constructs import Construct
from aws_cdk.pipelines import CodePipeline, CodePipelineSource, ShellStep
from aws_cdk import (
    Duration,
    Stack,
    aws_iam as iam,
    aws_sqs as sqs,
    aws_sns as sns,
    aws_sns_subscriptions as subs,
    aws_codepipeline as codepipeline,
)


class CicdprojectStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Creating a code pipeline
        pipeline = CodePipeline(self, "MyPipeline",
                        pipeline_name="MyPipeline",
                        synth=ShellStep("SynthStep",
                            input=CodePipelineSource.git_hub("JoHnZIN108/cicdproject", "master"),
                            commands=["npm install", "npm run build", "npx cdk synth"]
                        ))