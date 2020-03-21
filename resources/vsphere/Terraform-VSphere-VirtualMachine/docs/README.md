# Terraform::VSphere::VirtualMachine

CloudFormation equivalent of vsphere_virtual_machine

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::VSphere::VirtualMachine",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#alternateguestname" title="AlternateGuestName">AlternateGuestName</a>" : <i>String</i>,
        "<a href="#annotation" title="Annotation">Annotation</a>" : <i>String</i>,
        "<a href="#bootdelay" title="BootDelay">BootDelay</a>" : <i>Double</i>,
        "<a href="#bootretrydelay" title="BootRetryDelay">BootRetryDelay</a>" : <i>Double</i>,
        "<a href="#bootretryenabled" title="BootRetryEnabled">BootRetryEnabled</a>" : <i>Boolean</i>,
        "<a href="#changeversion" title="ChangeVersion">ChangeVersion</a>" : <i>String</i>,
        "<a href="#cpuhotaddenabled" title="CpuHotAddEnabled">CpuHotAddEnabled</a>" : <i>Boolean</i>,
        "<a href="#cpuhotremoveenabled" title="CpuHotRemoveEnabled">CpuHotRemoveEnabled</a>" : <i>Boolean</i>,
        "<a href="#cpulimit" title="CpuLimit">CpuLimit</a>" : <i>Double</i>,
        "<a href="#cpuperformancecountersenabled" title="CpuPerformanceCountersEnabled">CpuPerformanceCountersEnabled</a>" : <i>Boolean</i>,
        "<a href="#cpureservation" title="CpuReservation">CpuReservation</a>" : <i>Double</i>,
        "<a href="#cpusharecount" title="CpuShareCount">CpuShareCount</a>" : <i>Double</i>,
        "<a href="#cpusharelevel" title="CpuShareLevel">CpuShareLevel</a>" : <i>String</i>,
        "<a href="#customattributes" title="CustomAttributes">CustomAttributes</a>" : <i>[ &lt;a href=&#34;customattributes.md&#34;&gt;CustomAttributes&lt;/a&gt;, ... ]</i>,
        "<a href="#datastoreclusterid" title="DatastoreClusterId">DatastoreClusterId</a>" : <i>String</i>,
        "<a href="#datastoreid" title="DatastoreId">DatastoreId</a>" : <i>String</i>,
        "<a href="#defaultipaddress" title="DefaultIpAddress">DefaultIpAddress</a>" : <i>String</i>,
        "<a href="#efisecurebootenabled" title="EfiSecureBootEnabled">EfiSecureBootEnabled</a>" : <i>Boolean</i>,
        "<a href="#enablediskuuid" title="EnableDiskUuid">EnableDiskUuid</a>" : <i>Boolean</i>,
        "<a href="#enablelogging" title="EnableLogging">EnableLogging</a>" : <i>Boolean</i>,
        "<a href="#eptrvimode" title="EptRviMode">EptRviMode</a>" : <i>String</i>,
        "<a href="#extraconfig" title="ExtraConfig">ExtraConfig</a>" : <i>[ &lt;a href=&#34;extraconfig.md&#34;&gt;ExtraConfig&lt;/a&gt;, ... ]</i>,
        "<a href="#firmware" title="Firmware">Firmware</a>" : <i>String</i>,
        "<a href="#folder" title="Folder">Folder</a>" : <i>String</i>,
        "<a href="#forcepoweroff" title="ForcePowerOff">ForcePowerOff</a>" : <i>Boolean</i>,
        "<a href="#guestid" title="GuestId">GuestId</a>" : <i>String</i>,
        "<a href="#guestipaddresses" title="GuestIpAddresses">GuestIpAddresses</a>" : <i>[ String, ... ]</i>,
        "<a href="#hostsystemid" title="HostSystemId">HostSystemId</a>" : <i>String</i>,
        "<a href="#hvmode" title="HvMode">HvMode</a>" : <i>String</i>,
        "<a href="#ignoredguestips" title="IgnoredGuestIps">IgnoredGuestIps</a>" : <i>[ String, ... ]</i>,
        "<a href="#imported" title="Imported">Imported</a>" : <i>Boolean</i>,
        "<a href="#latencysensitivity" title="LatencySensitivity">LatencySensitivity</a>" : <i>String</i>,
        "<a href="#memory" title="Memory">Memory</a>" : <i>Double</i>,
        "<a href="#memoryhotaddenabled" title="MemoryHotAddEnabled">MemoryHotAddEnabled</a>" : <i>Boolean</i>,
        "<a href="#memorylimit" title="MemoryLimit">MemoryLimit</a>" : <i>Double</i>,
        "<a href="#memoryreservation" title="MemoryReservation">MemoryReservation</a>" : <i>Double</i>,
        "<a href="#memorysharecount" title="MemoryShareCount">MemoryShareCount</a>" : <i>Double</i>,
        "<a href="#memorysharelevel" title="MemoryShareLevel">MemoryShareLevel</a>" : <i>String</i>,
        "<a href="#migratewaittimeout" title="MigrateWaitTimeout">MigrateWaitTimeout</a>" : <i>Double</i>,
        "<a href="#moid" title="Moid">Moid</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#nestedhvenabled" title="NestedHvEnabled">NestedHvEnabled</a>" : <i>Boolean</i>,
        "<a href="#numcorespersocket" title="NumCoresPerSocket">NumCoresPerSocket</a>" : <i>Double</i>,
        "<a href="#numcpus" title="NumCpus">NumCpus</a>" : <i>Double</i>,
        "<a href="#rebootrequired" title="RebootRequired">RebootRequired</a>" : <i>Boolean</i>,
        "<a href="#resourcepoolid" title="ResourcePoolId">ResourcePoolId</a>" : <i>String</i>,
        "<a href="#runtoolsscriptsafterpoweron" title="RunToolsScriptsAfterPowerOn">RunToolsScriptsAfterPowerOn</a>" : <i>Boolean</i>,
        "<a href="#runtoolsscriptsafterresume" title="RunToolsScriptsAfterResume">RunToolsScriptsAfterResume</a>" : <i>Boolean</i>,
        "<a href="#runtoolsscriptsbeforeguestreboot" title="RunToolsScriptsBeforeGuestReboot">RunToolsScriptsBeforeGuestReboot</a>" : <i>Boolean</i>,
        "<a href="#runtoolsscriptsbeforeguestshutdown" title="RunToolsScriptsBeforeGuestShutdown">RunToolsScriptsBeforeGuestShutdown</a>" : <i>Boolean</i>,
        "<a href="#runtoolsscriptsbeforegueststandby" title="RunToolsScriptsBeforeGuestStandby">RunToolsScriptsBeforeGuestStandby</a>" : <i>Boolean</i>,
        "<a href="#scsibussharing" title="ScsiBusSharing">ScsiBusSharing</a>" : <i>String</i>,
        "<a href="#scsicontrollercount" title="ScsiControllerCount">ScsiControllerCount</a>" : <i>Double</i>,
        "<a href="#scsitype" title="ScsiType">ScsiType</a>" : <i>String</i>,
        "<a href="#shutdownwaittimeout" title="ShutdownWaitTimeout">ShutdownWaitTimeout</a>" : <i>Double</i>,
        "<a href="#storagepolicyid" title="StoragePolicyId">StoragePolicyId</a>" : <i>String</i>,
        "<a href="#swapplacementpolicy" title="SwapPlacementPolicy">SwapPlacementPolicy</a>" : <i>String</i>,
        "<a href="#synctimewithhost" title="SyncTimeWithHost">SyncTimeWithHost</a>" : <i>Boolean</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ String, ... ]</i>,
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
        "<a href="#vapptransport" title="VappTransport">VappTransport</a>" : <i>[ String, ... ]</i>,
        "<a href="#vmwaretoolsstatus" title="VmwareToolsStatus">VmwareToolsStatus</a>" : <i>String</i>,
        "<a href="#vmxpath" title="VmxPath">VmxPath</a>" : <i>String</i>,
        "<a href="#waitforguestiptimeout" title="WaitForGuestIpTimeout">WaitForGuestIpTimeout</a>" : <i>Double</i>,
        "<a href="#waitforguestnetroutable" title="WaitForGuestNetRoutable">WaitForGuestNetRoutable</a>" : <i>Boolean</i>,
        "<a href="#waitforguestnettimeout" title="WaitForGuestNetTimeout">WaitForGuestNetTimeout</a>" : <i>Double</i>,
        "<a href="#cdrom" title="Cdrom">Cdrom</a>" : <i>[ &lt;a href=&#34;cdrom.md&#34;&gt;Cdrom&lt;/a&gt;, ... ]</i>,
        "<a href="#clone" title="Clone">Clone</a>" : <i>[ &lt;a href=&#34;clone.md&#34;&gt;Clone&lt;/a&gt;, ... ]</i>,
        "<a href="#disk" title="Disk">Disk</a>" : <i>[ &lt;a href=&#34;disk.md&#34;&gt;Disk&lt;/a&gt;, ... ]</i>,
        "<a href="#networkinterface" title="NetworkInterface">NetworkInterface</a>" : <i>[ &lt;a href=&#34;networkinterface.md&#34;&gt;NetworkInterface&lt;/a&gt;, ... ]</i>,
        "<a href="#vapp" title="Vapp">Vapp</a>" : <i>[ &lt;a href=&#34;vapp.md&#34;&gt;Vapp&lt;/a&gt;, ... ]</i>,
        "<a href="#customize" title="Customize">Customize</a>" : <i>[ &lt;a href=&#34;customize.md&#34;&gt;Customize&lt;/a&gt;, ... ]</i>,
        "<a href="#linuxoptions" title="LinuxOptions">LinuxOptions</a>" : <i>[ &lt;a href=&#34;linuxoptions.md&#34;&gt;LinuxOptions&lt;/a&gt;, ... ]</i>,
        "<a href="#windowsoptions" title="WindowsOptions">WindowsOptions</a>" : <i>[ &lt;a href=&#34;windowsoptions.md&#34;&gt;WindowsOptions&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::VSphere::VirtualMachine
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#alternateguestname" title="AlternateGuestName">AlternateGuestName</a>: <i>String</i>
    <a href="#annotation" title="Annotation">Annotation</a>: <i>String</i>
    <a href="#bootdelay" title="BootDelay">BootDelay</a>: <i>Double</i>
    <a href="#bootretrydelay" title="BootRetryDelay">BootRetryDelay</a>: <i>Double</i>
    <a href="#bootretryenabled" title="BootRetryEnabled">BootRetryEnabled</a>: <i>Boolean</i>
    <a href="#changeversion" title="ChangeVersion">ChangeVersion</a>: <i>String</i>
    <a href="#cpuhotaddenabled" title="CpuHotAddEnabled">CpuHotAddEnabled</a>: <i>Boolean</i>
    <a href="#cpuhotremoveenabled" title="CpuHotRemoveEnabled">CpuHotRemoveEnabled</a>: <i>Boolean</i>
    <a href="#cpulimit" title="CpuLimit">CpuLimit</a>: <i>Double</i>
    <a href="#cpuperformancecountersenabled" title="CpuPerformanceCountersEnabled">CpuPerformanceCountersEnabled</a>: <i>Boolean</i>
    <a href="#cpureservation" title="CpuReservation">CpuReservation</a>: <i>Double</i>
    <a href="#cpusharecount" title="CpuShareCount">CpuShareCount</a>: <i>Double</i>
    <a href="#cpusharelevel" title="CpuShareLevel">CpuShareLevel</a>: <i>String</i>
    <a href="#customattributes" title="CustomAttributes">CustomAttributes</a>: <i>
      - &lt;a href=&#34;customattributes.md&#34;&gt;CustomAttributes&lt;/a&gt;</i>
    <a href="#datastoreclusterid" title="DatastoreClusterId">DatastoreClusterId</a>: <i>String</i>
    <a href="#datastoreid" title="DatastoreId">DatastoreId</a>: <i>String</i>
    <a href="#defaultipaddress" title="DefaultIpAddress">DefaultIpAddress</a>: <i>String</i>
    <a href="#efisecurebootenabled" title="EfiSecureBootEnabled">EfiSecureBootEnabled</a>: <i>Boolean</i>
    <a href="#enablediskuuid" title="EnableDiskUuid">EnableDiskUuid</a>: <i>Boolean</i>
    <a href="#enablelogging" title="EnableLogging">EnableLogging</a>: <i>Boolean</i>
    <a href="#eptrvimode" title="EptRviMode">EptRviMode</a>: <i>String</i>
    <a href="#extraconfig" title="ExtraConfig">ExtraConfig</a>: <i>
      - &lt;a href=&#34;extraconfig.md&#34;&gt;ExtraConfig&lt;/a&gt;</i>
    <a href="#firmware" title="Firmware">Firmware</a>: <i>String</i>
    <a href="#folder" title="Folder">Folder</a>: <i>String</i>
    <a href="#forcepoweroff" title="ForcePowerOff">ForcePowerOff</a>: <i>Boolean</i>
    <a href="#guestid" title="GuestId">GuestId</a>: <i>String</i>
    <a href="#guestipaddresses" title="GuestIpAddresses">GuestIpAddresses</a>: <i>
      - String</i>
    <a href="#hostsystemid" title="HostSystemId">HostSystemId</a>: <i>String</i>
    <a href="#hvmode" title="HvMode">HvMode</a>: <i>String</i>
    <a href="#ignoredguestips" title="IgnoredGuestIps">IgnoredGuestIps</a>: <i>
      - String</i>
    <a href="#imported" title="Imported">Imported</a>: <i>Boolean</i>
    <a href="#latencysensitivity" title="LatencySensitivity">LatencySensitivity</a>: <i>String</i>
    <a href="#memory" title="Memory">Memory</a>: <i>Double</i>
    <a href="#memoryhotaddenabled" title="MemoryHotAddEnabled">MemoryHotAddEnabled</a>: <i>Boolean</i>
    <a href="#memorylimit" title="MemoryLimit">MemoryLimit</a>: <i>Double</i>
    <a href="#memoryreservation" title="MemoryReservation">MemoryReservation</a>: <i>Double</i>
    <a href="#memorysharecount" title="MemoryShareCount">MemoryShareCount</a>: <i>Double</i>
    <a href="#memorysharelevel" title="MemoryShareLevel">MemoryShareLevel</a>: <i>String</i>
    <a href="#migratewaittimeout" title="MigrateWaitTimeout">MigrateWaitTimeout</a>: <i>Double</i>
    <a href="#moid" title="Moid">Moid</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#nestedhvenabled" title="NestedHvEnabled">NestedHvEnabled</a>: <i>Boolean</i>
    <a href="#numcorespersocket" title="NumCoresPerSocket">NumCoresPerSocket</a>: <i>Double</i>
    <a href="#numcpus" title="NumCpus">NumCpus</a>: <i>Double</i>
    <a href="#rebootrequired" title="RebootRequired">RebootRequired</a>: <i>Boolean</i>
    <a href="#resourcepoolid" title="ResourcePoolId">ResourcePoolId</a>: <i>String</i>
    <a href="#runtoolsscriptsafterpoweron" title="RunToolsScriptsAfterPowerOn">RunToolsScriptsAfterPowerOn</a>: <i>Boolean</i>
    <a href="#runtoolsscriptsafterresume" title="RunToolsScriptsAfterResume">RunToolsScriptsAfterResume</a>: <i>Boolean</i>
    <a href="#runtoolsscriptsbeforeguestreboot" title="RunToolsScriptsBeforeGuestReboot">RunToolsScriptsBeforeGuestReboot</a>: <i>Boolean</i>
    <a href="#runtoolsscriptsbeforeguestshutdown" title="RunToolsScriptsBeforeGuestShutdown">RunToolsScriptsBeforeGuestShutdown</a>: <i>Boolean</i>
    <a href="#runtoolsscriptsbeforegueststandby" title="RunToolsScriptsBeforeGuestStandby">RunToolsScriptsBeforeGuestStandby</a>: <i>Boolean</i>
    <a href="#scsibussharing" title="ScsiBusSharing">ScsiBusSharing</a>: <i>String</i>
    <a href="#scsicontrollercount" title="ScsiControllerCount">ScsiControllerCount</a>: <i>Double</i>
    <a href="#scsitype" title="ScsiType">ScsiType</a>: <i>String</i>
    <a href="#shutdownwaittimeout" title="ShutdownWaitTimeout">ShutdownWaitTimeout</a>: <i>Double</i>
    <a href="#storagepolicyid" title="StoragePolicyId">StoragePolicyId</a>: <i>String</i>
    <a href="#swapplacementpolicy" title="SwapPlacementPolicy">SwapPlacementPolicy</a>: <i>String</i>
    <a href="#synctimewithhost" title="SyncTimeWithHost">SyncTimeWithHost</a>: <i>Boolean</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - String</i>
    <a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
    <a href="#vapptransport" title="VappTransport">VappTransport</a>: <i>
      - String</i>
    <a href="#vmwaretoolsstatus" title="VmwareToolsStatus">VmwareToolsStatus</a>: <i>String</i>
    <a href="#vmxpath" title="VmxPath">VmxPath</a>: <i>String</i>
    <a href="#waitforguestiptimeout" title="WaitForGuestIpTimeout">WaitForGuestIpTimeout</a>: <i>Double</i>
    <a href="#waitforguestnetroutable" title="WaitForGuestNetRoutable">WaitForGuestNetRoutable</a>: <i>Boolean</i>
    <a href="#waitforguestnettimeout" title="WaitForGuestNetTimeout">WaitForGuestNetTimeout</a>: <i>Double</i>
    <a href="#cdrom" title="Cdrom">Cdrom</a>: <i>
      - &lt;a href=&#34;cdrom.md&#34;&gt;Cdrom&lt;/a&gt;</i>
    <a href="#clone" title="Clone">Clone</a>: <i>
      - &lt;a href=&#34;clone.md&#34;&gt;Clone&lt;/a&gt;</i>
    <a href="#disk" title="Disk">Disk</a>: <i>
      - &lt;a href=&#34;disk.md&#34;&gt;Disk&lt;/a&gt;</i>
    <a href="#networkinterface" title="NetworkInterface">NetworkInterface</a>: <i>
      - &lt;a href=&#34;networkinterface.md&#34;&gt;NetworkInterface&lt;/a&gt;</i>
    <a href="#vapp" title="Vapp">Vapp</a>: <i>
      - &lt;a href=&#34;vapp.md&#34;&gt;Vapp&lt;/a&gt;</i>
    <a href="#customize" title="Customize">Customize</a>: <i>
      - &lt;a href=&#34;customize.md&#34;&gt;Customize&lt;/a&gt;</i>
    <a href="#linuxoptions" title="LinuxOptions">LinuxOptions</a>: <i>
      - &lt;a href=&#34;linuxoptions.md&#34;&gt;LinuxOptions&lt;/a&gt;</i>
    <a href="#windowsoptions" title="WindowsOptions">WindowsOptions</a>: <i>
      - &lt;a href=&#34;windowsoptions.md&#34;&gt;WindowsOptions&lt;/a&gt;</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AlternateGuestName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Annotation

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BootDelay

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BootRetryDelay

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BootRetryEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ChangeVersion

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CpuHotAddEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CpuHotRemoveEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CpuLimit

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CpuPerformanceCountersEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CpuReservation

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CpuShareCount

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CpuShareLevel

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomAttributes

_Required_: No

_Type_: List of &lt;a href=&#34;customattributes.md&#34;&gt;CustomAttributes&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DatastoreClusterId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DatastoreId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultIpAddress

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EfiSecureBootEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableDiskUuid

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableLogging

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EptRviMode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExtraConfig

_Required_: No

_Type_: List of &lt;a href=&#34;extraconfig.md&#34;&gt;ExtraConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Firmware

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Folder

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForcePowerOff

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GuestId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GuestIpAddresses

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostSystemId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HvMode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IgnoredGuestIps

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Imported

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LatencySensitivity

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Memory

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MemoryHotAddEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MemoryLimit

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MemoryReservation

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MemoryShareCount

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MemoryShareLevel

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MigrateWaitTimeout

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Moid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NestedHvEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NumCoresPerSocket

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NumCpus

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RebootRequired

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourcePoolId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RunToolsScriptsAfterPowerOn

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RunToolsScriptsAfterResume

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RunToolsScriptsBeforeGuestReboot

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RunToolsScriptsBeforeGuestShutdown

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RunToolsScriptsBeforeGuestStandby

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScsiBusSharing

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScsiControllerCount

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScsiType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ShutdownWaitTimeout

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StoragePolicyId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SwapPlacementPolicy

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SyncTimeWithHost

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VappTransport

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VmwareToolsStatus

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VmxPath

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WaitForGuestIpTimeout

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WaitForGuestNetRoutable

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WaitForGuestNetTimeout

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cdrom

_Required_: No

_Type_: List of &lt;a href=&#34;cdrom.md&#34;&gt;Cdrom&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Clone

_Required_: No

_Type_: List of &lt;a href=&#34;clone.md&#34;&gt;Clone&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Disk

_Required_: No

_Type_: List of &lt;a href=&#34;disk.md&#34;&gt;Disk&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkInterface

_Required_: No

_Type_: List of &lt;a href=&#34;networkinterface.md&#34;&gt;NetworkInterface&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vapp

_Required_: No

_Type_: List of &lt;a href=&#34;vapp.md&#34;&gt;Vapp&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Customize

_Required_: No

_Type_: List of &lt;a href=&#34;customize.md&#34;&gt;Customize&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LinuxOptions

_Required_: No

_Type_: List of &lt;a href=&#34;linuxoptions.md&#34;&gt;LinuxOptions&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WindowsOptions

_Required_: No

_Type_: List of &lt;a href=&#34;windowsoptions.md&#34;&gt;WindowsOptions&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### ChangeVersion

Returns the &lt;code&gt;ChangeVersion&lt;/code&gt; value.

#### DefaultIpAddress

Returns the &lt;code&gt;DefaultIpAddress&lt;/code&gt; value.

#### GuestIpAddresses

Returns the &lt;code&gt;GuestIpAddresses&lt;/code&gt; value.

#### Imported

Returns the &lt;code&gt;Imported&lt;/code&gt; value.

#### Moid

Returns the &lt;code&gt;Moid&lt;/code&gt; value.

#### RebootRequired

Returns the &lt;code&gt;RebootRequired&lt;/code&gt; value.

#### Uuid

Returns the &lt;code&gt;Uuid&lt;/code&gt; value.

#### VappTransport

Returns the &lt;code&gt;VappTransport&lt;/code&gt; value.

#### VmwareToolsStatus

Returns the &lt;code&gt;VmwareToolsStatus&lt;/code&gt; value.

#### VmxPath

Returns the &lt;code&gt;VmxPath&lt;/code&gt; value.
