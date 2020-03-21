# Terraform::AWS::RamResourceShareAccepter

CloudFormation equivalent of aws_ram_resource_share_accepter

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::RamResourceShareAccepter",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#invitationarn" title="InvitationArn">InvitationArn</a>" : <i>String</i>,
        "<a href="#receiveraccountid" title="ReceiverAccountId">ReceiverAccountId</a>" : <i>String</i>,
        "<a href="#resources" title="Resources">Resources</a>" : <i>[ String, ... ]</i>,
        "<a href="#senderaccountid" title="SenderAccountId">SenderAccountId</a>" : <i>String</i>,
        "<a href="#sharearn" title="ShareArn">ShareArn</a>" : <i>String</i>,
        "<a href="#shareid" title="ShareId">ShareId</a>" : <i>String</i>,
        "<a href="#sharename" title="ShareName">ShareName</a>" : <i>String</i>,
        "<a href="#status" title="Status">Status</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::RamResourceShareAccepter
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#invitationarn" title="InvitationArn">InvitationArn</a>: <i>String</i>
    <a href="#receiveraccountid" title="ReceiverAccountId">ReceiverAccountId</a>: <i>String</i>
    <a href="#resources" title="Resources">Resources</a>: <i>
      - String</i>
    <a href="#senderaccountid" title="SenderAccountId">SenderAccountId</a>: <i>String</i>
    <a href="#sharearn" title="ShareArn">ShareArn</a>: <i>String</i>
    <a href="#shareid" title="ShareId">ShareId</a>: <i>String</i>
    <a href="#sharename" title="ShareName">ShareName</a>: <i>String</i>
    <a href="#status" title="Status">Status</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InvitationArn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReceiverAccountId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Resources

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SenderAccountId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ShareArn

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ShareId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ShareName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: &lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### InvitationArn

Returns the &lt;code&gt;InvitationArn&lt;/code&gt; value.

#### ReceiverAccountId

Returns the &lt;code&gt;ReceiverAccountId&lt;/code&gt; value.

#### Resources

Returns the &lt;code&gt;Resources&lt;/code&gt; value.

#### SenderAccountId

Returns the &lt;code&gt;SenderAccountId&lt;/code&gt; value.

#### ShareId

Returns the &lt;code&gt;ShareId&lt;/code&gt; value.

#### ShareName

Returns the &lt;code&gt;ShareName&lt;/code&gt; value.

#### Status

Returns the &lt;code&gt;Status&lt;/code&gt; value.
