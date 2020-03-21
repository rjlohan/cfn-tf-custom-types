# Terraform::Vault::IdentityGroupPolicies

CloudFormation equivalent of vault_identity_group_policies

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Vault::IdentityGroupPolicies",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#exclusive" title="Exclusive">Exclusive</a>" : <i>Boolean</i>,
        "<a href="#groupid" title="GroupId">GroupId</a>" : <i>String</i>,
        "<a href="#groupname" title="GroupName">GroupName</a>" : <i>String</i>,
        "<a href="#policies" title="Policies">Policies</a>" : <i>[ String, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Vault::IdentityGroupPolicies
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#exclusive" title="Exclusive">Exclusive</a>: <i>Boolean</i>
    <a href="#groupid" title="GroupId">GroupId</a>: <i>String</i>
    <a href="#groupname" title="GroupName">GroupName</a>: <i>String</i>
    <a href="#policies" title="Policies">Policies</a>: <i>
      - String</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Exclusive

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Policies

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### GroupName

Returns the &lt;code&gt;GroupName&lt;/code&gt; value.
