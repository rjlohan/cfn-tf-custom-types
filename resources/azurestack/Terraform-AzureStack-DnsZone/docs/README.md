# Terraform::AzureStack::DnsZone

CloudFormation equivalent of azurestack_dns_zone

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AzureStack::DnsZone",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#maxnumberofrecordsets" title="MaxNumberOfRecordSets">MaxNumberOfRecordSets</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#nameservers" title="NameServers">NameServers</a>" : <i>[ String, ... ]</i>,
        "<a href="#numberofrecordsets" title="NumberOfRecordSets">NumberOfRecordSets</a>" : <i>Double</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AzureStack::DnsZone
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#maxnumberofrecordsets" title="MaxNumberOfRecordSets">MaxNumberOfRecordSets</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#nameservers" title="NameServers">NameServers</a>: <i>
      - String</i>
    <a href="#numberofrecordsets" title="NumberOfRecordSets">NumberOfRecordSets</a>: <i>Double</i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxNumberOfRecordSets

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NameServers

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NumberOfRecordSets

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### MaxNumberOfRecordSets

Returns the &lt;code&gt;MaxNumberOfRecordSets&lt;/code&gt; value.

#### NameServers

Returns the &lt;code&gt;NameServers&lt;/code&gt; value.

#### NumberOfRecordSets

Returns the &lt;code&gt;NumberOfRecordSets&lt;/code&gt; value.
