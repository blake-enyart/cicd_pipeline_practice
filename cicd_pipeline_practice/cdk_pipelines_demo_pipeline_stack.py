from aws_cdk import (
    aws_codepipeline as cp,
    aws_codepipeline_actions as cp_actions,
    core,
    pipelines,
)

from cdk_pipelines_stage import MyApplication

import os


# class


class CdkPipelinesDemoStack(core.Stack):
    def __init__(self, scope: core.Construct, construct_id: str, **kwargs):
        super().__init__(scope, construct_id, **kwargs)

        source_artifact = cp.Artifact("SourceArtifact")
        cloud_assembly_artifact = cp.Artifact("CloudAssemblyArtifact")

        cicd_pipeline = pipelines.CdkPipeline(
            self,
            "DemoPipeline",
            cross_account_keys=False,
            cloud_assembly_artifact=cloud_assembly_artifact,
            pipeline_name="DemoPipeline",
            source_action=cp_actions.GitHubSourceAction(
                action_name="GitHub",
                output=source_artifact,
                oauth_token=core.SecretValue.secrets_manager(
                    "github-token-blake-enyart"
                ),
                owner="blake-enyart",
                repo="data_pipeline_practice",
                branch="main",
                trigger=cp_actions.GitHubTrigger.POLL,
            ),
            synth_action=pipelines.SimpleSynthAction(
                source_artifact=source_artifact,
                cloud_assembly_artifact=cloud_assembly_artifact,
                install_commands=[
                    "npm install -g aws-cdk@1.87.0",
                    "pip install -r requirements.txt",
                    "poetry config virtualenvs.create false",
                    "poetry install --no-dev",
                ],
                synth_command="cdk synth",
            ),
        )

        # dev_stage = cicd_pipeline.add_application_stage(
        #     app_stage=MyApplication(
        #         self,
        #         "PreProd",
        #         env=core.Environment(
        #             account=os.getenv("AWS_ACCOUNT_NUMBER"),
        #             region="us-east-1",
        #         ),
        #     ),
        # )

        # dev_stage.add_actions(
        #     pipelines.ShellScriptAction(
        #         action_name="IntegrationTestService",
        #         commands=[
        #             "pip install -r requirements.txt",
        #             "poetry config virtualenvs.create false",
        #             "poetry install --no-dev",
        #             "pytest tests",
        #         ],
        #         additional_artifacts=[
        #             source_artifact,
        #         ],
        #         run_order=3,
        #     ),
        # )

        # dev_stage.add_manual_approval_action(action_name="ManualApproval", run_order=4)

        # prod_stage = cicd_pipeline.add_application_stage(
        #     app_stage=MyApplication(
        #         self,
        #         "Prod",
        #         env=core.Environment(
        #             account=os.getenv("AWS_ACCOUNT_NUMBER"),
        #             region="us-east-1",
        #         ),
        #     )
        # )

        # prod_stage.deploys_stack(artifact_id=cloud_assembly_artifact.url)
