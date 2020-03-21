# Terraform::OpenTelekomCloud::NetworkingVipAssociateV2

CloudFormation equivalent of opentelekomcloud_networking_vip_associate_v2

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OpenTelekomCloud::NetworkingVipAssociateV2",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#portids" title="PortIds">PortIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#vipid" title="VipId">VipId</a>" : <i>String</i>,
        "<a href="#vipipaddress" title="VipIpAddress">VipIpAddress</a>" : <i>String</i>,
        "<a href="#vipsubnetid" title="VipSubnetId">VipSubnetId</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OpenTelekomCloud::NetworkingVipAssociateV2
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#portids" title="PortIds">PortIds</a>: <i>
      - String</i>
    <a href="#vipid" title="VipId">VipId</a>: <i>String</i>
    <a href="#vipipaddress" title="VipIpAddress">VipIpAddress</a>: <i>String</i>
    <a href="#vipsubnetid" title="VipSubnetId">VipSubnetId</a>: <i>String</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PortIds

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VipId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VipIpAddress

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VipSubnetId

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

#### VipIpAddress

Returns the &lt;code&gt;VipIpAddress&lt;/code&gt; value.

#### VipSubnetId

Returns the &lt;code&gt;VipSubnetId&lt;/code&gt; value.
