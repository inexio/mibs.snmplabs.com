#
# PySNMP MIB module COLUBRIS-TOOLS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/COLUBRIS-TOOLS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:26:07 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
colubrisMgmtV2, = mibBuilder.importSymbols("COLUBRIS-SMI", "colubrisMgmtV2")
ColubrisNotificationEnable, = mibBuilder.importSymbols("COLUBRIS-TC", "ColubrisNotificationEnable")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Counter32, ModuleIdentity, Gauge32, IpAddress, ObjectIdentity, Integer32, TimeTicks, Counter64, iso, Unsigned32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Counter32", "ModuleIdentity", "Gauge32", "IpAddress", "ObjectIdentity", "Integer32", "TimeTicks", "Counter64", "iso", "Unsigned32", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
colubrisToolsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 8744, 5, 12))
if mibBuilder.loadTexts: colubrisToolsMIB.setLastUpdated('200402200000Z')
if mibBuilder.loadTexts: colubrisToolsMIB.setOrganization('Colubris Networks, Inc.')
if mibBuilder.loadTexts: colubrisToolsMIB.setContactInfo('Colubris Networks Postal: 200 West Street Ste 300 Waltham, Massachusetts 02451-1121 UNITED STATES Phone: +1 781 684 0001 Fax: +1 781 684 0009 E-mail: cn-snmp@colubris.com')
if mibBuilder.loadTexts: colubrisToolsMIB.setDescription('Colubris Networks Tools MIB module.')
colubrisToolsMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 12, 1))
traceToolConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 12, 1, 1))
traceInterface = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 12, 1, 1, 1), InterfaceIndex()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: traceInterface.setStatus('current')
if mibBuilder.loadTexts: traceInterface.setDescription('Specifies the interface to apply the trace to.')
traceCaptureDestination = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 12, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("local", 1), ("remote", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: traceCaptureDestination.setStatus('current')
if mibBuilder.loadTexts: traceCaptureDestination.setDescription("Specifies if the traces shall be stored locally on the device or remotely on a distant system. 'local': Stores the traces locally on the device. 'remote': Stores the traces in a remote file specified by traceCaptureDestinationURL.")
traceCaptureDestinationURL = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 12, 1, 1, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: traceCaptureDestinationURL.setStatus('current')
if mibBuilder.loadTexts: traceCaptureDestinationURL.setDescription('Specifies the URL of the file to which trace data will be sent. If a valid URL is not defined, the trace data cannot be sent and will be discarded.')
traceTimeout = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 12, 1, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 99999)).clone(600)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: traceTimeout.setStatus('current')
if mibBuilder.loadTexts: traceTimeout.setDescription('Specifies the amount of time the trace will capture data. Once this limit is reached, the trace automatically stops.')
traceNumberOfPackets = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 12, 1, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 99999)).clone(100)).setUnits('packets').setMaxAccess("readwrite")
if mibBuilder.loadTexts: traceNumberOfPackets.setStatus('current')
if mibBuilder.loadTexts: traceNumberOfPackets.setDescription('Specifies the maximum number of packets (IP datagrams) the trace should capture. Once this limit is reached, the trace automatically stops.')
tracePacketSize = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 12, 1, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(68, 4096)).clone(128)).setUnits('bytes').setMaxAccess("readwrite")
if mibBuilder.loadTexts: tracePacketSize.setStatus('current')
if mibBuilder.loadTexts: tracePacketSize.setDescription('Specifies the maximum number of bytes to capture for each packet. The remaining data is discarded.')
traceCaptureFilter = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 12, 1, 1, 7), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: traceCaptureFilter.setStatus('current')
if mibBuilder.loadTexts: traceCaptureFilter.setDescription('Specifies the packet filter to use to capture data. The filter expression has the same format and behavior as the expression parameter used by the well-known TCPDUMP command.')
traceCaptureStatus = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 12, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("stop", 1), ("start", 2))).clone('stop')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: traceCaptureStatus.setStatus('current')
if mibBuilder.loadTexts: traceCaptureStatus.setDescription("IP Trace tool action trigger. 'stop': Stops the trace tool from functioning. If any capture was previously started it will end up. if no capture was started, 'stop' has no effect. 'start': Starts to capture the packets following the criteria specified in the management tool and in this MIB.")
traceNotificationEnabled = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 12, 1, 1, 9), ColubrisNotificationEnable().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: traceNotificationEnabled.setStatus('current')
if mibBuilder.loadTexts: traceNotificationEnabled.setDescription('Specifies if IP trace notifications are generated.')
colubrisToolsMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 12, 2))
colubrisToolsMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 12, 2, 0))
traceStatusNotification = NotificationType((1, 3, 6, 1, 4, 1, 8744, 5, 12, 2, 0, 1)).setObjects(("COLUBRIS-TOOLS-MIB", "traceCaptureStatus"))
if mibBuilder.loadTexts: traceStatusNotification.setStatus('current')
if mibBuilder.loadTexts: traceStatusNotification.setDescription('Sent when the user triggers the IP Trace tool either by starting a new trace or stopping an existing session.')
colubrisToolsMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 12, 3))
colubrisToolsMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 12, 3, 1))
colubrisToolsMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 12, 3, 2))
colubrisToolsMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 8744, 5, 12, 3, 1, 1)).setObjects(("COLUBRIS-TOOLS-MIB", "colubrisToolsMIBGroup"), ("COLUBRIS-TOOLS-MIB", "colubrisToolsNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisToolsMIBCompliance = colubrisToolsMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: colubrisToolsMIBCompliance.setDescription('The compliance statement for entities which implement the Colubris Networks Tools MIB.')
colubrisToolsMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8744, 5, 12, 3, 2, 1)).setObjects(("COLUBRIS-TOOLS-MIB", "traceInterface"), ("COLUBRIS-TOOLS-MIB", "traceCaptureDestination"), ("COLUBRIS-TOOLS-MIB", "traceCaptureDestinationURL"), ("COLUBRIS-TOOLS-MIB", "traceTimeout"), ("COLUBRIS-TOOLS-MIB", "traceNumberOfPackets"), ("COLUBRIS-TOOLS-MIB", "tracePacketSize"), ("COLUBRIS-TOOLS-MIB", "traceCaptureFilter"), ("COLUBRIS-TOOLS-MIB", "traceCaptureStatus"), ("COLUBRIS-TOOLS-MIB", "traceNotificationEnabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisToolsMIBGroup = colubrisToolsMIBGroup.setStatus('current')
if mibBuilder.loadTexts: colubrisToolsMIBGroup.setDescription('A collection of objects providing the Tools MIB capability.')
colubrisToolsNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 8744, 5, 12, 3, 2, 2)).setObjects(("COLUBRIS-TOOLS-MIB", "traceStatusNotification"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisToolsNotificationGroup = colubrisToolsNotificationGroup.setStatus('current')
if mibBuilder.loadTexts: colubrisToolsNotificationGroup.setDescription('A collection of supported notifications.')
mibBuilder.exportSymbols("COLUBRIS-TOOLS-MIB", colubrisToolsMIBCompliance=colubrisToolsMIBCompliance, colubrisToolsMIBGroup=colubrisToolsMIBGroup, traceTimeout=traceTimeout, traceStatusNotification=traceStatusNotification, colubrisToolsMIBNotificationPrefix=colubrisToolsMIBNotificationPrefix, colubrisToolsMIB=colubrisToolsMIB, traceToolConfig=traceToolConfig, traceCaptureFilter=traceCaptureFilter, colubrisToolsMIBCompliances=colubrisToolsMIBCompliances, traceCaptureStatus=traceCaptureStatus, colubrisToolsMIBNotifications=colubrisToolsMIBNotifications, traceNumberOfPackets=traceNumberOfPackets, PYSNMP_MODULE_ID=colubrisToolsMIB, colubrisToolsMIBObjects=colubrisToolsMIBObjects, colubrisToolsMIBConformance=colubrisToolsMIBConformance, colubrisToolsMIBGroups=colubrisToolsMIBGroups, colubrisToolsNotificationGroup=colubrisToolsNotificationGroup, traceCaptureDestinationURL=traceCaptureDestinationURL, traceInterface=traceInterface, tracePacketSize=tracePacketSize, traceNotificationEnabled=traceNotificationEnabled, traceCaptureDestination=traceCaptureDestination)