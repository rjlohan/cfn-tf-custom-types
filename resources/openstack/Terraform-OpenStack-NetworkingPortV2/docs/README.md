# Terraform::OpenStack::NetworkingPortV2

CloudFormation equivalent of openstack_networking_port_v2

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OpenStack::NetworkingPortV2",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#adminstateup" title="AdminStateUp">AdminStateUp</a>" : <i>Boolean</i>,
        "<a href="#allfixedips" title="AllFixedIps">AllFixedIps</a>" : <i>[ String, ... ]</i>,
        "<a href="#allsecuritygroupids" title="AllSecurityGroupIds">AllSecurityGroupIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#alltags" title="AllTags">AllTags</a>" : <i>[ String, ... ]</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#deviceid" title="DeviceId">DeviceId</a>" : <i>String</i>,
        "<a href="#deviceowner" title="DeviceOwner">DeviceOwner</a>" : <i>String</i>,
        "<a href="#dnsassignment" title="DnsAssignment">DnsAssignment</a>" : <i>[ [ &lt;a href=&#34;dnsassignment.md&#34;&gt;DnsAssignment&lt;/a&gt;, ... ], ... ]</i>,
        "<a href="#dnsname" title="DnsName">DnsName</a>" : <i>String</i>,
        "<a href="#macaddress" title="MacAddress">MacAddress</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#networkid" title="NetworkId">NetworkId</a>" : <i>String</i>,
        "<a href="#nofixedip" title="NoFixedIp">NoFixedIp</a>" : <i>Boolean</i>,
        "<a href="#nosecuritygroups" title="NoSecurityGroups">NoSecurityGroups</a>" : <i>Boolean</i>,
        "<a href="#portsecurityenabled" title="PortSecurityEnabled">PortSecurityEnabled</a>" : <i>Boolean</i>,
        "<a href="#qospolicyid" title="QosPolicyId">QosPolicyId</a>" : <i>String</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#securitygroupids" title="SecurityGroupIds">SecurityGroupIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ String, ... ]</i>,
        "<a href="#tenantid" title="TenantId">TenantId</a>" : <i>String</i>,
        "<a href="#valuespecs" title="ValueSpecs">ValueSpecs</a>" : <i>[ &lt;a href=&#34;valuespecs.md&#34;&gt;ValueSpecs&lt;/a&gt;, ... ]</i>,
        "<a href="#allowedaddresspairs" title="AllowedAddressPairs">AllowedAddressPairs</a>" : <i>[ &lt;a href=&#34;allowedaddresspairs.md&#34;&gt;AllowedAddressPairs&lt;/a&gt;, ... ]</i>,
        "<a href="#binding" title="Binding">Binding</a>" : <i>[ &lt;a href=&#34;binding.md&#34;&gt;Binding&lt;/a&gt;, ... ]</i>,
        "<a href="#extradhcpoption" title="ExtraDhcpOption">ExtraDhcpOption</a>" : <i>[ &lt;a href=&#34;extradhcpoption.md&#34;&gt;ExtraDhcpOption&lt;/a&gt;, ... ]</i>,
        "<a href="#fixedip" title="FixedIp">FixedIp</a>" : <i>[ &lt;a href=&#34;fixedip.md&#34;&gt;FixedIp&lt;/a&gt;, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OpenStack::NetworkingPortV2
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#adminstateup" title="AdminStateUp">AdminStateUp</a>: <i>Boolean</i>
    <a href="#allfixedips" title="AllFixedIps">AllFixedIps</a>: <i>
      - String</i>
    <a href="#allsecuritygroupids" title="AllSecurityGroupIds">AllSecurityGroupIds</a>: <i>
      - String</i>
    <a href="#alltags" title="AllTags">AllTags</a>: <i>
      - String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#deviceid" title="DeviceId">DeviceId</a>: <i>String</i>
    <a href="#deviceowner" title="DeviceOwner">DeviceOwner</a>: <i>String</i>
    <a href="#dnsassignment" title="DnsAssignment">DnsAssignment</a>: <i>
      - List of &lt;a href=&#34;dnsassignment.md&#34;&gt;DnsAssignment&lt;/a&gt;</i>
    <a href="#dnsname" title="DnsName">DnsName</a>: <i>String</i>
    <a href="#macaddress" title="MacAddress">MacAddress</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#networkid" title="NetworkId">NetworkId</a>: <i>String</i>
    <a href="#nofixedip" title="NoFixedIp">NoFixedIp</a>: <i>Boolean</i>
    <a href="#nosecuritygroups" title="NoSecurityGroups">NoSecurityGroups</a>: <i>Boolean</i>
    <a href="#portsecurityenabled" title="PortSecurityEnabled">PortSecurityEnabled</a>: <i>Boolean</i>
    <a href="#qospolicyid" title="QosPolicyId">QosPolicyId</a>: <i>String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#securitygroupids" title="SecurityGroupIds">SecurityGroupIds</a>: <i>
      - String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - String</i>
    <a href="#tenantid" title="TenantId">TenantId</a>: <i>String</i>
    <a href="#valuespecs" title="ValueSpecs">ValueSpecs</a>: <i>
      - &lt;a href=&#34;valuespecs.md&#34;&gt;ValueSpecs&lt;/a&gt;</i>
    <a href="#allowedaddresspairs" title="AllowedAddressPairs">AllowedAddressPairs</a>: <i>
      - &lt;a href=&#34;allowedaddresspairs.md&#34;&gt;AllowedAddressPairs&lt;/a&gt;</i>
    <a href="#binding" title="Binding">Binding</a>: <i>
      - &lt;a href=&#34;binding.md&#34;&gt;Binding&lt;/a&gt;</i>
    <a href="#extradhcpoption" title="ExtraDhcpOption">ExtraDhcpOption</a>: <i>
      - &lt;a href=&#34;extradhcpoption.md&#34;&gt;ExtraDhcpOption&lt;/a&gt;</i>
    <a href="#fixedip" title="FixedIp">FixedIp</a>: <i>
      - &lt;a href=&#34;fixedip.md&#34;&gt;FixedIp&lt;/a&gt;</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdminStateUp

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllFixedIps

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllSecurityGroupIds

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllTags

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeviceId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeviceOwner

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsAssignment

_Required_: No

_Type_: List of List of &lt;a href=&#34;dnsassignment.md&#34;&gt;DnsAssignment&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MacAddress

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NoFixedIp

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NoSecurityGroups

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PortSecurityEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QosPolicyId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityGroupIds

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TenantId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ValueSpecs

_Required_: No

_Type_: List of &lt;a href=&#34;valuespecs.md&#34;&gt;ValueSpecs&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowedAddressPairs

_Required_: No

_Type_: List of &lt;a href=&#34;allowedaddresspairs.md&#34;&gt;AllowedAddressPairs&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Binding

_Required_: No

_Type_: List of &lt;a href=&#34;binding.md&#34;&gt;Binding&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExtraDhcpOption

_Required_: No

_Type_: List of &lt;a href=&#34;extradhcpoption.md&#34;&gt;ExtraDhcpOption&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FixedIp

_Required_: No

_Type_: List of &lt;a href=&#34;fixedip.md&#34;&gt;FixedIp&lt;/a&gt;

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

#### AllFixedIps

Returns the &lt;code&gt;AllFixedIps&lt;/code&gt; value.

#### AllSecurityGroupIds

Returns the &lt;code&gt;AllSecurityGroupIds&lt;/code&gt; value.

#### AllTags

Returns the &lt;code&gt;AllTags&lt;/code&gt; value.

#### DnsAssignment

Returns the &lt;code&gt;DnsAssignment&lt;/code&gt; value.
