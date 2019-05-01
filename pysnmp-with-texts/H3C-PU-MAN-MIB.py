#
# PySNMP MIB module H3C-PU-MAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/H3C-PU-MAN-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:23:32 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
h3cSurveillanceMIB, = mibBuilder.importSymbols("HUAWEI-3COM-OID-MIB", "h3cSurveillanceMIB")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, NotificationType, Bits, IpAddress, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ObjectIdentity, MibIdentifier, Gauge32, Integer32, Unsigned32, iso, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "NotificationType", "Bits", "IpAddress", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ObjectIdentity", "MibIdentifier", "Gauge32", "Integer32", "Unsigned32", "iso", "Counter32")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
h3cPUMan = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 10, 9, 2))
if mibBuilder.loadTexts: h3cPUMan.setLastUpdated('200709050000Z')
if mibBuilder.loadTexts: h3cPUMan.setOrganization('H3C Technologies Co., Ltd.')
if mibBuilder.loadTexts: h3cPUMan.setContactInfo('Surveillance Network Management Team H3C Technologies Co.,Ltd. East-Com Information Industry Base, Bing-Jiang District Hangzhou P.R. China http://www.h3c.com Zip:100085')
if mibBuilder.loadTexts: h3cPUMan.setDescription('The PU includes those device like EC(Encoder), DC(Decoder) and ECR(Encoder Recorder). The PU will survey the remote video and audio. This MIB is defined to manage the PU as our private MIB node according to its specific capability.')
h3cPUCommonMan = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 9, 2, 1))
h3cPUCommonManObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 9, 2, 1, 1))
h3cPUisOnline = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 9, 2, 1, 1, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cPUisOnline.setStatus('current')
if mibBuilder.loadTexts: h3cPUisOnline.setDescription('The PU online status indicates whether the PU is normally registered into the VM. True indicates that the PU is normally registered into the VM.')
h3cPUCMSAddr = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 9, 2, 1, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cPUCMSAddr.setStatus('current')
if mibBuilder.loadTexts: h3cPUCMSAddr.setDescription('The IP address of the CMS. All zero address indicates the CMS address is not configured.')
h3cPUVersionServerAddr = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 9, 2, 1, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cPUVersionServerAddr.setStatus('current')
if mibBuilder.loadTexts: h3cPUVersionServerAddr.setDescription('The IP address of the version server. All zero address indicates the version server is not configured or does not support remote upgrade.')
h3cPUCommonManTables = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 9, 2, 1, 2))
h3cPUExternalInputAlarmTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 9, 2, 1, 2, 1), )
if mibBuilder.loadTexts: h3cPUExternalInputAlarmTable.setStatus('current')
if mibBuilder.loadTexts: h3cPUExternalInputAlarmTable.setDescription('External input alarm table')
h3cPUExternalInputAlarmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 9, 2, 1, 2, 1, 1), ).setIndexNames((0, "H3C-PU-MAN-MIB", "h3cPUExternalInputAlarmChannelID"))
if mibBuilder.loadTexts: h3cPUExternalInputAlarmEntry.setStatus('current')
if mibBuilder.loadTexts: h3cPUExternalInputAlarmEntry.setDescription('External input alarm entry')
h3cPUExternalInputAlarmChannelID = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 9, 2, 1, 2, 1, 1, 1), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: h3cPUExternalInputAlarmChannelID.setStatus('current')
if mibBuilder.loadTexts: h3cPUExternalInputAlarmChannelID.setDescription('The ID of the external input alarm channel.')
h3cPUExternalInputAlarmStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 9, 2, 1, 2, 1, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cPUExternalInputAlarmStatus.setStatus('current')
if mibBuilder.loadTexts: h3cPUExternalInputAlarmStatus.setDescription('True indicates that the current channel has alarm.')
h3cPUExternalOutputAlarmTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 9, 2, 1, 2, 2), )
if mibBuilder.loadTexts: h3cPUExternalOutputAlarmTable.setStatus('current')
if mibBuilder.loadTexts: h3cPUExternalOutputAlarmTable.setDescription('External output alarm table')
h3cPUExternalOutputAlarmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 9, 2, 1, 2, 2, 1), ).setIndexNames((0, "H3C-PU-MAN-MIB", "h3cPUExternalOutputAlarmChannelID"))
if mibBuilder.loadTexts: h3cPUExternalOutputAlarmEntry.setStatus('current')
if mibBuilder.loadTexts: h3cPUExternalOutputAlarmEntry.setDescription('External output alarm entry')
h3cPUExternalOutputAlarmChannelID = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 9, 2, 1, 2, 2, 1, 1), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: h3cPUExternalOutputAlarmChannelID.setStatus('current')
if mibBuilder.loadTexts: h3cPUExternalOutputAlarmChannelID.setDescription('The ID of the external output alarm channel')
h3cPUExternalOutputAlarmStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 9, 2, 1, 2, 2, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cPUExternalOutputAlarmStatus.setStatus('current')
if mibBuilder.loadTexts: h3cPUExternalOutputAlarmStatus.setDescription('True indicates that the current channel has alarm.')
h3cPUECMan = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 9, 2, 2))
h3cPUECManObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 9, 2, 2, 1))
h3cPUECCameraOnlines = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 9, 2, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cPUECCameraOnlines.setStatus('current')
if mibBuilder.loadTexts: h3cPUECCameraOnlines.setDescription('Number of online cameras connected to an EC.')
h3cPUECCameraAvailRate = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 9, 2, 2, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cPUECCameraAvailRate.setStatus('current')
if mibBuilder.loadTexts: h3cPUECCameraAvailRate.setDescription('Camera available rate. That is, the ratio of available cameras to total cameras connected to an EC. It ranges from 0 to 100.')
h3cPUECManTables = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 9, 2, 2, 2))
h3cPUECVideoChannelTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 9, 2, 2, 2, 1), )
if mibBuilder.loadTexts: h3cPUECVideoChannelTable.setStatus('current')
if mibBuilder.loadTexts: h3cPUECVideoChannelTable.setDescription('Video channel table')
h3cPUECVideoChannelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 9, 2, 2, 2, 1, 1), ).setIndexNames((0, "H3C-PU-MAN-MIB", "h3cPUECVideoChannelID"))
if mibBuilder.loadTexts: h3cPUECVideoChannelEntry.setStatus('current')
if mibBuilder.loadTexts: h3cPUECVideoChannelEntry.setDescription('Video channel entry')
h3cPUECVideoChannelID = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 9, 2, 2, 2, 1, 1, 1), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: h3cPUECVideoChannelID.setStatus('current')
if mibBuilder.loadTexts: h3cPUECVideoChannelID.setDescription('The ID of the video channel')
h3cPUECVideoChannelName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 9, 2, 2, 2, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cPUECVideoChannelName.setStatus('current')
if mibBuilder.loadTexts: h3cPUECVideoChannelName.setDescription('The name of the video channel. It is suggested that the name includes the channel ID information.')
h3cPUECVideoChannelServiceStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 9, 2, 2, 2, 1, 1, 3), Bits().clone(namedValues=NamedValues(("unknown", 0), ("unused", 1), ("kinescope", 2), ("snapshot", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cPUECVideoChannelServiceStatus.setStatus('current')
if mibBuilder.loadTexts: h3cPUECVideoChannelServiceStatus.setDescription('The service status of the video channel. 0 the status is not known. 1 the video is not used or the channel has no signal. 2 the camera is kinescoping. 3 the camera is take snapshot. ')
h3cPUDCMan = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 9, 2, 3))
h3cPUDCManObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 9, 2, 3, 1))
h3cPUDCRcvVideoPackets = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 9, 2, 3, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cPUDCRcvVideoPackets.setStatus('current')
if mibBuilder.loadTexts: h3cPUDCRcvVideoPackets.setDescription('The total number of video packets which are received from interfaces.')
h3cPUDCRcvVideoRefFrames = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 9, 2, 3, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cPUDCRcvVideoRefFrames.setStatus('current')
if mibBuilder.loadTexts: h3cPUDCRcvVideoRefFrames.setDescription('The total number of video reference frames which are received from interfaces.')
h3cPUDCVideoPacketsLoss = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 9, 2, 3, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cPUDCVideoPacketsLoss.setStatus('current')
if mibBuilder.loadTexts: h3cPUDCVideoPacketsLoss.setDescription('The total number of lost video packets.')
h3cPUDCVideoRefFramesLoss = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 9, 2, 3, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cPUDCVideoRefFramesLoss.setStatus('current')
if mibBuilder.loadTexts: h3cPUDCVideoRefFramesLoss.setDescription('The total number of lost video reference frames.')
h3cPUECManMIBTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 9, 2, 2, 3))
h3cPUECManTrapPrex = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 9, 2, 2, 3, 0))
h3cPUECManExternalSemaphoreTrap = NotificationType((1, 3, 6, 1, 4, 1, 2011, 10, 9, 2, 2, 3, 0, 1)).setObjects(("H3C-PU-MAN-MIB", "h3cPUExternalInputAlarmChannelID"))
if mibBuilder.loadTexts: h3cPUECManExternalSemaphoreTrap.setStatus('current')
if mibBuilder.loadTexts: h3cPUECManExternalSemaphoreTrap.setDescription('Send a trap about external semaphore alarm.')
h3cPUECManVideoLossTrap = NotificationType((1, 3, 6, 1, 4, 1, 2011, 10, 9, 2, 2, 3, 0, 2)).setObjects(("H3C-PU-MAN-MIB", "h3cPUECVideoChannelName"))
if mibBuilder.loadTexts: h3cPUECManVideoLossTrap.setStatus('current')
if mibBuilder.loadTexts: h3cPUECManVideoLossTrap.setDescription('Send a trap about video loss. Video loss is that no video signal is inputted to the EC.')
h3cPUECManVideoRecoverTrap = NotificationType((1, 3, 6, 1, 4, 1, 2011, 10, 9, 2, 2, 3, 0, 3)).setObjects(("H3C-PU-MAN-MIB", "h3cPUECVideoChannelName"))
if mibBuilder.loadTexts: h3cPUECManVideoRecoverTrap.setStatus('current')
if mibBuilder.loadTexts: h3cPUECManVideoRecoverTrap.setDescription('Send a trap about video recovery after loss.')
h3cPUECManMotionDetectTrap = NotificationType((1, 3, 6, 1, 4, 1, 2011, 10, 9, 2, 2, 3, 0, 4)).setObjects(("H3C-PU-MAN-MIB", "h3cPUECVideoChannelName"), ("H3C-PU-MAN-MIB", "h3cPUECRegionCoordinateX1"), ("H3C-PU-MAN-MIB", "h3cPUECRegionCoordinateY1"), ("H3C-PU-MAN-MIB", "h3cPUECRegionCoordinateX2"), ("H3C-PU-MAN-MIB", "h3cPUECRegionCoordinateY2"))
if mibBuilder.loadTexts: h3cPUECManMotionDetectTrap.setStatus('current')
if mibBuilder.loadTexts: h3cPUECManMotionDetectTrap.setDescription('Send a trap about motion detection.')
h3cPUECManOnLineFailureTrap = NotificationType((1, 3, 6, 1, 4, 1, 2011, 10, 9, 2, 2, 3, 0, 5)).setObjects(("H3C-PU-MAN-MIB", "h3cPUCMSAddr"))
if mibBuilder.loadTexts: h3cPUECManOnLineFailureTrap.setStatus('current')
if mibBuilder.loadTexts: h3cPUECManOnLineFailureTrap.setDescription('Send a trap when EC can not register the CMS.')
h3cPUECManConnectionCMSFailureTrap = NotificationType((1, 3, 6, 1, 4, 1, 2011, 10, 9, 2, 2, 3, 0, 6)).setObjects(("H3C-PU-MAN-MIB", "h3cPUCMSAddr"))
if mibBuilder.loadTexts: h3cPUECManConnectionCMSFailureTrap.setStatus('current')
if mibBuilder.loadTexts: h3cPUECManConnectionCMSFailureTrap.setDescription('Send a trap when the connection with the CMS breaks down.')
h3cPUECManConnectionVerSrvFailureTrap = NotificationType((1, 3, 6, 1, 4, 1, 2011, 10, 9, 2, 2, 3, 0, 7)).setObjects(("H3C-PU-MAN-MIB", "h3cPUVersionServerAddr"))
if mibBuilder.loadTexts: h3cPUECManConnectionVerSrvFailureTrap.setStatus('current')
if mibBuilder.loadTexts: h3cPUECManConnectionVerSrvFailureTrap.setDescription('Send a trap when the connection with the version server breaks down or can not create.')
h3cPUECManFlashFailureTrap = NotificationType((1, 3, 6, 1, 4, 1, 2011, 10, 9, 2, 2, 3, 0, 8))
if mibBuilder.loadTexts: h3cPUECManFlashFailureTrap.setStatus('current')
if mibBuilder.loadTexts: h3cPUECManFlashFailureTrap.setDescription('Send a trap about flash failure.')
h3cPUECManCameraShelterTrap = NotificationType((1, 3, 6, 1, 4, 1, 2011, 10, 9, 2, 2, 3, 0, 9)).setObjects(("H3C-PU-MAN-MIB", "h3cPUECVideoChannelName"), ("H3C-PU-MAN-MIB", "h3cPUECRegionCoordinateX1"), ("H3C-PU-MAN-MIB", "h3cPUECRegionCoordinateY1"), ("H3C-PU-MAN-MIB", "h3cPUECRegionCoordinateX2"), ("H3C-PU-MAN-MIB", "h3cPUECRegionCoordinateY2"))
if mibBuilder.loadTexts: h3cPUECManCameraShelterTrap.setStatus('current')
if mibBuilder.loadTexts: h3cPUECManCameraShelterTrap.setDescription('Send a trap when a camera is sheltered.')
h3cPUECManTrapObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 9, 2, 2, 3, 1))
h3cPUECRegionCoordinateX1 = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 9, 2, 2, 3, 1, 1), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: h3cPUECRegionCoordinateX1.setStatus('current')
if mibBuilder.loadTexts: h3cPUECRegionCoordinateX1.setDescription('The horizontal coordinate of top left point of the motion detection region.')
h3cPUECRegionCoordinateY1 = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 9, 2, 2, 3, 1, 2), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: h3cPUECRegionCoordinateY1.setStatus('current')
if mibBuilder.loadTexts: h3cPUECRegionCoordinateY1.setDescription('The vertical coordinate of top left point of the motion detection region.')
h3cPUECRegionCoordinateX2 = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 9, 2, 2, 3, 1, 3), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: h3cPUECRegionCoordinateX2.setStatus('current')
if mibBuilder.loadTexts: h3cPUECRegionCoordinateX2.setDescription('The horizontal coordinate of botton right point of the motion detection region.')
h3cPUECRegionCoordinateY2 = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 9, 2, 2, 3, 1, 4), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: h3cPUECRegionCoordinateY2.setStatus('current')
if mibBuilder.loadTexts: h3cPUECRegionCoordinateY2.setDescription('The horizontal coordinate of botton right point of the motion detection region.')
mibBuilder.exportSymbols("H3C-PU-MAN-MIB", h3cPUExternalInputAlarmTable=h3cPUExternalInputAlarmTable, h3cPUDCRcvVideoRefFrames=h3cPUDCRcvVideoRefFrames, h3cPUExternalOutputAlarmChannelID=h3cPUExternalOutputAlarmChannelID, h3cPUECVideoChannelEntry=h3cPUECVideoChannelEntry, h3cPUExternalOutputAlarmEntry=h3cPUExternalOutputAlarmEntry, h3cPUECVideoChannelServiceStatus=h3cPUECVideoChannelServiceStatus, h3cPUDCManObjects=h3cPUDCManObjects, h3cPUECCameraOnlines=h3cPUECCameraOnlines, h3cPUDCRcvVideoPackets=h3cPUDCRcvVideoPackets, h3cPUECManMotionDetectTrap=h3cPUECManMotionDetectTrap, h3cPUCMSAddr=h3cPUCMSAddr, h3cPUECManExternalSemaphoreTrap=h3cPUECManExternalSemaphoreTrap, h3cPUMan=h3cPUMan, h3cPUECManTrapObjects=h3cPUECManTrapObjects, h3cPUECVideoChannelName=h3cPUECVideoChannelName, h3cPUDCMan=h3cPUDCMan, h3cPUECRegionCoordinateX2=h3cPUECRegionCoordinateX2, h3cPUisOnline=h3cPUisOnline, h3cPUECManObjects=h3cPUECManObjects, h3cPUDCVideoRefFramesLoss=h3cPUDCVideoRefFramesLoss, h3cPUECVideoChannelTable=h3cPUECVideoChannelTable, h3cPUDCVideoPacketsLoss=h3cPUDCVideoPacketsLoss, h3cPUECManConnectionCMSFailureTrap=h3cPUECManConnectionCMSFailureTrap, h3cPUECManCameraShelterTrap=h3cPUECManCameraShelterTrap, h3cPUECManVideoLossTrap=h3cPUECManVideoLossTrap, h3cPUECManFlashFailureTrap=h3cPUECManFlashFailureTrap, h3cPUECRegionCoordinateX1=h3cPUECRegionCoordinateX1, PYSNMP_MODULE_ID=h3cPUMan, h3cPUExternalOutputAlarmStatus=h3cPUExternalOutputAlarmStatus, h3cPUCommonMan=h3cPUCommonMan, h3cPUECManTrapPrex=h3cPUECManTrapPrex, h3cPUCommonManObjects=h3cPUCommonManObjects, h3cPUECMan=h3cPUECMan, h3cPUECCameraAvailRate=h3cPUECCameraAvailRate, h3cPUExternalInputAlarmStatus=h3cPUExternalInputAlarmStatus, h3cPUECManOnLineFailureTrap=h3cPUECManOnLineFailureTrap, h3cPUECManTables=h3cPUECManTables, h3cPUVersionServerAddr=h3cPUVersionServerAddr, h3cPUECRegionCoordinateY1=h3cPUECRegionCoordinateY1, h3cPUExternalInputAlarmChannelID=h3cPUExternalInputAlarmChannelID, h3cPUECManConnectionVerSrvFailureTrap=h3cPUECManConnectionVerSrvFailureTrap, h3cPUECManVideoRecoverTrap=h3cPUECManVideoRecoverTrap, h3cPUExternalInputAlarmEntry=h3cPUExternalInputAlarmEntry, h3cPUExternalOutputAlarmTable=h3cPUExternalOutputAlarmTable, h3cPUCommonManTables=h3cPUCommonManTables, h3cPUECManMIBTrap=h3cPUECManMIBTrap, h3cPUECRegionCoordinateY2=h3cPUECRegionCoordinateY2, h3cPUECVideoChannelID=h3cPUECVideoChannelID)
