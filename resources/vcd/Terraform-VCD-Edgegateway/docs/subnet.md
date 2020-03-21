# Terraform::VCD::Edgegateway Subnet

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#gateway" title="Gateway">Gateway</a>" : <i>String</i>,
    "<a href="#ipaddress" title="IpAddress">IpAddress</a>" : <i>String</i>,
    "<a href="#netmask" title="Netmask">Netmask</a>" : <i>String</i>,
    "<a href="#usefordefaultroute" title="UseForDefaultRoute">UseForDefaultRoute</a>" : <i>Boolean</i>,
    "<a href="#suballocatepool" title="SuballocatePool">SuballocatePool</a>" : <i>[ &lt;a href=&#34;subnet-suballocatepool.md&#34;&gt;SuballocatePool&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#gateway" title="Gateway">Gateway</a>: <i>String</i>
<a href="#ipaddress" title="IpAddress">IpAddress</a>: <i>String</i>
<a href="#netmask" title="Netmask">Netmask</a>: <i>String</i>
<a href="#usefordefaultroute" title="UseForDefaultRoute">UseForDefaultRoute</a>: <i>Boolean</i>
<a href="#suballocatepool" title="SuballocatePool">SuballocatePool</a>: <i>
      - &lt;a href=&#34;subnet-suballocatepool.md&#34;&gt;SuballocatePool&lt;/a&gt;</i>
</pre>

## Properties

#### Gateway

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpAddress

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Netmask

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseForDefaultRoute

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SuballocatePool

_Required_: No
_Type_: List of &lt;a href=&#34;subnet-suballocatepool.md&#34;&gt;SuballocatePool&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
