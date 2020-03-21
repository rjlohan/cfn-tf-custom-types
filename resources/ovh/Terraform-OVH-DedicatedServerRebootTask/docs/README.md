# Terraform::OVH::DedicatedServerRebootTask

CloudFormation equivalent of ovh_dedicated_server_reboot_task

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OVH::DedicatedServerRebootTask",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#comment" title="Comment">Comment</a>" : <i>String</i>,
        "<a href="#donedate" title="DoneDate">DoneDate</a>" : <i>String</i>,
        "<a href="#function" title="Function">Function</a>" : <i>String</i>,
        "<a href="#keepers" title="Keepers">Keepers</a>" : <i>[ String, ... ]</i>,
        "<a href="#lastupdate" title="LastUpdate">LastUpdate</a>" : <i>String</i>,
        "<a href="#servicename" title="ServiceName">ServiceName</a>" : <i>String</i>,
        "<a href="#startdate" title="StartDate">StartDate</a>" : <i>String</i>,
        "<a href="#status" title="Status">Status</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OVH::DedicatedServerRebootTask
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#comment" title="Comment">Comment</a>: <i>String</i>
    <a href="#donedate" title="DoneDate">DoneDate</a>: <i>String</i>
    <a href="#function" title="Function">Function</a>: <i>String</i>
    <a href="#keepers" title="Keepers">Keepers</a>: <i>
      - String</i>
    <a href="#lastupdate" title="LastUpdate">LastUpdate</a>: <i>String</i>
    <a href="#servicename" title="ServiceName">ServiceName</a>: <i>String</i>
    <a href="#startdate" title="StartDate">StartDate</a>: <i>String</i>
    <a href="#status" title="Status">Status</a>: <i>String</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Comment

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DoneDate

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Function

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Keepers

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LastUpdate

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StartDate

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Comment

Returns the &lt;code&gt;Comment&lt;/code&gt; value.

#### DoneDate

Returns the &lt;code&gt;DoneDate&lt;/code&gt; value.

#### Function

Returns the &lt;code&gt;Function&lt;/code&gt; value.

#### LastUpdate

Returns the &lt;code&gt;LastUpdate&lt;/code&gt; value.

#### StartDate

Returns the &lt;code&gt;StartDate&lt;/code&gt; value.

#### Status

Returns the &lt;code&gt;Status&lt;/code&gt; value.
