# Terraform::HuaweiCloud::DliQueueV1

CloudFormation equivalent of huaweicloud_dli_queue_v1

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::HuaweiCloud::DliQueueV1",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#createtime" title="CreateTime">CreateTime</a>" : <i>String</i>,
        "<a href="#cucount" title="CuCount">CuCount</a>" : <i>Double</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#managementsubnetcidr" title="ManagementSubnetCidr">ManagementSubnetCidr</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#subnetcidr" title="SubnetCidr">SubnetCidr</a>" : <i>String</i>,
        "<a href="#vpccidr" title="VpcCidr">VpcCidr</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::HuaweiCloud::DliQueueV1
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#createtime" title="CreateTime">CreateTime</a>: <i>String</i>
    <a href="#cucount" title="CuCount">CuCount</a>: <i>Double</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#managementsubnetcidr" title="ManagementSubnetCidr">ManagementSubnetCidr</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#subnetcidr" title="SubnetCidr">SubnetCidr</a>: <i>String</i>
    <a href="#vpccidr" title="VpcCidr">VpcCidr</a>: <i>String</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CreateTime

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CuCount

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ManagementSubnetCidr

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubnetCidr

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcCidr

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

#### CreateTime

Returns the &lt;code&gt;CreateTime&lt;/code&gt; value.
