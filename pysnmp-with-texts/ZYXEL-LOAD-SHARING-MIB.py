#
# PySNMP MIB module ZYXEL-LOAD-SHARING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZYXEL-LOAD-SHARING-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:50:40 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, iso, Counter32, Integer32, Counter64, ObjectIdentity, TimeTicks, MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Unsigned32, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "iso", "Counter32", "Integer32", "Counter64", "ObjectIdentity", "TimeTicks", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Unsigned32", "ModuleIdentity", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
esMgmt, = mibBuilder.importSymbols("ZYXEL-ES-SMI", "esMgmt")
zyxelLoadSharing = ModuleIdentity((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 44))
if mibBuilder.loadTexts: zyxelLoadSharing.setLastUpdated('201207010000Z')
if mibBuilder.loadTexts: zyxelLoadSharing.setOrganization('Enterprise Solution ZyXEL')
if mibBuilder.loadTexts: zyxelLoadSharing.setContactInfo('')
if mibBuilder.loadTexts: zyxelLoadSharing.setDescription('The subtree for load sharing')
zyxelLoadSharingSetup = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 44, 1))
zyLoadSharingState = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 44, 1, 1), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyLoadSharingState.setStatus('current')
if mibBuilder.loadTexts: zyLoadSharingState.setDescription('Enable/Disable IP load-sharing on the Switch.')
zyLoadSharingCriteria = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 44, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("srcIp", 1), ("srcDstIp", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyLoadSharingCriteria.setStatus('current')
if mibBuilder.loadTexts: zyLoadSharingCriteria.setDescription('The switch selects the criteria to determine the routing path for a packet.')
zyLoadSharingAgingTime = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 44, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyLoadSharingAgingTime.setStatus('current')
if mibBuilder.loadTexts: zyLoadSharingAgingTime.setDescription('The polling time of resolved next-hops for equal-cost multipath routes.')
zyLoadSharingDiscoverTime = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 44, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyLoadSharingDiscoverTime.setStatus('current')
if mibBuilder.loadTexts: zyLoadSharingDiscoverTime.setDescription('The polling time of unresolved next-hops for equal-cost multipath routes.')
mibBuilder.exportSymbols("ZYXEL-LOAD-SHARING-MIB", zyLoadSharingAgingTime=zyLoadSharingAgingTime, zyxelLoadSharing=zyxelLoadSharing, PYSNMP_MODULE_ID=zyxelLoadSharing, zyxelLoadSharingSetup=zyxelLoadSharingSetup, zyLoadSharingCriteria=zyLoadSharingCriteria, zyLoadSharingState=zyLoadSharingState, zyLoadSharingDiscoverTime=zyLoadSharingDiscoverTime)
