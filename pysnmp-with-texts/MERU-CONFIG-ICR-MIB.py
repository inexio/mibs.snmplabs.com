#
# PySNMP MIB module MERU-CONFIG-ICR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MERU-CONFIG-ICR-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:11:22 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
Ipv6Address, = mibBuilder.importSymbols("IPV6-TC", "Ipv6Address")
mwConfiguration, = mibBuilder.importSymbols("MERU-SMI", "mwConfiguration")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, Integer32, iso, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, enterprises, Counter64, Gauge32, ObjectIdentity, TimeTicks, ModuleIdentity, Counter32, IpAddress, Unsigned32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "iso", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "enterprises", "Counter64", "Gauge32", "ObjectIdentity", "TimeTicks", "ModuleIdentity", "Counter32", "IpAddress", "Unsigned32", "MibIdentifier")
DateAndTime, TruthValue, TextualConvention, RowStatus, DisplayString, TimeInterval, TimeStamp, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "TruthValue", "TextualConvention", "RowStatus", "DisplayString", "TimeInterval", "TimeStamp", "MacAddress")
mwConfigIcr = ModuleIdentity((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 18))
if mibBuilder.loadTexts: mwConfigIcr.setLastUpdated('200506050000Z')
if mibBuilder.loadTexts: mwConfigIcr.setOrganization('Meru Networks')
if mibBuilder.loadTexts: mwConfigIcr.setContactInfo('support@merunetworks.com')
if mibBuilder.loadTexts: mwConfigIcr.setDescription('This MIB defines all the managed objects used to manage the Meru WLAN ICR Configuration infrastructure')
mwIcrTable = MibTable((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 18, 1), )
if mibBuilder.loadTexts: mwIcrTable.setStatus('current')
if mibBuilder.loadTexts: mwIcrTable.setDescription('This object describes Inter Controller Roaming ')
mwIcrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 18, 1, 1), ).setIndexNames((0, "MERU-CONFIG-ICR-MIB", "mwIcrTableIndex"))
if mibBuilder.loadTexts: mwIcrEntry.setStatus('current')
if mibBuilder.loadTexts: mwIcrEntry.setDescription('This object describes Inter Controller Roaming ')
mwIcrTableIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 18, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: mwIcrTableIndex.setStatus('current')
if mibBuilder.loadTexts: mwIcrTableIndex.setDescription('The index value of the table ')
mwIcrControllerIp = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 18, 1, 1, 2), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwIcrControllerIp.setStatus('current')
if mibBuilder.loadTexts: mwIcrControllerIp.setDescription('This object describes Controller IP')
mwIcrEssId = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 18, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwIcrEssId.setStatus('current')
if mibBuilder.loadTexts: mwIcrEssId.setDescription('This object describes ESSID')
mwIcrRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 18, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwIcrRowStatus.setStatus('current')
if mibBuilder.loadTexts: mwIcrRowStatus.setDescription('This object is used to create and delete rows in the table')
mibBuilder.exportSymbols("MERU-CONFIG-ICR-MIB", mwIcrTable=mwIcrTable, mwIcrControllerIp=mwIcrControllerIp, mwIcrEssId=mwIcrEssId, PYSNMP_MODULE_ID=mwConfigIcr, mwIcrTableIndex=mwIcrTableIndex, mwConfigIcr=mwConfigIcr, mwIcrEntry=mwIcrEntry, mwIcrRowStatus=mwIcrRowStatus)
