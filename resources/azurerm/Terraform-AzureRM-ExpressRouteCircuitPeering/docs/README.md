# Terraform::AzureRM::ExpressRouteCircuitPeering

CloudFormation equivalent of azurerm_express_route_circuit_peering

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AzureRM::ExpressRouteCircuitPeering",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#azureasn" title="AzureAsn">AzureAsn</a>" : <i>Double</i>,
        "<a href="#expressroutecircuitname" title="ExpressRouteCircuitName">ExpressRouteCircuitName</a>" : <i>String</i>,
        "<a href="#peerasn" title="PeerAsn">PeerAsn</a>" : <i>Double</i>,
        "<a href="#peeringtype" title="PeeringType">PeeringType</a>" : <i>String</i>,
        "<a href="#primaryazureport" title="PrimaryAzurePort">PrimaryAzurePort</a>" : <i>String</i>,
        "<a href="#primarypeeraddressprefix" title="PrimaryPeerAddressPrefix">PrimaryPeerAddressPrefix</a>" : <i>String</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
        "<a href="#secondaryazureport" title="SecondaryAzurePort">SecondaryAzurePort</a>" : <i>String</i>,
        "<a href="#secondarypeeraddressprefix" title="SecondaryPeerAddressPrefix">SecondaryPeerAddressPrefix</a>" : <i>String</i>,
        "<a href="#sharedkey" title="SharedKey">SharedKey</a>" : <i>String</i>,
        "<a href="#vlanid" title="VlanId">VlanId</a>" : <i>Double</i>,
        "<a href="#microsoftpeeringconfig" title="MicrosoftPeeringConfig">MicrosoftPeeringConfig</a>" : <i>[ &lt;a href=&#34;microsoftpeeringconfig.md&#34;&gt;MicrosoftPeeringConfig&lt;/a&gt;, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AzureRM::ExpressRouteCircuitPeering
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#azureasn" title="AzureAsn">AzureAsn</a>: <i>Double</i>
    <a href="#expressroutecircuitname" title="ExpressRouteCircuitName">ExpressRouteCircuitName</a>: <i>String</i>
    <a href="#peerasn" title="PeerAsn">PeerAsn</a>: <i>Double</i>
    <a href="#peeringtype" title="PeeringType">PeeringType</a>: <i>String</i>
    <a href="#primaryazureport" title="PrimaryAzurePort">PrimaryAzurePort</a>: <i>String</i>
    <a href="#primarypeeraddressprefix" title="PrimaryPeerAddressPrefix">PrimaryPeerAddressPrefix</a>: <i>String</i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
    <a href="#secondaryazureport" title="SecondaryAzurePort">SecondaryAzurePort</a>: <i>String</i>
    <a href="#secondarypeeraddressprefix" title="SecondaryPeerAddressPrefix">SecondaryPeerAddressPrefix</a>: <i>String</i>
    <a href="#sharedkey" title="SharedKey">SharedKey</a>: <i>String</i>
    <a href="#vlanid" title="VlanId">VlanId</a>: <i>Double</i>
    <a href="#microsoftpeeringconfig" title="MicrosoftPeeringConfig">MicrosoftPeeringConfig</a>: <i>
      - &lt;a href=&#34;microsoftpeeringconfig.md&#34;&gt;MicrosoftPeeringConfig&lt;/a&gt;</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AzureAsn

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExpressRouteCircuitName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PeerAsn

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PeeringType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrimaryAzurePort

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrimaryPeerAddressPrefix

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecondaryAzurePort

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecondaryPeerAddressPrefix

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SharedKey

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VlanId

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MicrosoftPeeringConfig

_Required_: No

_Type_: List of &lt;a href=&#34;microsoftpeeringconfig.md&#34;&gt;MicrosoftPeeringConfig&lt;/a&gt;

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

#### AzureAsn

Returns the &lt;code&gt;AzureAsn&lt;/code&gt; value.

#### PrimaryAzurePort

Returns the &lt;code&gt;PrimaryAzurePort&lt;/code&gt; value.

#### SecondaryAzurePort

Returns the &lt;code&gt;SecondaryAzurePort&lt;/code&gt; value.
