# Terraform::Cloudflare::AccessPolicy

CloudFormation equivalent of cloudflare_access_policy

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Cloudflare::AccessPolicy",
    "Properties" : {
        "<a href="#applicationid" title="ApplicationId">ApplicationId</a>" : <i>String</i>,
        "<a href="#decision" title="Decision">Decision</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#precedence" title="Precedence">Precedence</a>" : <i>Double</i>,
        "<a href="#zoneid" title="ZoneId">ZoneId</a>" : <i>String</i>,
        "<a href="#exclude" title="Exclude">Exclude</a>" : <i>[ <a href="exclude.md">Exclude</a>, ... ]</i>,
        "<a href="#include" title="Include">Include</a>" : <i>[ <a href="include.md">Include</a>, ... ]</i>,
        "<a href="#require" title="Require">Require</a>" : <i>[ <a href="require.md">Require</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Cloudflare::AccessPolicy
Properties:
    <a href="#applicationid" title="ApplicationId">ApplicationId</a>: <i>String</i>
    <a href="#decision" title="Decision">Decision</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#precedence" title="Precedence">Precedence</a>: <i>Double</i>
    <a href="#zoneid" title="ZoneId">ZoneId</a>: <i>String</i>
    <a href="#exclude" title="Exclude">Exclude</a>: <i>
      - <a href="exclude.md">Exclude</a></i>
    <a href="#include" title="Include">Include</a>: <i>
      - <a href="include.md">Include</a></i>
    <a href="#require" title="Require">Require</a>: <i>
      - <a href="require.md">Require</a></i>
</pre>

## Properties

#### ApplicationId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Decision

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Precedence

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ZoneId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Exclude

_Required_: No

_Type_: List of <a href="exclude.md">Exclude</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Include

_Required_: No

_Type_: List of <a href="include.md">Include</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Require

_Required_: No

_Type_: List of <a href="require.md">Require</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.
