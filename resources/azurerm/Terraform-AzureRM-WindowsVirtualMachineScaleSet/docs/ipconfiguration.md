# Terraform::AzureRM::WindowsVirtualMachineScaleSet IpConfiguration

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#applicationgatewaybackendaddresspoolids" title="ApplicationGatewayBackendAddressPoolIds">ApplicationGatewayBackendAddressPoolIds</a>" : <i>[ String, ... ]</i>,
    "<a href="#applicationsecuritygroupids" title="ApplicationSecurityGroupIds">ApplicationSecurityGroupIds</a>" : <i>[ String, ... ]</i>,
    "<a href="#loadbalancerbackendaddresspoolids" title="LoadBalancerBackendAddressPoolIds">LoadBalancerBackendAddressPoolIds</a>" : <i>[ String, ... ]</i>,
    "<a href="#loadbalancerinboundnatrulesids" title="LoadBalancerInboundNatRulesIds">LoadBalancerInboundNatRulesIds</a>" : <i>[ String, ... ]</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#primary" title="Primary">Primary</a>" : <i>Boolean</i>,
    "<a href="#subnetid" title="SubnetId">SubnetId</a>" : <i>String</i>,
    "<a href="#version" title="Version">Version</a>" : <i>String</i>,
    "<a href="#publicipaddress" title="PublicIpAddress">PublicIpAddress</a>" : <i>[ &lt;a href=&#34;ipconfiguration-publicipaddress.md&#34;&gt;PublicIpAddress&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#applicationgatewaybackendaddresspoolids" title="ApplicationGatewayBackendAddressPoolIds">ApplicationGatewayBackendAddressPoolIds</a>: <i>
      - String</i>
<a href="#applicationsecuritygroupids" title="ApplicationSecurityGroupIds">ApplicationSecurityGroupIds</a>: <i>
      - String</i>
<a href="#loadbalancerbackendaddresspoolids" title="LoadBalancerBackendAddressPoolIds">LoadBalancerBackendAddressPoolIds</a>: <i>
      - String</i>
<a href="#loadbalancerinboundnatrulesids" title="LoadBalancerInboundNatRulesIds">LoadBalancerInboundNatRulesIds</a>: <i>
      - String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#primary" title="Primary">Primary</a>: <i>Boolean</i>
<a href="#subnetid" title="SubnetId">SubnetId</a>: <i>String</i>
<a href="#version" title="Version">Version</a>: <i>String</i>
<a href="#publicipaddress" title="PublicIpAddress">PublicIpAddress</a>: <i>
      - &lt;a href=&#34;ipconfiguration-publicipaddress.md&#34;&gt;PublicIpAddress&lt;/a&gt;</i>
</pre>

## Properties

#### ApplicationGatewayBackendAddressPoolIds

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApplicationSecurityGroupIds

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoadBalancerBackendAddressPoolIds

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoadBalancerInboundNatRulesIds

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Primary

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubnetId

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Version

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PublicIpAddress

_Required_: No
_Type_: List of &lt;a href=&#34;ipconfiguration-publicipaddress.md&#34;&gt;PublicIpAddress&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
