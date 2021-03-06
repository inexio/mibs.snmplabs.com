#
# PySNMP MIB module HH3C-VM-MAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HH3C-VM-MAN-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:30:16 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
entPhysicalAssetID, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalAssetID")
hh3cSurveillanceMIB, = mibBuilder.importSymbols("HH3C-OID-MIB", "hh3cSurveillanceMIB")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, TimeTicks, ModuleIdentity, NotificationType, ObjectIdentity, IpAddress, MibIdentifier, Integer32, iso, Bits, Gauge32, Counter32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "TimeTicks", "ModuleIdentity", "NotificationType", "ObjectIdentity", "IpAddress", "MibIdentifier", "Integer32", "iso", "Bits", "Gauge32", "Counter32", "Unsigned32")
DateAndTime, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "TextualConvention", "DisplayString")
hh3cVMMan = ModuleIdentity((1, 3, 6, 1, 4, 1, 25506, 9, 1))
if mibBuilder.loadTexts: hh3cVMMan.setLastUpdated('200704130000Z')
if mibBuilder.loadTexts: hh3cVMMan.setOrganization('Hangzhou H3C Tech. Co., Ltd.')
if mibBuilder.loadTexts: hh3cVMMan.setContactInfo('Platform Team Hangzhou H3C Tech. Co., Ltd. Hai-Dian District Beijing P.R. China http://www.h3c.com Zip:100085 ')
if mibBuilder.loadTexts: hh3cVMMan.setDescription('VM is one of surveillance features, implementing user authentication, configuration management, network management and control signalling forwarding. This MIB contains objects to manage the VM feature.')
hh3cVMManMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 9, 1, 1))
hh3cVMCapabilitySet = MibScalar((1, 3, 6, 1, 4, 1, 25506, 9, 1, 1, 1), Bits().clone(namedValues=NamedValues(("cms", 0), ("css", 1), ("dm", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cVMCapabilitySet.setStatus('current')
if mibBuilder.loadTexts: hh3cVMCapabilitySet.setDescription('Components included in the VM feature represented by bit fields. VM feature includes three componets: CMS(Central Management Server), CSS(Control Signalling Server) and DM(Data Managment). A bit set to 1 indicates the corresponding component of this bit is included otherwise indicates the corresponding component of this bit is not included. VM can include one or more components at one time. ')
hh3cVMStat = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 9, 1, 1, 2))
hh3cVMStatTotalConnEstablishRequests = MibScalar((1, 3, 6, 1, 4, 1, 25506, 9, 1, 1, 2, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cVMStatTotalConnEstablishRequests.setStatus('current')
if mibBuilder.loadTexts: hh3cVMStatTotalConnEstablishRequests.setDescription('The total number of establishment requests for video connection.')
hh3cVMStatSuccConnEstablishRequests = MibScalar((1, 3, 6, 1, 4, 1, 25506, 9, 1, 1, 2, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cVMStatSuccConnEstablishRequests.setStatus('current')
if mibBuilder.loadTexts: hh3cVMStatSuccConnEstablishRequests.setDescription('The total number of successful establishment requests for video connection.')
hh3cVMStatFailConnEstablishRequests = MibScalar((1, 3, 6, 1, 4, 1, 25506, 9, 1, 1, 2, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cVMStatFailConnEstablishRequests.setStatus('current')
if mibBuilder.loadTexts: hh3cVMStatFailConnEstablishRequests.setDescription('The total number of unsuccessful establishment requests for video connection.')
hh3cVMStatTotalConnReleaseRequests = MibScalar((1, 3, 6, 1, 4, 1, 25506, 9, 1, 1, 2, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cVMStatTotalConnReleaseRequests.setStatus('current')
if mibBuilder.loadTexts: hh3cVMStatTotalConnReleaseRequests.setDescription('The total number of release requests for video connection.')
hh3cVMStatSuccConnReleaseRequests = MibScalar((1, 3, 6, 1, 4, 1, 25506, 9, 1, 1, 2, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cVMStatSuccConnReleaseRequests.setStatus('current')
if mibBuilder.loadTexts: hh3cVMStatSuccConnReleaseRequests.setDescription('The total number of successful release requests for video connection.')
hh3cVMStatFailConnReleaseRequests = MibScalar((1, 3, 6, 1, 4, 1, 25506, 9, 1, 1, 2, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cVMStatFailConnReleaseRequests.setStatus('current')
if mibBuilder.loadTexts: hh3cVMStatFailConnReleaseRequests.setDescription('The total number of unsuccessful release requests for video connection.')
hh3cVMStatExceptionTerminationConn = MibScalar((1, 3, 6, 1, 4, 1, 25506, 9, 1, 1, 2, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cVMStatExceptionTerminationConn.setStatus('current')
if mibBuilder.loadTexts: hh3cVMStatExceptionTerminationConn.setDescription('The total number of exceptional termination for video connection.')
hh3cVMManMIBTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 9, 1, 2))
hh3cVMManTrapPrex = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 9, 1, 2, 0))
hh3cVMManDeviceOnlineTrap = NotificationType((1, 3, 6, 1, 4, 1, 25506, 9, 1, 2, 0, 1)).setObjects(("ENTITY-MIB", "entPhysicalAssetID"), ("HH3C-VM-MAN-MIB", "hh3cVMManRegDevIP"), ("HH3C-VM-MAN-MIB", "hh3cVMManRegDevName"))
if mibBuilder.loadTexts: hh3cVMManDeviceOnlineTrap.setStatus('current')
if mibBuilder.loadTexts: hh3cVMManDeviceOnlineTrap.setDescription('Send a trap about the device having been registered to VM.')
hh3cVMManDeviceOfflineTrap = NotificationType((1, 3, 6, 1, 4, 1, 25506, 9, 1, 2, 0, 2)).setObjects(("ENTITY-MIB", "entPhysicalAssetID"), ("HH3C-VM-MAN-MIB", "hh3cVMManRegDevIP"), ("HH3C-VM-MAN-MIB", "hh3cVMManRegDevName"))
if mibBuilder.loadTexts: hh3cVMManDeviceOfflineTrap.setStatus('current')
if mibBuilder.loadTexts: hh3cVMManDeviceOfflineTrap.setDescription('Send a trap about the device having been unregistered to VM.')
hh3cVMManForwardDeviceExternalSemaphoreTrap = NotificationType((1, 3, 6, 1, 4, 1, 25506, 9, 1, 2, 0, 3)).setObjects(("ENTITY-MIB", "entPhysicalAssetID"), ("HH3C-VM-MAN-MIB", "hh3cVMManRegDevIP"), ("HH3C-VM-MAN-MIB", "hh3cVMManRegDevName"), ("HH3C-VM-MAN-MIB", "hh3cVMManPUExternalInputAlarmChannelID"))
if mibBuilder.loadTexts: hh3cVMManForwardDeviceExternalSemaphoreTrap.setStatus('current')
if mibBuilder.loadTexts: hh3cVMManForwardDeviceExternalSemaphoreTrap.setDescription('Forward a trap about external semaphore alarm, which is created by the third party device.')
hh3cVMManForwardDeviceVideoLossTrap = NotificationType((1, 3, 6, 1, 4, 1, 25506, 9, 1, 2, 0, 4)).setObjects(("ENTITY-MIB", "entPhysicalAssetID"), ("HH3C-VM-MAN-MIB", "hh3cVMManRegDevIP"), ("HH3C-VM-MAN-MIB", "hh3cVMManRegDevName"), ("HH3C-VM-MAN-MIB", "hh3cVMManPUECVideoChannelName"))
if mibBuilder.loadTexts: hh3cVMManForwardDeviceVideoLossTrap.setStatus('current')
if mibBuilder.loadTexts: hh3cVMManForwardDeviceVideoLossTrap.setDescription('Forward a trap about video loss, which is created by the third party device.')
hh3cVMManForwardDeviceVideoRecoverTrap = NotificationType((1, 3, 6, 1, 4, 1, 25506, 9, 1, 2, 0, 5)).setObjects(("ENTITY-MIB", "entPhysicalAssetID"), ("HH3C-VM-MAN-MIB", "hh3cVMManRegDevIP"), ("HH3C-VM-MAN-MIB", "hh3cVMManRegDevName"), ("HH3C-VM-MAN-MIB", "hh3cVMManPUECVideoChannelName"))
if mibBuilder.loadTexts: hh3cVMManForwardDeviceVideoRecoverTrap.setStatus('current')
if mibBuilder.loadTexts: hh3cVMManForwardDeviceVideoRecoverTrap.setDescription('Forward a trap about video recovery after loss, which is created by the third party device.')
hh3cVMManForwardDeviceMotionDetectTrap = NotificationType((1, 3, 6, 1, 4, 1, 25506, 9, 1, 2, 0, 6)).setObjects(("ENTITY-MIB", "entPhysicalAssetID"), ("HH3C-VM-MAN-MIB", "hh3cVMManRegDevIP"), ("HH3C-VM-MAN-MIB", "hh3cVMManRegDevName"), ("HH3C-VM-MAN-MIB", "hh3cVMManPUECVideoChannelName"), ("HH3C-VM-MAN-MIB", "hh3cVMManRegionCoordinateX1"), ("HH3C-VM-MAN-MIB", "hh3cVMManRegionCoordinateY1"), ("HH3C-VM-MAN-MIB", "hh3cVMManRegionCoordinateX2"), ("HH3C-VM-MAN-MIB", "hh3cVMManRegionCoordinateY2"))
if mibBuilder.loadTexts: hh3cVMManForwardDeviceMotionDetectTrap.setStatus('current')
if mibBuilder.loadTexts: hh3cVMManForwardDeviceMotionDetectTrap.setDescription('Forward a trap about motion detection, which is created by the third party device.')
hh3cVMManForwardDeviceCoverTrap = NotificationType((1, 3, 6, 1, 4, 1, 25506, 9, 1, 2, 0, 7)).setObjects(("ENTITY-MIB", "entPhysicalAssetID"), ("HH3C-VM-MAN-MIB", "hh3cVMManRegDevIP"), ("HH3C-VM-MAN-MIB", "hh3cVMManRegDevName"), ("HH3C-VM-MAN-MIB", "hh3cVMManPUECVideoChannelName"), ("HH3C-VM-MAN-MIB", "hh3cVMManRegionCoordinateX1"), ("HH3C-VM-MAN-MIB", "hh3cVMManRegionCoordinateY1"), ("HH3C-VM-MAN-MIB", "hh3cVMManRegionCoordinateX2"), ("HH3C-VM-MAN-MIB", "hh3cVMManRegionCoordinateY2"))
if mibBuilder.loadTexts: hh3cVMManForwardDeviceCoverTrap.setStatus('current')
if mibBuilder.loadTexts: hh3cVMManForwardDeviceCoverTrap.setDescription('Forward a trap about video cover, which is created by the third party device.')
hh3cVMManForwardDeviceCpuUsageThresholdTrap = NotificationType((1, 3, 6, 1, 4, 1, 25506, 9, 1, 2, 0, 8)).setObjects(("ENTITY-MIB", "entPhysicalAssetID"), ("HH3C-VM-MAN-MIB", "hh3cVMManRegDevIP"), ("HH3C-VM-MAN-MIB", "hh3cVMManRegDevName"), ("HH3C-VM-MAN-MIB", "hh3cVMManCpuUsage"), ("HH3C-VM-MAN-MIB", "hh3cVMManCpuUsageThreshold"))
if mibBuilder.loadTexts: hh3cVMManForwardDeviceCpuUsageThresholdTrap.setStatus('current')
if mibBuilder.loadTexts: hh3cVMManForwardDeviceCpuUsageThresholdTrap.setDescription('Forward a trap about cpu usage exceeding its threshold, which is created by the third party device.')
hh3cVMManForwardDeviceMemUsageThresholdTrap = NotificationType((1, 3, 6, 1, 4, 1, 25506, 9, 1, 2, 0, 9)).setObjects(("ENTITY-MIB", "entPhysicalAssetID"), ("HH3C-VM-MAN-MIB", "hh3cVMManRegDevIP"), ("HH3C-VM-MAN-MIB", "hh3cVMManRegDevName"), ("HH3C-VM-MAN-MIB", "hh3cVMManMemUsage"), ("HH3C-VM-MAN-MIB", "hh3cVMManMemUsageThreshold"))
if mibBuilder.loadTexts: hh3cVMManForwardDeviceMemUsageThresholdTrap.setStatus('current')
if mibBuilder.loadTexts: hh3cVMManForwardDeviceMemUsageThresholdTrap.setDescription('Forward a trap about memory usage exceeding its threshold, which is created by the third party device.')
hh3cVMManForwardDeviceHardDiskUsageThresholdTrap = NotificationType((1, 3, 6, 1, 4, 1, 25506, 9, 1, 2, 0, 10)).setObjects(("ENTITY-MIB", "entPhysicalAssetID"), ("HH3C-VM-MAN-MIB", "hh3cVMManRegDevIP"), ("HH3C-VM-MAN-MIB", "hh3cVMManRegDevName"), ("HH3C-VM-MAN-MIB", "hh3cVMManHardDiskUsage"), ("HH3C-VM-MAN-MIB", "hh3cVMManHardDiskUsageThreshold"))
if mibBuilder.loadTexts: hh3cVMManForwardDeviceHardDiskUsageThresholdTrap.setStatus('current')
if mibBuilder.loadTexts: hh3cVMManForwardDeviceHardDiskUsageThresholdTrap.setDescription('Forward a trap about harddisk usage exceeding its threshold, which is created by the third party device.')
hh3cVMManForwardDeviceTemperatureThresholdTrap = NotificationType((1, 3, 6, 1, 4, 1, 25506, 9, 1, 2, 0, 11)).setObjects(("ENTITY-MIB", "entPhysicalAssetID"), ("HH3C-VM-MAN-MIB", "hh3cVMManRegDevIP"), ("HH3C-VM-MAN-MIB", "hh3cVMManRegDevName"), ("HH3C-VM-MAN-MIB", "hh3cVMManTemperature"), ("HH3C-VM-MAN-MIB", "hh3cVMManTemperatureThreshold"))
if mibBuilder.loadTexts: hh3cVMManForwardDeviceTemperatureThresholdTrap.setStatus('current')
if mibBuilder.loadTexts: hh3cVMManForwardDeviceTemperatureThresholdTrap.setDescription('Forward a trap about temperature exceeding its threshold, which is created by the third party device.')
hh3cVMManForwardDeviceStartKinescopeTrap = NotificationType((1, 3, 6, 1, 4, 1, 25506, 9, 1, 2, 0, 12)).setObjects(("ENTITY-MIB", "entPhysicalAssetID"), ("HH3C-VM-MAN-MIB", "hh3cVMManRegDevIP"), ("HH3C-VM-MAN-MIB", "hh3cVMManRegDevName"), ("HH3C-VM-MAN-MIB", "hh3cVMManPUECVideoChannelName"))
if mibBuilder.loadTexts: hh3cVMManForwardDeviceStartKinescopeTrap.setStatus('current')
if mibBuilder.loadTexts: hh3cVMManForwardDeviceStartKinescopeTrap.setDescription('Forward a trap about starting kinescope, which is created by the third party device.')
hh3cVMManForwardDeviceStopKinescopeTrap = NotificationType((1, 3, 6, 1, 4, 1, 25506, 9, 1, 2, 0, 13)).setObjects(("ENTITY-MIB", "entPhysicalAssetID"), ("HH3C-VM-MAN-MIB", "hh3cVMManRegDevIP"), ("HH3C-VM-MAN-MIB", "hh3cVMManRegDevName"), ("HH3C-VM-MAN-MIB", "hh3cVMManPUECVideoChannelName"))
if mibBuilder.loadTexts: hh3cVMManForwardDeviceStopKinescopeTrap.setStatus('current')
if mibBuilder.loadTexts: hh3cVMManForwardDeviceStopKinescopeTrap.setDescription('Forward a trap about stopping kinescope, which is created by the third party device.')
hh3cVMManClientReportTrap = NotificationType((1, 3, 6, 1, 4, 1, 25506, 9, 1, 2, 0, 14)).setObjects(("ENTITY-MIB", "entPhysicalAssetID"), ("HH3C-VM-MAN-MIB", "hh3cVMManClientIP"), ("HH3C-VM-MAN-MIB", "hh3cVMManUserName"), ("HH3C-VM-MAN-MIB", "hh3cVMManReportContent"))
if mibBuilder.loadTexts: hh3cVMManClientReportTrap.setStatus('current')
if mibBuilder.loadTexts: hh3cVMManClientReportTrap.setDescription('Send a trap about the fault which is reported by clients.')
hh3cVMManClientRealtimeSurveillanceNoVideoTrap = NotificationType((1, 3, 6, 1, 4, 1, 25506, 9, 1, 2, 0, 15)).setObjects(("ENTITY-MIB", "entPhysicalAssetID"), ("HH3C-VM-MAN-MIB", "hh3cVMManClientIP"), ("HH3C-VM-MAN-MIB", "hh3cVMManUserName"), ("HH3C-VM-MAN-MIB", "hh3cVMManRegDevIP"), ("HH3C-VM-MAN-MIB", "hh3cVMManRegDevName"), ("HH3C-VM-MAN-MIB", "hh3cVMManPUECVideoChannelName"))
if mibBuilder.loadTexts: hh3cVMManClientRealtimeSurveillanceNoVideoTrap.setStatus('current')
if mibBuilder.loadTexts: hh3cVMManClientRealtimeSurveillanceNoVideoTrap.setDescription("Send a trap about no realtime surveillance video stream which is reported by clients. hh3cVMManRegDevIP, entPhysicalAssetID, hh3cVMManRegDevName and hh3cVMManPUECVideoChannelName describe an EC's relative information. ")
hh3cVMManClientVODNoVideoTrap = NotificationType((1, 3, 6, 1, 4, 1, 25506, 9, 1, 2, 0, 16)).setObjects(("ENTITY-MIB", "entPhysicalAssetID"), ("HH3C-VM-MAN-MIB", "hh3cVMManClientIP"), ("HH3C-VM-MAN-MIB", "hh3cVMManUserName"), ("HH3C-VM-MAN-MIB", "hh3cVMManRegDevIP"), ("HH3C-VM-MAN-MIB", "hh3cVMManRegDevName"), ("HH3C-VM-MAN-MIB", "hh3cVMManPUECVideoChannelName"), ("HH3C-VM-MAN-MIB", "hh3cVMManClientVODStart"), ("HH3C-VM-MAN-MIB", "hh3cVMManClientVODEnd"), ("HH3C-VM-MAN-MIB", "hh3cVMManIPSANDevIP"))
if mibBuilder.loadTexts: hh3cVMManClientVODNoVideoTrap.setStatus('current')
if mibBuilder.loadTexts: hh3cVMManClientVODNoVideoTrap.setDescription("Send a trap about no VOD video stream which is reported by clients. hh3cVMManRegDevIP, entPhysicalAssetID, hh3cVMManRegDevName and hh3cVMManPUECVideoChannelName describe an EC's relative information.")
hh3cVMManClientRealtimeSurveillanceVideoStreamDiscontinuityTrap = NotificationType((1, 3, 6, 1, 4, 1, 25506, 9, 1, 2, 0, 17)).setObjects(("ENTITY-MIB", "entPhysicalAssetID"), ("HH3C-VM-MAN-MIB", "hh3cVMManClientIP"), ("HH3C-VM-MAN-MIB", "hh3cVMManUserName"), ("HH3C-VM-MAN-MIB", "hh3cVMManRegDevIP"), ("HH3C-VM-MAN-MIB", "hh3cVMManRegDevName"), ("HH3C-VM-MAN-MIB", "hh3cVMManPUECVideoChannelName"), ("HH3C-VM-MAN-MIB", "hh3cVMManClientVideoStreamDiscontinuityInterval"), ("HH3C-VM-MAN-MIB", "hh3cVMManClientVideoStreamDiscontinuityIntervalThreshold"), ("HH3C-VM-MAN-MIB", "hh3cVMManClientStatPeriod"))
if mibBuilder.loadTexts: hh3cVMManClientRealtimeSurveillanceVideoStreamDiscontinuityTrap.setStatus('current')
if mibBuilder.loadTexts: hh3cVMManClientRealtimeSurveillanceVideoStreamDiscontinuityTrap.setDescription("Send a trap about the realtime surveillance video stream discontinuity which is reported by clients. entPhysicalAssetID, hh3cVMManRegDevIP, hh3cVMManRegDevName and hh3cVMManPUECVideoChannelName describe an EC's relative information.")
hh3cVMManClientVODVideoStreamDiscontinuityTrap = NotificationType((1, 3, 6, 1, 4, 1, 25506, 9, 1, 2, 0, 18)).setObjects(("ENTITY-MIB", "entPhysicalAssetID"), ("HH3C-VM-MAN-MIB", "hh3cVMManClientIP"), ("HH3C-VM-MAN-MIB", "hh3cVMManUserName"), ("HH3C-VM-MAN-MIB", "hh3cVMManRegDevIP"), ("HH3C-VM-MAN-MIB", "hh3cVMManRegDevName"), ("HH3C-VM-MAN-MIB", "hh3cVMManPUECVideoChannelName"), ("HH3C-VM-MAN-MIB", "hh3cVMManClientVODStart"), ("HH3C-VM-MAN-MIB", "hh3cVMManClientVODEnd"), ("HH3C-VM-MAN-MIB", "hh3cVMManIPSANDevIP"), ("HH3C-VM-MAN-MIB", "hh3cVMManClientVideoStreamDiscontinuityInterval"), ("HH3C-VM-MAN-MIB", "hh3cVMManClientVideoStreamDiscontinuityIntervalThreshold"), ("HH3C-VM-MAN-MIB", "hh3cVMManClientStatPeriod"))
if mibBuilder.loadTexts: hh3cVMManClientVODVideoStreamDiscontinuityTrap.setStatus('current')
if mibBuilder.loadTexts: hh3cVMManClientVODVideoStreamDiscontinuityTrap.setDescription("Send a trap about the VOD video stream discontinuity which is reported by clients. hh3cVMManRegDevIP, entPhysicalAssetID, hh3cVMManRegDevName and hh3cVMManPUECVideoChannelName describe an EC's relative information.")
hh3cVMManClientCtlConnExceptionTerminationTrap = NotificationType((1, 3, 6, 1, 4, 1, 25506, 9, 1, 2, 0, 19)).setObjects(("ENTITY-MIB", "entPhysicalAssetID"), ("HH3C-VM-MAN-MIB", "hh3cVMManClientIP"), ("HH3C-VM-MAN-MIB", "hh3cVMManUserName"))
if mibBuilder.loadTexts: hh3cVMManClientCtlConnExceptionTerminationTrap.setStatus('current')
if mibBuilder.loadTexts: hh3cVMManClientCtlConnExceptionTerminationTrap.setDescription('Send a trap about the exceptional termination for control connection. ')
hh3cVMManClientFrequencyLoginFailTrap = NotificationType((1, 3, 6, 1, 4, 1, 25506, 9, 1, 2, 0, 20)).setObjects(("ENTITY-MIB", "entPhysicalAssetID"), ("HH3C-VM-MAN-MIB", "hh3cVMManClientIP"), ("HH3C-VM-MAN-MIB", "hh3cVMManUserName"), ("HH3C-VM-MAN-MIB", "hh3cVMManClientLoginFailNum"), ("HH3C-VM-MAN-MIB", "hh3cVMManClientLoginFailNumThreshold"), ("HH3C-VM-MAN-MIB", "hh3cVMManClientStatPeriod"))
if mibBuilder.loadTexts: hh3cVMManClientFrequencyLoginFailTrap.setStatus('current')
if mibBuilder.loadTexts: hh3cVMManClientFrequencyLoginFailTrap.setDescription('Send a trap about the frequency of client login failure.')
hh3cVMManClientFrequencyVODFailTrap = NotificationType((1, 3, 6, 1, 4, 1, 25506, 9, 1, 2, 0, 21)).setObjects(("ENTITY-MIB", "entPhysicalAssetID"), ("HH3C-VM-MAN-MIB", "hh3cVMManClientIP"), ("HH3C-VM-MAN-MIB", "hh3cVMManUserName"), ("HH3C-VM-MAN-MIB", "hh3cVMManClientVODFailNum"), ("HH3C-VM-MAN-MIB", "hh3cVMManClientVODFailNumThreshold"), ("HH3C-VM-MAN-MIB", "hh3cVMManClientStatPeriod"))
if mibBuilder.loadTexts: hh3cVMManClientFrequencyVODFailTrap.setStatus('current')
if mibBuilder.loadTexts: hh3cVMManClientFrequencyVODFailTrap.setDescription('Send a trap about the frequency of client VOD failure.')
hh3cVMManDMECDisobeyStorageScheduleTrap = NotificationType((1, 3, 6, 1, 4, 1, 25506, 9, 1, 2, 0, 22)).setObjects(("ENTITY-MIB", "entPhysicalAssetID"), ("HH3C-VM-MAN-MIB", "hh3cVMManRegDevIP"), ("HH3C-VM-MAN-MIB", "hh3cVMManPUECVideoChannelName"))
if mibBuilder.loadTexts: hh3cVMManDMECDisobeyStorageScheduleTrap.setStatus('current')
if mibBuilder.loadTexts: hh3cVMManDMECDisobeyStorageScheduleTrap.setDescription('Send a trap about EC disobeying storage schedule created by DM.')
hh3cVMManDMECDisobeyStorageScheduleRecoverTrap = NotificationType((1, 3, 6, 1, 4, 1, 25506, 9, 1, 2, 0, 23)).setObjects(("ENTITY-MIB", "entPhysicalAssetID"), ("HH3C-VM-MAN-MIB", "hh3cVMManRegDevIP"), ("HH3C-VM-MAN-MIB", "hh3cVMManPUECVideoChannelName"))
if mibBuilder.loadTexts: hh3cVMManDMECDisobeyStorageScheduleRecoverTrap.setStatus('current')
if mibBuilder.loadTexts: hh3cVMManDMECDisobeyStorageScheduleRecoverTrap.setDescription('Send a trap about recovery after EC disobeying storage schedule created by DM.')
hh3cVMManTrapObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 9, 1, 2, 1))
hh3cVMManIPSANDevIP = MibScalar((1, 3, 6, 1, 4, 1, 25506, 9, 1, 2, 1, 1), IpAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cVMManIPSANDevIP.setStatus('current')
if mibBuilder.loadTexts: hh3cVMManIPSANDevIP.setDescription('IP address of IPSAN Device which can store video data.')
hh3cVMManRegDevIP = MibScalar((1, 3, 6, 1, 4, 1, 25506, 9, 1, 2, 1, 2), IpAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cVMManRegDevIP.setStatus('current')
if mibBuilder.loadTexts: hh3cVMManRegDevIP.setDescription('IP address of devices which can registered or unregistered to VM.')
hh3cVMManRegDevName = MibScalar((1, 3, 6, 1, 4, 1, 25506, 9, 1, 2, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cVMManRegDevName.setStatus('current')
if mibBuilder.loadTexts: hh3cVMManRegDevName.setDescription('Name of devices which can registered or unregistered to VM.')
hh3cVMManRegionCoordinateX1 = MibScalar((1, 3, 6, 1, 4, 1, 25506, 9, 1, 2, 1, 4), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cVMManRegionCoordinateX1.setStatus('current')
if mibBuilder.loadTexts: hh3cVMManRegionCoordinateX1.setDescription('The horizontal coordinate of top left point of the motion detection region.')
hh3cVMManRegionCoordinateY1 = MibScalar((1, 3, 6, 1, 4, 1, 25506, 9, 1, 2, 1, 5), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cVMManRegionCoordinateY1.setStatus('current')
if mibBuilder.loadTexts: hh3cVMManRegionCoordinateY1.setDescription('The vertical coordinate of top left point of the motion detection region.')
hh3cVMManRegionCoordinateX2 = MibScalar((1, 3, 6, 1, 4, 1, 25506, 9, 1, 2, 1, 6), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cVMManRegionCoordinateX2.setStatus('current')
if mibBuilder.loadTexts: hh3cVMManRegionCoordinateX2.setDescription('The horizontal coordinate of botton right point of the motion detection region.')
hh3cVMManRegionCoordinateY2 = MibScalar((1, 3, 6, 1, 4, 1, 25506, 9, 1, 2, 1, 7), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cVMManRegionCoordinateY2.setStatus('current')
if mibBuilder.loadTexts: hh3cVMManRegionCoordinateY2.setDescription('The horizontal coordinate of botton right point of the motion detection region.')
hh3cVMManCpuUsage = MibScalar((1, 3, 6, 1, 4, 1, 25506, 9, 1, 2, 1, 8), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cVMManCpuUsage.setStatus('current')
if mibBuilder.loadTexts: hh3cVMManCpuUsage.setDescription('The CPU usage for this entity. Generally, the CPU usage will caculate the overall CPU usage on the entity, and it is not sensible with the number of CPU on the entity. ')
hh3cVMManCpuUsageThreshold = MibScalar((1, 3, 6, 1, 4, 1, 25506, 9, 1, 2, 1, 9), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cVMManCpuUsageThreshold.setStatus('current')
if mibBuilder.loadTexts: hh3cVMManCpuUsageThreshold.setDescription('The threshold for the CPU usage. When the CPU usage exceeds the threshold, a notification will be sent.')
hh3cVMManMemUsage = MibScalar((1, 3, 6, 1, 4, 1, 25506, 9, 1, 2, 1, 10), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cVMManMemUsage.setStatus('current')
if mibBuilder.loadTexts: hh3cVMManMemUsage.setDescription('The memory usage for the entity. This object indicates what percent of memory are used. ')
hh3cVMManMemUsageThreshold = MibScalar((1, 3, 6, 1, 4, 1, 25506, 9, 1, 2, 1, 11), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cVMManMemUsageThreshold.setStatus('current')
if mibBuilder.loadTexts: hh3cVMManMemUsageThreshold.setDescription('The threshold for the Memory usage. When the memory usage exceeds the threshold, a notification will be sent. ')
hh3cVMManHardDiskUsage = MibScalar((1, 3, 6, 1, 4, 1, 25506, 9, 1, 2, 1, 12), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cVMManHardDiskUsage.setStatus('current')
if mibBuilder.loadTexts: hh3cVMManHardDiskUsage.setDescription('The hard disk usage for the entity. This object indicates what percent of hard disk are used. ')
hh3cVMManHardDiskUsageThreshold = MibScalar((1, 3, 6, 1, 4, 1, 25506, 9, 1, 2, 1, 13), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cVMManHardDiskUsageThreshold.setStatus('current')
if mibBuilder.loadTexts: hh3cVMManHardDiskUsageThreshold.setDescription('The threshold for the hard disk usage. When the hard disk usage exceeds the threshold, a notification will be sent. ')
hh3cVMManTemperature = MibScalar((1, 3, 6, 1, 4, 1, 25506, 9, 1, 2, 1, 14), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cVMManTemperature.setStatus('current')
if mibBuilder.loadTexts: hh3cVMManTemperature.setDescription('The temperature for the entity. ')
hh3cVMManTemperatureThreshold = MibScalar((1, 3, 6, 1, 4, 1, 25506, 9, 1, 2, 1, 15), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cVMManTemperatureThreshold.setStatus('current')
if mibBuilder.loadTexts: hh3cVMManTemperatureThreshold.setDescription('The threshold for the temperature. When the temperature exceeds the threshold, a notification will be sent. ')
hh3cVMManClientIP = MibScalar((1, 3, 6, 1, 4, 1, 25506, 9, 1, 2, 1, 16), IpAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cVMManClientIP.setStatus('current')
if mibBuilder.loadTexts: hh3cVMManClientIP.setDescription('The client device IP address.')
hh3cVMManUserName = MibScalar((1, 3, 6, 1, 4, 1, 25506, 9, 1, 2, 1, 17), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cVMManUserName.setStatus('current')
if mibBuilder.loadTexts: hh3cVMManUserName.setDescription('The client user name.')
hh3cVMManReportContent = MibScalar((1, 3, 6, 1, 4, 1, 25506, 9, 1, 2, 1, 18), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cVMManReportContent.setStatus('current')
if mibBuilder.loadTexts: hh3cVMManReportContent.setDescription('The details of the fault which reported by clients')
hh3cVMManClientVideoStreamDiscontinuityInterval = MibScalar((1, 3, 6, 1, 4, 1, 25506, 9, 1, 2, 1, 19), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cVMManClientVideoStreamDiscontinuityInterval.setStatus('current')
if mibBuilder.loadTexts: hh3cVMManClientVideoStreamDiscontinuityInterval.setDescription('Video stream discontinuity interval. ')
hh3cVMManClientVideoStreamDiscontinuityIntervalThreshold = MibScalar((1, 3, 6, 1, 4, 1, 25506, 9, 1, 2, 1, 20), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cVMManClientVideoStreamDiscontinuityIntervalThreshold.setStatus('current')
if mibBuilder.loadTexts: hh3cVMManClientVideoStreamDiscontinuityIntervalThreshold.setDescription('The threshold for the video stream discontinuity interval. When the discontinuity interval exceeds the threshold, a notification will be sent. ')
hh3cVMManClientStatPeriod = MibScalar((1, 3, 6, 1, 4, 1, 25506, 9, 1, 2, 1, 21), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cVMManClientStatPeriod.setStatus('current')
if mibBuilder.loadTexts: hh3cVMManClientStatPeriod.setDescription('The client statistic period. ')
hh3cVMManClientLoginFailNum = MibScalar((1, 3, 6, 1, 4, 1, 25506, 9, 1, 2, 1, 22), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cVMManClientLoginFailNum.setStatus('current')
if mibBuilder.loadTexts: hh3cVMManClientLoginFailNum.setDescription('The total number of client login failure in last statistic period which is defined by hh3cVMManClientStatPeriod entity.')
hh3cVMManClientLoginFailNumThreshold = MibScalar((1, 3, 6, 1, 4, 1, 25506, 9, 1, 2, 1, 23), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cVMManClientLoginFailNumThreshold.setStatus('current')
if mibBuilder.loadTexts: hh3cVMManClientLoginFailNumThreshold.setDescription('The threshold for the total number of client login failure in last statistic period. When the number exceeds the threshold, a notification will be sent. ')
hh3cVMManClientVODFailNum = MibScalar((1, 3, 6, 1, 4, 1, 25506, 9, 1, 2, 1, 24), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cVMManClientVODFailNum.setStatus('current')
if mibBuilder.loadTexts: hh3cVMManClientVODFailNum.setDescription('The total number of client VOD failure in last statistic period which is defined by hh3cVMManClientStatPeriod entity.')
hh3cVMManClientVODFailNumThreshold = MibScalar((1, 3, 6, 1, 4, 1, 25506, 9, 1, 2, 1, 25), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cVMManClientVODFailNumThreshold.setStatus('current')
if mibBuilder.loadTexts: hh3cVMManClientVODFailNumThreshold.setDescription('The threshold for the total number of client VOD failure in last statistic period. When the number exceeds the threshold, a notification will be sent. ')
hh3cVMManClientVODStart = MibScalar((1, 3, 6, 1, 4, 1, 25506, 9, 1, 2, 1, 26), DateAndTime()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cVMManClientVODStart.setStatus('current')
if mibBuilder.loadTexts: hh3cVMManClientVODStart.setDescription('The start time for VOD.')
hh3cVMManClientVODEnd = MibScalar((1, 3, 6, 1, 4, 1, 25506, 9, 1, 2, 1, 27), DateAndTime()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cVMManClientVODEnd.setStatus('current')
if mibBuilder.loadTexts: hh3cVMManClientVODEnd.setDescription('The end time for VOD.')
hh3cVMManPUExternalInputAlarmChannelID = MibScalar((1, 3, 6, 1, 4, 1, 25506, 9, 1, 2, 1, 28), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cVMManPUExternalInputAlarmChannelID.setStatus('current')
if mibBuilder.loadTexts: hh3cVMManPUExternalInputAlarmChannelID.setDescription('The ID of the external input alarm channel.')
hh3cVMManPUECVideoChannelName = MibScalar((1, 3, 6, 1, 4, 1, 25506, 9, 1, 2, 1, 29), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cVMManPUECVideoChannelName.setStatus('current')
if mibBuilder.loadTexts: hh3cVMManPUECVideoChannelName.setDescription('The name of the video channel. It is suggested that the name includes the channel ID information.')
mibBuilder.exportSymbols("HH3C-VM-MAN-MIB", hh3cVMManPUExternalInputAlarmChannelID=hh3cVMManPUExternalInputAlarmChannelID, hh3cVMManClientVODEnd=hh3cVMManClientVODEnd, hh3cVMManDMECDisobeyStorageScheduleRecoverTrap=hh3cVMManDMECDisobeyStorageScheduleRecoverTrap, hh3cVMManDeviceOfflineTrap=hh3cVMManDeviceOfflineTrap, hh3cVMManIPSANDevIP=hh3cVMManIPSANDevIP, hh3cVMManTemperatureThreshold=hh3cVMManTemperatureThreshold, hh3cVMManClientStatPeriod=hh3cVMManClientStatPeriod, hh3cVMManForwardDeviceCpuUsageThresholdTrap=hh3cVMManForwardDeviceCpuUsageThresholdTrap, hh3cVMManClientRealtimeSurveillanceNoVideoTrap=hh3cVMManClientRealtimeSurveillanceNoVideoTrap, hh3cVMManClientVODFailNumThreshold=hh3cVMManClientVODFailNumThreshold, hh3cVMMan=hh3cVMMan, hh3cVMStatFailConnEstablishRequests=hh3cVMStatFailConnEstablishRequests, hh3cVMStatTotalConnEstablishRequests=hh3cVMStatTotalConnEstablishRequests, hh3cVMStat=hh3cVMStat, hh3cVMStatSuccConnEstablishRequests=hh3cVMStatSuccConnEstablishRequests, hh3cVMStatExceptionTerminationConn=hh3cVMStatExceptionTerminationConn, hh3cVMManForwardDeviceExternalSemaphoreTrap=hh3cVMManForwardDeviceExternalSemaphoreTrap, hh3cVMManForwardDeviceStopKinescopeTrap=hh3cVMManForwardDeviceStopKinescopeTrap, hh3cVMManClientRealtimeSurveillanceVideoStreamDiscontinuityTrap=hh3cVMManClientRealtimeSurveillanceVideoStreamDiscontinuityTrap, hh3cVMManCpuUsageThreshold=hh3cVMManCpuUsageThreshold, hh3cVMManUserName=hh3cVMManUserName, hh3cVMManClientFrequencyLoginFailTrap=hh3cVMManClientFrequencyLoginFailTrap, hh3cVMManReportContent=hh3cVMManReportContent, hh3cVMManPUECVideoChannelName=hh3cVMManPUECVideoChannelName, hh3cVMStatFailConnReleaseRequests=hh3cVMStatFailConnReleaseRequests, hh3cVMManForwardDeviceMotionDetectTrap=hh3cVMManForwardDeviceMotionDetectTrap, hh3cVMManForwardDeviceHardDiskUsageThresholdTrap=hh3cVMManForwardDeviceHardDiskUsageThresholdTrap, hh3cVMManTrapPrex=hh3cVMManTrapPrex, hh3cVMStatTotalConnReleaseRequests=hh3cVMStatTotalConnReleaseRequests, hh3cVMManForwardDeviceStartKinescopeTrap=hh3cVMManForwardDeviceStartKinescopeTrap, hh3cVMManClientVODNoVideoTrap=hh3cVMManClientVODNoVideoTrap, hh3cVMManRegionCoordinateY2=hh3cVMManRegionCoordinateY2, hh3cVMManCpuUsage=hh3cVMManCpuUsage, hh3cVMManClientVideoStreamDiscontinuityIntervalThreshold=hh3cVMManClientVideoStreamDiscontinuityIntervalThreshold, hh3cVMManClientVODStart=hh3cVMManClientVODStart, hh3cVMManMIBTrap=hh3cVMManMIBTrap, hh3cVMCapabilitySet=hh3cVMCapabilitySet, hh3cVMManRegionCoordinateY1=hh3cVMManRegionCoordinateY1, hh3cVMManMIBObjects=hh3cVMManMIBObjects, hh3cVMManForwardDeviceTemperatureThresholdTrap=hh3cVMManForwardDeviceTemperatureThresholdTrap, hh3cVMManClientCtlConnExceptionTerminationTrap=hh3cVMManClientCtlConnExceptionTerminationTrap, hh3cVMManForwardDeviceMemUsageThresholdTrap=hh3cVMManForwardDeviceMemUsageThresholdTrap, hh3cVMManClientFrequencyVODFailTrap=hh3cVMManClientFrequencyVODFailTrap, hh3cVMManDMECDisobeyStorageScheduleTrap=hh3cVMManDMECDisobeyStorageScheduleTrap, hh3cVMManRegDevIP=hh3cVMManRegDevIP, hh3cVMManMemUsage=hh3cVMManMemUsage, hh3cVMManTemperature=hh3cVMManTemperature, hh3cVMManClientLoginFailNumThreshold=hh3cVMManClientLoginFailNumThreshold, hh3cVMManClientVODFailNum=hh3cVMManClientVODFailNum, hh3cVMManClientReportTrap=hh3cVMManClientReportTrap, hh3cVMManHardDiskUsage=hh3cVMManHardDiskUsage, hh3cVMManDeviceOnlineTrap=hh3cVMManDeviceOnlineTrap, hh3cVMManForwardDeviceVideoLossTrap=hh3cVMManForwardDeviceVideoLossTrap, hh3cVMManClientLoginFailNum=hh3cVMManClientLoginFailNum, hh3cVMManRegionCoordinateX1=hh3cVMManRegionCoordinateX1, hh3cVMManRegDevName=hh3cVMManRegDevName, hh3cVMManClientIP=hh3cVMManClientIP, PYSNMP_MODULE_ID=hh3cVMMan, hh3cVMManClientVODVideoStreamDiscontinuityTrap=hh3cVMManClientVODVideoStreamDiscontinuityTrap, hh3cVMManTrapObjects=hh3cVMManTrapObjects, hh3cVMManClientVideoStreamDiscontinuityInterval=hh3cVMManClientVideoStreamDiscontinuityInterval, hh3cVMManForwardDeviceCoverTrap=hh3cVMManForwardDeviceCoverTrap, hh3cVMManRegionCoordinateX2=hh3cVMManRegionCoordinateX2, hh3cVMStatSuccConnReleaseRequests=hh3cVMStatSuccConnReleaseRequests, hh3cVMManMemUsageThreshold=hh3cVMManMemUsageThreshold, hh3cVMManHardDiskUsageThreshold=hh3cVMManHardDiskUsageThreshold, hh3cVMManForwardDeviceVideoRecoverTrap=hh3cVMManForwardDeviceVideoRecoverTrap)
