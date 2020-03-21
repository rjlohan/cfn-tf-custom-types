# Terraform::AWS::BackupPlan Rule

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#completionwindow" title="CompletionWindow">CompletionWindow</a>" : <i>Double</i>,
    "<a href="#recoverypointtags" title="RecoveryPointTags">RecoveryPointTags</a>" : <i>[ &lt;a href=&#34;rule-recoverypointtags.md&#34;&gt;RecoveryPointTags&lt;/a&gt;, ... ]</i>,
    "<a href="#rulename" title="RuleName">RuleName</a>" : <i>String</i>,
    "<a href="#schedule" title="Schedule">Schedule</a>" : <i>String</i>,
    "<a href="#startwindow" title="StartWindow">StartWindow</a>" : <i>Double</i>,
    "<a href="#targetvaultname" title="TargetVaultName">TargetVaultName</a>" : <i>String</i>,
    "<a href="#lifecycle" title="Lifecycle">Lifecycle</a>" : <i>[ &lt;a href=&#34;rule-lifecycle.md&#34;&gt;Lifecycle&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#completionwindow" title="CompletionWindow">CompletionWindow</a>: <i>Double</i>
<a href="#recoverypointtags" title="RecoveryPointTags">RecoveryPointTags</a>: <i>
      - &lt;a href=&#34;rule-recoverypointtags.md&#34;&gt;RecoveryPointTags&lt;/a&gt;</i>
<a href="#rulename" title="RuleName">RuleName</a>: <i>String</i>
<a href="#schedule" title="Schedule">Schedule</a>: <i>String</i>
<a href="#startwindow" title="StartWindow">StartWindow</a>: <i>Double</i>
<a href="#targetvaultname" title="TargetVaultName">TargetVaultName</a>: <i>String</i>
<a href="#lifecycle" title="Lifecycle">Lifecycle</a>: <i>
      - &lt;a href=&#34;rule-lifecycle.md&#34;&gt;Lifecycle&lt;/a&gt;</i>
</pre>

## Properties

#### CompletionWindow

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RecoveryPointTags

_Required_: No
_Type_: List of &lt;a href=&#34;rule-recoverypointtags.md&#34;&gt;RecoveryPointTags&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RuleName

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Schedule

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StartWindow

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetVaultName

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Lifecycle

_Required_: No
_Type_: List of &lt;a href=&#34;rule-lifecycle.md&#34;&gt;Lifecycle&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
