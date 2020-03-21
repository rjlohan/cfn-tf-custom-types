# Terraform::Nutanix::VirtualMachine DiskList DeviceProperties

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#devicetype" title="DeviceType">DeviceType</a>" : <i>String</i>,
    "<a href="#diskaddress" title="DiskAddress">DiskAddress</a>" : <i>[ <a href="disklist-deviceproperties-diskaddress.md">DiskAddress</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#devicetype" title="DeviceType">DeviceType</a>: <i>String</i>
<a href="#diskaddress" title="DiskAddress">DiskAddress</a>: <i>
      - <a href="disklist-deviceproperties-diskaddress.md">DiskAddress</a></i>
</pre>

## Properties

#### DeviceType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiskAddress

_Required_: No

_Type_: List of <a href="disklist-deviceproperties-diskaddress.md">DiskAddress</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
