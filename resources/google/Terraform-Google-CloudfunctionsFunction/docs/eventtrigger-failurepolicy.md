# Terraform::Google::CloudfunctionsFunction EventTrigger FailurePolicy

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#retry" title="Retry">Retry</a>" : <i>Boolean</i>
}
</pre>

### YAML

<pre>
<a href="#retry" title="Retry">Retry</a>: <i>Boolean</i>
</pre>

## Properties

#### Retry

Whether the function should be retried on failure. Defaults to `false`.

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
