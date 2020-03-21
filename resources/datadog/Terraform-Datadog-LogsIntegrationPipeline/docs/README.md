# Terraform::Datadog::LogsIntegrationPipeline

CloudFormation equivalent of datadog_logs_integration_pipeline

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Datadog::LogsIntegrationPipeline",
    "Properties" : {
        "<a href="#isenabled" title="IsEnabled">IsEnabled</a>" : <i>Boolean</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Datadog::LogsIntegrationPipeline
Properties:
    <a href="#isenabled" title="IsEnabled">IsEnabled</a>: <i>Boolean</i>
</pre>

## Properties

#### IsEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.
