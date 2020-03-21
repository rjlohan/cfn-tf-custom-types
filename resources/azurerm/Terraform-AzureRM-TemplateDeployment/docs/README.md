# Terraform::AzureRM::TemplateDeployment

CloudFormation equivalent of azurerm_template_deployment

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AzureRM::TemplateDeployment",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#deploymentmode" title="DeploymentMode">DeploymentMode</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#outputs" title="Outputs">Outputs</a>" : <i>[ &lt;a href=&#34;outputs.md&#34;&gt;Outputs&lt;/a&gt;, ... ]</i>,
        "<a href="#parameters" title="Parameters">Parameters</a>" : <i>[ &lt;a href=&#34;parameters.md&#34;&gt;Parameters&lt;/a&gt;, ... ]</i>,
        "<a href="#parametersbody" title="ParametersBody">ParametersBody</a>" : <i>String</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
        "<a href="#templatebody" title="TemplateBody">TemplateBody</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AzureRM::TemplateDeployment
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#deploymentmode" title="DeploymentMode">DeploymentMode</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#outputs" title="Outputs">Outputs</a>: <i>
      - &lt;a href=&#34;outputs.md&#34;&gt;Outputs&lt;/a&gt;</i>
    <a href="#parameters" title="Parameters">Parameters</a>: <i>
      - &lt;a href=&#34;parameters.md&#34;&gt;Parameters&lt;/a&gt;</i>
    <a href="#parametersbody" title="ParametersBody">ParametersBody</a>: <i>String</i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
    <a href="#templatebody" title="TemplateBody">TemplateBody</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeploymentMode

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Outputs

_Required_: No

_Type_: List of &lt;a href=&#34;outputs.md&#34;&gt;Outputs&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Parameters

_Required_: No

_Type_: List of &lt;a href=&#34;parameters.md&#34;&gt;Parameters&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ParametersBody

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateBody

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: &lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Outputs

Returns the &lt;code&gt;Outputs&lt;/code&gt; value.
