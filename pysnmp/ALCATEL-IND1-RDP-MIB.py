#
# PySNMP MIB module ALCATEL-IND1-RDP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ALCATEL-IND1-RDP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:03:30 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
routingIND1RDP, = mibBuilder.importSymbols("ALCATEL-IND1-BASE", "routingIND1RDP")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, NotificationType, Counter64, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Integer32, iso, ObjectIdentity, TimeTicks, Unsigned32, Bits, IpAddress, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "NotificationType", "Counter64", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Integer32", "iso", "ObjectIdentity", "TimeTicks", "Unsigned32", "Bits", "IpAddress", "Counter32")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
alcatelIND1RouterDiscoveryProtocolMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 11, 1))
alcatelIND1RouterDiscoveryProtocolMIB.setRevisions(('2007-04-03 00:00',))
if mibBuilder.loadTexts: alcatelIND1RouterDiscoveryProtocolMIB.setLastUpdated('200704030000Z')
if mibBuilder.loadTexts: alcatelIND1RouterDiscoveryProtocolMIB.setOrganization('Alcatel-Lucent')
alcatelIND1RDPMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 11, 1, 1))
alaRDPConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 11, 1, 1, 1))
alaRDPStatus = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 11, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaRDPStatus.setStatus('current')
alaRDPIfTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 11, 1, 1, 1, 20), )
if mibBuilder.loadTexts: alaRDPIfTable.setStatus('current')
alaRDPIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 11, 1, 1, 1, 20, 1), ).setIndexNames((0, "ALCATEL-IND1-RDP-MIB", "alaRDPIfAddr"))
if mibBuilder.loadTexts: alaRDPIfEntry.setStatus('current')
alaRDPIfAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 11, 1, 1, 1, 20, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaRDPIfAddr.setStatus('current')
alaRDPIfStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 11, 1, 1, 1, 20, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaRDPIfStatus.setStatus('current')
alaRDPIfAdvtAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 11, 1, 1, 1, 20, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaRDPIfAdvtAddress.setStatus('current')
alaRDPIfMaxAdvtInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 11, 1, 1, 1, 20, 1, 4), Unsigned32().clone(600)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaRDPIfMaxAdvtInterval.setStatus('current')
alaRDPIfMinAdvtInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 11, 1, 1, 1, 20, 1, 5), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaRDPIfMinAdvtInterval.setStatus('current')
alaRDPIfAdvLifeTime = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 11, 1, 1, 1, 20, 1, 6), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaRDPIfAdvLifeTime.setStatus('current')
alaRDPIfPrefLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 11, 1, 1, 1, 20, 1, 7), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaRDPIfPrefLevel.setStatus('current')
alaRDPIfRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 11, 1, 1, 1, 20, 1, 8), RowStatus().clone('notInService')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaRDPIfRowStatus.setStatus('current')
alaRDPIfName = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 11, 1, 1, 1, 20, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaRDPIfName.setStatus('current')
alaRDPIPIfStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 11, 1, 1, 1, 20, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaRDPIPIfStatus.setStatus('current')
alaRDPVrrpStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 11, 1, 1, 1, 20, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaRDPVrrpStatus.setStatus('current')
alcatelIND1RDPMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 11, 1, 2))
alcatelIND1RDPMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 11, 1, 2, 1))
alcatelIND1RDPMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 11, 1, 2, 2))
alcatelIND1RDPMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 11, 1, 2, 1, 1)).setObjects(("ALCATEL-IND1-RDP-MIB", "alaRDPConfigMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alcatelIND1RDPMIBCompliance = alcatelIND1RDPMIBCompliance.setStatus('current')
alaRDPConfigMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 11, 1, 2, 2, 1)).setObjects(("ALCATEL-IND1-RDP-MIB", "alaRDPStatus"), ("ALCATEL-IND1-RDP-MIB", "alaRDPIfAddr"), ("ALCATEL-IND1-RDP-MIB", "alaRDPIfStatus"), ("ALCATEL-IND1-RDP-MIB", "alaRDPIfAdvtAddress"), ("ALCATEL-IND1-RDP-MIB", "alaRDPIfMaxAdvtInterval"), ("ALCATEL-IND1-RDP-MIB", "alaRDPIfMinAdvtInterval"), ("ALCATEL-IND1-RDP-MIB", "alaRDPIfAdvLifeTime"), ("ALCATEL-IND1-RDP-MIB", "alaRDPIfPrefLevel"), ("ALCATEL-IND1-RDP-MIB", "alaRDPIfRowStatus"), ("ALCATEL-IND1-RDP-MIB", "alaRDPIfName"), ("ALCATEL-IND1-RDP-MIB", "alaRDPIPIfStatus"), ("ALCATEL-IND1-RDP-MIB", "alaRDPVrrpStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaRDPConfigMIBGroup = alaRDPConfigMIBGroup.setStatus('current')
mibBuilder.exportSymbols("ALCATEL-IND1-RDP-MIB", alaRDPIfEntry=alaRDPIfEntry, alaRDPIfTable=alaRDPIfTable, alaRDPIfAdvLifeTime=alaRDPIfAdvLifeTime, alcatelIND1RouterDiscoveryProtocolMIB=alcatelIND1RouterDiscoveryProtocolMIB, alaRDPIfMinAdvtInterval=alaRDPIfMinAdvtInterval, alcatelIND1RDPMIBCompliances=alcatelIND1RDPMIBCompliances, alaRDPIPIfStatus=alaRDPIPIfStatus, alcatelIND1RDPMIBObjects=alcatelIND1RDPMIBObjects, alaRDPIfRowStatus=alaRDPIfRowStatus, alaRDPIfAdvtAddress=alaRDPIfAdvtAddress, alaRDPIfAddr=alaRDPIfAddr, alaRDPVrrpStatus=alaRDPVrrpStatus, alcatelIND1RDPMIBCompliance=alcatelIND1RDPMIBCompliance, PYSNMP_MODULE_ID=alcatelIND1RouterDiscoveryProtocolMIB, alcatelIND1RDPMIBConformance=alcatelIND1RDPMIBConformance, alaRDPConfigMIBGroup=alaRDPConfigMIBGroup, alaRDPIfMaxAdvtInterval=alaRDPIfMaxAdvtInterval, alcatelIND1RDPMIBGroups=alcatelIND1RDPMIBGroups, alaRDPStatus=alaRDPStatus, alaRDPIfName=alaRDPIfName, alaRDPIfPrefLevel=alaRDPIfPrefLevel, alaRDPConfig=alaRDPConfig, alaRDPIfStatus=alaRDPIfStatus)