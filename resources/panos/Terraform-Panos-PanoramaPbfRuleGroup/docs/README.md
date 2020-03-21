# Terraform::Panos::PanoramaPbfRuleGroup

CloudFormation equivalent of panos_panorama_pbf_rule_group

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Panos::PanoramaPbfRuleGroup",
    "Properties" : {
        "<a href="#devicegroup" title="DeviceGroup">DeviceGroup</a>" : <i>String</i>,
        "<a href="#positionkeyword" title="PositionKeyword">PositionKeyword</a>" : <i>String</i>,
        "<a href="#positionreference" title="PositionReference">PositionReference</a>" : <i>String</i>,
        "<a href="#rulebase" title="Rulebase">Rulebase</a>" : <i>String</i>,
        "<a href="#rule" title="Rule">Rule</a>" : <i>[ <a href="rule.md">Rule</a>, ... ]</i>,
        "<a href="#destination" title="Destination">Destination</a>" : <i>[ <a href="destination.md">Destination</a>, ... ]</i>,
        "<a href="#forwarding" title="Forwarding">Forwarding</a>" : <i>[ <a href="forwarding.md">Forwarding</a>, ... ]</i>,
        "<a href="#source" title="Source">Source</a>" : <i>[ <a href="source.md">Source</a>, ... ]</i>,
        "<a href="#target" title="Target">Target</a>" : <i>[ <a href="target.md">Target</a>, ... ]</i>,
        "<a href="#monitor" title="Monitor">Monitor</a>" : <i>[ <a href="monitor.md">Monitor</a>, ... ]</i>,
        "<a href="#symmetricreturn" title="SymmetricReturn">SymmetricReturn</a>" : <i>[ <a href="symmetricreturn.md">SymmetricReturn</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Panos::PanoramaPbfRuleGroup
Properties:
    <a href="#devicegroup" title="DeviceGroup">DeviceGroup</a>: <i>String</i>
    <a href="#positionkeyword" title="PositionKeyword">PositionKeyword</a>: <i>String</i>
    <a href="#positionreference" title="PositionReference">PositionReference</a>: <i>String</i>
    <a href="#rulebase" title="Rulebase">Rulebase</a>: <i>String</i>
    <a href="#rule" title="Rule">Rule</a>: <i>
      - <a href="rule.md">Rule</a></i>
    <a href="#destination" title="Destination">Destination</a>: <i>
      - <a href="destination.md">Destination</a></i>
    <a href="#forwarding" title="Forwarding">Forwarding</a>: <i>
      - <a href="forwarding.md">Forwarding</a></i>
    <a href="#source" title="Source">Source</a>: <i>
      - <a href="source.md">Source</a></i>
    <a href="#target" title="Target">Target</a>: <i>
      - <a href="target.md">Target</a></i>
    <a href="#monitor" title="Monitor">Monitor</a>: <i>
      - <a href="monitor.md">Monitor</a></i>
    <a href="#symmetricreturn" title="SymmetricReturn">SymmetricReturn</a>: <i>
      - <a href="symmetricreturn.md">SymmetricReturn</a></i>
</pre>

## Properties

#### DeviceGroup

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PositionKeyword

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PositionReference

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Rulebase

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Rule

_Required_: No

_Type_: List of <a href="rule.md">Rule</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Destination

_Required_: No

_Type_: List of <a href="destination.md">Destination</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Forwarding

_Required_: No

_Type_: List of <a href="forwarding.md">Forwarding</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Source

_Required_: No

_Type_: List of <a href="source.md">Source</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Target

_Required_: No

_Type_: List of <a href="target.md">Target</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Monitor

_Required_: No

_Type_: List of <a href="monitor.md">Monitor</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SymmetricReturn

_Required_: No

_Type_: List of <a href="symmetricreturn.md">SymmetricReturn</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.
