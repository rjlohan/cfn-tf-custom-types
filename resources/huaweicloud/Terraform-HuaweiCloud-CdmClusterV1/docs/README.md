# Terraform::HuaweiCloud::CdmClusterV1

CloudFormation equivalent of huaweicloud_cdm_cluster_v1

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::HuaweiCloud::CdmClusterV1",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#availabilityzone" title="AvailabilityZone">AvailabilityZone</a>" : <i>String</i>,
        "<a href="#created" title="Created">Created</a>" : <i>String</i>,
        "<a href="#email" title="Email">Email</a>" : <i>[ String, ... ]</i>,
        "<a href="#enterpriseprojectid" title="EnterpriseProjectId">EnterpriseProjectId</a>" : <i>[ String, ... ]</i>,
        "<a href="#flavorid" title="FlavorId">FlavorId</a>" : <i>String</i>,
        "<a href="#instances" title="Instances">Instances</a>" : <i>[ &lt;a href=&#34;instances.md&#34;&gt;Instances&lt;/a&gt;, ... ]</i>,
        "<a href="#isautooff" title="IsAutoOff">IsAutoOff</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#phonenum" title="PhoneNum">PhoneNum</a>" : <i>[ String, ... ]</i>,
        "<a href="#publidip" title="PublidIp">PublidIp</a>" : <i>String</i>,
        "<a href="#scheduleboottime" title="ScheduleBootTime">ScheduleBootTime</a>" : <i>String</i>,
        "<a href="#scheduleofftime" title="ScheduleOffTime">ScheduleOffTime</a>" : <i>String</i>,
        "<a href="#securitygroupid" title="SecurityGroupId">SecurityGroupId</a>" : <i>String</i>,
        "<a href="#subnetid" title="SubnetId">SubnetId</a>" : <i>String</i>,
        "<a href="#version" title="Version">Version</a>" : <i>String</i>,
        "<a href="#vpcid" title="VpcId">VpcId</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::HuaweiCloud::CdmClusterV1
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#availabilityzone" title="AvailabilityZone">AvailabilityZone</a>: <i>String</i>
    <a href="#created" title="Created">Created</a>: <i>String</i>
    <a href="#email" title="Email">Email</a>: <i>
      - String</i>
    <a href="#enterpriseprojectid" title="EnterpriseProjectId">EnterpriseProjectId</a>: <i>
      - String</i>
    <a href="#flavorid" title="FlavorId">FlavorId</a>: <i>String</i>
    <a href="#instances" title="Instances">Instances</a>: <i>
      - &lt;a href=&#34;instances.md&#34;&gt;Instances&lt;/a&gt;</i>
    <a href="#isautooff" title="IsAutoOff">IsAutoOff</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#phonenum" title="PhoneNum">PhoneNum</a>: <i>
      - String</i>
    <a href="#publidip" title="PublidIp">PublidIp</a>: <i>String</i>
    <a href="#scheduleboottime" title="ScheduleBootTime">ScheduleBootTime</a>: <i>String</i>
    <a href="#scheduleofftime" title="ScheduleOffTime">ScheduleOffTime</a>: <i>String</i>
    <a href="#securitygroupid" title="SecurityGroupId">SecurityGroupId</a>: <i>String</i>
    <a href="#subnetid" title="SubnetId">SubnetId</a>: <i>String</i>
    <a href="#version" title="Version">Version</a>: <i>String</i>
    <a href="#vpcid" title="VpcId">VpcId</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AvailabilityZone

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Created

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Email

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnterpriseProjectId

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FlavorId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Instances

_Required_: No

_Type_: List of &lt;a href=&#34;instances.md&#34;&gt;Instances&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsAutoOff

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PhoneNum

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PublidIp

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScheduleBootTime

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScheduleOffTime

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityGroupId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubnetId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Version

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: &lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Created

Returns the &lt;code&gt;Created&lt;/code&gt; value.

#### Instances

Returns the &lt;code&gt;Instances&lt;/code&gt; value.

#### PublidIp

Returns the &lt;code&gt;PublidIp&lt;/code&gt; value.
