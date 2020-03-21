# Terraform::AzureRM::FrontdoorFirewallPolicy Override

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#rulegroupname" title="RuleGroupName">RuleGroupName</a>" : <i>String</i>,
    "<a href="#exclusion" title="Exclusion">Exclusion</a>" : <i>[ &lt;a href=&#34;override-exclusion.md&#34;&gt;Exclusion&lt;/a&gt;, ... ]</i>,
    "<a href="#rule" title="Rule">Rule</a>" : <i>[ &lt;a href=&#34;override-rule.md&#34;&gt;Rule&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#rulegroupname" title="RuleGroupName">RuleGroupName</a>: <i>String</i>
<a href="#exclusion" title="Exclusion">Exclusion</a>: <i>
      - &lt;a href=&#34;override-exclusion.md&#34;&gt;Exclusion&lt;/a&gt;</i>
<a href="#rule" title="Rule">Rule</a>: <i>
      - &lt;a href=&#34;override-rule.md&#34;&gt;Rule&lt;/a&gt;</i>
</pre>

## Properties

#### RuleGroupName

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Exclusion

_Required_: No
_Type_: List of &lt;a href=&#34;override-exclusion.md&#34;&gt;Exclusion&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Rule

_Required_: No
_Type_: List of &lt;a href=&#34;override-rule.md&#34;&gt;Rule&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
