# Terraform::AWS::DxBgpPeer

CloudFormation equivalent of aws_dx_bgp_peer

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::DxBgpPeer",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#addressfamily" title="AddressFamily">AddressFamily</a>" : <i>String</i>,
        "<a href="#amazonaddress" title="AmazonAddress">AmazonAddress</a>" : <i>String</i>,
        "<a href="#awsdevice" title="AwsDevice">AwsDevice</a>" : <i>String</i>,
        "<a href="#bgpasn" title="BgpAsn">BgpAsn</a>" : <i>Double</i>,
        "<a href="#bgpauthkey" title="BgpAuthKey">BgpAuthKey</a>" : <i>String</i>,
        "<a href="#bgppeerid" title="BgpPeerId">BgpPeerId</a>" : <i>String</i>,
        "<a href="#bgpstatus" title="BgpStatus">BgpStatus</a>" : <i>String</i>,
        "<a href="#customeraddress" title="CustomerAddress">CustomerAddress</a>" : <i>String</i>,
        "<a href="#virtualinterfaceid" title="VirtualInterfaceId">VirtualInterfaceId</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::DxBgpPeer
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#addressfamily" title="AddressFamily">AddressFamily</a>: <i>String</i>
    <a href="#amazonaddress" title="AmazonAddress">AmazonAddress</a>: <i>String</i>
    <a href="#awsdevice" title="AwsDevice">AwsDevice</a>: <i>String</i>
    <a href="#bgpasn" title="BgpAsn">BgpAsn</a>: <i>Double</i>
    <a href="#bgpauthkey" title="BgpAuthKey">BgpAuthKey</a>: <i>String</i>
    <a href="#bgppeerid" title="BgpPeerId">BgpPeerId</a>: <i>String</i>
    <a href="#bgpstatus" title="BgpStatus">BgpStatus</a>: <i>String</i>
    <a href="#customeraddress" title="CustomerAddress">CustomerAddress</a>: <i>String</i>
    <a href="#virtualinterfaceid" title="VirtualInterfaceId">VirtualInterfaceId</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AddressFamily

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AmazonAddress

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AwsDevice

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BgpAsn

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BgpAuthKey

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BgpPeerId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BgpStatus

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomerAddress

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VirtualInterfaceId

_Required_: Yes

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

#### AwsDevice

Returns the &lt;code&gt;AwsDevice&lt;/code&gt; value.

#### BgpPeerId

Returns the &lt;code&gt;BgpPeerId&lt;/code&gt; value.

#### BgpStatus

Returns the &lt;code&gt;BgpStatus&lt;/code&gt; value.
