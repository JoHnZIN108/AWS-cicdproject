from constructs import Construct
from aws_cdk.pipelines import CodePipeline, CodePipelineSource, ShellStep
from aws_cdk import (
    Stack,
    Stage,
    Environment,
    aws_codepipeline as codepipeline,
)
from resource_stack.resource_stack import ResourceStack

class DeployStage(Stage):
    def __init__(self, scope: Construct, id: str, env: Environment, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
        ResourceStack(self, "ResourceStack", env=env, stack_name="resource-stack-deploy")

class CicdprojectStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Creating a code pipeline
        pipeline = CodePipeline(self, "MyPipeline",
            pipeline_name="MyPipeline",
            synth=ShellStep("Synth",
                input=CodePipelineSource.git_hub("JoHnZIN108/cicdproject", "master"),
                install_commands=[
                    "python -m pip install --upgrade pip",  # Update pip
                    "pip install -r requirements.txt",      # Install Python dependencies
                ],
                commands=[
                    "npx cdk synth"  # Synthesize the CDK app
                ],
            ),
            cross_account_keys=False
        )

        
        # Add the stage to the pipeline
        pipeline.add_stage(DeployStage(self, "DeployStage", env=Environment(account="539247456667", region="us-east-1")))

        