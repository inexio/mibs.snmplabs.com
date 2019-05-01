#
# PySNMP MIB module H3C-LB-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/H3C-LB-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:22:51 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
h3cCommon, = mibBuilder.importSymbols("HUAWEI-3COM-OID-MIB", "h3cCommon")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, IpAddress, MibIdentifier, TimeTicks, Bits, NotificationType, ModuleIdentity, Counter32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "IpAddress", "MibIdentifier", "TimeTicks", "Bits", "NotificationType", "ModuleIdentity", "Counter32", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
h3cLB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 10, 2, 116))
h3cLB.setRevisions(('2010-12-01 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: h3cLB.setRevisionsDescriptions(('The initial revision of this MIB module.',))
if mibBuilder.loadTexts: h3cLB.setLastUpdated('201012010000Z')
if mibBuilder.loadTexts: h3cLB.setOrganization('Hangzhou H3C Technologies Co., Ltd.')
if mibBuilder.loadTexts: h3cLB.setContactInfo('Platform Team Hangzhou H3C Tech. Co., Ltd. Hai-Dian District Beijing P.R. China http://www.h3c.com Zip:100085 ')
if mibBuilder.loadTexts: h3cLB.setDescription('The private mib file includes the loadbalance information of the device.')
h3cLBTables = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 116, 1))
h3cLBRealServerGroupTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 116, 1, 1), )
if mibBuilder.loadTexts: h3cLBRealServerGroupTable.setStatus('current')
if mibBuilder.loadTexts: h3cLBRealServerGroupTable.setDescription('Real server group table for loadbalance.')
h3cLBRealServerGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 116, 1, 1, 1), ).setIndexNames((0, "H3C-LB-MIB", "h3cLBRealServerGroupName"))
if mibBuilder.loadTexts: h3cLBRealServerGroupEntry.setStatus('current')
if mibBuilder.loadTexts: h3cLBRealServerGroupEntry.setDescription('An entry contains the information of the real server group.')
h3cLBRealServerGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 116, 1, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: h3cLBRealServerGroupName.setStatus('current')
if mibBuilder.loadTexts: h3cLBRealServerGroupName.setDescription('Real server group name.')
h3cLBRealServerTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 116, 1, 2), )
if mibBuilder.loadTexts: h3cLBRealServerTable.setStatus('current')
if mibBuilder.loadTexts: h3cLBRealServerTable.setDescription('Real server table for loadbalance.')
h3cLBRealServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 116, 1, 2, 1), ).setIndexNames((0, "H3C-LB-MIB", "h3cLBRealServerGroupName"), (0, "H3C-LB-MIB", "h3cLBRealServerName"))
if mibBuilder.loadTexts: h3cLBRealServerEntry.setStatus('current')
if mibBuilder.loadTexts: h3cLBRealServerEntry.setDescription('An entry contains the information of the real server.')
h3cLBRealServerName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 116, 1, 2, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: h3cLBRealServerName.setStatus('current')
if mibBuilder.loadTexts: h3cLBRealServerName.setDescription('Real server name.')
h3cLBRealServerStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 116, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2), ("slowdown", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cLBRealServerStatus.setStatus('current')
if mibBuilder.loadTexts: h3cLBRealServerStatus.setDescription('A list of real server status type. enabled: the real server is enabled. disabled: the real server is disabled, the loadbalance device does not assign any traffic to the real server. slowdown: the real server continues to process the existed session previously assigned to it, but the loadbalance device does not assign any new session to the real server.')
h3cLBRealServerConnectNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 116, 1, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cLBRealServerConnectNumber.setStatus('current')
if mibBuilder.loadTexts: h3cLBRealServerConnectNumber.setDescription('The connection number of real server.')
h3cLBTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 116, 2))
h3cLBTrapPrex = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 116, 2, 0))
h3cLBRealServerOverLoad = NotificationType((1, 3, 6, 1, 4, 1, 2011, 10, 2, 116, 2, 0, 1)).setObjects(("H3C-LB-MIB", "h3cLBRealServerGroupName"), ("H3C-LB-MIB", "h3cLBRealServerName"), ("H3C-LB-MIB", "h3cLBRealServerConnectNumber"))
if mibBuilder.loadTexts: h3cLBRealServerOverLoad.setStatus('current')
if mibBuilder.loadTexts: h3cLBRealServerOverLoad.setDescription('This trap is sent when the real server is overloaded.')
mibBuilder.exportSymbols("H3C-LB-MIB", h3cLBTrapPrex=h3cLBTrapPrex, h3cLBRealServerGroupEntry=h3cLBRealServerGroupEntry, h3cLBRealServerEntry=h3cLBRealServerEntry, h3cLBRealServerStatus=h3cLBRealServerStatus, h3cLBTrap=h3cLBTrap, h3cLBRealServerConnectNumber=h3cLBRealServerConnectNumber, h3cLBRealServerGroupTable=h3cLBRealServerGroupTable, h3cLBTables=h3cLBTables, h3cLBRealServerGroupName=h3cLBRealServerGroupName, h3cLBRealServerOverLoad=h3cLBRealServerOverLoad, h3cLBRealServerTable=h3cLBRealServerTable, PYSNMP_MODULE_ID=h3cLB, h3cLB=h3cLB, h3cLBRealServerName=h3cLBRealServerName)
