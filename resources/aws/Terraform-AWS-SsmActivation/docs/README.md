# Terraform::AWS::SsmActivation

CloudFormation equivalent of aws_ssm_activation

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::SsmActivation",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#activationcode" title="ActivationCode">ActivationCode</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#expirationdate" title="ExpirationDate">ExpirationDate</a>" : <i>String</i>,
        "<a href="#expired" title="Expired">Expired</a>" : <i>String</i>,
        "<a href="#iamrole" title="IamRole">IamRole</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#registrationcount" title="RegistrationCount">RegistrationCount</a>" : <i>Double</i>,
        "<a href="#registrationlimit" title="RegistrationLimit">RegistrationLimit</a>" : <i>Double</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::SsmActivation
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#activationcode" title="ActivationCode">ActivationCode</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#expirationdate" title="ExpirationDate">ExpirationDate</a>: <i>String</i>
    <a href="#expired" title="Expired">Expired</a>: <i>String</i>
    <a href="#iamrole" title="IamRole">IamRole</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#registrationcount" title="RegistrationCount">RegistrationCount</a>: <i>Double</i>
    <a href="#registrationlimit" title="RegistrationLimit">RegistrationLimit</a>: <i>Double</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ActivationCode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExpirationDate

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Expired

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IamRole

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RegistrationCount

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RegistrationLimit

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### ActivationCode

Returns the &lt;code&gt;ActivationCode&lt;/code&gt; value.

#### Expired

Returns the &lt;code&gt;Expired&lt;/code&gt; value.

#### RegistrationCount

Returns the &lt;code&gt;RegistrationCount&lt;/code&gt; value.
