# Terraform::Google::AccessContextManagerAccessLevel DevicePolicy

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#alloweddevicemanagementlevels" title="AllowedDeviceManagementLevels">AllowedDeviceManagementLevels</a>" : <i>[ String, ... ]</i>,
    "<a href="#allowedencryptionstatuses" title="AllowedEncryptionStatuses">AllowedEncryptionStatuses</a>" : <i>[ String, ... ]</i>,
    "<a href="#requireadminapproval" title="RequireAdminApproval">RequireAdminApproval</a>" : <i>Boolean</i>,
    "<a href="#requirecorpowned" title="RequireCorpOwned">RequireCorpOwned</a>" : <i>Boolean</i>,
    "<a href="#requirescreenlock" title="RequireScreenLock">RequireScreenLock</a>" : <i>Boolean</i>,
    "<a href="#osconstraints" title="OsConstraints">OsConstraints</a>" : <i>[ &lt;a href=&#34;devicepolicy-osconstraints.md&#34;&gt;OsConstraints&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#alloweddevicemanagementlevels" title="AllowedDeviceManagementLevels">AllowedDeviceManagementLevels</a>: <i>
      - String</i>
<a href="#allowedencryptionstatuses" title="AllowedEncryptionStatuses">AllowedEncryptionStatuses</a>: <i>
      - String</i>
<a href="#requireadminapproval" title="RequireAdminApproval">RequireAdminApproval</a>: <i>Boolean</i>
<a href="#requirecorpowned" title="RequireCorpOwned">RequireCorpOwned</a>: <i>Boolean</i>
<a href="#requirescreenlock" title="RequireScreenLock">RequireScreenLock</a>: <i>Boolean</i>
<a href="#osconstraints" title="OsConstraints">OsConstraints</a>: <i>
      - &lt;a href=&#34;devicepolicy-osconstraints.md&#34;&gt;OsConstraints&lt;/a&gt;</i>
</pre>

## Properties

#### AllowedDeviceManagementLevels

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowedEncryptionStatuses

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequireAdminApproval

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequireCorpOwned

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequireScreenLock

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OsConstraints

_Required_: No
_Type_: List of &lt;a href=&#34;devicepolicy-osconstraints.md&#34;&gt;OsConstraints&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
