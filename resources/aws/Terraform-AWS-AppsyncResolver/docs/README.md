# Terraform::AWS::AppsyncResolver

CloudFormation equivalent of aws_appsync_resolver

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::AppsyncResolver",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#apiid" title="ApiId">ApiId</a>" : <i>String</i>,
        "<a href="#arn" title="Arn">Arn</a>" : <i>String</i>,
        "<a href="#datasource" title="DataSource">DataSource</a>" : <i>String</i>,
        "<a href="#field" title="Field">Field</a>" : <i>String</i>,
        "<a href="#kind" title="Kind">Kind</a>" : <i>String</i>,
        "<a href="#requesttemplate" title="RequestTemplate">RequestTemplate</a>" : <i>String</i>,
        "<a href="#responsetemplate" title="ResponseTemplate">ResponseTemplate</a>" : <i>String</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#pipelineconfig" title="PipelineConfig">PipelineConfig</a>" : <i>[ &lt;a href=&#34;pipelineconfig.md&#34;&gt;PipelineConfig&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::AppsyncResolver
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#apiid" title="ApiId">ApiId</a>: <i>String</i>
    <a href="#arn" title="Arn">Arn</a>: <i>String</i>
    <a href="#datasource" title="DataSource">DataSource</a>: <i>String</i>
    <a href="#field" title="Field">Field</a>: <i>String</i>
    <a href="#kind" title="Kind">Kind</a>: <i>String</i>
    <a href="#requesttemplate" title="RequestTemplate">RequestTemplate</a>: <i>String</i>
    <a href="#responsetemplate" title="ResponseTemplate">ResponseTemplate</a>: <i>String</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#pipelineconfig" title="PipelineConfig">PipelineConfig</a>: <i>
      - &lt;a href=&#34;pipelineconfig.md&#34;&gt;PipelineConfig&lt;/a&gt;</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApiId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Arn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DataSource

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Field

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Kind

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestTemplate

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResponseTemplate

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PipelineConfig

_Required_: No

_Type_: List of &lt;a href=&#34;pipelineconfig.md&#34;&gt;PipelineConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Arn

Returns the &lt;code&gt;Arn&lt;/code&gt; value.
