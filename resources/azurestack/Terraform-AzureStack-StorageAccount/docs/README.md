# Terraform::AzureStack::StorageAccount

CloudFormation equivalent of azurestack_storage_account

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AzureStack::StorageAccount",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#accountencryptionsource" title="AccountEncryptionSource">AccountEncryptionSource</a>" : <i>String</i>,
        "<a href="#accountkind" title="AccountKind">AccountKind</a>" : <i>String</i>,
        "<a href="#accountreplicationtype" title="AccountReplicationType">AccountReplicationType</a>" : <i>String</i>,
        "<a href="#accounttier" title="AccountTier">AccountTier</a>" : <i>String</i>,
        "<a href="#accounttype" title="AccountType">AccountType</a>" : <i>String</i>,
        "<a href="#enableblobencryption" title="EnableBlobEncryption">EnableBlobEncryption</a>" : <i>Boolean</i>,
        "<a href="#location" title="Location">Location</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#primaryaccesskey" title="PrimaryAccessKey">PrimaryAccessKey</a>" : <i>String</i>,
        "<a href="#primaryblobconnectionstring" title="PrimaryBlobConnectionString">PrimaryBlobConnectionString</a>" : <i>String</i>,
        "<a href="#primaryblobendpoint" title="PrimaryBlobEndpoint">PrimaryBlobEndpoint</a>" : <i>String</i>,
        "<a href="#primaryconnectionstring" title="PrimaryConnectionString">PrimaryConnectionString</a>" : <i>String</i>,
        "<a href="#primaryfileendpoint" title="PrimaryFileEndpoint">PrimaryFileEndpoint</a>" : <i>String</i>,
        "<a href="#primarylocation" title="PrimaryLocation">PrimaryLocation</a>" : <i>String</i>,
        "<a href="#primaryqueueendpoint" title="PrimaryQueueEndpoint">PrimaryQueueEndpoint</a>" : <i>String</i>,
        "<a href="#primarytableendpoint" title="PrimaryTableEndpoint">PrimaryTableEndpoint</a>" : <i>String</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
        "<a href="#secondaryaccesskey" title="SecondaryAccessKey">SecondaryAccessKey</a>" : <i>String</i>,
        "<a href="#secondaryblobconnectionstring" title="SecondaryBlobConnectionString">SecondaryBlobConnectionString</a>" : <i>String</i>,
        "<a href="#secondaryblobendpoint" title="SecondaryBlobEndpoint">SecondaryBlobEndpoint</a>" : <i>String</i>,
        "<a href="#secondaryconnectionstring" title="SecondaryConnectionString">SecondaryConnectionString</a>" : <i>String</i>,
        "<a href="#secondarylocation" title="SecondaryLocation">SecondaryLocation</a>" : <i>String</i>,
        "<a href="#secondaryqueueendpoint" title="SecondaryQueueEndpoint">SecondaryQueueEndpoint</a>" : <i>String</i>,
        "<a href="#secondarytableendpoint" title="SecondaryTableEndpoint">SecondaryTableEndpoint</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;, ... ]</i>,
        "<a href="#customdomain" title="CustomDomain">CustomDomain</a>" : <i>[ &lt;a href=&#34;customdomain.md&#34;&gt;CustomDomain&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AzureStack::StorageAccount
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#accountencryptionsource" title="AccountEncryptionSource">AccountEncryptionSource</a>: <i>String</i>
    <a href="#accountkind" title="AccountKind">AccountKind</a>: <i>String</i>
    <a href="#accountreplicationtype" title="AccountReplicationType">AccountReplicationType</a>: <i>String</i>
    <a href="#accounttier" title="AccountTier">AccountTier</a>: <i>String</i>
    <a href="#accounttype" title="AccountType">AccountType</a>: <i>String</i>
    <a href="#enableblobencryption" title="EnableBlobEncryption">EnableBlobEncryption</a>: <i>Boolean</i>
    <a href="#location" title="Location">Location</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#primaryaccesskey" title="PrimaryAccessKey">PrimaryAccessKey</a>: <i>String</i>
    <a href="#primaryblobconnectionstring" title="PrimaryBlobConnectionString">PrimaryBlobConnectionString</a>: <i>String</i>
    <a href="#primaryblobendpoint" title="PrimaryBlobEndpoint">PrimaryBlobEndpoint</a>: <i>String</i>
    <a href="#primaryconnectionstring" title="PrimaryConnectionString">PrimaryConnectionString</a>: <i>String</i>
    <a href="#primaryfileendpoint" title="PrimaryFileEndpoint">PrimaryFileEndpoint</a>: <i>String</i>
    <a href="#primarylocation" title="PrimaryLocation">PrimaryLocation</a>: <i>String</i>
    <a href="#primaryqueueendpoint" title="PrimaryQueueEndpoint">PrimaryQueueEndpoint</a>: <i>String</i>
    <a href="#primarytableendpoint" title="PrimaryTableEndpoint">PrimaryTableEndpoint</a>: <i>String</i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
    <a href="#secondaryaccesskey" title="SecondaryAccessKey">SecondaryAccessKey</a>: <i>String</i>
    <a href="#secondaryblobconnectionstring" title="SecondaryBlobConnectionString">SecondaryBlobConnectionString</a>: <i>String</i>
    <a href="#secondaryblobendpoint" title="SecondaryBlobEndpoint">SecondaryBlobEndpoint</a>: <i>String</i>
    <a href="#secondaryconnectionstring" title="SecondaryConnectionString">SecondaryConnectionString</a>: <i>String</i>
    <a href="#secondarylocation" title="SecondaryLocation">SecondaryLocation</a>: <i>String</i>
    <a href="#secondaryqueueendpoint" title="SecondaryQueueEndpoint">SecondaryQueueEndpoint</a>: <i>String</i>
    <a href="#secondarytableendpoint" title="SecondaryTableEndpoint">SecondaryTableEndpoint</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;</i>
    <a href="#customdomain" title="CustomDomain">CustomDomain</a>: <i>
      - &lt;a href=&#34;customdomain.md&#34;&gt;CustomDomain&lt;/a&gt;</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AccountEncryptionSource

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AccountKind

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AccountReplicationType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AccountTier

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AccountType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableBlobEncryption

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Location

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrimaryAccessKey

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrimaryBlobConnectionString

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrimaryBlobEndpoint

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrimaryConnectionString

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrimaryFileEndpoint

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrimaryLocation

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrimaryQueueEndpoint

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrimaryTableEndpoint

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecondaryAccessKey

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecondaryBlobConnectionString

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecondaryBlobEndpoint

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecondaryConnectionString

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecondaryLocation

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecondaryQueueEndpoint

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecondaryTableEndpoint

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomDomain

_Required_: No

_Type_: List of &lt;a href=&#34;customdomain.md&#34;&gt;CustomDomain&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### PrimaryAccessKey

Returns the &lt;code&gt;PrimaryAccessKey&lt;/code&gt; value.

#### PrimaryBlobConnectionString

Returns the &lt;code&gt;PrimaryBlobConnectionString&lt;/code&gt; value.

#### PrimaryBlobEndpoint

Returns the &lt;code&gt;PrimaryBlobEndpoint&lt;/code&gt; value.

#### PrimaryConnectionString

Returns the &lt;code&gt;PrimaryConnectionString&lt;/code&gt; value.

#### PrimaryFileEndpoint

Returns the &lt;code&gt;PrimaryFileEndpoint&lt;/code&gt; value.

#### PrimaryLocation

Returns the &lt;code&gt;PrimaryLocation&lt;/code&gt; value.

#### PrimaryQueueEndpoint

Returns the &lt;code&gt;PrimaryQueueEndpoint&lt;/code&gt; value.

#### PrimaryTableEndpoint

Returns the &lt;code&gt;PrimaryTableEndpoint&lt;/code&gt; value.

#### SecondaryAccessKey

Returns the &lt;code&gt;SecondaryAccessKey&lt;/code&gt; value.

#### SecondaryBlobConnectionString

Returns the &lt;code&gt;SecondaryBlobConnectionString&lt;/code&gt; value.

#### SecondaryBlobEndpoint

Returns the &lt;code&gt;SecondaryBlobEndpoint&lt;/code&gt; value.

#### SecondaryConnectionString

Returns the &lt;code&gt;SecondaryConnectionString&lt;/code&gt; value.

#### SecondaryLocation

Returns the &lt;code&gt;SecondaryLocation&lt;/code&gt; value.

#### SecondaryQueueEndpoint

Returns the &lt;code&gt;SecondaryQueueEndpoint&lt;/code&gt; value.

#### SecondaryTableEndpoint

Returns the &lt;code&gt;SecondaryTableEndpoint&lt;/code&gt; value.
