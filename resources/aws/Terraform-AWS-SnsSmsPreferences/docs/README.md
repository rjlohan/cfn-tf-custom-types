# Terraform::AWS::SnsSmsPreferences

CloudFormation equivalent of aws_sns_sms_preferences

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::SnsSmsPreferences",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#defaultsenderid" title="DefaultSenderId">DefaultSenderId</a>" : <i>String</i>,
        "<a href="#defaultsmstype" title="DefaultSmsType">DefaultSmsType</a>" : <i>String</i>,
        "<a href="#deliverystatusiamrolearn" title="DeliveryStatusIamRoleArn">DeliveryStatusIamRoleArn</a>" : <i>String</i>,
        "<a href="#deliverystatussuccesssamplingrate" title="DeliveryStatusSuccessSamplingRate">DeliveryStatusSuccessSamplingRate</a>" : <i>String</i>,
        "<a href="#monthlyspendlimit" title="MonthlySpendLimit">MonthlySpendLimit</a>" : <i>String</i>,
        "<a href="#usagereports3bucket" title="UsageReportS3Bucket">UsageReportS3Bucket</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::SnsSmsPreferences
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#defaultsenderid" title="DefaultSenderId">DefaultSenderId</a>: <i>String</i>
    <a href="#defaultsmstype" title="DefaultSmsType">DefaultSmsType</a>: <i>String</i>
    <a href="#deliverystatusiamrolearn" title="DeliveryStatusIamRoleArn">DeliveryStatusIamRoleArn</a>: <i>String</i>
    <a href="#deliverystatussuccesssamplingrate" title="DeliveryStatusSuccessSamplingRate">DeliveryStatusSuccessSamplingRate</a>: <i>String</i>
    <a href="#monthlyspendlimit" title="MonthlySpendLimit">MonthlySpendLimit</a>: <i>String</i>
    <a href="#usagereports3bucket" title="UsageReportS3Bucket">UsageReportS3Bucket</a>: <i>String</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultSenderId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultSmsType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeliveryStatusIamRoleArn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeliveryStatusSuccessSamplingRate

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MonthlySpendLimit

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UsageReportS3Bucket

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.
