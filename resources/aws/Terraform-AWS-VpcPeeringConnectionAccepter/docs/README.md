# Terraform::AWS::VpcPeeringConnectionAccepter

CloudFormation equivalent of aws_vpc_peering_connection_accepter

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::VpcPeeringConnectionAccepter",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#acceptstatus" title="AcceptStatus">AcceptStatus</a>" : <i>String</i>,
        "<a href="#autoaccept" title="AutoAccept">AutoAccept</a>" : <i>Boolean</i>,
        "<a href="#peerownerid" title="PeerOwnerId">PeerOwnerId</a>" : <i>String</i>,
        "<a href="#peerregion" title="PeerRegion">PeerRegion</a>" : <i>String</i>,
        "<a href="#peervpcid" title="PeerVpcId">PeerVpcId</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;, ... ]</i>,
        "<a href="#vpcid" title="VpcId">VpcId</a>" : <i>String</i>,
        "<a href="#vpcpeeringconnectionid" title="VpcPeeringConnectionId">VpcPeeringConnectionId</a>" : <i>String</i>,
        "<a href="#accepter" title="Accepter">Accepter</a>" : <i>[ &lt;a href=&#34;accepter.md&#34;&gt;Accepter&lt;/a&gt;, ... ]</i>,
        "<a href="#requester" title="Requester">Requester</a>" : <i>[ &lt;a href=&#34;requester.md&#34;&gt;Requester&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::VpcPeeringConnectionAccepter
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#acceptstatus" title="AcceptStatus">AcceptStatus</a>: <i>String</i>
    <a href="#autoaccept" title="AutoAccept">AutoAccept</a>: <i>Boolean</i>
    <a href="#peerownerid" title="PeerOwnerId">PeerOwnerId</a>: <i>String</i>
    <a href="#peerregion" title="PeerRegion">PeerRegion</a>: <i>String</i>
    <a href="#peervpcid" title="PeerVpcId">PeerVpcId</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;</i>
    <a href="#vpcid" title="VpcId">VpcId</a>: <i>String</i>
    <a href="#vpcpeeringconnectionid" title="VpcPeeringConnectionId">VpcPeeringConnectionId</a>: <i>String</i>
    <a href="#accepter" title="Accepter">Accepter</a>: <i>
      - &lt;a href=&#34;accepter.md&#34;&gt;Accepter&lt;/a&gt;</i>
    <a href="#requester" title="Requester">Requester</a>: <i>
      - &lt;a href=&#34;requester.md&#34;&gt;Requester&lt;/a&gt;</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AcceptStatus

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoAccept

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PeerOwnerId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PeerRegion

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PeerVpcId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcPeeringConnectionId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Accepter

_Required_: No

_Type_: List of &lt;a href=&#34;accepter.md&#34;&gt;Accepter&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Requester

_Required_: No

_Type_: List of &lt;a href=&#34;requester.md&#34;&gt;Requester&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### AcceptStatus

Returns the &lt;code&gt;AcceptStatus&lt;/code&gt; value.

#### PeerOwnerId

Returns the &lt;code&gt;PeerOwnerId&lt;/code&gt; value.

#### PeerRegion

Returns the &lt;code&gt;PeerRegion&lt;/code&gt; value.

#### PeerVpcId

Returns the &lt;code&gt;PeerVpcId&lt;/code&gt; value.

#### VpcId

Returns the &lt;code&gt;VpcId&lt;/code&gt; value.
