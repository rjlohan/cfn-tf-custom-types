# Terraform::AWS::LambdaFunctionEventInvokeConfig DestinationConfig

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#onfailure" title="OnFailure">OnFailure</a>" : <i>[ &lt;a href=&#34;destinationconfig-onfailure.md&#34;&gt;OnFailure&lt;/a&gt;, ... ]</i>,
    "<a href="#onsuccess" title="OnSuccess">OnSuccess</a>" : <i>[ &lt;a href=&#34;destinationconfig-onsuccess.md&#34;&gt;OnSuccess&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#onfailure" title="OnFailure">OnFailure</a>: <i>
      - &lt;a href=&#34;destinationconfig-onfailure.md&#34;&gt;OnFailure&lt;/a&gt;</i>
<a href="#onsuccess" title="OnSuccess">OnSuccess</a>: <i>
      - &lt;a href=&#34;destinationconfig-onsuccess.md&#34;&gt;OnSuccess&lt;/a&gt;</i>
</pre>

## Properties

#### OnFailure

_Required_: No
_Type_: List of &lt;a href=&#34;destinationconfig-onfailure.md&#34;&gt;OnFailure&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OnSuccess

_Required_: No
_Type_: List of &lt;a href=&#34;destinationconfig-onsuccess.md&#34;&gt;OnSuccess&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
