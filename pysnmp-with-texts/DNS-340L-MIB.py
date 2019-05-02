#
# PySNMP MIB module DNS-340L-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DNS-340L-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:52:17 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, Counter64, iso, Gauge32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, enterprises, IpAddress, Integer32, Bits, TimeTicks, ModuleIdentity, Counter32, Unsigned32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Counter64", "iso", "Gauge32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "enterprises", "IpAddress", "Integer32", "Bits", "TimeTicks", "ModuleIdentity", "Counter32", "Unsigned32", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
d_link = MibIdentifier((1, 3, 6, 1, 4, 1, 171)).setLabel("d-link")
productID = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 50))
projectID = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 50, 1))
modelID = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 50, 1, 10))
submodelID = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 50, 1, 10, 1))
nasAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 50, 1, 10, 1, 1))
dns340LAgentVer = MibScalar((1, 3, 6, 1, 4, 1, 171, 50, 1, 10, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dns340LAgentVer.setStatus('current')
if mibBuilder.loadTexts: dns340LAgentVer.setDescription('Version information for the agent of SNMP of DNS-340L.')
dns340LSoftwareVersion = MibScalar((1, 3, 6, 1, 4, 1, 171, 50, 1, 10, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dns340LSoftwareVersion.setStatus('current')
if mibBuilder.loadTexts: dns340LSoftwareVersion.setDescription('The device software version.')
dns340LHostName = MibScalar((1, 3, 6, 1, 4, 1, 171, 50, 1, 10, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dns340LHostName.setStatus('current')
if mibBuilder.loadTexts: dns340LHostName.setDescription('The device host name.')
dns340LFTPServer = MibScalar((1, 3, 6, 1, 4, 1, 171, 50, 1, 10, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dns340LFTPServer.setStatus('current')
if mibBuilder.loadTexts: dns340LFTPServer.setDescription('Ftp Server status. (Disable/Enable)')
dns340LNetType = MibScalar((1, 3, 6, 1, 4, 1, 171, 50, 1, 10, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dns340LNetType.setStatus('current')
if mibBuilder.loadTexts: dns340LNetType.setDescription('The Network type. (Workgroup/Active Directory)')
dns340LTemperature = MibScalar((1, 3, 6, 1, 4, 1, 171, 50, 1, 10, 1, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dns340LTemperature.setStatus('current')
if mibBuilder.loadTexts: dns340LTemperature.setDescription('The temperature of the system.')
dns340LFanStatus = MibScalar((1, 3, 6, 1, 4, 1, 171, 50, 1, 10, 1, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dns340LFanStatus.setStatus('current')
if mibBuilder.loadTexts: dns340LFanStatus.setDescription('The status of the fan')
dns340LVolumeTable = MibTable((1, 3, 6, 1, 4, 1, 171, 50, 1, 10, 1, 1, 9), )
if mibBuilder.loadTexts: dns340LVolumeTable.setStatus('current')
if mibBuilder.loadTexts: dns340LVolumeTable.setDescription('A table of active volumes on the NAS device.')
dns340LVolumeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 50, 1, 10, 1, 1, 9, 1), ).setIndexNames((0, "DNS-340L-MIB", "dns340LVolumeNum"))
if mibBuilder.loadTexts: dns340LVolumeEntry.setStatus('current')
if mibBuilder.loadTexts: dns340LVolumeEntry.setDescription('An entry in the volume table.')
dns340LVolumeNum = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 50, 1, 10, 1, 1, 9, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dns340LVolumeNum.setStatus('current')
if mibBuilder.loadTexts: dns340LVolumeNum.setDescription('Instance number of the volume entry.')
dns340LVolumeName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 50, 1, 10, 1, 1, 9, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dns340LVolumeName.setStatus('current')
if mibBuilder.loadTexts: dns340LVolumeName.setDescription('The name of the volume.')
dns340LVolumeFsType = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 50, 1, 10, 1, 1, 9, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dns340LVolumeFsType.setStatus('current')
if mibBuilder.loadTexts: dns340LVolumeFsType.setDescription('The type of file system of the volume. Example : ext3 or ext4')
dns340LVolumeRaidLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 50, 1, 10, 1, 1, 9, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dns340LVolumeRaidLevel.setStatus('current')
if mibBuilder.loadTexts: dns340LVolumeRaidLevel.setDescription('The RAID level of the volume. (STANDARD LINEAR RAID0 RAID1 RAID5 RAID10 RAID5+SPARE)')
dns340LVolumeSize = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 50, 1, 10, 1, 1, 9, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dns340LVolumeSize.setStatus('current')
if mibBuilder.loadTexts: dns340LVolumeSize.setDescription('The size of the volume in bytes.')
dns340LVolumeFreeSpace = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 50, 1, 10, 1, 1, 9, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dns340LVolumeFreeSpace.setStatus('current')
if mibBuilder.loadTexts: dns340LVolumeFreeSpace.setDescription('Free space on the volume in bytes.')
dns340LDiskTable = MibTable((1, 3, 6, 1, 4, 1, 171, 50, 1, 10, 1, 1, 10), )
if mibBuilder.loadTexts: dns340LDiskTable.setStatus('current')
if mibBuilder.loadTexts: dns340LDiskTable.setDescription('A table of physical disks attached to the NAS device.')
dns340LDiskEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 50, 1, 10, 1, 1, 10, 1), ).setIndexNames((0, "DNS-340L-MIB", "dns340LDiskNum"))
if mibBuilder.loadTexts: dns340LDiskEntry.setStatus('current')
if mibBuilder.loadTexts: dns340LDiskEntry.setDescription('An entry in the physical disk table.')
dns340LDiskNum = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 50, 1, 10, 1, 1, 10, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dns340LDiskNum.setStatus('current')
if mibBuilder.loadTexts: dns340LDiskNum.setDescription('Instance number of the disk entry.')
dns340LDiskVendor = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 50, 1, 10, 1, 1, 10, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dns340LDiskVendor.setStatus('current')
if mibBuilder.loadTexts: dns340LDiskVendor.setDescription('The vendor of the disk drive.')
dns340LDiskModel = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 50, 1, 10, 1, 1, 10, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dns340LDiskModel.setStatus('current')
if mibBuilder.loadTexts: dns340LDiskModel.setDescription("The disk drive's model name.")
dns340LDiskSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 50, 1, 10, 1, 1, 10, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dns340LDiskSerialNumber.setStatus('current')
if mibBuilder.loadTexts: dns340LDiskSerialNumber.setDescription("The disk drive's serial number.")
dns340LDiskTemperature = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 50, 1, 10, 1, 1, 10, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dns340LDiskTemperature.setStatus('current')
if mibBuilder.loadTexts: dns340LDiskTemperature.setDescription('The centigrade temperature of this disk.')
dns340LDiskCapacity = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 50, 1, 10, 1, 1, 10, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dns340LDiskCapacity.setStatus('current')
if mibBuilder.loadTexts: dns340LDiskCapacity.setDescription('The capacity of the disk in GB.')
dns340LUPSTable = MibTable((1, 3, 6, 1, 4, 1, 171, 50, 1, 10, 1, 1, 11), )
if mibBuilder.loadTexts: dns340LUPSTable.setStatus('current')
if mibBuilder.loadTexts: dns340LUPSTable.setDescription('A table of UPS attached to the NAS device.')
dns340LUPSEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 50, 1, 10, 1, 1, 11, 1), ).setIndexNames((0, "DNS-340L-MIB", "dns340LUPSNum"))
if mibBuilder.loadTexts: dns340LUPSEntry.setStatus('current')
if mibBuilder.loadTexts: dns340LUPSEntry.setDescription('An entry in the UPS table.')
dns340LUPSNum = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 50, 1, 10, 1, 1, 11, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dns340LUPSNum.setStatus('current')
if mibBuilder.loadTexts: dns340LUPSNum.setDescription('Instance number of the UPS entry.')
dns340LUPSMode = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 50, 1, 10, 1, 1, 11, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dns340LUPSMode.setStatus('current')
if mibBuilder.loadTexts: dns340LUPSMode.setDescription('The mode of the UPS ')
dns340LUPSManufacturer = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 50, 1, 10, 1, 1, 11, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dns340LUPSManufacturer.setStatus('current')
if mibBuilder.loadTexts: dns340LUPSManufacturer.setDescription('The manufacturer of the UPS.')
dns340LUPSProduct = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 50, 1, 10, 1, 1, 11, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dns340LUPSProduct.setStatus('current')
if mibBuilder.loadTexts: dns340LUPSProduct.setDescription('The product name of the UPS.')
dns340LUPSBatteryCharge = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 50, 1, 10, 1, 1, 11, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dns340LUPSBatteryCharge.setStatus('current')
if mibBuilder.loadTexts: dns340LUPSBatteryCharge.setDescription('The battery charge of the UPS.')
dns340LUPSStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 50, 1, 10, 1, 1, 11, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dns340LUPSStatus.setStatus('current')
if mibBuilder.loadTexts: dns340LUPSStatus.setDescription('The status of this UPS.')
notifyEvts = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 50, 1, 10, 1, 1, 200))
notifyPasswdChanged = NotificationType((1, 3, 6, 1, 4, 1, 171, 50, 1, 10, 1, 1, 200, 1))
if mibBuilder.loadTexts: notifyPasswdChanged.setStatus('current')
if mibBuilder.loadTexts: notifyPasswdChanged.setDescription("An indication that the Administrator's password has been changed.")
notifyFirmwareUpgraded = NotificationType((1, 3, 6, 1, 4, 1, 171, 50, 1, 10, 1, 1, 200, 2))
if mibBuilder.loadTexts: notifyFirmwareUpgraded.setStatus('current')
if mibBuilder.loadTexts: notifyFirmwareUpgraded.setDescription('An indication that firmware has been upgraded.')
notifyNetworkChanged = NotificationType((1, 3, 6, 1, 4, 1, 171, 50, 1, 10, 1, 1, 200, 3))
if mibBuilder.loadTexts: notifyNetworkChanged.setStatus('current')
if mibBuilder.loadTexts: notifyNetworkChanged.setDescription('An indication that the network settings has been changed.')
notifyTemperatureExceeded = NotificationType((1, 3, 6, 1, 4, 1, 171, 50, 1, 10, 1, 1, 200, 4))
if mibBuilder.loadTexts: notifyTemperatureExceeded.setStatus('current')
if mibBuilder.loadTexts: notifyTemperatureExceeded.setDescription('An indication that system temperature has exceeded.')
mibBuilder.exportSymbols("DNS-340L-MIB", dns340LVolumeTable=dns340LVolumeTable, dns340LDiskEntry=dns340LDiskEntry, dns340LDiskTemperature=dns340LDiskTemperature, dns340LUPSNum=dns340LUPSNum, notifyNetworkChanged=notifyNetworkChanged, dns340LVolumeSize=dns340LVolumeSize, notifyEvts=notifyEvts, dns340LUPSMode=dns340LUPSMode, dns340LDiskNum=dns340LDiskNum, dns340LUPSStatus=dns340LUPSStatus, notifyPasswdChanged=notifyPasswdChanged, notifyTemperatureExceeded=notifyTemperatureExceeded, dns340LUPSBatteryCharge=dns340LUPSBatteryCharge, notifyFirmwareUpgraded=notifyFirmwareUpgraded, dns340LTemperature=dns340LTemperature, dns340LDiskCapacity=dns340LDiskCapacity, dns340LVolumeFreeSpace=dns340LVolumeFreeSpace, d_link=d_link, dns340LSoftwareVersion=dns340LSoftwareVersion, dns340LVolumeName=dns340LVolumeName, dns340LVolumeNum=dns340LVolumeNum, dns340LFanStatus=dns340LFanStatus, dns340LUPSEntry=dns340LUPSEntry, dns340LUPSManufacturer=dns340LUPSManufacturer, dns340LAgentVer=dns340LAgentVer, submodelID=submodelID, dns340LDiskSerialNumber=dns340LDiskSerialNumber, dns340LVolumeRaidLevel=dns340LVolumeRaidLevel, dns340LDiskVendor=dns340LDiskVendor, dns340LFTPServer=dns340LFTPServer, dns340LNetType=dns340LNetType, dns340LUPSProduct=dns340LUPSProduct, dns340LVolumeFsType=dns340LVolumeFsType, modelID=modelID, dns340LUPSTable=dns340LUPSTable, dns340LDiskTable=dns340LDiskTable, dns340LVolumeEntry=dns340LVolumeEntry, productID=productID, nasAgent=nasAgent, dns340LDiskModel=dns340LDiskModel, dns340LHostName=dns340LHostName, projectID=projectID)