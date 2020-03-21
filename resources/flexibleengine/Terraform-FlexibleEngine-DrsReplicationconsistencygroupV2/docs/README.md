# Terraform::FlexibleEngine::DrsReplicationconsistencygroupV2

CloudFormation equivalent of flexibleengine_drs_replicationconsistencygroup_v2

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::FlexibleEngine::DrsReplicationconsistencygroupV2",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#prioritystation" title="PriorityStation">PriorityStation</a>" : <i>String</i>,
        "<a href="#replicationids" title="ReplicationIds">ReplicationIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#replicationmodel" title="ReplicationModel">ReplicationModel</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: Terraform::FlexibleEngine::DrsReplicationconsistencygroupV2
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#prioritystation" title="PriorityStation">PriorityStation</a>: <i>String</i>
    <a href="#replicationids" title="ReplicationIds">ReplicationIds</a>: <i>
      - String</i>
    <a href="#replicationmodel" title="ReplicationModel">ReplicationModel</a>: <i>String</i>
</pre>

## Properties

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PriorityStation

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReplicationIds

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReplicationModel

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

#### CreatedAt

Returns the <code>CreatedAt</code> value.

#### FailureDetail

Returns the <code>FailureDetail</code> value.

#### FaultLevel

Returns the <code>FaultLevel</code> value.

#### ReplicationStatus

Returns the <code>ReplicationStatus</code> value.

#### Status

Returns the <code>Status</code> value.

#### UpdatedAt

Returns the <code>UpdatedAt</code> value.
