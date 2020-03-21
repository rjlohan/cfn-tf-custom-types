# Terraform::AzureRM::RedisCache

CloudFormation equivalent of azurerm_redis_cache

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AzureRM::RedisCache",
    "Properties" : {
        "<a href="#capacity" title="Capacity">Capacity</a>" : <i>Double</i>,
        "<a href="#enablenonsslport" title="EnableNonSslPort">EnableNonSslPort</a>" : <i>Boolean</i>,
        "<a href="#family" title="Family">Family</a>" : <i>String</i>,
        "<a href="#location" title="Location">Location</a>" : <i>String</i>,
        "<a href="#minimumtlsversion" title="MinimumTlsVersion">MinimumTlsVersion</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#privatestaticipaddress" title="PrivateStaticIpAddress">PrivateStaticIpAddress</a>" : <i>String</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
        "<a href="#shardcount" title="ShardCount">ShardCount</a>" : <i>Double</i>,
        "<a href="#skuname" title="SkuName">SkuName</a>" : <i>String</i>,
        "<a href="#subnetid" title="SubnetId">SubnetId</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
        "<a href="#zones" title="Zones">Zones</a>" : <i>[ String, ... ]</i>,
        "<a href="#patchschedule" title="PatchSchedule">PatchSchedule</a>" : <i>[ <a href="patchschedule.md">PatchSchedule</a>, ... ]</i>,
        "<a href="#redisconfiguration" title="RedisConfiguration">RedisConfiguration</a>" : <i>[ <a href="redisconfiguration.md">RedisConfiguration</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AzureRM::RedisCache
Properties:
    <a href="#capacity" title="Capacity">Capacity</a>: <i>Double</i>
    <a href="#enablenonsslport" title="EnableNonSslPort">EnableNonSslPort</a>: <i>Boolean</i>
    <a href="#family" title="Family">Family</a>: <i>String</i>
    <a href="#location" title="Location">Location</a>: <i>String</i>
    <a href="#minimumtlsversion" title="MinimumTlsVersion">MinimumTlsVersion</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#privatestaticipaddress" title="PrivateStaticIpAddress">PrivateStaticIpAddress</a>: <i>String</i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
    <a href="#shardcount" title="ShardCount">ShardCount</a>: <i>Double</i>
    <a href="#skuname" title="SkuName">SkuName</a>: <i>String</i>
    <a href="#subnetid" title="SubnetId">SubnetId</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
    <a href="#zones" title="Zones">Zones</a>: <i>
      - String</i>
    <a href="#patchschedule" title="PatchSchedule">PatchSchedule</a>: <i>
      - <a href="patchschedule.md">PatchSchedule</a></i>
    <a href="#redisconfiguration" title="RedisConfiguration">RedisConfiguration</a>: <i>
      - <a href="redisconfiguration.md">RedisConfiguration</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### Capacity

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableNonSslPort

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Family

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Location

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinimumTlsVersion

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivateStaticIpAddress

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ShardCount

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SkuName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubnetId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Zones

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PatchSchedule

_Required_: No

_Type_: List of <a href="patchschedule.md">PatchSchedule</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RedisConfiguration

_Required_: No

_Type_: List of <a href="redisconfiguration.md">RedisConfiguration</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Hostname

Returns the <code>Hostname</code> value.

#### Port

Returns the <code>Port</code> value.

#### PrimaryAccessKey

Returns the <code>PrimaryAccessKey</code> value.

#### PrimaryConnectionString

Returns the <code>PrimaryConnectionString</code> value.

#### SecondaryAccessKey

Returns the <code>SecondaryAccessKey</code> value.

#### SecondaryConnectionString

Returns the <code>SecondaryConnectionString</code> value.

#### SslPort

Returns the <code>SslPort</code> value.
