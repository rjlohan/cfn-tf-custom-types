# Terraform::HuaweiCloud::EcsInstanceV1

CloudFormation equivalent of huaweicloud_ecs_instance_v1

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::HuaweiCloud::EcsInstanceV1",
    "Properties" : {
        "<a href="#autorecovery" title="AutoRecovery">AutoRecovery</a>" : <i>Boolean</i>,
        "<a href="#availabilityzone" title="AvailabilityZone">AvailabilityZone</a>" : <i>String</i>,
        "<a href="#chargingmode" title="ChargingMode">ChargingMode</a>" : <i>String</i>,
        "<a href="#deletedisksontermination" title="DeleteDisksOnTermination">DeleteDisksOnTermination</a>" : <i>Boolean</i>,
        "<a href="#enterpriseprojectid" title="EnterpriseProjectId">EnterpriseProjectId</a>" : <i>String</i>,
        "<a href="#flavor" title="Flavor">Flavor</a>" : <i>String</i>,
        "<a href="#imageid" title="ImageId">ImageId</a>" : <i>String</i>,
        "<a href="#keyname" title="KeyName">KeyName</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#opsvcuserid" title="OpSvcUserid">OpSvcUserid</a>" : <i>String</i>,
        "<a href="#password" title="Password">Password</a>" : <i>String</i>,
        "<a href="#period" title="Period">Period</a>" : <i>Double</i>,
        "<a href="#periodunit" title="PeriodUnit">PeriodUnit</a>" : <i>String</i>,
        "<a href="#securitygroups" title="SecurityGroups">SecurityGroups</a>" : <i>[ String, ... ]</i>,
        "<a href="#systemdisksize" title="SystemDiskSize">SystemDiskSize</a>" : <i>Double</i>,
        "<a href="#systemdisktype" title="SystemDiskType">SystemDiskType</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
        "<a href="#userdata" title="UserData">UserData</a>" : <i>String</i>,
        "<a href="#vpcid" title="VpcId">VpcId</a>" : <i>String</i>,
        "<a href="#datadisks" title="DataDisks">DataDisks</a>" : <i>[ <a href="datadisks.md">DataDisks</a>, ... ]</i>,
        "<a href="#nics" title="Nics">Nics</a>" : <i>[ <a href="nics.md">Nics</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::HuaweiCloud::EcsInstanceV1
Properties:
    <a href="#autorecovery" title="AutoRecovery">AutoRecovery</a>: <i>Boolean</i>
    <a href="#availabilityzone" title="AvailabilityZone">AvailabilityZone</a>: <i>String</i>
    <a href="#chargingmode" title="ChargingMode">ChargingMode</a>: <i>String</i>
    <a href="#deletedisksontermination" title="DeleteDisksOnTermination">DeleteDisksOnTermination</a>: <i>Boolean</i>
    <a href="#enterpriseprojectid" title="EnterpriseProjectId">EnterpriseProjectId</a>: <i>String</i>
    <a href="#flavor" title="Flavor">Flavor</a>: <i>String</i>
    <a href="#imageid" title="ImageId">ImageId</a>: <i>String</i>
    <a href="#keyname" title="KeyName">KeyName</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#opsvcuserid" title="OpSvcUserid">OpSvcUserid</a>: <i>String</i>
    <a href="#password" title="Password">Password</a>: <i>String</i>
    <a href="#period" title="Period">Period</a>: <i>Double</i>
    <a href="#periodunit" title="PeriodUnit">PeriodUnit</a>: <i>String</i>
    <a href="#securitygroups" title="SecurityGroups">SecurityGroups</a>: <i>
      - String</i>
    <a href="#systemdisksize" title="SystemDiskSize">SystemDiskSize</a>: <i>Double</i>
    <a href="#systemdisktype" title="SystemDiskType">SystemDiskType</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
    <a href="#userdata" title="UserData">UserData</a>: <i>String</i>
    <a href="#vpcid" title="VpcId">VpcId</a>: <i>String</i>
    <a href="#datadisks" title="DataDisks">DataDisks</a>: <i>
      - <a href="datadisks.md">DataDisks</a></i>
    <a href="#nics" title="Nics">Nics</a>: <i>
      - <a href="nics.md">Nics</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### AutoRecovery

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AvailabilityZone

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ChargingMode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeleteDisksOnTermination

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnterpriseProjectId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Flavor

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImageId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OpSvcUserid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Password

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Period

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PeriodUnit

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityGroups

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SystemDiskSize

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SystemDiskType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserData

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DataDisks

_Required_: No

_Type_: List of <a href="datadisks.md">DataDisks</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Nics

_Required_: No

_Type_: List of <a href="nics.md">Nics</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.
