# Terraform::OCI::OceOceInstance

CloudFormation equivalent of oci_oce_oce_instance

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OCI::OceOceInstance",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#adminemail" title="AdminEmail">AdminEmail</a>" : <i>String</i>,
        "<a href="#compartmentid" title="CompartmentId">CompartmentId</a>" : <i>String</i>,
        "<a href="#definedtags" title="DefinedTags">DefinedTags</a>" : <i>[ &lt;a href=&#34;definedtags.md&#34;&gt;DefinedTags&lt;/a&gt;, ... ]</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#freeformtags" title="FreeformTags">FreeformTags</a>" : <i>[ &lt;a href=&#34;freeformtags.md&#34;&gt;FreeformTags&lt;/a&gt;, ... ]</i>,
        "<a href="#guid" title="Guid">Guid</a>" : <i>String</i>,
        "<a href="#idcsaccesstoken" title="IdcsAccessToken">IdcsAccessToken</a>" : <i>String</i>,
        "<a href="#idcstenancy" title="IdcsTenancy">IdcsTenancy</a>" : <i>String</i>,
        "<a href="#instanceusagetype" title="InstanceUsageType">InstanceUsageType</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#objectstoragenamespace" title="ObjectStorageNamespace">ObjectStorageNamespace</a>" : <i>String</i>,
        "<a href="#service" title="Service">Service</a>" : <i>[ &lt;a href=&#34;service.md&#34;&gt;Service&lt;/a&gt;, ... ]</i>,
        "<a href="#state" title="State">State</a>" : <i>String</i>,
        "<a href="#statemessage" title="StateMessage">StateMessage</a>" : <i>String</i>,
        "<a href="#tenancyid" title="TenancyId">TenancyId</a>" : <i>String</i>,
        "<a href="#tenancyname" title="TenancyName">TenancyName</a>" : <i>String</i>,
        "<a href="#timecreated" title="TimeCreated">TimeCreated</a>" : <i>String</i>,
        "<a href="#timeupdated" title="TimeUpdated">TimeUpdated</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OCI::OceOceInstance
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#adminemail" title="AdminEmail">AdminEmail</a>: <i>String</i>
    <a href="#compartmentid" title="CompartmentId">CompartmentId</a>: <i>String</i>
    <a href="#definedtags" title="DefinedTags">DefinedTags</a>: <i>
      - &lt;a href=&#34;definedtags.md&#34;&gt;DefinedTags&lt;/a&gt;</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#freeformtags" title="FreeformTags">FreeformTags</a>: <i>
      - &lt;a href=&#34;freeformtags.md&#34;&gt;FreeformTags&lt;/a&gt;</i>
    <a href="#guid" title="Guid">Guid</a>: <i>String</i>
    <a href="#idcsaccesstoken" title="IdcsAccessToken">IdcsAccessToken</a>: <i>String</i>
    <a href="#idcstenancy" title="IdcsTenancy">IdcsTenancy</a>: <i>String</i>
    <a href="#instanceusagetype" title="InstanceUsageType">InstanceUsageType</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#objectstoragenamespace" title="ObjectStorageNamespace">ObjectStorageNamespace</a>: <i>String</i>
    <a href="#service" title="Service">Service</a>: <i>
      - &lt;a href=&#34;service.md&#34;&gt;Service&lt;/a&gt;</i>
    <a href="#state" title="State">State</a>: <i>String</i>
    <a href="#statemessage" title="StateMessage">StateMessage</a>: <i>String</i>
    <a href="#tenancyid" title="TenancyId">TenancyId</a>: <i>String</i>
    <a href="#tenancyname" title="TenancyName">TenancyName</a>: <i>String</i>
    <a href="#timecreated" title="TimeCreated">TimeCreated</a>: <i>String</i>
    <a href="#timeupdated" title="TimeUpdated">TimeUpdated</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdminEmail

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CompartmentId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefinedTags

_Required_: No

_Type_: List of &lt;a href=&#34;definedtags.md&#34;&gt;DefinedTags&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FreeformTags

_Required_: No

_Type_: List of &lt;a href=&#34;freeformtags.md&#34;&gt;FreeformTags&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Guid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IdcsAccessToken

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IdcsTenancy

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceUsageType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ObjectStorageNamespace

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Service

_Required_: No

_Type_: List of &lt;a href=&#34;service.md&#34;&gt;Service&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### State

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StateMessage

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TenancyId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TenancyName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeCreated

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeUpdated

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

#### Guid

Returns the &lt;code&gt;Guid&lt;/code&gt; value.

#### IdcsTenancy

Returns the &lt;code&gt;IdcsTenancy&lt;/code&gt; value.

#### Service

Returns the &lt;code&gt;Service&lt;/code&gt; value.

#### State

Returns the &lt;code&gt;State&lt;/code&gt; value.

#### StateMessage

Returns the &lt;code&gt;StateMessage&lt;/code&gt; value.

#### TimeCreated

Returns the &lt;code&gt;TimeCreated&lt;/code&gt; value.

#### TimeUpdated

Returns the &lt;code&gt;TimeUpdated&lt;/code&gt; value.
