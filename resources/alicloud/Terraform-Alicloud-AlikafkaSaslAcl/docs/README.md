# Terraform::Alicloud::AlikafkaSaslAcl

CloudFormation equivalent of alicloud_alikafka_sasl_acl

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Alicloud::AlikafkaSaslAcl",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#acloperationtype" title="AclOperationType">AclOperationType</a>" : <i>String</i>,
        "<a href="#aclresourcename" title="AclResourceName">AclResourceName</a>" : <i>String</i>,
        "<a href="#aclresourcepatterntype" title="AclResourcePatternType">AclResourcePatternType</a>" : <i>String</i>,
        "<a href="#aclresourcetype" title="AclResourceType">AclResourceType</a>" : <i>String</i>,
        "<a href="#host" title="Host">Host</a>" : <i>String</i>,
        "<a href="#instanceid" title="InstanceId">InstanceId</a>" : <i>String</i>,
        "<a href="#username" title="Username">Username</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Alicloud::AlikafkaSaslAcl
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#acloperationtype" title="AclOperationType">AclOperationType</a>: <i>String</i>
    <a href="#aclresourcename" title="AclResourceName">AclResourceName</a>: <i>String</i>
    <a href="#aclresourcepatterntype" title="AclResourcePatternType">AclResourcePatternType</a>: <i>String</i>
    <a href="#aclresourcetype" title="AclResourceType">AclResourceType</a>: <i>String</i>
    <a href="#host" title="Host">Host</a>: <i>String</i>
    <a href="#instanceid" title="InstanceId">InstanceId</a>: <i>String</i>
    <a href="#username" title="Username">Username</a>: <i>String</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AclOperationType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AclResourceName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AclResourcePatternType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AclResourceType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Host

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceId

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

#### Host

Returns the &lt;code&gt;Host&lt;/code&gt; value.
