from aws_cdk import (
    Stack,
    aws_sagemaker as sagemaker,
    aws_iam as iam
)
from constructs import Construct

class SagemakerCdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create an IAM role for the notebook instance
        role = iam.Role(
            self, "NotebookInstanceRole",
            assumed_by=iam.ServicePrincipal("sagemaker.amazonaws.com"),
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name("AmazonSageMakerFullAccess")
            ]
        )

        # Create the notebook instance
        sagemaker.CfnNotebookInstance(
            self, "NotebookInstance",
            instance_type="ml.t3.medium",
            role_arn=role.role_arn,
            notebook_instance_name="my-notebook-instance",
            default_code_repository="https://github.com/canesqal/keras-ocr-sagemaker.git"
        )
