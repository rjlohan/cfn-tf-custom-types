# Terraform::AzureRM::CosmosdbGremlinGraph

CloudFormation equivalent of azurerm_cosmosdb_gremlin_graph

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AzureRM::CosmosdbGremlinGraph",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#accountname" title="AccountName">AccountName</a>" : <i>String</i>,
        "<a href="#databasename" title="DatabaseName">DatabaseName</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#partitionkeypath" title="PartitionKeyPath">PartitionKeyPath</a>" : <i>String</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
        "<a href="#throughput" title="Throughput">Throughput</a>" : <i>Double</i>,
        "<a href="#conflictresolutionpolicy" title="ConflictResolutionPolicy">ConflictResolutionPolicy</a>" : <i>[ &lt;a href=&#34;conflictresolutionpolicy.md&#34;&gt;ConflictResolutionPolicy&lt;/a&gt;, ... ]</i>,
        "<a href="#indexpolicy" title="IndexPolicy">IndexPolicy</a>" : <i>[ &lt;a href=&#34;indexpolicy.md&#34;&gt;IndexPolicy&lt;/a&gt;, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>,
        "<a href="#uniquekey" title="UniqueKey">UniqueKey</a>" : <i>[ &lt;a href=&#34;uniquekey.md&#34;&gt;UniqueKey&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AzureRM::CosmosdbGremlinGraph
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#accountname" title="AccountName">AccountName</a>: <i>String</i>
    <a href="#databasename" title="DatabaseName">DatabaseName</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#partitionkeypath" title="PartitionKeyPath">PartitionKeyPath</a>: <i>String</i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
    <a href="#throughput" title="Throughput">Throughput</a>: <i>Double</i>
    <a href="#conflictresolutionpolicy" title="ConflictResolutionPolicy">ConflictResolutionPolicy</a>: <i>
      - &lt;a href=&#34;conflictresolutionpolicy.md&#34;&gt;ConflictResolutionPolicy&lt;/a&gt;</i>
    <a href="#indexpolicy" title="IndexPolicy">IndexPolicy</a>: <i>
      - &lt;a href=&#34;indexpolicy.md&#34;&gt;IndexPolicy&lt;/a&gt;</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
    <a href="#uniquekey" title="UniqueKey">UniqueKey</a>: <i>
      - &lt;a href=&#34;uniquekey.md&#34;&gt;UniqueKey&lt;/a&gt;</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AccountName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DatabaseName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PartitionKeyPath

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Throughput

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConflictResolutionPolicy

_Required_: No

_Type_: List of &lt;a href=&#34;conflictresolutionpolicy.md&#34;&gt;ConflictResolutionPolicy&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IndexPolicy

_Required_: No

_Type_: List of &lt;a href=&#34;indexpolicy.md&#34;&gt;IndexPolicy&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: &lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UniqueKey

_Required_: No

_Type_: List of &lt;a href=&#34;uniquekey.md&#34;&gt;UniqueKey&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.
