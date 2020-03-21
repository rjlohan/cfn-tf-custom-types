# Terraform::Heroku::Config

CloudFormation equivalent of heroku_config

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Heroku::Config",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#sensitivevars" title="SensitiveVars">SensitiveVars</a>" : <i>[ &lt;a href=&#34;sensitivevars.md&#34;&gt;SensitiveVars&lt;/a&gt;, ... ]</i>,
        "<a href="#vars" title="Vars">Vars</a>" : <i>[ &lt;a href=&#34;vars.md&#34;&gt;Vars&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Heroku::Config
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#sensitivevars" title="SensitiveVars">SensitiveVars</a>: <i>
      - &lt;a href=&#34;sensitivevars.md&#34;&gt;SensitiveVars&lt;/a&gt;</i>
    <a href="#vars" title="Vars">Vars</a>: <i>
      - &lt;a href=&#34;vars.md&#34;&gt;Vars&lt;/a&gt;</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SensitiveVars

_Required_: No

_Type_: List of &lt;a href=&#34;sensitivevars.md&#34;&gt;SensitiveVars&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vars

_Required_: No

_Type_: List of &lt;a href=&#34;vars.md&#34;&gt;Vars&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.
