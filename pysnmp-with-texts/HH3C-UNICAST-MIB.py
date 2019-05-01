#
# PySNMP MIB module HH3C-UNICAST-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HH3C-UNICAST-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:30:09 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
hh3cCommon, = mibBuilder.importSymbols("HH3C-OID-MIB", "hh3cCommon")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, Counter32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, NotificationType, ModuleIdentity, Counter64, Gauge32, ObjectIdentity, IpAddress, MibIdentifier, iso, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Counter32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "NotificationType", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "IpAddress", "MibIdentifier", "iso", "Bits")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
hh3cUnicast = ModuleIdentity((1, 3, 6, 1, 4, 1, 25506, 2, 44))
hh3cUnicast.setRevisions(('2005-03-24 14:54',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hh3cUnicast.setRevisionsDescriptions((' Revisions made by Hangzhou MIB team.',))
if mibBuilder.loadTexts: hh3cUnicast.setLastUpdated('200501311454Z')
if mibBuilder.loadTexts: hh3cUnicast.setOrganization('Hangzhou H3C Tech. Co., Ltd.')
if mibBuilder.loadTexts: hh3cUnicast.setContactInfo('Platform Team Hangzhou H3C Tech. Co., Ltd. Hai-Dian District Beijing P.R. China http://www.h3c.com Zip:100085 ')
if mibBuilder.loadTexts: hh3cUnicast.setDescription(' This MIB is a framework MIB for unicast related features.')
hh3cURPFTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 44, 1), )
if mibBuilder.loadTexts: hh3cURPFTable.setStatus('current')
if mibBuilder.loadTexts: hh3cURPFTable.setDescription(' Unicast Reverse Path Forwarding (URPF) is used to prevent the network attacks caused by source address spoofing. This table is used to configure URPF on specific interfaces.')
hh3cURPFEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 44, 1, 1), ).setIndexNames((0, "HH3C-UNICAST-MIB", "hh3cURPFIfIndex"))
if mibBuilder.loadTexts: hh3cURPFEntry.setStatus('current')
if mibBuilder.loadTexts: hh3cURPFEntry.setDescription(' The entry of hh3cURPFTable, indexed by vlan interface index.')
hh3cURPFIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 44, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: hh3cURPFIfIndex.setStatus('current')
if mibBuilder.loadTexts: hh3cURPFIfIndex.setDescription(' The ifIndex of vlan interface.')
hh3cURPFEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 44, 1, 1, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cURPFEnabled.setStatus('current')
if mibBuilder.loadTexts: hh3cURPFEnabled.setDescription(' This object is used to enable or disable URPF on certain vlan interfaces.')
hh3cURPFSlotID = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 44, 1, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cURPFSlotID.setStatus('current')
if mibBuilder.loadTexts: hh3cURPFSlotID.setDescription(' This object specifies to which slot packets are redirected in order to perform URPF check.')
hh3cURPFTotalReceivedPacket = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 44, 1, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cURPFTotalReceivedPacket.setStatus('current')
if mibBuilder.loadTexts: hh3cURPFTotalReceivedPacket.setDescription(' This object provides total received packets number.')
hh3cURPFDroppedPacket = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 44, 1, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cURPFDroppedPacket.setStatus('current')
if mibBuilder.loadTexts: hh3cURPFDroppedPacket.setDescription(' This object provides total dropped invalid packets number.')
hh3cURPFClearStat = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 44, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("reserved", 0), ("reset", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cURPFClearStat.setStatus('current')
if mibBuilder.loadTexts: hh3cURPFClearStat.setDescription(' This object is used to clear the URPF statistics on certain vlan interfaces. This object is actually a write-only object. When read, it always returns 0. When set to 1, the objects hh3cURPFTotalReceivedPacket and hh3cURPFDroppedPacket are reset to 0.')
mibBuilder.exportSymbols("HH3C-UNICAST-MIB", PYSNMP_MODULE_ID=hh3cUnicast, hh3cURPFEntry=hh3cURPFEntry, hh3cURPFDroppedPacket=hh3cURPFDroppedPacket, hh3cURPFIfIndex=hh3cURPFIfIndex, hh3cUnicast=hh3cUnicast, hh3cURPFClearStat=hh3cURPFClearStat, hh3cURPFSlotID=hh3cURPFSlotID, hh3cURPFTable=hh3cURPFTable, hh3cURPFEnabled=hh3cURPFEnabled, hh3cURPFTotalReceivedPacket=hh3cURPFTotalReceivedPacket)
