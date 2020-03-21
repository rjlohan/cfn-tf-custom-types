# Terraform::AzureStack::VirtualMachine StorageDataDisk

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#caching" title="Caching">Caching</a>" : <i>String</i>,
    "<a href="#createoption" title="CreateOption">CreateOption</a>" : <i>String</i>,
    "<a href="#disksizegb" title="DiskSizeGb">DiskSizeGb</a>" : <i>Double</i>,
    "<a href="#lun" title="Lun">Lun</a>" : <i>Double</i>,
    "<a href="#manageddiskid" title="ManagedDiskId">ManagedDiskId</a>" : <i>String</i>,
    "<a href="#manageddisktype" title="ManagedDiskType">ManagedDiskType</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#vhduri" title="VhdUri">VhdUri</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#caching" title="Caching">Caching</a>: <i>String</i>
<a href="#createoption" title="CreateOption">CreateOption</a>: <i>String</i>
<a href="#disksizegb" title="DiskSizeGb">DiskSizeGb</a>: <i>Double</i>
<a href="#lun" title="Lun">Lun</a>: <i>Double</i>
<a href="#manageddiskid" title="ManagedDiskId">ManagedDiskId</a>: <i>String</i>
<a href="#manageddisktype" title="ManagedDiskType">ManagedDiskType</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#vhduri" title="VhdUri">VhdUri</a>: <i>String</i>
</pre>

## Properties

#### Caching

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CreateOption

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiskSizeGb

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Lun

_Required_: Yes
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ManagedDiskId

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ManagedDiskType

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VhdUri

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
