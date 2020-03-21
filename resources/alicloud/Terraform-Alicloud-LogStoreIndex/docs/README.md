# Terraform::Alicloud::LogStoreIndex

CloudFormation equivalent of alicloud_log_store_index

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Alicloud::LogStoreIndex",
    "Properties" : {
        "<a href="#logstore" title="Logstore">Logstore</a>" : <i>String</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#fieldsearch" title="FieldSearch">FieldSearch</a>" : <i>[ <a href="fieldsearch.md">FieldSearch</a>, ... ]</i>,
        "<a href="#fulltext" title="FullText">FullText</a>" : <i>[ <a href="fulltext.md">FullText</a>, ... ]</i>,
        "<a href="#jsonkeys" title="JsonKeys">JsonKeys</a>" : <i>[ <a href="jsonkeys.md">JsonKeys</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Alicloud::LogStoreIndex
Properties:
    <a href="#logstore" title="Logstore">Logstore</a>: <i>String</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#fieldsearch" title="FieldSearch">FieldSearch</a>: <i>
      - <a href="fieldsearch.md">FieldSearch</a></i>
    <a href="#fulltext" title="FullText">FullText</a>: <i>
      - <a href="fulltext.md">FullText</a></i>
    <a href="#jsonkeys" title="JsonKeys">JsonKeys</a>: <i>
      - <a href="jsonkeys.md">JsonKeys</a></i>
</pre>

## Properties

#### Logstore

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FieldSearch

_Required_: No

_Type_: List of <a href="fieldsearch.md">FieldSearch</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FullText

_Required_: No

_Type_: List of <a href="fulltext.md">FullText</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### JsonKeys

_Required_: No

_Type_: List of <a href="jsonkeys.md">JsonKeys</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.
