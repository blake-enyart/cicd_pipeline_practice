#!/usr/bin/env python3

from aws_cdk import core

from cicd_pipeline_practice.cdk_pipelines_demo_pipeline_stack import (
    CdkPipelinesDemoStack,
)


app = core.App()
CdkPipelinesDemoStack(app, "cicd-pipeline-practice", env={"region": "us-west-2"})

app.synth()
