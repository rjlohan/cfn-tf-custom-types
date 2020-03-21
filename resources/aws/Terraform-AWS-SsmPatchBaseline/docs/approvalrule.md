# Terraform::AWS::SsmPatchBaseline ApprovalRule

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#approveafterdays" title="ApproveAfterDays">ApproveAfterDays</a>" : <i>Double</i>,
    "<a href="#compliancelevel" title="ComplianceLevel">ComplianceLevel</a>" : <i>String</i>,
    "<a href="#enablenonsecurity" title="EnableNonSecurity">EnableNonSecurity</a>" : <i>Boolean</i>,
    "<a href="#patchfilter" title="PatchFilter">PatchFilter</a>" : <i>[ &lt;a href=&#34;approvalrule-patchfilter.md&#34;&gt;PatchFilter&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#approveafterdays" title="ApproveAfterDays">ApproveAfterDays</a>: <i>Double</i>
<a href="#compliancelevel" title="ComplianceLevel">ComplianceLevel</a>: <i>String</i>
<a href="#enablenonsecurity" title="EnableNonSecurity">EnableNonSecurity</a>: <i>Boolean</i>
<a href="#patchfilter" title="PatchFilter">PatchFilter</a>: <i>
      - &lt;a href=&#34;approvalrule-patchfilter.md&#34;&gt;PatchFilter&lt;/a&gt;</i>
</pre>

## Properties

#### ApproveAfterDays

_Required_: Yes
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ComplianceLevel

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableNonSecurity

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PatchFilter

_Required_: No
_Type_: List of &lt;a href=&#34;approvalrule-patchfilter.md&#34;&gt;PatchFilter&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
