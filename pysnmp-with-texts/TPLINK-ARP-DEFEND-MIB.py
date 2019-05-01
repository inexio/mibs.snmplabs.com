#
# PySNMP MIB module TPLINK-ARP-DEFEND-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TPLINK-ARP-DEFEND-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:24:13 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, TimeTicks, Counter32, Counter64, ModuleIdentity, MibIdentifier, Integer32, ObjectIdentity, iso, NotificationType, Gauge32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "TimeTicks", "Counter32", "Counter64", "ModuleIdentity", "MibIdentifier", "Integer32", "ObjectIdentity", "iso", "NotificationType", "Gauge32", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
tplinkArpInspectionMIBObjects, = mibBuilder.importSymbols("TPLINK-ARP-INSPECTION-MIB", "tplinkArpInspectionMIBObjects")
tpArpDefend = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 28, 1, 2))
tpArpDefendConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 28, 1, 2, 1))
tpArpDefendConfigTable = MibTable((1, 3, 6, 1, 4, 1, 11863, 6, 28, 1, 2, 1, 1), )
if mibBuilder.loadTexts: tpArpDefendConfigTable.setStatus('current')
if mibBuilder.loadTexts: tpArpDefendConfigTable.setDescription('A list of arp defend config entries. Here you can configure the ARP Defend feature.')
tpArpDefendConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11863, 6, 28, 1, 2, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: tpArpDefendConfigEntry.setStatus('current')
if mibBuilder.loadTexts: tpArpDefendConfigEntry.setDescription('An entry contains of the information of arp defend attack config.')
tpArpDefendConfigPort = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 28, 1, 2, 1, 1, 1, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpArpDefendConfigPort.setStatus('current')
if mibBuilder.loadTexts: tpArpDefendConfigPort.setDescription('port number')
tpArpDefendConfigEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 28, 1, 2, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 0))).clone(namedValues=NamedValues(("enable", 1), ("disable", 0)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpArpDefendConfigEnable.setStatus('current')
if mibBuilder.loadTexts: tpArpDefendConfigEnable.setDescription('0. disable 1. enable Select Enable/Disable the ARP Defend feature for the port. ')
tpArpDefendConfigRate = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 28, 1, 2, 1, 1, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpArpDefendConfigRate.setStatus('current')
if mibBuilder.loadTexts: tpArpDefendConfigRate.setDescription('specify the maximum amount of the received ARP packets per second.(10-100pps)')
tpArpDefendConfigState = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 28, 1, 2, 1, 1, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpArpDefendConfigState.setStatus('current')
if mibBuilder.loadTexts: tpArpDefendConfigState.setDescription('the state of port, when the rate exceed, the port will discard the arp pkt.')
tpArpDefendConfigPortLag = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 28, 1, 2, 1, 1, 1, 5), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpArpDefendConfigPortLag.setStatus('current')
if mibBuilder.loadTexts: tpArpDefendConfigPortLag.setDescription('the lag the port belong to')
mibBuilder.exportSymbols("TPLINK-ARP-DEFEND-MIB", tpArpDefendConfigPort=tpArpDefendConfigPort, tpArpDefendConfigEnable=tpArpDefendConfigEnable, tpArpDefendConfigPortLag=tpArpDefendConfigPortLag, tpArpDefendConfigTable=tpArpDefendConfigTable, tpArpDefend=tpArpDefend, tpArpDefendConfigRate=tpArpDefendConfigRate, tpArpDefendConfigState=tpArpDefendConfigState, tpArpDefendConfigEntry=tpArpDefendConfigEntry, tpArpDefendConfig=tpArpDefendConfig)
