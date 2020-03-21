# Terraform::AzureAD::Application AppRole

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#allowedmembertypes" title="AllowedMemberTypes">AllowedMemberTypes</a>" : <i>[ String, ... ]</i>,
    "<a href="#description" title="Description">Description</a>" : <i>String</i>,
    "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
    "<a href="#isenabled" title="IsEnabled">IsEnabled</a>" : <i>Boolean</i>,
    "<a href="#value" title="Value">Value</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#allowedmembertypes" title="AllowedMemberTypes">AllowedMemberTypes</a>: <i>
      - String</i>
<a href="#description" title="Description">Description</a>: <i>String</i>
<a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
<a href="#isenabled" title="IsEnabled">IsEnabled</a>: <i>Boolean</i>
<a href="#value" title="Value">Value</a>: <i>String</i>
</pre>

## Properties

#### AllowedMemberTypes

_Required_: Yes
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsEnabled

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Value

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
