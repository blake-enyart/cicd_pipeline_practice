#!/usr/bin/env python3

from aws_cdk import core

from cicd_pipeline_practice.cicd_pipeline_practice_stack import CicdPipelinePracticeStack


app = core.App()
CicdPipelinePracticeStack(app, "cicd-pipeline-practice", env={'region': 'us-west-2'})

app.synth()
