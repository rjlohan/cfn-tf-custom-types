# Terraform::NSXT::LogicalRouterDownlinkPort

CloudFormation equivalent of nsxt_logical_router_downlink_port

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::NSXT::LogicalRouterDownlinkPort",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#ipaddress" title="IpAddress">IpAddress</a>" : <i>String</i>,
        "<a href="#linkedlogicalswitchportid" title="LinkedLogicalSwitchPortId">LinkedLogicalSwitchPortId</a>" : <i>String</i>,
        "<a href="#logicalrouterid" title="LogicalRouterId">LogicalRouterId</a>" : <i>String</i>,
        "<a href="#macaddress" title="MacAddress">MacAddress</a>" : <i>String</i>,
        "<a href="#revision" title="Revision">Revision</a>" : <i>Double</i>,
        "<a href="#urpfmode" title="UrpfMode">UrpfMode</a>" : <i>String</i>,
        "<a href="#servicebinding" title="ServiceBinding">ServiceBinding</a>" : <i>[ &lt;a href=&#34;servicebinding.md&#34;&gt;ServiceBinding&lt;/a&gt;, ... ]</i>,
        "<a href="#tag" title="Tag">Tag</a>" : <i>[ &lt;a href=&#34;tag.md&#34;&gt;Tag&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::NSXT::LogicalRouterDownlinkPort
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#ipaddress" title="IpAddress">IpAddress</a>: <i>String</i>
    <a href="#linkedlogicalswitchportid" title="LinkedLogicalSwitchPortId">LinkedLogicalSwitchPortId</a>: <i>String</i>
    <a href="#logicalrouterid" title="LogicalRouterId">LogicalRouterId</a>: <i>String</i>
    <a href="#macaddress" title="MacAddress">MacAddress</a>: <i>String</i>
    <a href="#revision" title="Revision">Revision</a>: <i>Double</i>
    <a href="#urpfmode" title="UrpfMode">UrpfMode</a>: <i>String</i>
    <a href="#servicebinding" title="ServiceBinding">ServiceBinding</a>: <i>
      - &lt;a href=&#34;servicebinding.md&#34;&gt;ServiceBinding&lt;/a&gt;</i>
    <a href="#tag" title="Tag">Tag</a>: <i>
      - &lt;a href=&#34;tag.md&#34;&gt;Tag&lt;/a&gt;</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpAddress

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LinkedLogicalSwitchPortId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogicalRouterId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MacAddress

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Revision

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UrpfMode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceBinding

_Required_: No

_Type_: List of &lt;a href=&#34;servicebinding.md&#34;&gt;ServiceBinding&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tag

_Required_: No

_Type_: List of &lt;a href=&#34;tag.md&#34;&gt;Tag&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### MacAddress

Returns the &lt;code&gt;MacAddress&lt;/code&gt; value.

#### Revision

Returns the &lt;code&gt;Revision&lt;/code&gt; value.
