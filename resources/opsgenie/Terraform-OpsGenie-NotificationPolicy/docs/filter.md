# Terraform::OpsGenie::NotificationPolicy Filter

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#type" title="Type">Type</a>" : <i>String</i>,
    "<a href="#conditions" title="Conditions">Conditions</a>" : <i>[ &lt;a href=&#34;filter-conditions.md&#34;&gt;Conditions&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#type" title="Type">Type</a>: <i>String</i>
<a href="#conditions" title="Conditions">Conditions</a>: <i>
      - &lt;a href=&#34;filter-conditions.md&#34;&gt;Conditions&lt;/a&gt;</i>
</pre>

## Properties

#### Type

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Conditions

_Required_: No
_Type_: List of &lt;a href=&#34;filter-conditions.md&#34;&gt;Conditions&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
