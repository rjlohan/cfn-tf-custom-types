# Terraform::Google::OrganizationIamAuditConfig AuditLogConfig

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#exemptedmembers" title="ExemptedMembers">ExemptedMembers</a>" : <i>[ String, ... ]</i>,
    "<a href="#logtype" title="LogType">LogType</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#exemptedmembers" title="ExemptedMembers">ExemptedMembers</a>: <i>
      - String</i>
<a href="#logtype" title="LogType">LogType</a>: <i>String</i>
</pre>

## Properties

#### ExemptedMembers

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogType

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
