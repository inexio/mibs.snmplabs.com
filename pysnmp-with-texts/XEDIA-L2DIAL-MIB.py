#
# PySNMP MIB module XEDIA-L2DIAL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/XEDIA-L2DIAL-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:42:55 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Counter32, Counter64, Bits, ModuleIdentity, iso, IpAddress, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, TimeTicks, NotificationType, ObjectIdentity, Unsigned32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Counter64", "Bits", "ModuleIdentity", "iso", "IpAddress", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "TimeTicks", "NotificationType", "ObjectIdentity", "Unsigned32", "Integer32")
DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus")
xediaMibs, = mibBuilder.importSymbols("XEDIA-REG", "xediaMibs")
xediaL2DialMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 838, 3, 30))
if mibBuilder.loadTexts: xediaL2DialMIB.setLastUpdated('9902272155Z')
if mibBuilder.loadTexts: xediaL2DialMIB.setOrganization('Xedia Corp.')
if mibBuilder.loadTexts: xediaL2DialMIB.setContactInfo('support@xedia.com')
if mibBuilder.loadTexts: xediaL2DialMIB.setDescription("This module defines objects for management of Xedia's Layer 2 Dial layer (l2Dial).")
l2DialObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 838, 3, 30, 1))
l2DialConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 838, 3, 30, 2))
l2DialStatusTable = MibTable((1, 3, 6, 1, 4, 1, 838, 3, 30, 1, 1), )
if mibBuilder.loadTexts: l2DialStatusTable.setStatus('current')
if mibBuilder.loadTexts: l2DialStatusTable.setDescription('The L2Dial status table.')
l2DialStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 838, 3, 30, 1, 1, 1), ).setIndexNames((0, "XEDIA-L2DIAL-MIB", "l2DialStatusIpAddress"))
if mibBuilder.loadTexts: l2DialStatusEntry.setStatus('current')
if mibBuilder.loadTexts: l2DialStatusEntry.setDescription('An L2Dial status entry. An entry in this table corresponds to an ip addresses / sublayer mapping.')
l2DialStatusIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 30, 1, 1, 1, 1), IpAddress())
if mibBuilder.loadTexts: l2DialStatusIpAddress.setStatus('current')
if mibBuilder.loadTexts: l2DialStatusIpAddress.setDescription('An IP address.')
l2DialStatusSublayer = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 30, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: l2DialStatusSublayer.setStatus('current')
if mibBuilder.loadTexts: l2DialStatusSublayer.setDescription('A sublayer.')
l2DialCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 838, 3, 30, 2, 1))
l2DialGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 838, 3, 30, 2, 2))
l2DialCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 838, 3, 30, 2, 1, 1)).setObjects(("XEDIA-L2DIAL-MIB", "l2DialStatusGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    l2DialCompliance = l2DialCompliance.setStatus('current')
if mibBuilder.loadTexts: l2DialCompliance.setDescription('The compliance statement for all agents that support this MIB. A compliant agent implements all objects defined in this MIB.')
l2DialStatusGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 838, 3, 30, 2, 2, 1)).setObjects(("XEDIA-L2DIAL-MIB", "l2DialStatusSublayer"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    l2DialStatusGroup = l2DialStatusGroup.setStatus('current')
if mibBuilder.loadTexts: l2DialStatusGroup.setDescription('A collection of objects providing addresses to sublayer mappings.')
mibBuilder.exportSymbols("XEDIA-L2DIAL-MIB", PYSNMP_MODULE_ID=xediaL2DialMIB, l2DialCompliances=l2DialCompliances, l2DialStatusGroup=l2DialStatusGroup, l2DialStatusEntry=l2DialStatusEntry, xediaL2DialMIB=xediaL2DialMIB, l2DialStatusSublayer=l2DialStatusSublayer, l2DialStatusIpAddress=l2DialStatusIpAddress, l2DialGroups=l2DialGroups, l2DialConformance=l2DialConformance, l2DialCompliance=l2DialCompliance, l2DialStatusTable=l2DialStatusTable, l2DialObjects=l2DialObjects)
