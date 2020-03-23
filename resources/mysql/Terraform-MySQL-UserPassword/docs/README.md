# Terraform::MySQL::UserPassword

The `mysql_user_password` resource sets and manages a password for a given 
user on a MySQL server.

~> **NOTE on MySQL Passwords:** This resource conflicts with the `password` 
   argument for `mysql_user`. This resource uses PGP encryption to avoid 
   storing unencrypted passwords in Terraform state.
   
~> **NOTE on How Passwords are Created:** This resource **automatically**
   generates a **random** password. The password will be a random UUID.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::MySQL::UserPassword",
    "Properties" : {
        "<a href="#host" title="Host">Host</a>" : <i>String</i>,
        "<a href="#pgpkey" title="PgpKey">PgpKey</a>" : <i>String</i>,
        "<a href="#user" title="User">User</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::MySQL::UserPassword
Properties:
    <a href="#host" title="Host">Host</a>: <i>String</i>
    <a href="#pgpkey" title="PgpKey">PgpKey</a>: <i>String</i>
    <a href="#user" title="User">User</a>: <i>String</i>
</pre>

## Properties

#### Host

The source host of the user. Defaults to `localhost`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PgpKey

Either a base-64 encoded PGP public key, or a keybase username in the form `keybase:some_person_that_exists`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### User

The IAM user to associate with this access key.

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

#### EncryptedPassword

Returns the <code>EncryptedPassword</code> value.

#### Id

Returns the <code>Id</code> value.

#### KeyFingerprint

Returns the <code>KeyFingerprint</code> value.
