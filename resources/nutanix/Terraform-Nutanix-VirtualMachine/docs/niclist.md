# Terraform::Nutanix::VirtualMachine NicList

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#isconnected" title="IsConnected">IsConnected</a>" : <i>String</i>,
    "<a href="#macaddress" title="MacAddress">MacAddress</a>" : <i>String</i>,
    "<a href="#model" title="Model">Model</a>" : <i>String</i>,
    "<a href="#networkfunctionchainreference" title="NetworkFunctionChainReference">NetworkFunctionChainReference</a>" : <i>[ <a href="niclist-networkfunctionchainreference.md">NetworkFunctionChainReference</a>, ... ]</i>,
    "<a href="#networkfunctionnictype" title="NetworkFunctionNicType">NetworkFunctionNicType</a>" : <i>String</i>,
    "<a href="#nictype" title="NicType">NicType</a>" : <i>String</i>,
    "<a href="#subnetname" title="SubnetName">SubnetName</a>" : <i>String</i>,
    "<a href="#subnetuuid" title="SubnetUuid">SubnetUuid</a>" : <i>String</i>,
    "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
    "<a href="#ipendpointlist" title="IpEndpointList">IpEndpointList</a>" : <i>[ <a href="niclist-ipendpointlist.md">IpEndpointList</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#isconnected" title="IsConnected">IsConnected</a>: <i>String</i>
<a href="#macaddress" title="MacAddress">MacAddress</a>: <i>String</i>
<a href="#model" title="Model">Model</a>: <i>String</i>
<a href="#networkfunctionchainreference" title="NetworkFunctionChainReference">NetworkFunctionChainReference</a>: <i>
      - <a href="niclist-networkfunctionchainreference.md">NetworkFunctionChainReference</a></i>
<a href="#networkfunctionnictype" title="NetworkFunctionNicType">NetworkFunctionNicType</a>: <i>String</i>
<a href="#nictype" title="NicType">NicType</a>: <i>String</i>
<a href="#subnetname" title="SubnetName">SubnetName</a>: <i>String</i>
<a href="#subnetuuid" title="SubnetUuid">SubnetUuid</a>: <i>String</i>
<a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
<a href="#ipendpointlist" title="IpEndpointList">IpEndpointList</a>: <i>
      - <a href="niclist-ipendpointlist.md">IpEndpointList</a></i>
</pre>

## Properties

#### IsConnected

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MacAddress

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Model

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkFunctionChainReference

_Required_: No

_Type_: List of <a href="niclist-networkfunctionchainreference.md">NetworkFunctionChainReference</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkFunctionNicType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NicType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubnetName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubnetUuid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpEndpointList

_Required_: No

_Type_: List of <a href="niclist-ipendpointlist.md">IpEndpointList</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
