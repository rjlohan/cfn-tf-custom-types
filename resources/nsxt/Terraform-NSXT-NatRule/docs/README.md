# Terraform::NSXT::NatRule

CloudFormation equivalent of nsxt_nat_rule

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::NSXT::NatRule",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#action" title="Action">Action</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
        "<a href="#logging" title="Logging">Logging</a>" : <i>Boolean</i>,
        "<a href="#logicalrouterid" title="LogicalRouterId">LogicalRouterId</a>" : <i>String</i>,
        "<a href="#matchdestinationnetwork" title="MatchDestinationNetwork">MatchDestinationNetwork</a>" : <i>String</i>,
        "<a href="#matchsourcenetwork" title="MatchSourceNetwork">MatchSourceNetwork</a>" : <i>String</i>,
        "<a href="#natpass" title="NatPass">NatPass</a>" : <i>Boolean</i>,
        "<a href="#revision" title="Revision">Revision</a>" : <i>Double</i>,
        "<a href="#rulepriority" title="RulePriority">RulePriority</a>" : <i>Double</i>,
        "<a href="#translatednetwork" title="TranslatedNetwork">TranslatedNetwork</a>" : <i>String</i>,
        "<a href="#translatedports" title="TranslatedPorts">TranslatedPorts</a>" : <i>String</i>,
        "<a href="#tag" title="Tag">Tag</a>" : <i>[ &lt;a href=&#34;tag.md&#34;&gt;Tag&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::NSXT::NatRule
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#action" title="Action">Action</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
    <a href="#logging" title="Logging">Logging</a>: <i>Boolean</i>
    <a href="#logicalrouterid" title="LogicalRouterId">LogicalRouterId</a>: <i>String</i>
    <a href="#matchdestinationnetwork" title="MatchDestinationNetwork">MatchDestinationNetwork</a>: <i>String</i>
    <a href="#matchsourcenetwork" title="MatchSourceNetwork">MatchSourceNetwork</a>: <i>String</i>
    <a href="#natpass" title="NatPass">NatPass</a>: <i>Boolean</i>
    <a href="#revision" title="Revision">Revision</a>: <i>Double</i>
    <a href="#rulepriority" title="RulePriority">RulePriority</a>: <i>Double</i>
    <a href="#translatednetwork" title="TranslatedNetwork">TranslatedNetwork</a>: <i>String</i>
    <a href="#translatedports" title="TranslatedPorts">TranslatedPorts</a>: <i>String</i>
    <a href="#tag" title="Tag">Tag</a>: <i>
      - &lt;a href=&#34;tag.md&#34;&gt;Tag&lt;/a&gt;</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Action

_Required_: Yes

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

#### Enabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Logging

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogicalRouterId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MatchDestinationNetwork

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MatchSourceNetwork

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NatPass

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Revision

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RulePriority

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TranslatedNetwork

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TranslatedPorts

_Required_: No

_Type_: String

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

#### Revision

Returns the &lt;code&gt;Revision&lt;/code&gt; value.
