# Terraform::OCI::DatabaseBackupDestination

CloudFormation equivalent of oci_database_backup_destination

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OCI::DatabaseBackupDestination",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#associateddatabases" title="AssociatedDatabases">AssociatedDatabases</a>" : <i>[ &lt;a href=&#34;associateddatabases.md&#34;&gt;AssociatedDatabases&lt;/a&gt;, ... ]</i>,
        "<a href="#compartmentid" title="CompartmentId">CompartmentId</a>" : <i>String</i>,
        "<a href="#connectionstring" title="ConnectionString">ConnectionString</a>" : <i>String</i>,
        "<a href="#definedtags" title="DefinedTags">DefinedTags</a>" : <i>[ &lt;a href=&#34;definedtags.md&#34;&gt;DefinedTags&lt;/a&gt;, ... ]</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#freeformtags" title="FreeformTags">FreeformTags</a>" : <i>[ &lt;a href=&#34;freeformtags.md&#34;&gt;FreeformTags&lt;/a&gt;, ... ]</i>,
        "<a href="#lifecycledetails" title="LifecycleDetails">LifecycleDetails</a>" : <i>String</i>,
        "<a href="#localmountpointpath" title="LocalMountPointPath">LocalMountPointPath</a>" : <i>String</i>,
        "<a href="#state" title="State">State</a>" : <i>String</i>,
        "<a href="#timecreated" title="TimeCreated">TimeCreated</a>" : <i>String</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#vpcusers" title="VpcUsers">VpcUsers</a>" : <i>[ String, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OCI::DatabaseBackupDestination
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#associateddatabases" title="AssociatedDatabases">AssociatedDatabases</a>: <i>
      - &lt;a href=&#34;associateddatabases.md&#34;&gt;AssociatedDatabases&lt;/a&gt;</i>
    <a href="#compartmentid" title="CompartmentId">CompartmentId</a>: <i>String</i>
    <a href="#connectionstring" title="ConnectionString">ConnectionString</a>: <i>String</i>
    <a href="#definedtags" title="DefinedTags">DefinedTags</a>: <i>
      - &lt;a href=&#34;definedtags.md&#34;&gt;DefinedTags&lt;/a&gt;</i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#freeformtags" title="FreeformTags">FreeformTags</a>: <i>
      - &lt;a href=&#34;freeformtags.md&#34;&gt;FreeformTags&lt;/a&gt;</i>
    <a href="#lifecycledetails" title="LifecycleDetails">LifecycleDetails</a>: <i>String</i>
    <a href="#localmountpointpath" title="LocalMountPointPath">LocalMountPointPath</a>: <i>String</i>
    <a href="#state" title="State">State</a>: <i>String</i>
    <a href="#timecreated" title="TimeCreated">TimeCreated</a>: <i>String</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#vpcusers" title="VpcUsers">VpcUsers</a>: <i>
      - String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AssociatedDatabases

_Required_: No

_Type_: List of &lt;a href=&#34;associateddatabases.md&#34;&gt;AssociatedDatabases&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CompartmentId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnectionString

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefinedTags

_Required_: No

_Type_: List of &lt;a href=&#34;definedtags.md&#34;&gt;DefinedTags&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FreeformTags

_Required_: No

_Type_: List of &lt;a href=&#34;freeformtags.md&#34;&gt;FreeformTags&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LifecycleDetails

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalMountPointPath

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### State

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeCreated

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcUsers

_Required_: No

_Type_: List of String

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

#### AssociatedDatabases

Returns the &lt;code&gt;AssociatedDatabases&lt;/code&gt; value.

#### LifecycleDetails

Returns the &lt;code&gt;LifecycleDetails&lt;/code&gt; value.

#### State

Returns the &lt;code&gt;State&lt;/code&gt; value.

#### TimeCreated

Returns the &lt;code&gt;TimeCreated&lt;/code&gt; value.
