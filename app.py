#!/usr/bin/env python3

import aws_cdk as cdk

from cicdproject.cicdproject_stack import CicdprojectStack


app = cdk.App()
CicdprojectStack(app, "CicdprojectStack", env=cdk.Environment(account="539247456667", region="us-east-1"),stack_name="CicdprojectStack")

app.synth()
