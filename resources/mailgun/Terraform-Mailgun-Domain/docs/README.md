# Terraform::Mailgun::Domain

CloudFormation equivalent of mailgun_domain

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Mailgun::Domain",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#receivingrecords" title="ReceivingRecords">ReceivingRecords</a>" : <i>[ &lt;a href=&#34;receivingrecords.md&#34;&gt;ReceivingRecords&lt;/a&gt;, ... ]</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#sendingrecords" title="SendingRecords">SendingRecords</a>" : <i>[ &lt;a href=&#34;sendingrecords.md&#34;&gt;SendingRecords&lt;/a&gt;, ... ]</i>,
        "<a href="#smtplogin" title="SmtpLogin">SmtpLogin</a>" : <i>String</i>,
        "<a href="#smtppassword" title="SmtpPassword">SmtpPassword</a>" : <i>String</i>,
        "<a href="#spamaction" title="SpamAction">SpamAction</a>" : <i>String</i>,
        "<a href="#wildcard" title="Wildcard">Wildcard</a>" : <i>Boolean</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Mailgun::Domain
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#receivingrecords" title="ReceivingRecords">ReceivingRecords</a>: <i>
      - &lt;a href=&#34;receivingrecords.md&#34;&gt;ReceivingRecords&lt;/a&gt;</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#sendingrecords" title="SendingRecords">SendingRecords</a>: <i>
      - &lt;a href=&#34;sendingrecords.md&#34;&gt;SendingRecords&lt;/a&gt;</i>
    <a href="#smtplogin" title="SmtpLogin">SmtpLogin</a>: <i>String</i>
    <a href="#smtppassword" title="SmtpPassword">SmtpPassword</a>: <i>String</i>
    <a href="#spamaction" title="SpamAction">SpamAction</a>: <i>String</i>
    <a href="#wildcard" title="Wildcard">Wildcard</a>: <i>Boolean</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReceivingRecords

_Required_: No

_Type_: List of &lt;a href=&#34;receivingrecords.md&#34;&gt;ReceivingRecords&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SendingRecords

_Required_: No

_Type_: List of &lt;a href=&#34;sendingrecords.md&#34;&gt;SendingRecords&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SmtpLogin

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SmtpPassword

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SpamAction

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Wildcard

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

#### ReceivingRecords

Returns the &lt;code&gt;ReceivingRecords&lt;/code&gt; value.

#### SendingRecords

Returns the &lt;code&gt;SendingRecords&lt;/code&gt; value.

#### SmtpLogin

Returns the &lt;code&gt;SmtpLogin&lt;/code&gt; value.

#### SmtpPassword

Returns the &lt;code&gt;SmtpPassword&lt;/code&gt; value.
