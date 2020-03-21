# Terraform::Google::OrganizationIamCustomRole

CloudFormation equivalent of google_organization_iam_custom_role

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Google::OrganizationIamCustomRole",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#deleted" title="Deleted">Deleted</a>" : <i>Boolean</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#orgid" title="OrgId">OrgId</a>" : <i>String</i>,
        "<a href="#permissions" title="Permissions">Permissions</a>" : <i>[ String, ... ]</i>,
        "<a href="#roleid" title="RoleId">RoleId</a>" : <i>String</i>,
        "<a href="#stage" title="Stage">Stage</a>" : <i>String</i>,
        "<a href="#title" title="Title">Title</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Google::OrganizationIamCustomRole
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#deleted" title="Deleted">Deleted</a>: <i>Boolean</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#orgid" title="OrgId">OrgId</a>: <i>String</i>
    <a href="#permissions" title="Permissions">Permissions</a>: <i>
      - String</i>
    <a href="#roleid" title="RoleId">RoleId</a>: <i>String</i>
    <a href="#stage" title="Stage">Stage</a>: <i>String</i>
    <a href="#title" title="Title">Title</a>: <i>String</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Deleted

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OrgId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Permissions

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RoleId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Stage

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Title

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

#### Deleted

Returns the &lt;code&gt;Deleted&lt;/code&gt; value.
