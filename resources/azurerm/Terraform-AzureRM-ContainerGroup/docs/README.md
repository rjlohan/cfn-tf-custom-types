# Terraform::AzureRM::ContainerGroup

CloudFormation equivalent of azurerm_container_group

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AzureRM::ContainerGroup",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#dnsnamelabel" title="DnsNameLabel">DnsNameLabel</a>" : <i>String</i>,
        "<a href="#fqdn" title="Fqdn">Fqdn</a>" : <i>String</i>,
        "<a href="#ipaddress" title="IpAddress">IpAddress</a>" : <i>String</i>,
        "<a href="#ipaddresstype" title="IpAddressType">IpAddressType</a>" : <i>String</i>,
        "<a href="#location" title="Location">Location</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#networkprofileid" title="NetworkProfileId">NetworkProfileId</a>" : <i>String</i>,
        "<a href="#ostype" title="OsType">OsType</a>" : <i>String</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
        "<a href="#restartpolicy" title="RestartPolicy">RestartPolicy</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;, ... ]</i>,
        "<a href="#container" title="Container">Container</a>" : <i>[ &lt;a href=&#34;container.md&#34;&gt;Container&lt;/a&gt;, ... ]</i>,
        "<a href="#diagnostics" title="Diagnostics">Diagnostics</a>" : <i>[ &lt;a href=&#34;diagnostics.md&#34;&gt;Diagnostics&lt;/a&gt;, ... ]</i>,
        "<a href="#identity" title="Identity">Identity</a>" : <i>[ &lt;a href=&#34;identity.md&#34;&gt;Identity&lt;/a&gt;, ... ]</i>,
        "<a href="#imageregistrycredential" title="ImageRegistryCredential">ImageRegistryCredential</a>" : <i>[ &lt;a href=&#34;imageregistrycredential.md&#34;&gt;ImageRegistryCredential&lt;/a&gt;, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>,
        "<a href="#gpu" title="Gpu">Gpu</a>" : <i>[ &lt;a href=&#34;gpu.md&#34;&gt;Gpu&lt;/a&gt;, ... ]</i>,
        "<a href="#livenessprobe" title="LivenessProbe">LivenessProbe</a>" : <i>[ &lt;a href=&#34;livenessprobe.md&#34;&gt;LivenessProbe&lt;/a&gt;, ... ]</i>,
        "<a href="#ports" title="Ports">Ports</a>" : <i>[ &lt;a href=&#34;ports.md&#34;&gt;Ports&lt;/a&gt;, ... ]</i>,
        "<a href="#readinessprobe" title="ReadinessProbe">ReadinessProbe</a>" : <i>[ &lt;a href=&#34;readinessprobe.md&#34;&gt;ReadinessProbe&lt;/a&gt;, ... ]</i>,
        "<a href="#volume" title="Volume">Volume</a>" : <i>[ &lt;a href=&#34;volume.md&#34;&gt;Volume&lt;/a&gt;, ... ]</i>,
        "<a href="#loganalytics" title="LogAnalytics">LogAnalytics</a>" : <i>[ &lt;a href=&#34;loganalytics.md&#34;&gt;LogAnalytics&lt;/a&gt;, ... ]</i>,
        "<a href="#httpget" title="HttpGet">HttpGet</a>" : <i>[ &lt;a href=&#34;httpget.md&#34;&gt;HttpGet&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AzureRM::ContainerGroup
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#dnsnamelabel" title="DnsNameLabel">DnsNameLabel</a>: <i>String</i>
    <a href="#fqdn" title="Fqdn">Fqdn</a>: <i>String</i>
    <a href="#ipaddress" title="IpAddress">IpAddress</a>: <i>String</i>
    <a href="#ipaddresstype" title="IpAddressType">IpAddressType</a>: <i>String</i>
    <a href="#location" title="Location">Location</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#networkprofileid" title="NetworkProfileId">NetworkProfileId</a>: <i>String</i>
    <a href="#ostype" title="OsType">OsType</a>: <i>String</i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
    <a href="#restartpolicy" title="RestartPolicy">RestartPolicy</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;</i>
    <a href="#container" title="Container">Container</a>: <i>
      - &lt;a href=&#34;container.md&#34;&gt;Container&lt;/a&gt;</i>
    <a href="#diagnostics" title="Diagnostics">Diagnostics</a>: <i>
      - &lt;a href=&#34;diagnostics.md&#34;&gt;Diagnostics&lt;/a&gt;</i>
    <a href="#identity" title="Identity">Identity</a>: <i>
      - &lt;a href=&#34;identity.md&#34;&gt;Identity&lt;/a&gt;</i>
    <a href="#imageregistrycredential" title="ImageRegistryCredential">ImageRegistryCredential</a>: <i>
      - &lt;a href=&#34;imageregistrycredential.md&#34;&gt;ImageRegistryCredential&lt;/a&gt;</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
    <a href="#gpu" title="Gpu">Gpu</a>: <i>
      - &lt;a href=&#34;gpu.md&#34;&gt;Gpu&lt;/a&gt;</i>
    <a href="#livenessprobe" title="LivenessProbe">LivenessProbe</a>: <i>
      - &lt;a href=&#34;livenessprobe.md&#34;&gt;LivenessProbe&lt;/a&gt;</i>
    <a href="#ports" title="Ports">Ports</a>: <i>
      - &lt;a href=&#34;ports.md&#34;&gt;Ports&lt;/a&gt;</i>
    <a href="#readinessprobe" title="ReadinessProbe">ReadinessProbe</a>: <i>
      - &lt;a href=&#34;readinessprobe.md&#34;&gt;ReadinessProbe&lt;/a&gt;</i>
    <a href="#volume" title="Volume">Volume</a>: <i>
      - &lt;a href=&#34;volume.md&#34;&gt;Volume&lt;/a&gt;</i>
    <a href="#loganalytics" title="LogAnalytics">LogAnalytics</a>: <i>
      - &lt;a href=&#34;loganalytics.md&#34;&gt;LogAnalytics&lt;/a&gt;</i>
    <a href="#httpget" title="HttpGet">HttpGet</a>: <i>
      - &lt;a href=&#34;httpget.md&#34;&gt;HttpGet&lt;/a&gt;</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsNameLabel

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Fqdn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpAddress

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpAddressType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Location

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkProfileId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OsType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RestartPolicy

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Container

_Required_: No

_Type_: List of &lt;a href=&#34;container.md&#34;&gt;Container&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Diagnostics

_Required_: No

_Type_: List of &lt;a href=&#34;diagnostics.md&#34;&gt;Diagnostics&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Identity

_Required_: No

_Type_: List of &lt;a href=&#34;identity.md&#34;&gt;Identity&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImageRegistryCredential

_Required_: No

_Type_: List of &lt;a href=&#34;imageregistrycredential.md&#34;&gt;ImageRegistryCredential&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: &lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Gpu

_Required_: No

_Type_: List of &lt;a href=&#34;gpu.md&#34;&gt;Gpu&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LivenessProbe

_Required_: No

_Type_: List of &lt;a href=&#34;livenessprobe.md&#34;&gt;LivenessProbe&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ports

_Required_: No

_Type_: List of &lt;a href=&#34;ports.md&#34;&gt;Ports&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReadinessProbe

_Required_: No

_Type_: List of &lt;a href=&#34;readinessprobe.md&#34;&gt;ReadinessProbe&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Volume

_Required_: No

_Type_: List of &lt;a href=&#34;volume.md&#34;&gt;Volume&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogAnalytics

_Required_: No

_Type_: List of &lt;a href=&#34;loganalytics.md&#34;&gt;LogAnalytics&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpGet

_Required_: No

_Type_: List of &lt;a href=&#34;httpget.md&#34;&gt;HttpGet&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Fqdn

Returns the &lt;code&gt;Fqdn&lt;/code&gt; value.

#### IpAddress

Returns the &lt;code&gt;IpAddress&lt;/code&gt; value.
