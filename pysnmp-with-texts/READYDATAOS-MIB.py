#
# PySNMP MIB module READYDATAOS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/READYDATAOS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:55:11 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, enterprises, Counter64, iso, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Counter32, Bits, IpAddress, Integer32, ObjectIdentity, TimeTicks, Unsigned32, MibIdentifier, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "enterprises", "Counter64", "iso", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Counter32", "Bits", "IpAddress", "Integer32", "ObjectIdentity", "TimeTicks", "Unsigned32", "MibIdentifier", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
netgear = MibIdentifier((1, 3, 6, 1, 4, 1, 4526))
productID = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100))
ReadyDATAOS = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 15))
ngNasManager = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 22))
nasMgrSoftwareVersion = MibScalar((1, 3, 6, 1, 4, 1, 4526, 22, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nasMgrSoftwareVersion.setStatus('current')
if mibBuilder.loadTexts: nasMgrSoftwareVersion.setDescription('Version information for the ReadyDATAOS ngNasManager software.')
diskTable = MibTable((1, 3, 6, 1, 4, 1, 4526, 22, 3), )
if mibBuilder.loadTexts: diskTable.setStatus('mandatory')
if mibBuilder.loadTexts: diskTable.setDescription('A table of physical disks attached to the storage device.')
diskEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4526, 22, 3, 1), ).setIndexNames((0, "READYDATAOS-MIB", "diskNumber"))
if mibBuilder.loadTexts: diskEntry.setStatus('mandatory')
if mibBuilder.loadTexts: diskEntry.setDescription('An entry in the physical disk table.')
diskNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 22, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskNumber.setStatus('mandatory')
if mibBuilder.loadTexts: diskNumber.setDescription('Instance number of the disk entry.')
diskID = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 22, 3, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskID.setStatus('mandatory')
if mibBuilder.loadTexts: diskID.setDescription('Disk ID.')
diskSlotName = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 22, 3, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskSlotName.setStatus('mandatory')
if mibBuilder.loadTexts: diskSlotName.setDescription('The slot location of the disk.')
diskSerial = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 22, 3, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskSerial.setStatus('mandatory')
if mibBuilder.loadTexts: diskSerial.setDescription('Disk Serial number.')
diskModel = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 22, 3, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskModel.setStatus('mandatory')
if mibBuilder.loadTexts: diskModel.setDescription("The disk drive's model name.")
ataError = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 22, 3, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ataError.setStatus('mandatory')
if mibBuilder.loadTexts: ataError.setDescription('ATA error number for this disk from S.M.A.R.T read.')
diskCapacity = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 22, 3, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskCapacity.setStatus('mandatory')
if mibBuilder.loadTexts: diskCapacity.setDescription('The capacity of the disk in bytes.')
diskInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 22, 3, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskInterface.setStatus('mandatory')
if mibBuilder.loadTexts: diskInterface.setDescription('The disk connect interface, such as SATA, USB etc.')
diskState = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 22, 3, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskState.setStatus('mandatory')
if mibBuilder.loadTexts: diskState.setDescription('The current state of the Disk. Possible states: 0: Online 1: Offline')
diskTemperature = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 22, 3, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskTemperature.setStatus('mandatory')
if mibBuilder.loadTexts: diskTemperature.setDescription('temperature of this disk(in Fahrenheit unit).')
fanTable = MibTable((1, 3, 6, 1, 4, 1, 4526, 22, 4), )
if mibBuilder.loadTexts: fanTable.setStatus('current')
fanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4526, 22, 4, 1), ).setIndexNames((0, "READYDATAOS-MIB", "fanNumber"))
if mibBuilder.loadTexts: fanEntry.setStatus('current')
fanNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 22, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10000000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fanNumber.setStatus('mandatory')
if mibBuilder.loadTexts: fanNumber.setDescription('Instance number of this fan entry.')
fanRPM = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 22, 4, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fanRPM.setStatus('mandatory')
if mibBuilder.loadTexts: fanRPM.setDescription('The current speed of the fan.')
fanStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 22, 4, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fanStatus.setStatus('mandatory')
if mibBuilder.loadTexts: fanStatus.setDescription('The status of Fan')
fanType = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 22, 4, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fanType.setStatus('mandatory')
if mibBuilder.loadTexts: fanType.setDescription('What fan is used for: SYS: for system board CPU: for CPU CASE: for system case')
temperatureTable = MibTable((1, 3, 6, 1, 4, 1, 4526, 22, 5), )
if mibBuilder.loadTexts: temperatureTable.setStatus('mandatory')
temperatureEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4526, 22, 5, 1), ).setIndexNames((0, "READYDATAOS-MIB", "temperatureNumber"))
if mibBuilder.loadTexts: temperatureEntry.setStatus('mandatory')
temperatureNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 22, 5, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: temperatureNumber.setStatus('mandatory')
if mibBuilder.loadTexts: temperatureNumber.setDescription('Instance number of this temperature probe entry.')
temperatureValue = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 22, 5, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: temperatureValue.setStatus('mandatory')
if mibBuilder.loadTexts: temperatureValue.setDescription('The current temperature of this probe (in Fahrenheit unit).')
temperatureTyoe = MibScalar((1, 3, 6, 1, 4, 1, 4526, 22, 5, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: temperatureTyoe.setStatus('mandatory')
if mibBuilder.loadTexts: temperatureTyoe.setDescription('The current temperature refer to')
temperatureMin = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 22, 5, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: temperatureMin.setStatus('mandatory')
if mibBuilder.loadTexts: temperatureMin.setDescription('The min temperature of this probe (in Fahrenheit unit).')
temperatureMax = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 22, 5, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: temperatureMax.setStatus('mandatory')
if mibBuilder.loadTexts: temperatureMax.setDescription('The max temperature of this probe (in Fahrenheit unit).')
volumeTable = MibTable((1, 3, 6, 1, 4, 1, 4526, 22, 7), )
if mibBuilder.loadTexts: volumeTable.setStatus('mandatory')
if mibBuilder.loadTexts: volumeTable.setDescription('A table of active volumes on the storage device.')
volumeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4526, 22, 7, 1), ).setIndexNames((0, "READYDATAOS-MIB", "volumeNumber"))
if mibBuilder.loadTexts: volumeEntry.setStatus('mandatory')
if mibBuilder.loadTexts: volumeEntry.setDescription('An entry in the volume table.')
volumeNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 22, 7, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volumeNumber.setStatus('mandatory')
if mibBuilder.loadTexts: volumeNumber.setDescription('Instance number of the volume entry.')
volumeName = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 22, 7, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volumeName.setStatus('mandatory')
if mibBuilder.loadTexts: volumeName.setDescription('The name of the volume.')
volumeRAIDLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 22, 7, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volumeRAIDLevel.setStatus('mandatory')
if mibBuilder.loadTexts: volumeRAIDLevel.setDescription('The RAID level of the volume.')
volumeStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 22, 7, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volumeStatus.setStatus('mandatory')
if mibBuilder.loadTexts: volumeStatus.setDescription('The severity of the volume. Possible values: 1: ONLINE 2: OFFLINE 3: DEGRADED 4: FAULTED 5: REMOVED 6: UNAVAILABLE 7: UNKNOWN')
volumeSize = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 22, 7, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volumeSize.setStatus('mandatory')
if mibBuilder.loadTexts: volumeSize.setDescription('The size of the volume in megabytes.')
volumeFreeSpace = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 22, 7, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volumeFreeSpace.setStatus('mandatory')
if mibBuilder.loadTexts: volumeFreeSpace.setDescription('Free space on the volume in megabytes.')
psuTable = MibTable((1, 3, 6, 1, 4, 1, 4526, 22, 8), )
if mibBuilder.loadTexts: psuTable.setStatus('mandatory')
psuEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4526, 22, 8, 1), ).setMaxAccess("readonly").setIndexNames((0, "READYDATAOS-MIB", "psuNumber"))
if mibBuilder.loadTexts: psuEntry.setStatus('mandatory')
psuNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 22, 8, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: psuNumber.setStatus('mandatory')
if mibBuilder.loadTexts: psuNumber.setDescription('Instance number of this power supply unit.')
psuDesc = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 22, 8, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: psuDesc.setStatus('mandatory')
if mibBuilder.loadTexts: psuDesc.setDescription('The description of this PSU.')
psuStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 22, 8, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: psuStatus.setStatus('mandatory')
if mibBuilder.loadTexts: psuStatus.setDescription('The current PSU status.')
aryMgrEvts = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 22, 200))
controllerNameEv = MibScalar((1, 3, 6, 1, 4, 1, 4526, 22, 200, 201), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: controllerNameEv.setStatus('mandatory')
if mibBuilder.loadTexts: controllerNameEv.setDescription('Controller Name for which trap is generated.')
channelNumberEv = MibScalar((1, 3, 6, 1, 4, 1, 4526, 22, 200, 202), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 3))).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelNumberEv.setStatus('mandatory')
if mibBuilder.loadTexts: channelNumberEv.setDescription('Channel Number for which trap is generated.')
targetIDEv = MibScalar((1, 3, 6, 1, 4, 1, 4526, 22, 200, 203), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: targetIDEv.setStatus('mandatory')
if mibBuilder.loadTexts: targetIDEv.setDescription('SCSI ID of the device for which trap is generated.')
virtualDiskNameEv = MibScalar((1, 3, 6, 1, 4, 1, 4526, 22, 200, 204), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtualDiskNameEv.setStatus('mandatory')
if mibBuilder.loadTexts: virtualDiskNameEv.setDescription('Virtual Disk for which trap is generated.')
arrayDiskNameEv = MibScalar((1, 3, 6, 1, 4, 1, 4526, 22, 200, 205), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: arrayDiskNameEv.setStatus('mandatory')
if mibBuilder.loadTexts: arrayDiskNameEv.setDescription('Array Disk for which trap is generated.')
oldVDConfigEv = MibScalar((1, 3, 6, 1, 4, 1, 4526, 22, 200, 206), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: oldVDConfigEv.setStatus('mandatory')
if mibBuilder.loadTexts: oldVDConfigEv.setDescription('Current Virtual Disk configuration for which trap is generated')
newVDConfigEv = MibScalar((1, 3, 6, 1, 4, 1, 4526, 22, 200, 207), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: newVDConfigEv.setStatus('mandatory')
if mibBuilder.loadTexts: newVDConfigEv.setDescription('New Virtual Disk configuration for which trap is generated.')
enclosureNumberEv = MibScalar((1, 3, 6, 1, 4, 1, 4526, 22, 200, 208), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: enclosureNumberEv.setStatus('mandatory')
if mibBuilder.loadTexts: enclosureNumberEv.setDescription('Enclosure Number for which trap is generated.')
unitNumberEv = MibScalar((1, 3, 6, 1, 4, 1, 4526, 22, 200, 209), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: unitNumberEv.setStatus('mandatory')
if mibBuilder.loadTexts: unitNumberEv.setDescription('Unit Number for which trap is generated. (Fan, Power Supply, Temperature Probe)')
enclosureNameEv = MibScalar((1, 3, 6, 1, 4, 1, 4526, 22, 200, 210), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: enclosureNameEv.setStatus('mandatory')
if mibBuilder.loadTexts: enclosureNameEv.setDescription('Enclosure Name for which trap is generated.')
unitNameEv = MibScalar((1, 3, 6, 1, 4, 1, 4526, 22, 200, 211), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: unitNameEv.setStatus('mandatory')
if mibBuilder.loadTexts: unitNameEv.setDescription('Unit Number for which trap is generated. (Fan, Power Supply, Temperature Probe)')
timeEv = MibScalar((1, 3, 6, 1, 4, 1, 4526, 22, 200, 212), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: timeEv.setStatus('mandatory')
if mibBuilder.loadTexts: timeEv.setDescription('Amount of time specified in the trap message.')
volumeNameEv = MibScalar((1, 3, 6, 1, 4, 1, 4526, 22, 200, 213), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volumeNameEv.setStatus('mandatory')
if mibBuilder.loadTexts: volumeNameEv.setDescription('Volume Drive Letter for which trap is generated.')
fanFailureMesg = MibScalar((1, 3, 6, 1, 4, 1, 4526, 22, 400), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fanFailureMesg.setStatus('current')
if mibBuilder.loadTexts: fanFailureMesg.setDescription('Failure message for Fan')
tempFailureMesg = MibScalar((1, 3, 6, 1, 4, 1, 4526, 22, 401), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tempFailureMesg.setStatus('current')
if mibBuilder.loadTexts: tempFailureMesg.setDescription('Failure message for system temperature')
powerVoltageMesg = MibScalar((1, 3, 6, 1, 4, 1, 4526, 22, 402), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: powerVoltageMesg.setStatus('current')
if mibBuilder.loadTexts: powerVoltageMesg.setDescription('Failure message for system power')
raidEventNoticeMesg = MibScalar((1, 3, 6, 1, 4, 1, 4526, 22, 403), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: raidEventNoticeMesg.setStatus('current')
if mibBuilder.loadTexts: raidEventNoticeMesg.setDescription('RAID hotplug event message')
snapshotEventNoticeMesg = MibScalar((1, 3, 6, 1, 4, 1, 4526, 22, 404), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snapshotEventNoticeMesg.setStatus('current')
if mibBuilder.loadTexts: snapshotEventNoticeMesg.setDescription('Snapshot messages')
upsEventNoticeMesg = MibScalar((1, 3, 6, 1, 4, 1, 4526, 22, 405), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: upsEventNoticeMesg.setStatus('current')
if mibBuilder.loadTexts: upsEventNoticeMesg.setDescription('UPS status message')
hotplugDiskNoticeMesg = MibScalar((1, 3, 6, 1, 4, 1, 4526, 22, 406), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hotplugDiskNoticeMesg.setStatus('current')
if mibBuilder.loadTexts: hotplugDiskNoticeMesg.setDescription('Disk hotplug event messages')
volumeNoticeMesg = MibScalar((1, 3, 6, 1, 4, 1, 4526, 22, 407), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volumeNoticeMesg.setStatus('current')
if mibBuilder.loadTexts: volumeNoticeMesg.setDescription('Disk usage warning')
diskTempWarningMesg = MibScalar((1, 3, 6, 1, 4, 1, 4526, 22, 408), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskTempWarningMesg.setStatus('current')
if mibBuilder.loadTexts: diskTempWarningMesg.setDescription('Disk temperature warning messages')
backupNoticeMesg = MibScalar((1, 3, 6, 1, 4, 1, 4526, 22, 409), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: backupNoticeMesg.setStatus('current')
if mibBuilder.loadTexts: backupNoticeMesg.setDescription('Backup job status messages')
diskSmartWarningMesg = MibScalar((1, 3, 6, 1, 4, 1, 4526, 22, 410), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskSmartWarningMesg.setStatus('current')
if mibBuilder.loadTexts: diskSmartWarningMesg.setDescription('Disk SMART messages')
psuWarningMesg = MibScalar((1, 3, 6, 1, 4, 1, 4526, 22, 411), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: psuWarningMesg.setStatus('current')
if mibBuilder.loadTexts: psuWarningMesg.setDescription('PSU status messages')
nasTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 22, 300))
fanFailure = NotificationType((1, 3, 6, 1, 4, 1, 4526, 22, 300) + (0,10)).setObjects(("READYDATAOS-MIB", "fanFailureMesg"))
if mibBuilder.loadTexts: fanFailure.setDescription('Fan failure, fan speed is %s.')
tempFailure = NotificationType((1, 3, 6, 1, 4, 1, 4526, 22, 300) + (0,20)).setObjects(("READYDATAOS-MIB", "tempFailureMesg"))
if mibBuilder.loadTexts: tempFailure.setDescription('Temperature sensor reports out of normal range. ')
powerVoltage = NotificationType((1, 3, 6, 1, 4, 1, 4526, 22, 300) + (0,30)).setObjects(("READYDATAOS-MIB", "powerVoltageMesg"))
if mibBuilder.loadTexts: powerVoltage.setDescription('System power is out of spec, please check system status! ')
raidEventNotice = NotificationType((1, 3, 6, 1, 4, 1, 4526, 22, 300) + (0,40)).setObjects(("READYDATAOS-MIB", "raidEventNoticeMesg"))
if mibBuilder.loadTexts: raidEventNotice.setDescription('RAID event detected! ')
snapshotEventNotice = NotificationType((1, 3, 6, 1, 4, 1, 4526, 22, 300) + (0,50)).setObjects(("READYDATAOS-MIB", "snapshotEventNoticeMesg"))
if mibBuilder.loadTexts: snapshotEventNotice.setDescription('Snapshot event detected! ')
hotplugDiskNotice = NotificationType((1, 3, 6, 1, 4, 1, 4526, 22, 300) + (0,60)).setObjects(("READYDATAOS-MIB", "hotplugDiskNoticeMesg"))
if mibBuilder.loadTexts: hotplugDiskNotice.setDescription(' Hotplug disk event detected! ')
upsEventNotice = NotificationType((1, 3, 6, 1, 4, 1, 4526, 22, 300) + (0,70)).setObjects(("READYDATAOS-MIB", "upsEventNoticeMesg"))
if mibBuilder.loadTexts: upsEventNotice.setDescription('UPS status. ')
volumeNotice = NotificationType((1, 3, 6, 1, 4, 1, 4526, 22, 300) + (0,80)).setObjects(("READYDATAOS-MIB", "volumeNoticeMesg"))
if mibBuilder.loadTexts: volumeNotice.setDescription('Volume is approaching capacity. ')
diskTempWarning = NotificationType((1, 3, 6, 1, 4, 1, 4526, 22, 300) + (0,90)).setObjects(("READYDATAOS-MIB", "diskTempWarningMesg"))
if mibBuilder.loadTexts: diskTempWarning.setDescription('Disk temperature warning. ')
backupNotice = NotificationType((1, 3, 6, 1, 4, 1, 4526, 22, 300) + (0,100)).setObjects(("READYDATAOS-MIB", "backupNoticeMesg"))
if mibBuilder.loadTexts: backupNotice.setDescription('Backup job status. ')
diskSmartWarning = NotificationType((1, 3, 6, 1, 4, 1, 4526, 22, 300) + (0,110)).setObjects(("READYDATAOS-MIB", "diskSmartWarningMesg"))
if mibBuilder.loadTexts: diskSmartWarning.setDescription('Disk SMART warning. ')
psuWarning = NotificationType((1, 3, 6, 1, 4, 1, 4526, 22, 300) + (0,120)).setObjects(("READYDATAOS-MIB", "psuWarningMesg"))
if mibBuilder.loadTexts: psuWarning.setDescription('Power supply unit warning. ')
mibBuilder.exportSymbols("READYDATAOS-MIB", fanFailure=fanFailure, psuWarning=psuWarning, enclosureNumberEv=enclosureNumberEv, diskCapacity=diskCapacity, temperatureMax=temperatureMax, psuTable=psuTable, fanEntry=fanEntry, controllerNameEv=controllerNameEv, nasTraps=nasTraps, volumeFreeSpace=volumeFreeSpace, newVDConfigEv=newVDConfigEv, fanType=fanType, volumeNotice=volumeNotice, psuStatus=psuStatus, diskTempWarning=diskTempWarning, diskTable=diskTable, volumeTable=volumeTable, enclosureNameEv=enclosureNameEv, hotplugDiskNoticeMesg=hotplugDiskNoticeMesg, volumeRAIDLevel=volumeRAIDLevel, volumeNumber=volumeNumber, tempFailure=tempFailure, diskSerial=diskSerial, unitNumberEv=unitNumberEv, psuEntry=psuEntry, psuNumber=psuNumber, diskState=diskState, volumeNameEv=volumeNameEv, upsEventNoticeMesg=upsEventNoticeMesg, volumeNoticeMesg=volumeNoticeMesg, raidEventNoticeMesg=raidEventNoticeMesg, timeEv=timeEv, tempFailureMesg=tempFailureMesg, diskID=diskID, backupNotice=backupNotice, volumeEntry=volumeEntry, volumeName=volumeName, psuWarningMesg=psuWarningMesg, psuDesc=psuDesc, oldVDConfigEv=oldVDConfigEv, unitNameEv=unitNameEv, volumeStatus=volumeStatus, diskSmartWarning=diskSmartWarning, temperatureNumber=temperatureNumber, ataError=ataError, backupNoticeMesg=backupNoticeMesg, aryMgrEvts=aryMgrEvts, volumeSize=volumeSize, diskNumber=diskNumber, fanNumber=fanNumber, ReadyDATAOS=ReadyDATAOS, temperatureMin=temperatureMin, powerVoltageMesg=powerVoltageMesg, productID=productID, diskSlotName=diskSlotName, hotplugDiskNotice=hotplugDiskNotice, diskInterface=diskInterface, nasMgrSoftwareVersion=nasMgrSoftwareVersion, arrayDiskNameEv=arrayDiskNameEv, fanRPM=fanRPM, virtualDiskNameEv=virtualDiskNameEv, fanFailureMesg=fanFailureMesg, temperatureEntry=temperatureEntry, temperatureValue=temperatureValue, fanStatus=fanStatus, diskSmartWarningMesg=diskSmartWarningMesg, diskTempWarningMesg=diskTempWarningMesg, diskModel=diskModel, snapshotEventNoticeMesg=snapshotEventNoticeMesg, upsEventNotice=upsEventNotice, temperatureTable=temperatureTable, targetIDEv=targetIDEv, ngNasManager=ngNasManager, snapshotEventNotice=snapshotEventNotice, temperatureTyoe=temperatureTyoe, raidEventNotice=raidEventNotice, channelNumberEv=channelNumberEv, diskTemperature=diskTemperature, powerVoltage=powerVoltage, fanTable=fanTable, diskEntry=diskEntry, netgear=netgear)
