# Terraform::AWS::GameliftFleet

CloudFormation equivalent of aws_gamelift_fleet

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::GameliftFleet",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#arn" title="Arn">Arn</a>" : <i>String</i>,
        "<a href="#buildid" title="BuildId">BuildId</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#ec2instancetype" title="Ec2InstanceType">Ec2InstanceType</a>" : <i>String</i>,
        "<a href="#fleettype" title="FleetType">FleetType</a>" : <i>String</i>,
        "<a href="#instancerolearn" title="InstanceRoleArn">InstanceRoleArn</a>" : <i>String</i>,
        "<a href="#logpaths" title="LogPaths">LogPaths</a>" : <i>[ String, ... ]</i>,
        "<a href="#metricgroups" title="MetricGroups">MetricGroups</a>" : <i>[ String, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#newgamesessionprotectionpolicy" title="NewGameSessionProtectionPolicy">NewGameSessionProtectionPolicy</a>" : <i>String</i>,
        "<a href="#operatingsystem" title="OperatingSystem">OperatingSystem</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;, ... ]</i>,
        "<a href="#ec2inboundpermission" title="Ec2InboundPermission">Ec2InboundPermission</a>" : <i>[ &lt;a href=&#34;ec2inboundpermission.md&#34;&gt;Ec2InboundPermission&lt;/a&gt;, ... ]</i>,
        "<a href="#resourcecreationlimitpolicy" title="ResourceCreationLimitPolicy">ResourceCreationLimitPolicy</a>" : <i>[ &lt;a href=&#34;resourcecreationlimitpolicy.md&#34;&gt;ResourceCreationLimitPolicy&lt;/a&gt;, ... ]</i>,
        "<a href="#runtimeconfiguration" title="RuntimeConfiguration">RuntimeConfiguration</a>" : <i>[ &lt;a href=&#34;runtimeconfiguration.md&#34;&gt;RuntimeConfiguration&lt;/a&gt;, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>,
        "<a href="#serverprocess" title="ServerProcess">ServerProcess</a>" : <i>[ &lt;a href=&#34;serverprocess.md&#34;&gt;ServerProcess&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::GameliftFleet
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#arn" title="Arn">Arn</a>: <i>String</i>
    <a href="#buildid" title="BuildId">BuildId</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#ec2instancetype" title="Ec2InstanceType">Ec2InstanceType</a>: <i>String</i>
    <a href="#fleettype" title="FleetType">FleetType</a>: <i>String</i>
    <a href="#instancerolearn" title="InstanceRoleArn">InstanceRoleArn</a>: <i>String</i>
    <a href="#logpaths" title="LogPaths">LogPaths</a>: <i>
      - String</i>
    <a href="#metricgroups" title="MetricGroups">MetricGroups</a>: <i>
      - String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#newgamesessionprotectionpolicy" title="NewGameSessionProtectionPolicy">NewGameSessionProtectionPolicy</a>: <i>String</i>
    <a href="#operatingsystem" title="OperatingSystem">OperatingSystem</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;</i>
    <a href="#ec2inboundpermission" title="Ec2InboundPermission">Ec2InboundPermission</a>: <i>
      - &lt;a href=&#34;ec2inboundpermission.md&#34;&gt;Ec2InboundPermission&lt;/a&gt;</i>
    <a href="#resourcecreationlimitpolicy" title="ResourceCreationLimitPolicy">ResourceCreationLimitPolicy</a>: <i>
      - &lt;a href=&#34;resourcecreationlimitpolicy.md&#34;&gt;ResourceCreationLimitPolicy&lt;/a&gt;</i>
    <a href="#runtimeconfiguration" title="RuntimeConfiguration">RuntimeConfiguration</a>: <i>
      - &lt;a href=&#34;runtimeconfiguration.md&#34;&gt;RuntimeConfiguration&lt;/a&gt;</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
    <a href="#serverprocess" title="ServerProcess">ServerProcess</a>: <i>
      - &lt;a href=&#34;serverprocess.md&#34;&gt;ServerProcess&lt;/a&gt;</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Arn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BuildId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ec2InstanceType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FleetType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceRoleArn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogPaths

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MetricGroups

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NewGameSessionProtectionPolicy

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OperatingSystem

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ec2InboundPermission

_Required_: No

_Type_: List of &lt;a href=&#34;ec2inboundpermission.md&#34;&gt;Ec2InboundPermission&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceCreationLimitPolicy

_Required_: No

_Type_: List of &lt;a href=&#34;resourcecreationlimitpolicy.md&#34;&gt;ResourceCreationLimitPolicy&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RuntimeConfiguration

_Required_: No

_Type_: List of &lt;a href=&#34;runtimeconfiguration.md&#34;&gt;RuntimeConfiguration&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: &lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerProcess

_Required_: No

_Type_: List of &lt;a href=&#34;serverprocess.md&#34;&gt;ServerProcess&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Arn

Returns the &lt;code&gt;Arn&lt;/code&gt; value.

#### LogPaths

Returns the &lt;code&gt;LogPaths&lt;/code&gt; value.

#### OperatingSystem

Returns the &lt;code&gt;OperatingSystem&lt;/code&gt; value.
