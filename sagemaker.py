import aws_cdk.aws_sagemaker as sagemaker

import { aws_sagemaker as sagemaker } from 'aws-cdk-lib';
cfnNotebookInstance = new sagemaker.CfnNotebookInstance(this, 'MyCfnNotebookInstance', {
  instanceType: 'ml.t3.medium',
  roleArn: 'AmazonSageMaker-ExecutionRole-20230823T170348',

  # the properties below are optional
"""   acceleratorTypes: ['acceleratorTypes'],
  additionalCodeRepositories: ['additionalCodeRepositories'],
  defaultCodeRepository: 'defaultCodeRepository',
  directInternetAccess: 'directInternetAccess',
  instanceMetadataServiceConfiguration: {
    minimumInstanceMetadataServiceVersion: 'minimumInstanceMetadataServiceVersion',
  },
  kmsKeyId: 'kmsKeyId',
  lifecycleConfigName: 'lifecycleConfigName',
  notebookInstanceName: 'notebookInstanceName',
  platformIdentifier: 'platformIdentifier',
  rootAccess: 'rootAccess',
  securityGroupIds: ['securityGroupIds'],
  subnetId: 'subnetId',
  tags: [{
    key: 'key',
    value: 'value',
  }],
  volumeSizeInGb: 123, """
});