from aws_cdk import Duration, Stack
from constructs import Construct
from aws_cdk.aws_events import Rule, Schedule
from aws_cdk.aws_events_targets import LambdaFunction
from aws_cdk.aws_lambda import Function, Runtime, Code
from aws_cdk.aws_s3 import Bucket, BlockPublicAccess


# Load Lambda environment variables from .env file
env_vars = dict()
with open(".env") as env_file:
    for line in env_file:
        key, value = line.strip().split("=")
        env_vars[key] = value


class AwsCdkPythonStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Example Lambda function
        # example_function = Function(
        #     self, 
        #     "ExampleFunction", 
        #     runtime=Runtime.PYTHON_3_11, 
        #     handler="handler.handler", 
        #     code=Code.from_asset("lambda"), 
        #     timeout=Duration.minutes(5), 
        #     function_name="ExampleFunction", 
        #     environment=env_vars,
        # )

        # Example CloudWatch Rule 
        # example_rule = Rule(self, "ExampleRule", schedule=Schedule.cron(hour="14",minute="0"), rule_name="ExampleRule", enabled=True)
        # example_rule.add_target(LambdaFunction(example_function))

        # Example S3 Bucket
        # example_bucket = Bucket(
        #     self,
        #     "ExampleBucket",
        #     bucket_name="ExampleBucket",  # needs to be globally unique
        #     block_public_access=BlockPublicAccess.BLOCK_ALL,
        # )