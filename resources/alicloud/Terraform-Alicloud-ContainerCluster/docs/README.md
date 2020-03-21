# Terraform::Alicloud::ContainerCluster

CloudFormation equivalent of alicloud_container_cluster

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Alicloud::ContainerCluster",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#agentversion" title="AgentVersion">AgentVersion</a>" : <i>String</i>,
        "<a href="#cidrblock" title="CidrBlock">CidrBlock</a>" : <i>String</i>,
        "<a href="#diskcategory" title="DiskCategory">DiskCategory</a>" : <i>String</i>,
        "<a href="#disksize" title="DiskSize">DiskSize</a>" : <i>Double</i>,
        "<a href="#imageid" title="ImageId">ImageId</a>" : <i>String</i>,
        "<a href="#instancetype" title="InstanceType">InstanceType</a>" : <i>String</i>,
        "<a href="#isoutdated" title="IsOutdated">IsOutdated</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#nameprefix" title="NamePrefix">NamePrefix</a>" : <i>String</i>,
        "<a href="#needslb" title="NeedSlb">NeedSlb</a>" : <i>Boolean</i>,
        "<a href="#nodenumber" title="NodeNumber">NodeNumber</a>" : <i>Double</i>,
        "<a href="#nodes" title="Nodes">Nodes</a>" : <i>[ &lt;a href=&#34;nodes.md&#34;&gt;Nodes&lt;/a&gt;, ... ]</i>,
        "<a href="#password" title="Password">Password</a>" : <i>String</i>,
        "<a href="#releaseeip" title="ReleaseEip">ReleaseEip</a>" : <i>Boolean</i>,
        "<a href="#securitygroupid" title="SecurityGroupId">SecurityGroupId</a>" : <i>String</i>,
        "<a href="#size" title="Size">Size</a>" : <i>Double</i>,
        "<a href="#slbid" title="SlbId">SlbId</a>" : <i>String</i>,
        "<a href="#vpcid" title="VpcId">VpcId</a>" : <i>String</i>,
        "<a href="#vswitchid" title="VswitchId">VswitchId</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Alicloud::ContainerCluster
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#agentversion" title="AgentVersion">AgentVersion</a>: <i>String</i>
    <a href="#cidrblock" title="CidrBlock">CidrBlock</a>: <i>String</i>
    <a href="#diskcategory" title="DiskCategory">DiskCategory</a>: <i>String</i>
    <a href="#disksize" title="DiskSize">DiskSize</a>: <i>Double</i>
    <a href="#imageid" title="ImageId">ImageId</a>: <i>String</i>
    <a href="#instancetype" title="InstanceType">InstanceType</a>: <i>String</i>
    <a href="#isoutdated" title="IsOutdated">IsOutdated</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#nameprefix" title="NamePrefix">NamePrefix</a>: <i>String</i>
    <a href="#needslb" title="NeedSlb">NeedSlb</a>: <i>Boolean</i>
    <a href="#nodenumber" title="NodeNumber">NodeNumber</a>: <i>Double</i>
    <a href="#nodes" title="Nodes">Nodes</a>: <i>
      - &lt;a href=&#34;nodes.md&#34;&gt;Nodes&lt;/a&gt;</i>
    <a href="#password" title="Password">Password</a>: <i>String</i>
    <a href="#releaseeip" title="ReleaseEip">ReleaseEip</a>: <i>Boolean</i>
    <a href="#securitygroupid" title="SecurityGroupId">SecurityGroupId</a>: <i>String</i>
    <a href="#size" title="Size">Size</a>: <i>Double</i>
    <a href="#slbid" title="SlbId">SlbId</a>: <i>String</i>
    <a href="#vpcid" title="VpcId">VpcId</a>: <i>String</i>
    <a href="#vswitchid" title="VswitchId">VswitchId</a>: <i>String</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AgentVersion

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CidrBlock

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiskCategory

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiskSize

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImageId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsOutdated

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NamePrefix

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NeedSlb

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeNumber

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Nodes

_Required_: No

_Type_: List of &lt;a href=&#34;nodes.md&#34;&gt;Nodes&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Password

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReleaseEip

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityGroupId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Size

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlbId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VswitchId

_Required_: Yes

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

#### AgentVersion

Returns the &lt;code&gt;AgentVersion&lt;/code&gt; value.

#### Nodes

Returns the &lt;code&gt;Nodes&lt;/code&gt; value.

#### SecurityGroupId

Returns the &lt;code&gt;SecurityGroupId&lt;/code&gt; value.

#### SlbId

Returns the &lt;code&gt;SlbId&lt;/code&gt; value.

#### VpcId

Returns the &lt;code&gt;VpcId&lt;/code&gt; value.
