# Terraform::AzureAD::Application RequiredResourceAccess

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#resourceappid" title="ResourceAppId">ResourceAppId</a>" : <i>String</i>,
    "<a href="#resourceaccess" title="ResourceAccess">ResourceAccess</a>" : <i>[ &lt;a href=&#34;requiredresourceaccess-resourceaccess.md&#34;&gt;ResourceAccess&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#resourceappid" title="ResourceAppId">ResourceAppId</a>: <i>String</i>
<a href="#resourceaccess" title="ResourceAccess">ResourceAccess</a>: <i>
      - &lt;a href=&#34;requiredresourceaccess-resourceaccess.md&#34;&gt;ResourceAccess&lt;/a&gt;</i>
</pre>

## Properties

#### ResourceAppId

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceAccess

_Required_: No
_Type_: List of &lt;a href=&#34;requiredresourceaccess-resourceaccess.md&#34;&gt;ResourceAccess&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
