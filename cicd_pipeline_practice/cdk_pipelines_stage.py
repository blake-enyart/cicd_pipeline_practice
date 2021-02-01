from aws_cdk import core

from my_practice_stack import (
    MyPracticeStack,
)


class MyApplication(core.Stage):
    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        MyPracticeStack(self, "MyPracticeStack")
