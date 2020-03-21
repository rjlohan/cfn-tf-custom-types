# Terraform::Alicloud::KmsCiphertext

CloudFormation equivalent of alicloud_kms_ciphertext

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Alicloud::KmsCiphertext",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#ciphertextblob" title="CiphertextBlob">CiphertextBlob</a>" : <i>String</i>,
        "<a href="#encryptioncontext" title="EncryptionContext">EncryptionContext</a>" : <i>[ &lt;a href=&#34;encryptioncontext.md&#34;&gt;EncryptionContext&lt;/a&gt;, ... ]</i>,
        "<a href="#keyid" title="KeyId">KeyId</a>" : <i>String</i>,
        "<a href="#plaintext" title="Plaintext">Plaintext</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Alicloud::KmsCiphertext
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#ciphertextblob" title="CiphertextBlob">CiphertextBlob</a>: <i>String</i>
    <a href="#encryptioncontext" title="EncryptionContext">EncryptionContext</a>: <i>
      - &lt;a href=&#34;encryptioncontext.md&#34;&gt;EncryptionContext&lt;/a&gt;</i>
    <a href="#keyid" title="KeyId">KeyId</a>: <i>String</i>
    <a href="#plaintext" title="Plaintext">Plaintext</a>: <i>String</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CiphertextBlob

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EncryptionContext

_Required_: No

_Type_: List of &lt;a href=&#34;encryptioncontext.md&#34;&gt;EncryptionContext&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Plaintext

_Required_: Yes

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

#### CiphertextBlob

Returns the &lt;code&gt;CiphertextBlob&lt;/code&gt; value.
