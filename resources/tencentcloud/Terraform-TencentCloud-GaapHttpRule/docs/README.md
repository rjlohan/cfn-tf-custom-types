# Terraform::TencentCloud::GaapHttpRule

CloudFormation equivalent of tencentcloud_gaap_http_rule

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::TencentCloud::GaapHttpRule",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#connecttimeout" title="ConnectTimeout">ConnectTimeout</a>" : <i>Double</i>,
        "<a href="#domain" title="Domain">Domain</a>" : <i>String</i>,
        "<a href="#forwardhost" title="ForwardHost">ForwardHost</a>" : <i>String</i>,
        "<a href="#healthcheck" title="HealthCheck">HealthCheck</a>" : <i>Boolean</i>,
        "<a href="#healthcheckmethod" title="HealthCheckMethod">HealthCheckMethod</a>" : <i>String</i>,
        "<a href="#healthcheckpath" title="HealthCheckPath">HealthCheckPath</a>" : <i>String</i>,
        "<a href="#healthcheckstatuscodes" title="HealthCheckStatusCodes">HealthCheckStatusCodes</a>" : <i>[ Double, ... ]</i>,
        "<a href="#interval" title="Interval">Interval</a>" : <i>Double</i>,
        "<a href="#listenerid" title="ListenerId">ListenerId</a>" : <i>String</i>,
        "<a href="#path" title="Path">Path</a>" : <i>String</i>,
        "<a href="#realservertype" title="RealserverType">RealserverType</a>" : <i>String</i>,
        "<a href="#scheduler" title="Scheduler">Scheduler</a>" : <i>String</i>,
        "<a href="#realservers" title="Realservers">Realservers</a>" : <i>[ &lt;a href=&#34;realservers.md&#34;&gt;Realservers&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::TencentCloud::GaapHttpRule
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#connecttimeout" title="ConnectTimeout">ConnectTimeout</a>: <i>Double</i>
    <a href="#domain" title="Domain">Domain</a>: <i>String</i>
    <a href="#forwardhost" title="ForwardHost">ForwardHost</a>: <i>String</i>
    <a href="#healthcheck" title="HealthCheck">HealthCheck</a>: <i>Boolean</i>
    <a href="#healthcheckmethod" title="HealthCheckMethod">HealthCheckMethod</a>: <i>String</i>
    <a href="#healthcheckpath" title="HealthCheckPath">HealthCheckPath</a>: <i>String</i>
    <a href="#healthcheckstatuscodes" title="HealthCheckStatusCodes">HealthCheckStatusCodes</a>: <i>
      - Double</i>
    <a href="#interval" title="Interval">Interval</a>: <i>Double</i>
    <a href="#listenerid" title="ListenerId">ListenerId</a>: <i>String</i>
    <a href="#path" title="Path">Path</a>: <i>String</i>
    <a href="#realservertype" title="RealserverType">RealserverType</a>: <i>String</i>
    <a href="#scheduler" title="Scheduler">Scheduler</a>: <i>String</i>
    <a href="#realservers" title="Realservers">Realservers</a>: <i>
      - &lt;a href=&#34;realservers.md&#34;&gt;Realservers&lt;/a&gt;</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnectTimeout

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Domain

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForwardHost

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheck

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheckMethod

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheckPath

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheckStatusCodes

_Required_: No

_Type_: List of Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Interval

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ListenerId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Path

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RealserverType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Scheduler

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Realservers

_Required_: No

_Type_: List of &lt;a href=&#34;realservers.md&#34;&gt;Realservers&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.
