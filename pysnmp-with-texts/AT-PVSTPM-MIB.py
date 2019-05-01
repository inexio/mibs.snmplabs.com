#
# PySNMP MIB module AT-PVSTPM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/AT-PVSTPM-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:30:33 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
modules, = mibBuilder.importSymbols("AT-SMI-MIB", "modules")
VlanIndex, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, iso, Integer32, Counter32, TimeTicks, ObjectIdentity, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Bits, Counter64, MibIdentifier, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "iso", "Integer32", "Counter32", "TimeTicks", "ObjectIdentity", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Bits", "Counter64", "MibIdentifier", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
pvstpm = ModuleIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 140))
pvstpm.setRevisions(('2006-03-29 16:51',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: pvstpm.setRevisionsDescriptions(('Initial revision',))
if mibBuilder.loadTexts: pvstpm.setLastUpdated('200603291651Z')
if mibBuilder.loadTexts: pvstpm.setOrganization('Allied Telesis, Inc')
if mibBuilder.loadTexts: pvstpm.setContactInfo('http://www.alliedtelesis.com')
if mibBuilder.loadTexts: pvstpm.setDescription('The MIB module for managing PVSTPM enterprise functionality on Allied Telesis switches. ')
pvstpmEvents = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 140, 0))
pvstpmEventVariables = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 140, 1))
pvstpmBridgeId = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 140, 1, 1), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: pvstpmBridgeId.setStatus('current')
if mibBuilder.loadTexts: pvstpmBridgeId.setDescription('The bridge identifier for the bridge that sent the trap.')
pvstpmTopologyChangeVlan = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 140, 1, 2), VlanIndex()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: pvstpmTopologyChangeVlan.setStatus('current')
if mibBuilder.loadTexts: pvstpmTopologyChangeVlan.setDescription('The VLAN ID of the vlan that has experienced a topology change.')
pvstpmRxPort = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 140, 1, 3), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: pvstpmRxPort.setStatus('current')
if mibBuilder.loadTexts: pvstpmRxPort.setDescription('The port the inconsistent BPDU was received on.')
pvstpmRxVlan = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 140, 1, 4), VlanIndex()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: pvstpmRxVlan.setStatus('current')
if mibBuilder.loadTexts: pvstpmRxVlan.setDescription('The vlan the inconsistent BPDU was received on.')
pvstpmTxVlan = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 140, 1, 5), VlanIndex()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: pvstpmTxVlan.setStatus('current')
if mibBuilder.loadTexts: pvstpmTxVlan.setDescription('The vlan the inconsistent BPDU was transmitted on.')
pvstpmTopologyChange = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 140, 0, 1)).setObjects(("AT-PVSTPM-MIB", "pvstpmBridgeId"), ("AT-PVSTPM-MIB", "pvstpmTopologyChangeVlan"))
if mibBuilder.loadTexts: pvstpmTopologyChange.setStatus('current')
if mibBuilder.loadTexts: pvstpmTopologyChange.setDescription('A pvstpmTopologyChange trap signifies that a topology change has occurred on the specified VLAN')
pvstpmInconsistentBPDU = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 140, 0, 2)).setObjects(("AT-PVSTPM-MIB", "pvstpmBridgeId"), ("AT-PVSTPM-MIB", "pvstpmRxPort"), ("AT-PVSTPM-MIB", "pvstpmRxVlan"), ("AT-PVSTPM-MIB", "pvstpmTxVlan"))
if mibBuilder.loadTexts: pvstpmInconsistentBPDU.setStatus('current')
if mibBuilder.loadTexts: pvstpmInconsistentBPDU.setDescription('A pvstpmInconsistentBPDU trap signifies that an inconsistent PVSTPM packet has been received on a port.')
mibBuilder.exportSymbols("AT-PVSTPM-MIB", pvstpmBridgeId=pvstpmBridgeId, pvstpmRxVlan=pvstpmRxVlan, pvstpmTxVlan=pvstpmTxVlan, pvstpm=pvstpm, pvstpmEventVariables=pvstpmEventVariables, pvstpmTopologyChangeVlan=pvstpmTopologyChangeVlan, pvstpmEvents=pvstpmEvents, pvstpmTopologyChange=pvstpmTopologyChange, PYSNMP_MODULE_ID=pvstpm, pvstpmInconsistentBPDU=pvstpmInconsistentBPDU, pvstpmRxPort=pvstpmRxPort)
