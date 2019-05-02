#
# PySNMP MIB module WWP-XCVR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/WWP-XCVR-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:38:54 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, TimeTicks, ObjectIdentity, Integer32, Counter64, Bits, Gauge32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, IpAddress, MibIdentifier, ModuleIdentity, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "TimeTicks", "ObjectIdentity", "Integer32", "Counter64", "Bits", "Gauge32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "IpAddress", "MibIdentifier", "ModuleIdentity", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
wwpModules, = mibBuilder.importSymbols("WWP-SMI", "wwpModules")
wwpXcvrMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6141, 2, 14))
wwpXcvrMIB.setRevisions(('2001-04-03 17:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: wwpXcvrMIB.setRevisionsDescriptions(('Initial creation.',))
if mibBuilder.loadTexts: wwpXcvrMIB.setLastUpdated('200104031700Z')
if mibBuilder.loadTexts: wwpXcvrMIB.setOrganization('World Wide Packets, Inc')
if mibBuilder.loadTexts: wwpXcvrMIB.setContactInfo(' Mib Meister Postal: World Wide Packets P.O. Box 950 Veradale, WA 99037 USA Phone: +1 509 242 9000 Email: mib.meister@worldwidepackets.com')
if mibBuilder.loadTexts: wwpXcvrMIB.setDescription('The MIB module for the WWP System physical transceiver devices.')
wwpXcvrMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 14, 1))
wwpXcvr = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 14, 1, 1))
wwpXcvrNotif = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 14, 1, 2))
wwpXcvrMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 14, 2))
wwpXcvrMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 14, 2, 0))
wwpXcvrMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 14, 3))
wwpXcvrMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 14, 3, 1))
wwpXcvrMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 14, 3, 2))
wwpXcvrTable = MibTable((1, 3, 6, 1, 4, 1, 6141, 2, 14, 1, 1, 1), )
if mibBuilder.loadTexts: wwpXcvrTable.setStatus('current')
if mibBuilder.loadTexts: wwpXcvrTable.setDescription('This table contains descriptions and settings for each of the physical transceiver devices.')
wwpXcvrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6141, 2, 14, 1, 1, 1, 1), ).setIndexNames((0, "WWP-XCVR-MIB", "wwpXcvrPortXcvrId"), (0, "WWP-XCVR-MIB", "wwpXcvrId"))
if mibBuilder.loadTexts: wwpXcvrEntry.setStatus('current')
if mibBuilder.loadTexts: wwpXcvrEntry.setDescription('The Transciever Device Entry.')
wwpXcvrPortXcvrId = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 14, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpXcvrPortXcvrId.setStatus('current')
if mibBuilder.loadTexts: wwpXcvrPortXcvrId.setDescription('Indicates the logical port in-which this transciever belongs to.')
wwpXcvrId = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 14, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpXcvrId.setStatus('current')
if mibBuilder.loadTexts: wwpXcvrId.setDescription('The id for the transceiver.')
wwpXcvrFiberType = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 14, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("lx", 1), ("sx", 2), ("cx", 3), ("t", 4), ("unknown", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpXcvrFiberType.setStatus('current')
if mibBuilder.loadTexts: wwpXcvrFiberType.setDescription('The fiber type of this transceiver. Possible values: lx 1000BASE-LX fiber sx 1000BASE-SX fiber cx 1000BASE-CX fiber t 1000BASE-T unknown Unknown type')
wwpXcvrVendorName = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 14, 1, 1, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpXcvrVendorName.setStatus('current')
if mibBuilder.loadTexts: wwpXcvrVendorName.setDescription("String containing this transceiver's vendor name.")
wwpXcvrPartNum = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 14, 1, 1, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpXcvrPartNum.setStatus('current')
if mibBuilder.loadTexts: wwpXcvrPartNum.setDescription("String containing this transceiver's part number.")
wwpXcvrPartRev = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 14, 1, 1, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpXcvrPartRev.setStatus('current')
if mibBuilder.loadTexts: wwpXcvrPartRev.setDescription("String containing this tranceiver's part revision.")
wwpXcvrTxEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 14, 1, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpXcvrTxEnabled.setStatus('current')
if mibBuilder.loadTexts: wwpXcvrTxEnabled.setDescription('Indicates whether this transceiver is currently set to transmit.')
wwpXcvrRxSignalStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 14, 1, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("detected", 1), ("notDetected", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpXcvrRxSignalStatus.setStatus('current')
if mibBuilder.loadTexts: wwpXcvrRxSignalStatus.setDescription('Indicates whether this transceiver is currently detecting a Receive (RX) signal.')
wwpXcvrTxFaultStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 14, 1, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("fault", 1), ("noFault", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpXcvrTxFaultStatus.setStatus('current')
if mibBuilder.loadTexts: wwpXcvrTxFaultStatus.setDescription('Indicates the fault status of this transceiver.')
wwpXcvrPortTable = MibTable((1, 3, 6, 1, 4, 1, 6141, 2, 14, 1, 1, 2), )
if mibBuilder.loadTexts: wwpXcvrPortTable.setStatus('current')
if mibBuilder.loadTexts: wwpXcvrPortTable.setDescription('The table contains of the logical ports which have transceivers.')
wwpXcvrPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6141, 2, 14, 1, 1, 2, 1), ).setIndexNames((0, "WWP-XCVR-MIB", "wwpXcvrPortId"))
if mibBuilder.loadTexts: wwpXcvrPortEntry.setStatus('current')
if mibBuilder.loadTexts: wwpXcvrPortEntry.setDescription('The logical Port Entry.')
wwpXcvrPortId = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 14, 1, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpXcvrPortId.setStatus('current')
if mibBuilder.loadTexts: wwpXcvrPortId.setDescription('Indicates the logical port in-which this transciever belongs to.')
wwpXcvrPortHoldDownTime = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 14, 1, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 30))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpXcvrPortHoldDownTime.setStatus('deprecated')
if mibBuilder.loadTexts: wwpXcvrPortHoldDownTime.setDescription('Indicates the hold-down time (in seconds) for this logical port. This value is used to help smooth out possible flapping between XCVRs of the bank when a link goes down. When this HoldDown timer expires, the selected XCVR(in link-down state) may attempt to select the adjacent XCVR of the bank.')
wwpXcvrPortRedOrDiagMode = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 14, 1, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpXcvrPortRedOrDiagMode.setStatus('current')
if mibBuilder.loadTexts: wwpXcvrPortRedOrDiagMode.setDescription('This object can be used to bring the Xcvr to the Manual mode. This also shows the port redundancy status for this logical port.')
wwpXcvrPortPreferredXcvr = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 14, 1, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpXcvrPortPreferredXcvr.setStatus('current')
if mibBuilder.loadTexts: wwpXcvrPortPreferredXcvr.setDescription('Indicates which transceiver is preferred. This transceiver will be used by default, but if it goes down, the alternate will be used.')
wwpXcvrPortActiveXcvr = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 14, 1, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpXcvrPortActiveXcvr.setStatus('current')
if mibBuilder.loadTexts: wwpXcvrPortActiveXcvr.setDescription('Indicates which transceiver is currently active.')
wwpXcvrEventType = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 14, 1, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("none", 0), ("up", 1), ("down", 2), ("select", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpXcvrEventType.setStatus('current')
if mibBuilder.loadTexts: wwpXcvrEventType.setDescription('Indicates if the Xcvr specified by the wwpXcvrPortId and wwpXcvrId has come up, gone down or has been selected. This object only make sense for wwpXcvrLinkStateChangeNotification and should return none otherwise.')
wwpXcvrErrorType = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 14, 1, 2, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("none", 0), ("chksumFailed", 1), ("opticalFault", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpXcvrErrorType.setStatus('current')
if mibBuilder.loadTexts: wwpXcvrErrorType.setDescription('Indicates if the Xcvr specified by the wwpXcvrPortId and wwpXcvrId is faulted because of checksum failed or optical fault. This object only make sense if some xcvr has been detected faulted otherwise it returns none.')
wwpXcvrLinkStateChangeNotification = NotificationType((1, 3, 6, 1, 4, 1, 6141, 2, 14, 2, 0, 4)).setObjects(("WWP-XCVR-MIB", "wwpXcvrPortId"), ("WWP-XCVR-MIB", "wwpXcvrId"), ("WWP-XCVR-MIB", "wwpXcvrEventType"))
if mibBuilder.loadTexts: wwpXcvrLinkStateChangeNotification.setStatus('current')
if mibBuilder.loadTexts: wwpXcvrLinkStateChangeNotification.setDescription('A wwpXcvrLinkStateChangeNotification is sent if the Xcvr state has changed.')
wwpXcvrErrorTypeNotification = NotificationType((1, 3, 6, 1, 4, 1, 6141, 2, 14, 2, 0, 5)).setObjects(("WWP-XCVR-MIB", "wwpXcvrPortId"), ("WWP-XCVR-MIB", "wwpXcvrId"), ("WWP-XCVR-MIB", "wwpXcvrErrorType"))
if mibBuilder.loadTexts: wwpXcvrErrorTypeNotification.setStatus('current')
if mibBuilder.loadTexts: wwpXcvrErrorTypeNotification.setDescription('A wwpXcvrErrorTypeNotification is sent if the Xcvr is detected faulted because of some reason. Reason of failure is specifed by wwpXcvrErrorType.')
mibBuilder.exportSymbols("WWP-XCVR-MIB", wwpXcvrRxSignalStatus=wwpXcvrRxSignalStatus, wwpXcvrId=wwpXcvrId, wwpXcvrPartRev=wwpXcvrPartRev, wwpXcvrFiberType=wwpXcvrFiberType, wwpXcvrPortRedOrDiagMode=wwpXcvrPortRedOrDiagMode, wwpXcvrMIB=wwpXcvrMIB, wwpXcvrTxFaultStatus=wwpXcvrTxFaultStatus, wwpXcvrPortActiveXcvr=wwpXcvrPortActiveXcvr, wwpXcvrErrorType=wwpXcvrErrorType, wwpXcvrEntry=wwpXcvrEntry, wwpXcvrTxEnabled=wwpXcvrTxEnabled, wwpXcvrMIBNotificationPrefix=wwpXcvrMIBNotificationPrefix, PYSNMP_MODULE_ID=wwpXcvrMIB, wwpXcvrMIBObjects=wwpXcvrMIBObjects, wwpXcvrMIBGroups=wwpXcvrMIBGroups, wwpXcvrPortEntry=wwpXcvrPortEntry, wwpXcvrPortId=wwpXcvrPortId, wwpXcvrEventType=wwpXcvrEventType, wwpXcvrMIBNotifications=wwpXcvrMIBNotifications, wwpXcvrPortHoldDownTime=wwpXcvrPortHoldDownTime, wwpXcvrPartNum=wwpXcvrPartNum, wwpXcvrMIBCompliances=wwpXcvrMIBCompliances, wwpXcvrMIBConformance=wwpXcvrMIBConformance, wwpXcvrVendorName=wwpXcvrVendorName, wwpXcvrTable=wwpXcvrTable, wwpXcvrPortTable=wwpXcvrPortTable, wwpXcvrLinkStateChangeNotification=wwpXcvrLinkStateChangeNotification, wwpXcvrPortXcvrId=wwpXcvrPortXcvrId, wwpXcvrErrorTypeNotification=wwpXcvrErrorTypeNotification, wwpXcvrNotif=wwpXcvrNotif, wwpXcvrPortPreferredXcvr=wwpXcvrPortPreferredXcvr, wwpXcvr=wwpXcvr)