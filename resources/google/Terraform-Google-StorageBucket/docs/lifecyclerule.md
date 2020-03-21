# Terraform::Google::StorageBucket LifecycleRule

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#action" title="Action">Action</a>" : <i>[ &lt;a href=&#34;lifecyclerule-action.md&#34;&gt;Action&lt;/a&gt;, ... ]</i>,
    "<a href="#condition" title="Condition">Condition</a>" : <i>[ &lt;a href=&#34;lifecyclerule-condition.md&#34;&gt;Condition&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#action" title="Action">Action</a>: <i>
      - &lt;a href=&#34;lifecyclerule-action.md&#34;&gt;Action&lt;/a&gt;</i>
<a href="#condition" title="Condition">Condition</a>: <i>
      - &lt;a href=&#34;lifecyclerule-condition.md&#34;&gt;Condition&lt;/a&gt;</i>
</pre>

## Properties

#### Action

_Required_: No
_Type_: List of &lt;a href=&#34;lifecyclerule-action.md&#34;&gt;Action&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Condition

_Required_: No
_Type_: List of &lt;a href=&#34;lifecyclerule-condition.md&#34;&gt;Condition&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
