# Terraform::Spotinst::ElastigroupAwsBeanstalk

CloudFormation equivalent of spotinst_elastigroup_aws_beanstalk

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Spotinst::ElastigroupAwsBeanstalk",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#beanstalkenvironmentid" title="BeanstalkEnvironmentId">BeanstalkEnvironmentId</a>" : <i>String</i>,
        "<a href="#beanstalkenvironmentname" title="BeanstalkEnvironmentName">BeanstalkEnvironmentName</a>" : <i>String</i>,
        "<a href="#desiredcapacity" title="DesiredCapacity">DesiredCapacity</a>" : <i>Double</i>,
        "<a href="#instancetypesspot" title="InstanceTypesSpot">InstanceTypesSpot</a>" : <i>[ String, ... ]</i>,
        "<a href="#maintenance" title="Maintenance">Maintenance</a>" : <i>String</i>,
        "<a href="#maxsize" title="MaxSize">MaxSize</a>" : <i>Double</i>,
        "<a href="#minsize" title="MinSize">MinSize</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#product" title="Product">Product</a>" : <i>String</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#deploymentpreferences" title="DeploymentPreferences">DeploymentPreferences</a>" : <i>[ &lt;a href=&#34;deploymentpreferences.md&#34;&gt;DeploymentPreferences&lt;/a&gt;, ... ]</i>,
        "<a href="#managedactions" title="ManagedActions">ManagedActions</a>" : <i>[ &lt;a href=&#34;managedactions.md&#34;&gt;ManagedActions&lt;/a&gt;, ... ]</i>,
        "<a href="#scheduledtask" title="ScheduledTask">ScheduledTask</a>" : <i>[ &lt;a href=&#34;scheduledtask.md&#34;&gt;ScheduledTask&lt;/a&gt;, ... ]</i>,
        "<a href="#strategy" title="Strategy">Strategy</a>" : <i>[ &lt;a href=&#34;strategy.md&#34;&gt;Strategy&lt;/a&gt;, ... ]</i>,
        "<a href="#platformupdate" title="PlatformUpdate">PlatformUpdate</a>" : <i>[ &lt;a href=&#34;platformupdate.md&#34;&gt;PlatformUpdate&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Spotinst::ElastigroupAwsBeanstalk
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#beanstalkenvironmentid" title="BeanstalkEnvironmentId">BeanstalkEnvironmentId</a>: <i>String</i>
    <a href="#beanstalkenvironmentname" title="BeanstalkEnvironmentName">BeanstalkEnvironmentName</a>: <i>String</i>
    <a href="#desiredcapacity" title="DesiredCapacity">DesiredCapacity</a>: <i>Double</i>
    <a href="#instancetypesspot" title="InstanceTypesSpot">InstanceTypesSpot</a>: <i>
      - String</i>
    <a href="#maintenance" title="Maintenance">Maintenance</a>: <i>String</i>
    <a href="#maxsize" title="MaxSize">MaxSize</a>: <i>Double</i>
    <a href="#minsize" title="MinSize">MinSize</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#product" title="Product">Product</a>: <i>String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#deploymentpreferences" title="DeploymentPreferences">DeploymentPreferences</a>: <i>
      - &lt;a href=&#34;deploymentpreferences.md&#34;&gt;DeploymentPreferences&lt;/a&gt;</i>
    <a href="#managedactions" title="ManagedActions">ManagedActions</a>: <i>
      - &lt;a href=&#34;managedactions.md&#34;&gt;ManagedActions&lt;/a&gt;</i>
    <a href="#scheduledtask" title="ScheduledTask">ScheduledTask</a>: <i>
      - &lt;a href=&#34;scheduledtask.md&#34;&gt;ScheduledTask&lt;/a&gt;</i>
    <a href="#strategy" title="Strategy">Strategy</a>: <i>
      - &lt;a href=&#34;strategy.md&#34;&gt;Strategy&lt;/a&gt;</i>
    <a href="#platformupdate" title="PlatformUpdate">PlatformUpdate</a>: <i>
      - &lt;a href=&#34;platformupdate.md&#34;&gt;PlatformUpdate&lt;/a&gt;</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BeanstalkEnvironmentId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BeanstalkEnvironmentName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DesiredCapacity

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceTypesSpot

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Maintenance

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxSize

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinSize

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Product

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeploymentPreferences

_Required_: No

_Type_: List of &lt;a href=&#34;deploymentpreferences.md&#34;&gt;DeploymentPreferences&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ManagedActions

_Required_: No

_Type_: List of &lt;a href=&#34;managedactions.md&#34;&gt;ManagedActions&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScheduledTask

_Required_: No

_Type_: List of &lt;a href=&#34;scheduledtask.md&#34;&gt;ScheduledTask&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Strategy

_Required_: No

_Type_: List of &lt;a href=&#34;strategy.md&#34;&gt;Strategy&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PlatformUpdate

_Required_: No

_Type_: List of &lt;a href=&#34;platformupdate.md&#34;&gt;PlatformUpdate&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.
