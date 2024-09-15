#!/usr/bin/env python3

import aws_cdk as cdk

from cicdproject.cicdproject_stack import CicdprojectStack


app = cdk.App()
CicdprojectStack(app, "CicdprojectStack")

app.synth()
