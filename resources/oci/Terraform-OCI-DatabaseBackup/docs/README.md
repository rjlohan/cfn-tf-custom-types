# Terraform::OCI::DatabaseBackup

CloudFormation equivalent of oci_database_backup

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OCI::DatabaseBackup",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#availabilitydomain" title="AvailabilityDomain">AvailabilityDomain</a>" : <i>String</i>,
        "<a href="#compartmentid" title="CompartmentId">CompartmentId</a>" : <i>String</i>,
        "<a href="#databaseedition" title="DatabaseEdition">DatabaseEdition</a>" : <i>String</i>,
        "<a href="#databaseid" title="DatabaseId">DatabaseId</a>" : <i>String</i>,
        "<a href="#databasesizeingbs" title="DatabaseSizeInGbs">DatabaseSizeInGbs</a>" : <i>Double</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#lifecycledetails" title="LifecycleDetails">LifecycleDetails</a>" : <i>String</i>,
        "<a href="#state" title="State">State</a>" : <i>String</i>,
        "<a href="#timeended" title="TimeEnded">TimeEnded</a>" : <i>String</i>,
        "<a href="#timestarted" title="TimeStarted">TimeStarted</a>" : <i>String</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OCI::DatabaseBackup
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#availabilitydomain" title="AvailabilityDomain">AvailabilityDomain</a>: <i>String</i>
    <a href="#compartmentid" title="CompartmentId">CompartmentId</a>: <i>String</i>
    <a href="#databaseedition" title="DatabaseEdition">DatabaseEdition</a>: <i>String</i>
    <a href="#databaseid" title="DatabaseId">DatabaseId</a>: <i>String</i>
    <a href="#databasesizeingbs" title="DatabaseSizeInGbs">DatabaseSizeInGbs</a>: <i>Double</i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#lifecycledetails" title="LifecycleDetails">LifecycleDetails</a>: <i>String</i>
    <a href="#state" title="State">State</a>: <i>String</i>
    <a href="#timeended" title="TimeEnded">TimeEnded</a>: <i>String</i>
    <a href="#timestarted" title="TimeStarted">TimeStarted</a>: <i>String</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AvailabilityDomain

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CompartmentId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DatabaseEdition

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DatabaseId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DatabaseSizeInGbs

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LifecycleDetails

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### State

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeEnded

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeStarted

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

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

#### AvailabilityDomain

Returns the &lt;code&gt;AvailabilityDomain&lt;/code&gt; value.

#### CompartmentId

Returns the &lt;code&gt;CompartmentId&lt;/code&gt; value.

#### DatabaseEdition

Returns the &lt;code&gt;DatabaseEdition&lt;/code&gt; value.

#### DatabaseSizeInGbs

Returns the &lt;code&gt;DatabaseSizeInGbs&lt;/code&gt; value.

#### LifecycleDetails

Returns the &lt;code&gt;LifecycleDetails&lt;/code&gt; value.

#### State

Returns the &lt;code&gt;State&lt;/code&gt; value.

#### TimeEnded

Returns the &lt;code&gt;TimeEnded&lt;/code&gt; value.

#### TimeStarted

Returns the &lt;code&gt;TimeStarted&lt;/code&gt; value.

#### Type

Returns the &lt;code&gt;Type&lt;/code&gt; value.
