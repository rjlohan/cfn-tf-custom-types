# Terraform::Spotinst::OceanAws Autoscaler

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#autoscalecooldown" title="AutoscaleCooldown">AutoscaleCooldown</a>" : <i>Double</i>,
    "<a href="#autoscaleisautoconfig" title="AutoscaleIsAutoConfig">AutoscaleIsAutoConfig</a>" : <i>Boolean</i>,
    "<a href="#autoscaleisenabled" title="AutoscaleIsEnabled">AutoscaleIsEnabled</a>" : <i>Boolean</i>,
    "<a href="#autoscaledown" title="AutoscaleDown">AutoscaleDown</a>" : <i>[ &lt;a href=&#34;autoscaler-autoscaledown.md&#34;&gt;AutoscaleDown&lt;/a&gt;, ... ]</i>,
    "<a href="#autoscaleheadroom" title="AutoscaleHeadroom">AutoscaleHeadroom</a>" : <i>[ &lt;a href=&#34;autoscaler-autoscaleheadroom.md&#34;&gt;AutoscaleHeadroom&lt;/a&gt;, ... ]</i>,
    "<a href="#resourcelimits" title="ResourceLimits">ResourceLimits</a>" : <i>[ &lt;a href=&#34;autoscaler-resourcelimits.md&#34;&gt;ResourceLimits&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#autoscalecooldown" title="AutoscaleCooldown">AutoscaleCooldown</a>: <i>Double</i>
<a href="#autoscaleisautoconfig" title="AutoscaleIsAutoConfig">AutoscaleIsAutoConfig</a>: <i>Boolean</i>
<a href="#autoscaleisenabled" title="AutoscaleIsEnabled">AutoscaleIsEnabled</a>: <i>Boolean</i>
<a href="#autoscaledown" title="AutoscaleDown">AutoscaleDown</a>: <i>
      - &lt;a href=&#34;autoscaler-autoscaledown.md&#34;&gt;AutoscaleDown&lt;/a&gt;</i>
<a href="#autoscaleheadroom" title="AutoscaleHeadroom">AutoscaleHeadroom</a>: <i>
      - &lt;a href=&#34;autoscaler-autoscaleheadroom.md&#34;&gt;AutoscaleHeadroom&lt;/a&gt;</i>
<a href="#resourcelimits" title="ResourceLimits">ResourceLimits</a>: <i>
      - &lt;a href=&#34;autoscaler-resourcelimits.md&#34;&gt;ResourceLimits&lt;/a&gt;</i>
</pre>

## Properties

#### AutoscaleCooldown

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoscaleIsAutoConfig

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoscaleIsEnabled

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoscaleDown

_Required_: No
_Type_: List of &lt;a href=&#34;autoscaler-autoscaledown.md&#34;&gt;AutoscaleDown&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoscaleHeadroom

_Required_: No
_Type_: List of &lt;a href=&#34;autoscaler-autoscaleheadroom.md&#34;&gt;AutoscaleHeadroom&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceLimits

_Required_: No
_Type_: List of &lt;a href=&#34;autoscaler-resourcelimits.md&#34;&gt;ResourceLimits&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
