# Terraform::Panos::ApplicationGroup

CloudFormation equivalent of panos_application_group

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Panos::ApplicationGroup",
    "Properties" : {
        "<a href="#applications" title="Applications">Applications</a>" : <i>[ String, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#vsys" title="Vsys">Vsys</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Panos::ApplicationGroup
Properties:
    <a href="#applications" title="Applications">Applications</a>: <i>
      - String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#vsys" title="Vsys">Vsys</a>: <i>String</i>
</pre>

## Properties

#### Applications

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vsys

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
