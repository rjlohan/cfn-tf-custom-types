# Terraform::AWS::WafregionalRegexMatchSet

CloudFormation equivalent of aws_wafregional_regex_match_set

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::WafregionalRegexMatchSet",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#regexmatchtuple" title="RegexMatchTuple">RegexMatchTuple</a>" : <i>[ &lt;a href=&#34;regexmatchtuple.md&#34;&gt;RegexMatchTuple&lt;/a&gt;, ... ]</i>,
        "<a href="#fieldtomatch" title="FieldToMatch">FieldToMatch</a>" : <i>[ &lt;a href=&#34;fieldtomatch.md&#34;&gt;FieldToMatch&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::WafregionalRegexMatchSet
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#regexmatchtuple" title="RegexMatchTuple">RegexMatchTuple</a>: <i>
      - &lt;a href=&#34;regexmatchtuple.md&#34;&gt;RegexMatchTuple&lt;/a&gt;</i>
    <a href="#fieldtomatch" title="FieldToMatch">FieldToMatch</a>: <i>
      - &lt;a href=&#34;fieldtomatch.md&#34;&gt;FieldToMatch&lt;/a&gt;</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RegexMatchTuple

_Required_: No

_Type_: List of &lt;a href=&#34;regexmatchtuple.md&#34;&gt;RegexMatchTuple&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FieldToMatch

_Required_: No

_Type_: List of &lt;a href=&#34;fieldtomatch.md&#34;&gt;FieldToMatch&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.
