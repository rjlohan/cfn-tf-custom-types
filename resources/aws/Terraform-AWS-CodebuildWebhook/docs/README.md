# Terraform::AWS::CodebuildWebhook

CloudFormation equivalent of aws_codebuild_webhook

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::CodebuildWebhook",
    "Properties" : {
        "<a href="#branchfilter" title="BranchFilter">BranchFilter</a>" : <i>String</i>,
        "<a href="#projectname" title="ProjectName">ProjectName</a>" : <i>String</i>,
        "<a href="#filtergroup" title="FilterGroup">FilterGroup</a>" : <i>[ <a href="filtergroup.md">FilterGroup</a>, ... ]</i>,
        "<a href="#filter" title="Filter">Filter</a>" : <i>[ <a href="filter.md">Filter</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::CodebuildWebhook
Properties:
    <a href="#branchfilter" title="BranchFilter">BranchFilter</a>: <i>String</i>
    <a href="#projectname" title="ProjectName">ProjectName</a>: <i>String</i>
    <a href="#filtergroup" title="FilterGroup">FilterGroup</a>: <i>
      - <a href="filtergroup.md">FilterGroup</a></i>
    <a href="#filter" title="Filter">Filter</a>: <i>
      - <a href="filter.md">Filter</a></i>
</pre>

## Properties

#### BranchFilter

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProjectName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FilterGroup

_Required_: No

_Type_: List of <a href="filtergroup.md">FilterGroup</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Filter

_Required_: No

_Type_: List of <a href="filter.md">Filter</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### PayloadUrl

Returns the <code>PayloadUrl</code> value.

#### Secret

Returns the <code>Secret</code> value.

#### Url

Returns the <code>Url</code> value.
