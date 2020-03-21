# Terraform::Brightbox::OrbitContainer

CloudFormation equivalent of brightbox_orbit_container

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Brightbox::OrbitContainer",
    "Properties" : {
        "<a href="#containerread" title="ContainerRead">ContainerRead</a>" : <i>[ String, ... ]</i>,
        "<a href="#containersynckey" title="ContainerSyncKey">ContainerSyncKey</a>" : <i>String</i>,
        "<a href="#containersyncto" title="ContainerSyncTo">ContainerSyncTo</a>" : <i>String</i>,
        "<a href="#containerwrite" title="ContainerWrite">ContainerWrite</a>" : <i>[ String, ... ]</i>,
        "<a href="#historylocation" title="HistoryLocation">HistoryLocation</a>" : <i>String</i>,
        "<a href="#metadata" title="Metadata">Metadata</a>" : <i>[ <a href="metadata.md">Metadata</a>, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#versionslocation" title="VersionsLocation">VersionsLocation</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Brightbox::OrbitContainer
Properties:
    <a href="#containerread" title="ContainerRead">ContainerRead</a>: <i>
      - String</i>
    <a href="#containersynckey" title="ContainerSyncKey">ContainerSyncKey</a>: <i>String</i>
    <a href="#containersyncto" title="ContainerSyncTo">ContainerSyncTo</a>: <i>String</i>
    <a href="#containerwrite" title="ContainerWrite">ContainerWrite</a>: <i>
      - String</i>
    <a href="#historylocation" title="HistoryLocation">HistoryLocation</a>: <i>String</i>
    <a href="#metadata" title="Metadata">Metadata</a>: <i>
      - <a href="metadata.md">Metadata</a></i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#versionslocation" title="VersionsLocation">VersionsLocation</a>: <i>String</i>
</pre>

## Properties

#### ContainerRead

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ContainerSyncKey

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ContainerSyncTo

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ContainerWrite

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HistoryLocation

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Metadata

_Required_: No

_Type_: List of <a href="metadata.md">Metadata</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VersionsLocation

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### BytesUsed

Returns the <code>BytesUsed</code> value.

#### CreatedAt

Returns the <code>CreatedAt</code> value.

#### ObjectCount

Returns the <code>ObjectCount</code> value.

#### StoragePolicy

Returns the <code>StoragePolicy</code> value.
