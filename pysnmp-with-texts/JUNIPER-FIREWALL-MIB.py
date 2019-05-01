#
# PySNMP MIB module JUNIPER-FIREWALL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/JUNIPER-FIREWALL-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:59:11 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
jnxMibs, = mibBuilder.importSymbols("JUNIPER-SMI", "jnxMibs")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, Counter32, Integer32, MibIdentifier, IpAddress, ModuleIdentity, Bits, NotificationType, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, ObjectIdentity, TimeTicks, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Counter32", "Integer32", "MibIdentifier", "IpAddress", "ModuleIdentity", "Bits", "NotificationType", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "ObjectIdentity", "TimeTicks", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
jnxFirewalls = ModuleIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 5))
jnxFirewalls.setRevisions(('2016-01-23 15:53',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: jnxFirewalls.setRevisionsDescriptions(('MIB support for firewall Hier policer stats.',))
if mibBuilder.loadTexts: jnxFirewalls.setLastUpdated('201601231553Z')
if mibBuilder.loadTexts: jnxFirewalls.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: jnxFirewalls.setContactInfo(' Juniper Technical Assistance Center Juniper Networks, Inc. 1194 N. Mathilda Avenue Sunnyvale, CA 94089 E-mail: support@juniper.net')
if mibBuilder.loadTexts: jnxFirewalls.setDescription("This is Juniper Networks' implementation of enterprise specific MIB for firewalls filters/policers.")
jnxFirewallsTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 5, 1), )
if mibBuilder.loadTexts: jnxFirewallsTable.setStatus('deprecated')
if mibBuilder.loadTexts: jnxFirewallsTable.setDescription('A list of firewalls entries. NOTE: This table is deprecated and exists for backward compatibility. The user is encouraged to use jnxFirewallCounterTable. This table does not handle: 1) counter and filter names greater than 24 characters 2) counters with same names but different types (the first duplicate is returned only)')
jnxFirewallsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 5, 1, 1), ).setIndexNames((0, "JUNIPER-FIREWALL-MIB", "jnxFWFilter"), (0, "JUNIPER-FIREWALL-MIB", "jnxFWCounter"))
if mibBuilder.loadTexts: jnxFirewallsEntry.setStatus('current')
if mibBuilder.loadTexts: jnxFirewallsEntry.setDescription('An entry of firewalls table.')
jnxFWFilter = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 5, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 24))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxFWFilter.setStatus('current')
if mibBuilder.loadTexts: jnxFWFilter.setDescription('The name of the firewall filter.')
jnxFWCounter = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 5, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 24))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxFWCounter.setStatus('current')
if mibBuilder.loadTexts: jnxFWCounter.setDescription('The name of the counter, policer or Hier policer. This name is specific within the firewall filter. Whether this object is associated with a counter, policer or a Hier policer is indicated by jnxFWType. See DESCRIPTION of jnxFirewallsTable for details on this assumption.')
jnxFWType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 5, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("other", 1), ("counter", 2), ("policer", 3), ("hpolagg", 4), ("hpolpre", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxFWType.setStatus('current')
if mibBuilder.loadTexts: jnxFWType.setDescription('The type of the object jnxFWCounter. What it is associated with a counter, policer or Hier policer.')
jnxFWPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 5, 1, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxFWPackets.setStatus('current')
if mibBuilder.loadTexts: jnxFWPackets.setDescription('The number of packets being counted pertaining to the specified counter or policer.')
jnxFWBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 5, 1, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxFWBytes.setStatus('current')
if mibBuilder.loadTexts: jnxFWBytes.setDescription('The number of bytes being counted pertaining to the specified counter. For policers, this field is always zero because policers do not count number of bytes.')
jnxFirewallCounterTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 5, 2), )
if mibBuilder.loadTexts: jnxFirewallCounterTable.setStatus('current')
if mibBuilder.loadTexts: jnxFirewallCounterTable.setDescription('A list of firewall filter counters.')
jnxFirewallCounterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 5, 2, 1), ).setIndexNames((0, "JUNIPER-FIREWALL-MIB", "jnxFWCounterFilterName"), (0, "JUNIPER-FIREWALL-MIB", "jnxFWCounterName"), (0, "JUNIPER-FIREWALL-MIB", "jnxFWCounterType"))
if mibBuilder.loadTexts: jnxFirewallCounterEntry.setStatus('current')
if mibBuilder.loadTexts: jnxFirewallCounterEntry.setDescription('An entry of firewalls table.')
jnxFWCounterFilterName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 5, 2, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 127)))
if mibBuilder.loadTexts: jnxFWCounterFilterName.setStatus('current')
if mibBuilder.loadTexts: jnxFWCounterFilterName.setDescription('The name of the firewall filter.')
jnxFWCounterName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 5, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 127)))
if mibBuilder.loadTexts: jnxFWCounterName.setStatus('current')
if mibBuilder.loadTexts: jnxFWCounterName.setDescription('The name of the counter, policer or Hier policer. This name is specific within the firewall filter. Whether this object is associated with a counter, policer or a Hier policer is indicated by jnxFWCounterType.')
jnxFWCounterType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 5, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("other", 1), ("counter", 2), ("policer", 3), ("hpolagg", 4), ("hpolpre", 5))))
if mibBuilder.loadTexts: jnxFWCounterType.setStatus('current')
if mibBuilder.loadTexts: jnxFWCounterType.setDescription('The type of the object jnxFWCounterName identifies. What it is associated with - a counter, policer or Hier policer. It is possible to have two counters of the same name and different type.')
jnxFWCounterPacketCount = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 5, 2, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxFWCounterPacketCount.setStatus('current')
if mibBuilder.loadTexts: jnxFWCounterPacketCount.setDescription('The number of packets being counted pertaining to the specified counter or policer.')
jnxFWCounterByteCount = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 5, 2, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxFWCounterByteCount.setStatus('current')
if mibBuilder.loadTexts: jnxFWCounterByteCount.setDescription('The number of bytes being counted pertaining to the specified counter. For policers, this field is always zero because policers do not count number of bytes.')
jnxFWCounterDisplayFilterName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 5, 2, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 127))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxFWCounterDisplayFilterName.setStatus('current')
if mibBuilder.loadTexts: jnxFWCounterDisplayFilterName.setDescription('The name of the firewall filter.')
jnxFWCounterDisplayName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 5, 2, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 127))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxFWCounterDisplayName.setStatus('current')
if mibBuilder.loadTexts: jnxFWCounterDisplayName.setDescription('The name of the counter, policer or Hier policer. Whether this object is associated with a counter, policer or Hier policer is indicated by jnxFWCounterType.')
jnxFWCounterDisplayType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 5, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("other", 1), ("counter", 2), ("policer", 3), ("hpolagg", 4), ("hpolpre", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxFWCounterDisplayType.setStatus('current')
if mibBuilder.loadTexts: jnxFWCounterDisplayType.setDescription('The type of the object jnxFWCounterName identifies. What it is associated with - a counter, policer or Hier policer. It is possible to have two counters of the same name and different type.')
jnxFWCntrXTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 5, 3), )
if mibBuilder.loadTexts: jnxFWCntrXTable.setStatus('current')
if mibBuilder.loadTexts: jnxFWCntrXTable.setDescription('An extended list of firewall filter counters. This table maintains the additional statistics for the additional policer counters and is only supported on MX platform for now.')
jnxFWCntrXEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 5, 3, 1), )
jnxFirewallCounterEntry.registerAugmentions(("JUNIPER-FIREWALL-MIB", "jnxFWCntrXEntry"))
jnxFWCntrXEntry.setIndexNames(*jnxFirewallCounterEntry.getIndexNames())
if mibBuilder.loadTexts: jnxFWCntrXEntry.setStatus('current')
if mibBuilder.loadTexts: jnxFWCntrXEntry.setDescription('An entry of extended firewall table.')
jnxFWCntrPolicerOfferedPktCount = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 5, 3, 1, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxFWCntrPolicerOfferedPktCount.setStatus('current')
if mibBuilder.loadTexts: jnxFWCntrPolicerOfferedPktCount.setDescription(' ')
jnxFWCntrPolicerOfferedByteCount = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 5, 3, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxFWCntrPolicerOfferedByteCount.setStatus('current')
if mibBuilder.loadTexts: jnxFWCntrPolicerOfferedByteCount.setDescription(' ')
jnxFWCntrPolicerOutSpecPktCount = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 5, 3, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxFWCntrPolicerOutSpecPktCount.setStatus('current')
if mibBuilder.loadTexts: jnxFWCntrPolicerOutSpecPktCount.setDescription(' ')
jnxFWCntrPolicerOutSpecByteCount = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 5, 3, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxFWCntrPolicerOutSpecByteCount.setStatus('current')
if mibBuilder.loadTexts: jnxFWCntrPolicerOutSpecByteCount.setDescription(' ')
jnxFWCntrPolicerTxPktCount = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 5, 3, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxFWCntrPolicerTxPktCount.setStatus('current')
if mibBuilder.loadTexts: jnxFWCntrPolicerTxPktCount.setDescription(' ')
jnxFWCntrPolicerTxByteCount = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 5, 3, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxFWCntrPolicerTxByteCount.setStatus('current')
if mibBuilder.loadTexts: jnxFWCntrPolicerTxByteCount.setDescription(' ')
mibBuilder.exportSymbols("JUNIPER-FIREWALL-MIB", jnxFirewallsEntry=jnxFirewallsEntry, jnxFirewallCounterEntry=jnxFirewallCounterEntry, jnxFWCounterDisplayFilterName=jnxFWCounterDisplayFilterName, jnxFWBytes=jnxFWBytes, jnxFirewalls=jnxFirewalls, jnxFWPackets=jnxFWPackets, jnxFWCounter=jnxFWCounter, jnxFWCounterFilterName=jnxFWCounterFilterName, jnxFWCounterByteCount=jnxFWCounterByteCount, jnxFWCounterName=jnxFWCounterName, jnxFWCounterPacketCount=jnxFWCounterPacketCount, PYSNMP_MODULE_ID=jnxFirewalls, jnxFWCntrPolicerOfferedPktCount=jnxFWCntrPolicerOfferedPktCount, jnxFWCntrPolicerOutSpecPktCount=jnxFWCntrPolicerOutSpecPktCount, jnxFWFilter=jnxFWFilter, jnxFirewallCounterTable=jnxFirewallCounterTable, jnxFWCounterType=jnxFWCounterType, jnxFWCntrPolicerOfferedByteCount=jnxFWCntrPolicerOfferedByteCount, jnxFWCounterDisplayType=jnxFWCounterDisplayType, jnxFWCounterDisplayName=jnxFWCounterDisplayName, jnxFWCntrXTable=jnxFWCntrXTable, jnxFWCntrXEntry=jnxFWCntrXEntry, jnxFWCntrPolicerTxByteCount=jnxFWCntrPolicerTxByteCount, jnxFWType=jnxFWType, jnxFirewallsTable=jnxFirewallsTable, jnxFWCntrPolicerOutSpecByteCount=jnxFWCntrPolicerOutSpecByteCount, jnxFWCntrPolicerTxPktCount=jnxFWCntrPolicerTxPktCount)
