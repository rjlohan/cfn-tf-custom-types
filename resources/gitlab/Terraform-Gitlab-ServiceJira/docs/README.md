# Terraform::Gitlab::ServiceJira

CloudFormation equivalent of gitlab_service_jira

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Gitlab::ServiceJira",
    "Properties" : {
        "<a href="#jiraissuetransitionid" title="JiraIssueTransitionId">JiraIssueTransitionId</a>" : <i>String</i>,
        "<a href="#password" title="Password">Password</a>" : <i>String</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#projectkey" title="ProjectKey">ProjectKey</a>" : <i>String</i>,
        "<a href="#url" title="Url">Url</a>" : <i>String</i>,
        "<a href="#username" title="Username">Username</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Gitlab::ServiceJira
Properties:
    <a href="#jiraissuetransitionid" title="JiraIssueTransitionId">JiraIssueTransitionId</a>: <i>String</i>
    <a href="#password" title="Password">Password</a>: <i>String</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#projectkey" title="ProjectKey">ProjectKey</a>: <i>String</i>
    <a href="#url" title="Url">Url</a>: <i>String</i>
    <a href="#username" title="Username">Username</a>: <i>String</i>
</pre>

## Properties

#### JiraIssueTransitionId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Password

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProjectKey

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Url

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Username

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

#### Active

Returns the <code>Active</code> value.

#### CreatedAt

Returns the <code>CreatedAt</code> value.

#### Title

Returns the <code>Title</code> value.

#### UpdatedAt

Returns the <code>UpdatedAt</code> value.
