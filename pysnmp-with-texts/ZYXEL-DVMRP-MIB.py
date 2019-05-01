#
# PySNMP MIB module ZYXEL-DVMRP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZYXEL-DVMRP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:49:32 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, Gauge32, Counter32, MibIdentifier, ObjectIdentity, NotificationType, Counter64, Bits, Integer32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ModuleIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Gauge32", "Counter32", "MibIdentifier", "ObjectIdentity", "NotificationType", "Counter64", "Bits", "Integer32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ModuleIdentity", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
esMgmt, = mibBuilder.importSymbols("ZYXEL-ES-SMI", "esMgmt")
zyRouteDomainIpAddress, zyRouteDomainIpMaskBits = mibBuilder.importSymbols("ZYXEL-IP-FORWARD-MIB", "zyRouteDomainIpAddress", "zyRouteDomainIpMaskBits")
zyxelDvmrp = ModuleIdentity((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 23))
if mibBuilder.loadTexts: zyxelDvmrp.setLastUpdated('201207010000Z')
if mibBuilder.loadTexts: zyxelDvmrp.setOrganization('Enterprise Solution ZyXEL')
if mibBuilder.loadTexts: zyxelDvmrp.setContactInfo('')
if mibBuilder.loadTexts: zyxelDvmrp.setDescription('The subtree for Distance Vector Multicast Routing Protocol (DVMRP)')
zyxelDvmrpSetup = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 23, 1))
zyDvmrpState = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 23, 1, 1), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyDvmrpState.setStatus('current')
if mibBuilder.loadTexts: zyDvmrpState.setDescription('Enable/Disable DVMRP on the switch.')
zyDvmrpThreshold = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 23, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyDvmrpThreshold.setStatus('current')
if mibBuilder.loadTexts: zyDvmrpThreshold.setDescription('The maximum time to live value. This applies only to multicast traffic this switch sends out.')
zyxelDvmrpRouteDomainTable = MibTable((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 23, 1, 3), )
if mibBuilder.loadTexts: zyxelDvmrpRouteDomainTable.setStatus('current')
if mibBuilder.loadTexts: zyxelDvmrpRouteDomainTable.setDescription('The table contains DVMRP configuration.')
zyxelDvmrpRouteDomainEntry = MibTableRow((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 23, 1, 3, 1), ).setIndexNames((0, "ZYXEL-IP-FORWARD-MIB", "zyRouteDomainIpAddress"), (0, "ZYXEL-IP-FORWARD-MIB", "zyRouteDomainIpMaskBits"))
if mibBuilder.loadTexts: zyxelDvmrpRouteDomainEntry.setStatus('current')
if mibBuilder.loadTexts: zyxelDvmrpRouteDomainEntry.setDescription('An entry contains DVMRP configuration.')
zyDvmrpRouteDomainState = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 23, 1, 3, 1, 1), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyDvmrpRouteDomainState.setStatus('current')
if mibBuilder.loadTexts: zyDvmrpRouteDomainState.setDescription('Enable/Disable DVMRP on this IP routing domain.')
mibBuilder.exportSymbols("ZYXEL-DVMRP-MIB", zyDvmrpState=zyDvmrpState, zyxelDvmrpSetup=zyxelDvmrpSetup, zyDvmrpThreshold=zyDvmrpThreshold, zyxelDvmrpRouteDomainTable=zyxelDvmrpRouteDomainTable, zyDvmrpRouteDomainState=zyDvmrpRouteDomainState, PYSNMP_MODULE_ID=zyxelDvmrp, zyxelDvmrp=zyxelDvmrp, zyxelDvmrpRouteDomainEntry=zyxelDvmrpRouteDomainEntry)
