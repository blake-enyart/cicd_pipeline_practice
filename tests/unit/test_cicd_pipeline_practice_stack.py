import json
import pytest

from aws_cdk import core
from cicd_pipeline_practice.cicd_pipeline_practice_stack import CicdPipelinePracticeStack


def get_template():
    app = core.App()
    CicdPipelinePracticeStack(app, "cicd-pipeline-practice")
    return json.dumps(app.synth().get_stack("cicd-pipeline-practice").template)


def test_sqs_queue_created():
    assert("AWS::SQS::Queue" in get_template())


def test_sns_topic_created():
    assert("AWS::SNS::Topic" in get_template())
