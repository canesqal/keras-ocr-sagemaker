#!/usr/bin/env python3
import os

import aws_cdk as cdk

from sagemaker_cdk.sagemaker_cdk_stack import SagemakerCdkStack


app = cdk.App()
SagemakerCdkStack(app, "SagemakerCdkStack")

app.synth()
