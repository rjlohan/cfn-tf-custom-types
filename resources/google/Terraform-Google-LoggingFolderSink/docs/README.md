# Terraform::Google::LoggingFolderSink

CloudFormation equivalent of google_logging_folder_sink

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Google::LoggingFolderSink",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#destination" title="Destination">Destination</a>" : <i>String</i>,
        "<a href="#filter" title="Filter">Filter</a>" : <i>String</i>,
        "<a href="#folder" title="Folder">Folder</a>" : <i>String</i>,
        "<a href="#includechildren" title="IncludeChildren">IncludeChildren</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#writeridentity" title="WriterIdentity">WriterIdentity</a>" : <i>String</i>,
        "<a href="#bigqueryoptions" title="BigqueryOptions">BigqueryOptions</a>" : <i>[ &lt;a href=&#34;bigqueryoptions.md&#34;&gt;BigqueryOptions&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Google::LoggingFolderSink
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#destination" title="Destination">Destination</a>: <i>String</i>
    <a href="#filter" title="Filter">Filter</a>: <i>String</i>
    <a href="#folder" title="Folder">Folder</a>: <i>String</i>
    <a href="#includechildren" title="IncludeChildren">IncludeChildren</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#writeridentity" title="WriterIdentity">WriterIdentity</a>: <i>String</i>
    <a href="#bigqueryoptions" title="BigqueryOptions">BigqueryOptions</a>: <i>
      - &lt;a href=&#34;bigqueryoptions.md&#34;&gt;BigqueryOptions&lt;/a&gt;</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Destination

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Filter

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Folder

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IncludeChildren

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WriterIdentity

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BigqueryOptions

_Required_: No

_Type_: List of &lt;a href=&#34;bigqueryoptions.md&#34;&gt;BigqueryOptions&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### WriterIdentity

Returns the &lt;code&gt;WriterIdentity&lt;/code&gt; value.
