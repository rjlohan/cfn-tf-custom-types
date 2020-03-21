# Terraform::OpenTelekomCloud::AntiddosV1

CloudFormation equivalent of opentelekomcloud_antiddos_v1

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OpenTelekomCloud::AntiddosV1",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#apptypeid" title="AppTypeId">AppTypeId</a>" : <i>Double</i>,
        "<a href="#cleaningaccessposid" title="CleaningAccessPosId">CleaningAccessPosId</a>" : <i>Double</i>,
        "<a href="#enablel7" title="EnableL7">EnableL7</a>" : <i>Boolean</i>,
        "<a href="#floatingipid" title="FloatingIpId">FloatingIpId</a>" : <i>String</i>,
        "<a href="#httprequestposid" title="HttpRequestPosId">HttpRequestPosId</a>" : <i>Double</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#trafficposid" title="TrafficPosId">TrafficPosId</a>" : <i>Double</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OpenTelekomCloud::AntiddosV1
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#apptypeid" title="AppTypeId">AppTypeId</a>: <i>Double</i>
    <a href="#cleaningaccessposid" title="CleaningAccessPosId">CleaningAccessPosId</a>: <i>Double</i>
    <a href="#enablel7" title="EnableL7">EnableL7</a>: <i>Boolean</i>
    <a href="#floatingipid" title="FloatingIpId">FloatingIpId</a>: <i>String</i>
    <a href="#httprequestposid" title="HttpRequestPosId">HttpRequestPosId</a>: <i>Double</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#trafficposid" title="TrafficPosId">TrafficPosId</a>: <i>Double</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AppTypeId

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CleaningAccessPosId

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableL7

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FloatingIpId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpRequestPosId

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TrafficPosId

_Required_: Yes

_Type_: Double

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
