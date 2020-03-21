# Terraform::HuaweiCloud::ElbBackendecs

CloudFormation equivalent of huaweicloud_elb_backendecs

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::HuaweiCloud::ElbBackendecs",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#createtime" title="CreateTime">CreateTime</a>" : <i>String</i>,
        "<a href="#healthstatus" title="HealthStatus">HealthStatus</a>" : <i>String</i>,
        "<a href="#listenerid" title="ListenerId">ListenerId</a>" : <i>String</i>,
        "<a href="#listeners" title="Listeners">Listeners</a>" : <i>[ &lt;a href=&#34;listeners.md&#34;&gt;Listeners&lt;/a&gt;, ... ]</i>,
        "<a href="#privateaddress" title="PrivateAddress">PrivateAddress</a>" : <i>String</i>,
        "<a href="#publicaddress" title="PublicAddress">PublicAddress</a>" : <i>String</i>,
        "<a href="#serverid" title="ServerId">ServerId</a>" : <i>String</i>,
        "<a href="#servername" title="ServerName">ServerName</a>" : <i>String</i>,
        "<a href="#status" title="Status">Status</a>" : <i>String</i>,
        "<a href="#updatetime" title="UpdateTime">UpdateTime</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::HuaweiCloud::ElbBackendecs
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#createtime" title="CreateTime">CreateTime</a>: <i>String</i>
    <a href="#healthstatus" title="HealthStatus">HealthStatus</a>: <i>String</i>
    <a href="#listenerid" title="ListenerId">ListenerId</a>: <i>String</i>
    <a href="#listeners" title="Listeners">Listeners</a>: <i>
      - &lt;a href=&#34;listeners.md&#34;&gt;Listeners&lt;/a&gt;</i>
    <a href="#privateaddress" title="PrivateAddress">PrivateAddress</a>: <i>String</i>
    <a href="#publicaddress" title="PublicAddress">PublicAddress</a>: <i>String</i>
    <a href="#serverid" title="ServerId">ServerId</a>: <i>String</i>
    <a href="#servername" title="ServerName">ServerName</a>: <i>String</i>
    <a href="#status" title="Status">Status</a>: <i>String</i>
    <a href="#updatetime" title="UpdateTime">UpdateTime</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CreateTime

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthStatus

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ListenerId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Listeners

_Required_: No

_Type_: List of &lt;a href=&#34;listeners.md&#34;&gt;Listeners&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivateAddress

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PublicAddress

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UpdateTime

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

#### CreateTime

Returns the &lt;code&gt;CreateTime&lt;/code&gt; value.

#### HealthStatus

Returns the &lt;code&gt;HealthStatus&lt;/code&gt; value.

#### Listeners

Returns the &lt;code&gt;Listeners&lt;/code&gt; value.

#### PublicAddress

Returns the &lt;code&gt;PublicAddress&lt;/code&gt; value.

#### ServerName

Returns the &lt;code&gt;ServerName&lt;/code&gt; value.

#### Status

Returns the &lt;code&gt;Status&lt;/code&gt; value.

#### UpdateTime

Returns the &lt;code&gt;UpdateTime&lt;/code&gt; value.
